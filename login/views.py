from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as Login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
import json
from .forms import RegisterForm

# Create your views here.

def login(request):
    msg = {
        'site_title': "Sec-tools",
        'site_header': "Sec-tools 登录",
        'error': '',
        'color': 'transparent',
    }
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            msg['error'] = "用户名或密码错误！"
            msg['color'] = "#fef0f0"
        else:
            Login(request, user)
            return redirect("/index")
        # print(user)
        # print(msg)
    return render(request, "login.html", msg)


def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()
            # 注册成功，跳转回首页
            return redirect('/login/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'register.html', context={'form': form})


def login_out(request):
    logout(request)  # 注销
    return redirect("/index")  # 页面跳转


