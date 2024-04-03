"""
URL configuration for foodMenu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_views.register, name='register'),

    # 在 Django 中，类视图是一种处理请求和生成响应的方法，它们基于类而不是函数。
    # 类视图提供了一种更加面向对象的方式来组织视图逻辑，并且可以利用类的继承和方法重写等特性来实现更加复杂的逻辑。
    # 在给定的代码中，auth_views.LoginView 就是一个类视图，它负责处理用户登录的逻辑。通过调用 .as_view() 方法，
    # 将这个类视图转换为可调用的视图，以便在 URL 配置中使用。
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    # 老师这个写法只能通过post请求进行logout，所以注释掉
    # path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    # 用这个
    path('logout/', user_views.logout_view, name='logout'),

    path('profilepage/', user_views.profilepage, name='profilepage')
]
