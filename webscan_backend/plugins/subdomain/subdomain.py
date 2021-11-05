# -*- coding:utf-8 -*-
#!/usr/bin/python
import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
    'Referer': 'http://www.baidu.com/',
}

def get_subdomain(domain):
    requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    res = requests.get('http://site.ip138.com/{}/domain.htm'.format(domain), headers=headers)
    p = re.compile(r'target="_blank">(.*?)</a></p>')
    sub = p.findall(res.text)
    print(sub)
    if (len(sub) == 0):
        print('[+] ip138接口可能出现问题!')
    return sub
if __name__ == '__main__':
    print(get_subdomain('baidu.com'))



