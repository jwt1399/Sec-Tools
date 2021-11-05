#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import json
import requests
import chardet
from ..randheader.randheader import get_ua
from bs4 import BeautifulSoup

# Reference: https://github.com/boy-hack/w8scan


class WebPage(object):
    """
    Simple representation of a web page, decoupled
    from any particular HTTP library's API.
    """

    def __init__(self, url, html, headers):
        """
        Initialize a new WebPage object.

        Parameters
        ----------

        url : str
            The web page URL.
        html : str
            The web page content (HTML)
        headers : dict
            The HTTP response headers
        """
        # if use response.text, could have some error
        self.html = html
        self.url = url
        self.headers = headers

        # Parse the HTML with BeautifulSoup to find <script> and <meta> tags.
        self.parsed_html = soup = BeautifulSoup(self.html, "html.parser")
        self.scripts = [script['src'] for script in soup.findAll('script', src=True)]
        self.meta = {
            meta['name'].lower(): meta['content'] for meta in soup.findAll('meta', attrs=dict(name=True, content=True))
        }

        self.title = soup.title.string if soup.title else 'None'
        wappalyzer = Wappalyzer()
        self.apps = wappalyzer.analyze(self)
        self.result = ';'.join(self.apps)

    def check(self):
        out = []
        apps = []
        with open(os.path.dirname(__file__) + '/../../database/apps.txt', 'r') as f:
            for i in f.readlines():
                apps.append(i.strip('\n'))

        for i in apps:
            name, method, position, regex = i.strip().split("|", 3)
            if method == 'headers':
                if self.headers.get(position) is not None:
                    if re.search(regex, str(self.headers.get(position))) is not None:
                        out.append(name)
            else:
                if re.search(regex, self.html):
                    out.append(name)
        return out

    def info(self):
        result = self.result.split(';')
        result.extend(self.check())
        try:
            server = self.headers['Server']
        except:
            server = 'None'
        security = []
        if self.headers.get('Content-Security-Policy'):
            security.append('Content-Security-Policy')
        if self.headers.get('X-Webkit-CSP'):
            security.append('X-Webkit-CSP')
        if self.headers.get('X-XSS-Protection'):
            security.append('X-XSS-Protection')
        if self.headers.get('Strict-Transport-Security'):
            security.append('Strict-Transport-Security')
        return {
            "apps": list(set(result)),
            "title": self.title,
            "server": server,
            'security': security
        }


class Wappalyzer(object):
    """
    Python Wappalyzer driver.
    """

    def __init__(self, apps_file=None):
        """
        Initialize a new Wappalyzer instance.
        初始化一个新的Wappalyzer实例。
        Parameters
        ----------

        categories : dict
            Map of category ids to names, as in apps.json.
        apps : dict
            Map of app names to app dicts, as in apps.json.

            类别:dict类型
            分类id到名称的映射，如app.json。
            应用:dict类型
            应用名称到应用字典的映射，如在app.json中。
        """

        with open(os.path.dirname(__file__) + '/../../database/apps.json', 'rb') as fd:
            obj = json.load(fd)

        self.categories = obj['categories']
        self.apps = obj['apps']

        for name, app in self.apps.items():
            self._prepare_app(app)

    def _prepare_app(self, app):
        """
        Normalize app data, preparing it for the detection phase.
        标准化应用程序数据，为检测阶段做好准备。
        """

        # Ensure these keys' values are lists
        # 确保这些键的值是列表
        for key in ['url', 'html', 'script', 'implies']:
            value = app.get(key)
            if value is None:
                app[key] = []
            else:
                if not isinstance(value, list):
                    app[key] = [value]

        # Ensure these keys exist
        # 确保这些键存在
        for key in ['headers', 'meta']:
            value = app.get(key)
            if value is None:
                app[key] = {}

        # Ensure the 'meta' key is a dict
        # 确保“meta”键是一个字典
        obj = app['meta']
        if not isinstance(obj, dict):
            app['meta'] = {'generator': obj}

        # Ensure keys are lowercase
        # 确保键是小写的
        for key in ['headers', 'meta']:
            obj = app[key]
            app[key] = {k.lower(): v for k, v in obj.items()}

        # Prepare regular expression patterns
        # 准备正则表达式模式
        for key in ['url', 'html', 'script']:
            app[key] = [self._prepare_pattern(pattern) for pattern in app[key]]

        for key in ['headers', 'meta']:
            obj = app[key]
            for name, pattern in obj.items():
                obj[name] = self._prepare_pattern(obj[name])

    def _prepare_pattern(self, pattern):
        """
        Strip out key:value pairs from the pattern and compile the regular
        expression.
        从模式中删除键:值对，并编译正则表达式。
        """
        regex, _, rest = pattern.partition('\\;')
        try:
            return re.compile(regex, re.I)
        except re.error as e:
            # regex that never matches:
            # 从不匹配的正则表达式:
            # http://stackoverflow.com/a/1845097/413622
            return re.compile(r'(?!x)x')

    def _has_app(self, app, webpage):
        """
        Determine whether the web page matches the app signature.
        判断web页面是否与应用程序签名匹配。
        """
        # Search the easiest things first and save the full-text search of the
        # HTML for last

        for regex in app['url']:
            if regex.search(webpage.url):
                return True

        for name, regex in app['headers'].items():
            if name in webpage.headers:
                content = webpage.headers[name]
                if regex.search(content):
                    return True

        for regex in app['script']:
            for script in webpage.scripts:
                if regex.search(script):
                    return True

        for name, regex in app['meta'].items():
            if name in webpage.meta:
                content = webpage.meta[name]
                if regex.search(content):
                    return True

        for regex in app['html']:
            if regex.search(webpage.html):
                return True

    def _get_implied_apps(self, detected_apps):
        """
        Get the set of apps implied by `detected_apps`.
        获取' detected_apps '隐含的一组应用程序。
        """

        def __get_implied_apps(apps):
            _implied_apps = set()
            try:
                for app in apps:
                    if 'implies' in self.apps[app]:
                        _implied_apps.update(set(self.apps[app]['implies']))
                return _implied_apps
            except:
                pass

        implied_apps = __get_implied_apps(detected_apps)
        all_implied_apps = set()

        # Descend recursively until we've found all implied apps
        # 递归查询，直到我们找到所有隐含的应用
        try:
            while not all_implied_apps.issuperset(implied_apps):
                all_implied_apps.update(implied_apps)
                implied_apps = __get_implied_apps(all_implied_apps)
        except:
            pass
        return all_implied_apps

    def get_categories(self, app_name):
        """
        Returns a list of the categories for an app name.
        返回应用程序名称的类别列表。
        """
        cat_nums = self.apps.get(app_name, {}).get("cats", [])
        cat_names = [
            self.categories.get("%s" % cat_num, "") for cat_num in cat_nums
        ]

        return cat_names

    def analyze(self, webpage):
        """
        Return a list of applications that can be detected on the web page.
        返回可以在网页上检测到的应用程序列表。
        """
        detected_apps = set()

        for app_name, app in self.apps.items():
            if self._has_app(app, webpage):
                detected_apps.add(app_name)

        detected_apps |= self._get_implied_apps(detected_apps)

        return detected_apps

    def analyze_with_categories(self, webpage):
        detected_apps = self.analyze(webpage)
        categorised_apps = {}

        for app_name in detected_apps:
            cat_names = self.get_categories(app_name)
            categorised_apps[app_name] = {"categories": cat_names}

        return categorised_apps


def getwhatcms(url=''):
    """
    获取cms类型和相关框架的信息
    :param url:
    :return:
    """
    return_str = '未能识别，请联系管理员'
    webinfo = {}
    if url.startswith('https://') or url.startswith('http://'):
        try:
            html = requests.get(url=url, headers=get_ua(), timeout=4)
            if html:
                try:
                    codetype = chardet.detect(html.content).get('encoding')
                    html.encoding = codetype
                    webinfo = WebPage(html.url, html.text, html.headers).info()
                    print('[LOG WhatCms]:', webinfo)
                except Exception as e:
                    pass
        except Exception as e:
            pass
        if webinfo:
            return_str = '，'.join(webinfo.get('apps')) + '，Server【{}】'.format(webinfo.get('server'))
    return return_str


if __name__ == '__main__':
    print('test')
