from django.test import TestCase

# Create your tests here.


# -*- coding:utf-8 -*-
import requests
import json


# def get_web_weight(domain):
#     """
#     获取网站权重
#     :param domain:
#     :return:
#     """
    #api_url = 'https://api.ooopn.com/rank/aizhan/api.php?url='
api_url = "https://apistore.aizhan.com/baidurank/siteinfos/[37c7d94115d0c84a46527e7689a2ab72]?domains="
res = requests.get(api_url + 'jwt1399.top')
print(res.text)
res_json = json.loads(res.text)
result_str = '百度({})，Google({})，搜狗({})  --数据来源于aizhan.com'.format(res_json['code'], res_json['status'],res_json['status'])
print(res_json)
print(result_str)

print(res_json["data"]["success"][0]["domain"])
print(res_json["data"]["success"][0]["ip"])


    # try:
    #     res = requests.get(api_url+'jwt1399.top', timeout=4)
    #     res_json = json.loads(res.text)
    #     result_str = '百度({})，Google({})，搜狗({})  --数据来源于aizhan.com'.format(res_json['domain'], res_json['pc_br'], res_json['m_br'])
    # except Exception as e:
    #     result_str = '获取数据失败，稍后再试'
    # return result_str


# if __name__ == '__main__':
#     print(get_web_weight('https://jwt1399.top/'))
