#-*- coding =utf-8 -*-
#@Time:2021/3/4 17:49
#@Author:简简
#@File：iplocating.py
#@software:PyCharm


# -*- coding:utf-8 -*-
from ast import literal_eval
import requests



def get_locating(ip):
    """
    获取ip归属地
    """
    api_url = 'http://freeapi.ipip.net/'
    try:
        res = requests.get(api_url+ip, timeout=4)
        result_str = literal_eval(res.text)
        # result_str = (result[0])
        # print(result)
        # result_str = '国家({})，省份({})，城市({})'.format(result[0],result[1],result[2])
    except Exception as e:
        result_str = '获取数据失败，请稍后再试'
        print(result_str)
    return result_str


if __name__ == '__main__':
    print(get_locating('139.224.112.182'))



