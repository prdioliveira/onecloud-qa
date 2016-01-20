# coding: utf-8

from django.contrib import admin

from .models import Provider, Service


admin.site.register(Provider)
admin.site.register(Service)
