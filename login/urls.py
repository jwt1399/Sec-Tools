

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('login_out/', views.login_out, name="login_out"),
    path('register/', views.register, name="register"),
    path('password-reset/', include('password_reset.urls'), name='password_reset'),
]
