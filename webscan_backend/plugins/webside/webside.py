# -*- coding:utf-8 -*-

import requests
import json

header = {
    'Host': 'api.webscan.cc',
    'Origin': 'http://webscan.cc',
    'Pragma': 'no-cache',
    'Referer': 'http://webscan.cc/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132'
}


def get_side_info(ip):
    """
    获取旁站信息
    :param ip:
    :return:
    """
    api_url = 'http://api.webscan.cc/'
    query_data = {
        'action': 'query',
        'ip': ip
    }
    try:
        html = requests.post(api_url, data=query_data, headers=header, timeout=8)
        text = html.text
        # 去掉text首部的BOM字符
        if text.startswith(u'\ufeff'):
            text = text.encode('utf8')[3:].decode('utf8')
        # 检查返回内容是否为空
        if text.find('null') > -1:
            return False
        else:
            return json.loads(text)
    except Exception as e:
        pass  # 空语句
    return False
