
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# -*- coding:utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from .plugins.common.common import success, error, addslashes, getdomain, getdomainip, check_ip, check_url
import time
from .plugins.common.common import getuserip
from .plugins.loginfo.loginfo import LogHandler
MYLOGGER = LogHandler(time.strftime("%Y-%m-%d", time.localtime()) + 'log')


@csrf_exempt     # 标识一个视图可以被跨域访问
@login_required  # 用户登陆系统才可以访问
def port_scan(request):
    """
    获取开放端口列表
    """
    from .plugins.portscan.portscan import ScanPort
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = ScanPort(ip).pool()
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok!')
    return error(400, '请填写正确的IP地址', 'error')

@csrf_exempt
def info_leak(request):
    """
    信息泄漏检测
    """
    from .plugins.infoleak.infoleak import get_infoleak
    url = check_url(request.POST.get('url'))
    if url:
        result = get_infoleak(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')

@csrf_exempt
def getwebsideinfo(request):
    """
    获取旁站信息
    """
    from .plugins.webside.webside import get_side_info
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = get_side_info(ip)
        if result:
            return success(200, result, 'ok')
        return error(400, '未找到旁站信息！', 'error')
    return error(400, '请填写正确的IP地址', 'error')

@csrf_exempt
def baseinfo(request):
    """
    返回网站的基本信息接口
    """
    from .plugins.baseinfo.baseinfo import getbaseinfo
    url = check_url(request.POST.get('url'))
    if url:
        res = getbaseinfo(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(res))
        return success(res['code'], res, res['msg'])
    return error(400, '请填写正确的URL地址', '请输入正确的网址， 例如：http://example.cn')

@csrf_exempt
def webweight(request):
    """
    获取网站权重
    """
    from .plugins.webweight.webweight import get_web_weight
    url = check_url(request.POST.get('url'))
    if url:
        result = get_web_weight(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')


@csrf_exempt
def iplocating(request):
    """
    ip定位
    """
    from .plugins.iplocating.iplocating import get_locating
    ip = request.POST.get('ip')
    if check_ip(ip):
        result = get_locating(ip)
        return success(200, result, 'ok')
    return error(400, '请填写正确的IP地址', 'error')

@csrf_exempt
def isexistcdn(request):
    """
    判断当前域名是否使用了CDN
    """
    from .plugins.cdnexist.cdnexist import iscdn
    url = check_url(request.POST.get('url'))
    if url:
        result_str = iscdn(url)
        if result_str == '目标站点不可访问':
            return success(200, result_str, '网络错误')
        if result_str:
            result_str = '存在CDN（源IP可能不正确）'
        else:
            result_str = '无CDN'
        return success(200, result_str, 'Success!')
    return error(400, '请填写正确的IP地址', 'error')

@csrf_exempt
def is_waf(request):
    """
    判断当前域名是否使用了WAF
    """
    from .plugins.waf.waf import getwaf
    url = check_url(request.POST.get('url'))
    if url:
        return success(200, getwaf(url), 'ok')
    return error(400, '请填写正确的URL地址', 'error')

@csrf_exempt
def what_cms(request):
    """
    判断当前域名使用了什么框架，cms等指纹信息
    """
    from .plugins.whatcms.whatcms import getwhatcms
    url = check_url(request.POST.get('url'))
    if url:
        result = getwhatcms(url)
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(
            request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')

@csrf_exempt
def _subdomain(request):
    '''子域名扫描'''
    from .plugins.subdomain.subdomain import get_subdomain
    domain = request.POST.get('domain')
    print(domain)
    if domain:
        result = get_subdomain(domain)
        print(len(result))
        MYLOGGER.info('M:' + request.method + ' P:' + request.path + ' UPOST:' + str(request.POST) + ' SC:200 UIP:' + getuserip(request) + ' RDATA:' + str(result))
        return success(200, result, 'ok')
    return error(400, '请填写正确的URL地址', 'error')


