"""
URL configuration for bookapp project.

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
<<<<<<< HEAD:back/bookapp/urls.py
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls"))
=======
from django.urls import path
from .view import api_login
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login/', api_login, name='api_login'),
>>>>>>> 66beba28b905f6c27aadbc8885f051adb9114d1b:api/back/bookapp/urls.py
]
