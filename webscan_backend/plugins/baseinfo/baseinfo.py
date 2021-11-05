# -*- coding:utf-8 -*-
import requests
import socket
import json
from ..common.common import getdomain
from ..randheader.randheader import get_ua


def get_ip_list(domain):
    """
    获取域名解析的IP列表
    :param domain:
    :return:
    """
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_str = item[4][0] + get_ip_addr(item[4][0])
                ip_list.append(ip_str)
    except Exception as e:
        ip_list = ['server error']
    return ip_list


def get_ip_addr(ip):
    result_str = ' (未查询到物理地址)  '
    try:
        res = requests.get('http://ip-api.com/json/'+ip, timeout=8)
        addr_data = json.loads(res.text)
        if addr_data['status'] == 'success':
            result_str = ' (物理地址: ' + addr_data['country'] + ',' + addr_data['regionName'] + ',' + addr_data['city'] \
                         + ',' + addr_data['as'] + ')  '
    except Exception as e:
        result_str = ' (Server Error)'
    return result_str


def getbaseinfo(url):
    """
    返回IP、中间件、OS、域名、语言
    :param url:
    :return:
    """
    domain = getdomain(url)
    info = {'code': 400, 'msg': '网络错误'}
    if domain:
        try:
            res = requests.get(url, headers=get_ua(), timeout=8)
        except Exception as e:
            res = 0
        if res:
            info['domain'] = domain
            info['server'] = str(res.headers.get('server', 'nothing'))  # 从返回的Header头中获取服务信息
            info['language'] = str(res.headers.get('X-Powered-By', 'nothing'))
            try:
                info['ip'] = get_ip_list(domain)
            except Exception as e:
                info['ip'] = 'Not Found'
            if 'iis' in info['server'].lower():
                info['os'] = "Windows Server"
            else:
                info['os'] = 'Linux'
            info['register'] = 'http://whois.chinaz.com/'+domain
            info['code'] = 200
            info['msg'] = '查询成功'
    return info


if __name__ == '__main__':
    # test
    getbaseinfo('https://jwt1399.top/')