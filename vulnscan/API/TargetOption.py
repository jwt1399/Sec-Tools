#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .Base import Base
import requests
import json


class TargetOption(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)

        self.excluded_hours_dict = {
            'default': '',
            '9am_to_5pm': 'cb869c0f-756e-439f-8895-d2502626a002',
            'except_working_hour': '851d89b6-32f5-4094-94c0-20abf77f7a6a',
            'no_weekends': '6275cc9e-d146-4268-b4b4-4ff747868ecc'
        }

        self.logger = self.get_logger

    def set_criticality(self, target_id, criticality, description=None):
        """设置目标危险程度和描述

        Args:
            target_id (string): 目标ID
            criticality (int): 30->critical, 20->high, 10-normal, 0->low
            description (None, optional): 目标描述

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_criticality_api = f'{self.targets_api}/{target_id}'
        try:
            data = dict()
            if description:
                data['description'] = description
            data['criticality'] = criticality
            response = requests.patch(set_criticality_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set General Criticality Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set General Criticality Failed......', exc_info=True)
            return False

    def set_scan_speed(self, target_id, scan_speed):
        """设置扫描速度

        Args:
            target_id (string): 目标ID
            scan_speed (string): 可选值为，sequential/slow/moderate/fast

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_scan_speed_api = f'{self.targets_api}/{target_id}/configuration'
        try:
            data = {'scan_speed': scan_speed}
            response = requests.patch(set_scan_speed_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set Scan Speed Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Scan Speed Failed......', exc_info=True)
            return False

    def set_continuous_scan(self, target_id, enabled=False):
        """启用持续扫描

        Args:
            target_id (string): 目标ID
            enabled (bool, optional): 启用True, 关闭False

        Returns:
            接口请求成功返回对应JSON，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_continuous_scan_api = f'{self.targets_api}/{target_id}/continuous_scan'
        try:
            data = {'enabled': enabled}
            response = requests.post(set_continuous_scan_api, json=data, headers=self.auth_headers, verify=False)
            response_data = response.json()
            if 'enabled' in response_data:
                return True
            else:
                self.logger.error(f'Set Continuous Scan Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Continuous Scan Failed......', exc_info=True)
            return False

    def set_site_login(self, target_id, login_kind, login_info):
        """设置目标登录信息

        Args:
            target_id (string): 目标ID
            login_kind (string): 无登录none, 用户名和密码登录automatic, 暂不实现录屏登录序列
            login_info (dict): 登录信息，格式: {'username': 'tudouya', 'password': 'password123'}

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_site_login_api = f'{self.targets_api}/{target_id}/configuration'
        try:
            data = {
                'login': {
                    'kind': login_kind,
                }
            }
            if login_kind == 'automatic':
                data['login']['credentials'] = {
                    'enabled': True,
                    'username': login_info.get('username'),
                    'password': login_info.get('password')
                }

            response = requests.patch(set_site_login_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set Scan Speed Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Site Login Failed......', exc_info=True)
            return False

    def set_crawler(self, target_id, user_agent, case_sensitive, excluded_paths, limit_crawler_scope):
        """设置爬虫信息

        Args:
            target_id (string): 目标ID
            limit_crawler_scope (bool): 仅限爬行到地址和子目录
            case_sensitive (string): 大小写敏感, auto/no/yes
            excluded_paths (list): 排除路径
            user_agent (string): UA头

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_crawler_api = f'{self.targets_api}/{target_id}/configuration'
        data = {
            'limit_crawler_scope': limit_crawler_scope,
            'case_sensitive': case_sensitive,
            'excluded_paths': excluded_paths,
            'user_agent': user_agent
        }
        try:
            response = requests.patch(set_crawler_api, data=json.dumps(
                data), headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set Crawler Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Crawler Failed......', exc_info=True)

    def set_http_auth(self, target_id, enabled, username=None, password=None):
        """设置HTTP认证信息

        Args:
            target_id (string): 目标ID
            enabled (bool): 启用True, 关闭False
            username (string, optional): 用户名
            password (string, optional): 密码

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_http_auth_api = f'{self.targets_api}/{target_id}/configuration'
        data = {
            'authentication': {
                'enabled': enabled
            }
        }
        if enabled:
            data['authentication']['username'] = username
            data['authentication']['password'] = password
        try:
            response = requests.patch(set_http_auth_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set HTTP Auth Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set HTTP Auth Failed......', exc_info=True)
            return False

    def set_http_cert(self, target_id):
        set_http_cert_api = f'{self.targets_api}/{target_id}/client_certificate'
        pass

    def upload_http_cert(self, upload_url):
        pass

    def set_http_cert_password(self, target_id, client_certificate_password):
        """设置客户端证书密码

        Args:
            target_id (string): 目标ID
            client_certificate_password (string): 密码

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_http_cert_password_api = f'{self.targets_api}/{target_id}/configuration'
        data = {
            'client_certificate_password': client_certificate_password
        }
        try:
            response = requests.patch(set_http_cert_password_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set HTTP Cert Password Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error(
                'Set HTTP Cert Password Failed......', exc_info=True)
            return False

    def set_proxy(self, target_id, enabled, proxy_info=None):
        """设置代理

        Args:
            target_id (string): 目标ID
            enabled (bool): 启用True, 关闭False
            proxy_info (dict, optional): {'address': '', 'protocol': '', 'port': '', 'username': '', 'password': ''}

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_proxy_api = f'{self.targets_api}/{target_id}/configuration'
        data = {
            'proxy': {
                'enabled': enabled
            }
        }
        if enabled:
            data['proxy']['address'] = proxy_info['address']
            data['proxy']['protocol'] = proxy_info['protocol']
            data['proxy']['port'] = proxy_info['port']
            data['proxy']['username'] = proxy_info['username']
            data['proxy']['password'] = proxy_info['password']
        try:
            response = requests.patch(set_proxy_api, json=data, headers=self
                                      .auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set Proxy Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Proxy Failed......', exc_info=True)

    def set_advance(self, target_id, technologies, custom_headers, custom_cookies, excluded_hours_id, debug=False, issue_tracker_id=''):
        """高级设置

        Args:
            target_id (string): 目标ID
            issue_tracker_id (TYPE): Description
            technologies (list): 目标相关技术
            custom_headers (list): 自定义HTTP头
            custom_cookies (list): 自定义Cookie
            debug (bool): 启用True, 关闭False
            excluded_hours_id (string): 非扫描时段, 如果为空，则使用默认值

        Returns:
            接口请求成功返回空，失败返回错误信息
            该函数成功返回True, 失败返回False
        """
        set_advance_api = f'{self.targets_api}/{target_id}/configuration'
        data = {
            'issue_tracker_id': issue_tracker_id,
            'technologies': technologies,
            'custom_headers': custom_headers,
            'custom_cookies': custom_cookies,
            'debug': debug,
            'excluded_hours_id': self.excluded_hours_dict.get(excluded_hours_id)
        }
        try:
            response = requests.patch(set_advance_api, json=data, headers=self.auth_headers, verify=False)
            if not response.text:
                return True
            else:
                self.logger.error(f'Set Proxy Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Set Proxy Failed......', exc_info=True)
