# coding: utf-8

from rest_framework import viewsets
from rest_framework import serializers

from onecloud.models import Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    provider_name = serializers.CharField(source='provider.name')

    class Meta:
        model = Service
        fields = ('name', 'provider_name', 'cpu', 'memory', 'disk', 'price')


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.select_related('provider').all()
    serializer_class = ServiceSerializer
