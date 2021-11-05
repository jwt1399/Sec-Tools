#!/usr/bin/python3 
# -*- coding:utf-8 -*-

import socket
from urllib.parse import urlparse

result_data = ''

def doSendOne(ip,port,data):
    sock=None
    res=None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(7)
        server_addr = (ip, int(port))
        sock.connect(server_addr)
        sock.send(data)
        res = sock.recv(20)
        if b'GIOP' in res:
            return True
    except Exception as e:
        pass
    finally:
        if sock!=None:
            sock.close()
    return False
g_bPipe=False
def poc(url):
    global g_bPipe
    global result_data
    try:
        oH=urlparse(url)
        a=oH.netloc.split(':')
        port=80
        if 2 == len(a):
            port=a[1]
        elif 'https' in oH.scheme:
            port=443
        if doSendOne(a[0],port,bytes.fromhex('47494f50010200030000001700000002000000000000000b4e616d6553657276696365')):
            print('[+] found CVE-2020-2551 ', oH.netloc)
            return True
        elif g_bPipe == False:
            print('[-] not found CVE-2020-2551 ', oH.netloc)
            return False
    except:
        return False

if __name__=='__main__':
    import datetime
    start = datetime.datetime.now()
    print(poc('http://127.0.0.1:7001'))
    end = datetime.datetime.now()
    print(end - start)
