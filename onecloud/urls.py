# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from . import api
from . import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'services', api.ServiceViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
