# -*- coding:utf-8 -*-
import requests
import json
from ..common.common import getdomain

def get_web_weight(domain):
    """
    获取网站权重
    :param domain:
    :return:
    """
    #api_url = 'https://api.ooopn.com/rank/aizhan/api.php?url='
    api_url = "https://apistore.aizhan.com/baidurank/siteinfos/[37c7d94115d0c84a46527e7689a2ab72]?domains="
    try:
        res = requests.get(api_url+getdomain(domain), timeout=4)
        res_json = json.loads(res.text)
        #result_str = '百度({})，Google({})，搜狗({})  --数据来源于aizhan.com'.format(res_json['bdm'], res_json['google'], res_json['sogou'])
        result_str = 'PC权重({})，移动权重({})，预计来路({})  --数据来源于aizhan.com'.format(res_json["data"]["success"][0]["pc_br"], res_json["data"]["success"][0]["m_br"], res_json["data"]["success"][0]["ip"])
    except Exception as e:
        result_str = '获取数据失败，请稍再试'
    return result_str


if __name__ == '__main__':
    print(get_web_weight('https://jwt1399.top/'))
