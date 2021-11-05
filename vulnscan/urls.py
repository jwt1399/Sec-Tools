from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('vulnscan', views.vulnscan, name="vulnscan"),
    # path('vulnscantest', views.vulnscantest, name="vulnscantest"),
    path('vuln_scan', views.vuln_scan, name='vuln_scan'),
    path('test1', views.get_vuln_rank, name='test1'),
    path('get_vuln_rank',views.get_vuln_rank, name='get_vuln_rank'),
    path('get_vuln_value',views.get_vuln_value, name='get_vuln_value'),
    path('Middleware_scan', views.Middleware_scan, name='Middleware_scan'),
    path('start_Middleware_scan', views.start_Middleware_scan, name='start_Middleware_scan'),
    path('test2',views.test2, name='test2')

]

target_ids = views.get_target_id()
vuln_ids = views.get_vuln_id()
for target_id in target_ids:
    urlpatterns.append(url(r'^vuln_result/(?P<target_id>.*)$', views.vuln_result, name = 'vuln_result/'+target_id))
for vuln_id in vuln_ids:
    urlpatterns.append(url(r'^vuln_detail/(?P<vuln_id>.*)$', views.vuln_detail, name='vuln_detail/' + vuln_id))


