"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Proyecto.settings import STATIC_URL
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.index, name="index"),
    path('/favicon.ico', views.index, name="inicio"),
    path('blog/', views.blog, name='blog'),
    path('blog/casilla-de-salida/', views.salida, name='salida'),
    path('blog/a-la-montana/', views.montana, name='montana'),
    path('buscador/', views.buscador, name='buscador'), 
    path('prueba1/', views.elFiltro, name='elFiltro'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)