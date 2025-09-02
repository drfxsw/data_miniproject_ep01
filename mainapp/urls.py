"""
URL configuration for mainapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
# 3-1-1
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # 3-1-2
    path("", views.dashboard, name="dashboard"), # 기본 url경로에서 views의 dashboard 함수를 사용
    path("sol/", views.sol, name = "sol"), # sol 이하의 url경로에서 views의 sol 함수를 사용
    path("tack/", views.tack, name = "tack"), # tack 이하의 url경로에서 views의 tack 함수를 사용
    path("jong/", views.jong, name = "jong"), # jong 이하의 url경로에서 views의 jong 함수를 사용
    path('final/', views.final, name='final'),
]
