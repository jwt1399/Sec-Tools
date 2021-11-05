import os

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
import json

base_file_path = 'dirscan/dirsearch/reports/target.json'

@login_required
def dirresult(request):
    if os.access(base_file_path, os.F_OK):
        f = open(base_file_path)
        data = json.load(f)  # json被转换为python字典

        # 获取扫描url的端口等信息，将字典的键转为集合
        k = set(data)
        # 移除集合中的time
        # k.remove('time')
        # 安全移除time
        k.discard('time')
        # 键值集合转为列表
        key_list = list(k)

        # 计数
        n = 0
        for key in data:
            n = n + 1
        # 列表合一
        a = []
        num = 0
        for key in data:
            num = num + 1
            if num < n:
                a = a + data[key]
        print({"a": a, "key_list": key_list})
        return render(request, "dir-result.html", {"a": a, "key_list": key_list})
    else:
        error = "暂无结果"
        return render(request, "dir-result.html", {"error": error})
