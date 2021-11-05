#-*- coding =utf-8 -*-
#@Time:2020/12/20 15:25
#@Author:简简
#@File：url.py
#@software:PyCharm

from django.urls import path
from django.views.generic import TemplateView


from webscan import views


urlpatterns = [
    # 欢迎页
    path('', views.welcome, name='welcome'),
    #首页
    path('index', views.index, name='index'),
    #文档页
    path('docs', views.docs, name='docs'),
    # 关于
    path('about', views.about, name='about'),
    # 端口扫描
    path('portscan', views.portscan, name='portscan'),
    #信息泄露
    path('infoleak', views.infoleak, name='infoleak'),
    # 旁站扫描
    path('webside', views.webside, name='webside'),
    #测试
    path('test', views.test, name='test'),
    path('testfp', views.testfp, name='testfp'),
    #导航
    path('navigation', views.navigation, name='navigation'),
    # 指纹识别
    path('fingerprint', views.fingerprint, name='fingerprint'),
    #子域名探测
    path('subdomain', views.subdomain, name='subdomain'),
]

