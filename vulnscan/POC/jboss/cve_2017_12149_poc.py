##!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import sys


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0",
    'Accept': "*/*",
    'Content-Type': "application/json",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "close",
    'Cache-Control': "no-cache"
}

def poc(url):
    vulurl = url + "/invoker/readonly"
    try:
        r =requests.post(vulurl, headers=headers, verify=False)
    except:
        print ("[-] Target "+url+" Not CVE-2017-12149 Good Luck")
    e = r.status_code
    if e == 500:
        print ("[+] Target "+url+" Find CVE-2017-12149  EXP:https://github.com/zhzyker/exphub")
        return True
    else:
        print ("[-] Target "+url+" Not CVE-2017-12149 Good Luck")
    return False

if __name__ == "__main__":
    poc("http://127.0.0.1:8080/")

