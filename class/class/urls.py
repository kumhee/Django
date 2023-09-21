"""
URL configuration for class project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # '/admin/' 경로로 접근하면 Django 관리자 페이지로 이동
    path('board/', include('board.urls')), 
    # '/board/' 경로로 접근하면 'board' 애플리케이션의 URL 설정을 포함하도록 include 함수를 사용
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>', views.post_datail, name='post_datail')
]
