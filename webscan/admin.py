from django.contrib import admin

from .models import Category,Item,PortList,FpCategory,FingerPrint
from import_export.admin import ImportExportModelAdmin
from django.db import models
from django.forms import TextInput
# Register your models here.

#修改后台管理页面头部显示内容和后台名称
admin.site.site_header = 'Sec-tools 后台'
admin.site.site_title = 'Sec-tools | 后台'


# 导航分类
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['sort','name','add_menu','get_items','icon','icon_data']
    list_editable = ['sort','add_menu','icon']
    search_fields = ('name',)
    list_display_links = ('name',) #设置哪些字段可以点击进入编辑界面

# 导航条目
@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ['title', 'url', 'img_admin','img_width','category']
    list_editable = ['url', 'category','img_width']
    search_fields = ('title', 'url', 'desc')
    list_display_links = ('title',) #设置哪些字段可以点击进入编辑界面
    list_filter = ('category',)  # 过滤器，按字段进行筛选
    list_per_page = 10  # 设置每页显示多少条记录，默认是100条

# 指纹分类
@admin.register(FpCategory)
class ComponentCategory(ImportExportModelAdmin):
    list_display = ['id','name','get_items']
    search_fields = ('name',)
    list_display_links = ('name',) #设置哪些字段可以点击进入编辑界面
    ordering = ('id',)  # 设置默认排序字段，负号表示降序排序

# 常见指纹
@admin.register(FingerPrint)
class ComponentAdmin(ImportExportModelAdmin):
    list_display = ('name','icon_data', 'desc','category')
    list_display_links = ('name',) #设置哪些字段可以点击进入编辑界面
    list_editable = ['category']
    search_fields = ('name', 'desc',)
    list_filter = ('category',)  # 过滤器，按字段进行筛选
    readonly_fields = ('icon_data',)
    ordering = ('name',)  # 设置默认排序字段，负号表示降序排序
    list_per_page = 15
    fieldsets = (
        ('编辑组件', {
            'fields': ('name', 'desc', 'category', 'icon', 'icon_data')
        }),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
    }

# 端口列表
@admin.register(PortList)
class PortListAdmin(ImportExportModelAdmin):
    list_display = ('num', 'service', 'protocol', 'status',)
    list_display_links = ('num',)  # 设置哪些字段可以点击进入编辑界面
    search_fields = ('num', 'service',)
    list_filter = ('protocol','status')  # 过滤器，按字段进行筛选
    ordering = ('num', )#设置默认排序字段，负号表示降序排序
    list_per_page = 15