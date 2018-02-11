"""hda_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from desg_t18 import views
from desg_t18 import urls as desg_app
from automation import urls as automation_app
from pdc import urls as pdc_app
from ldm import urls as ldm_app

app_name='hda_forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('pdc/', include(pdc_app)),
    path('desg/', include(desg_app)),
    path('ldm/', include(ldm_app)),
    path('automation/', include(automation_app)),
    path('admin/', admin.site.urls),


]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
