from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Item,FingerPrint,FpCategory,PortList
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    '''欢迎页'''
    return render(request, 'other/welcome.html')

def index(request):
    '''主页'''
    cms_items = FingerPrint.objects.all()
    categories =FpCategory.objects.all()
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    items = Item.objects.all()
    # 需要传递给模板（templates）的对象

    context ={
        'cms_items':cms_items,
        'categories':categories,
        'category_nav': category_nav,
        'items': items,
    }
    return render(request, 'other/index.html',context)

def about(request):
    '''关于'''
    return render(request, 'other/about.html')

def docs(request):
    '''文档'''
    return render(request, 'other/docs.html')


def navigation(request):
    '''安全导航'''
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    items = Item.objects.all()
    # 需要传递给模板（templates）的对象
    context = {
        'category_nav': category_nav,
        'items': items,
    }
    return render(request, 'other/navigation.html', context)

def test(request):
        return HttpResponse("Hello World!")

def testfp(request):
    '''测试指纹'''
    # 取出要添加到导航栏的分类
    category_nav = Category.objects.filter(add_menu=True).order_by('sort')
    # 取出条目
    # 需要传递给模板（templates）的对象
    context = {
        'category_nav': category_nav,
    }
    return render(request, 'other/testfp.html', context)

@login_required
def fingerprint(request):
    '''指纹识别'''
    cms_items = FingerPrint.objects.all()
    categories =FpCategory.objects.all()
    context ={
        'cms_items':cms_items,
        'categories':categories,

    }
    return render(request, 'scan/scan_fingerprint.html',context)

@login_required
def portscan(request):
    '''端口扫描'''
    portlists = PortList.objects.all()
    context = {'portlists': portlists}
    return render(request, 'scan/scan_portscan.html',context)


@login_required
def infoleak(request):
    '''信息泄露'''
    return render(request, 'scan/scan_infoleak.html')

@login_required
def webside(request):
    '''旁站扫描'''
    return render(request, 'scan/scan_webside.html')

@login_required
def subdomain(request):
    '''子域名扫描'''
    return render(request, 'scan/scan_subdomain.html')