# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib.auth.decorators import login_required

# 接收POST请求数据
@login_required
def search_post(request):
    import os

    parm = []  # 勾选参数列表
    base_file_path = 'dirscan/dirsearch/reports/target.json'  # json文件地址
    fixes = {}
    if request.POST:
        # 获取用户输入的url
        enter_url = ' -u ' + request.POST.get('url') + ' '
        # 获取用户选择的参数，存入列表
        parm.append(request.POST.get('php'))
        parm.append(request.POST.get('asp'))
        parm.append(request.POST.get('jsp'))
        parm.append(request.POST.get('txt'))
        parm.append(request.POST.get('zip'))
        parm.append(request.POST.get('html'))
        parm.append(request.POST.get('js'))

        p = ''
        for parm in parm:
            if parm is not None:
                parm = parm + ','
                p = parm + p
        options = ' -e ' + p[:-1]

        # 递归扫描
        recursive = ''
        if request.POST.get('r_check') == "r_yes":
            recursive = '-r' + ' '

        # 前后缀
        # 前缀
        pre_num = 1
        pre = ''
        while request.POST.get('prefixe_' + str(pre_num)) is not None and request.POST.get(
                'prefixe_' + str(pre_num)) != '':
            pre = request.POST.get('prefixe_' + str(pre_num)) + ',' + pre
            pre_num = pre_num + 1
        if pre != '' and pre != ',':
            pre = '--prefixes ' + pre[:-1] + ' '
        else:
            pre = pre[:-1]

        # 后缀
        suf_num = 1
        suf = ''
        while request.POST.get('suffixe_' + str(suf_num)) is not None and request.POST.get(
                'suffixe_' + str(suf_num)) != '':
            suf = request.POST.get('suffixe_' + str(suf_num)) + ',' + suf
            suf_num = suf_num + 1
        if suf != '' and suf != ',':
            suf = '--suffixes ' + suf[:-1] + ' '
        else:
            suf = suf[:-1]

        # 指定子目录扫描
        s_num = 1
        subdir = ''
        # print(request.POST.get('subdirs_' + str(s_num)))
        # print(request.POST.get('subdirs_3'))
        while request.POST.get('subdirs_' + str(s_num)) is not None and request.POST.get(
                'subdirs_' + str(s_num)) != '':
            subdir = request.POST.get('subdirs_' + str(s_num)) + '/,' + subdir
            s_num = s_num + 1

        if subdir != '/,' and subdir != '':
            subdir = '--subdirs ' + subdir[:-1] + ' '
        else:
            subdir = subdir[:-2]

        # 清空上次扫描数据
        open(base_file_path, 'w').close()
        # 基础命令拼接
        c = 'python dirscan/dirsearch/dirsearch.py' + \
            options + enter_url + recursive + pre + suf + subdir + \
            '--json-report ' + base_file_path
        print(c)
        os.system(c)

    return render(request, "dir-scan.html", fixes)


