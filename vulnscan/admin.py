from django.contrib import admin
from .models import Middleware_vuln
from import_export.admin import ImportExportModelAdmin
# Register your models here.



# 中间件扫描
@admin.register(Middleware_vuln)
class Middleware_vulnAdmin(ImportExportModelAdmin):
    list_display = ['id','url','status','result','CVE_id','time']
    search_fields = ('url','status')
    readonly_fields = ('id','url','status','result','CVE_id','time')
