# coding: utf-8

from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=80)
    provider = models.ForeignKey(Provider, related_name='services')
    cpu = models.PositiveIntegerField()
    memory = models.PositiveIntegerField(help_text='Memory(Ram) in GB')
    disk = models.PositiveIntegerField(help_text='Disk size in GB')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['price']

    def __unicode__(self):
        return self.name
