# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User


# Create your models here.


class ServerGroup(models.Model):
    # 资产组信息
    name = models.CharField(max_length=64, unique=True, verbose_name=u'资产组名')
    created_by = models.ForeignKey(User, null=True, verbose_name=u'创建者')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=u'创建时间')
    comment = models.TextField(blank=True, verbose_name=u'描述')

    def __unicode__(self):
        return self.name

    __str__ = __unicode__
    class Meta:
        verbose_name = u'资产'
        verbose_name_plural = verbose_name

class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'机房名称')
    bandwidth = models.CharField(
        max_length=32, blank=True, verbose_name=u'带宽')
    contact = models.CharField(
        max_length=128, blank=True, verbose_name=u'联系人')
    phone = models.CharField(max_length=32, blank=True,
                             verbose_name=u'手机')
    address = models.CharField(
        max_length=128, blank=True, verbose_name=u'地址')
    intranet = models.TextField(blank=True, verbose_name=u'内网')
    extranet = models.TextField(blank=True, verbose_name=u'外网')
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=u'创建时间')
    operator = models.CharField(
        max_length=32, blank=True, verbose_name=u'运营商')
    created_by = models.ForeignKey(User, null=True, verbose_name=u'创建者')
    comment = models.TextField(blank=True, verbose_name=u'描述')

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = verbose_name

class Server(models.Model):
    # 服务器信息
    in_ip = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name=u'内网IP')  # 内网ip
    idc = models.ForeignKey(IDC, blank=True, null=True, related_name='servers', on_delete=models.SET_NULL,
                            verbose_name=u'IDC')
    groups = models.ManyToManyField(ServerGroup, blank=True, related_name='servers', verbose_name=u'资产组')
    ex_ip = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'外网IP')  # 弹性ip
    project_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'项目名称')
    host_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'主机名')
    service_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'服务名')
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'位置')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    author = models.ForeignKey(User, null=True, verbose_name=u'创建者')

    cpu_model = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'CPU型号')
    cpu_cores = models.IntegerField(null=True, blank=True, verbose_name=u'CPU核数')
    cpu_count = models.IntegerField(null=True, blank=True, verbose_name=u'CPU个数')

    mem = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'内存')
    disk = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'磁盘')
    os_version = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'系统版本')
    os_kernel = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'系统内核')
    status = models.NullBooleanField(default=False, null=True, blank=True, verbose_name=u'运行状态')
    max_open_files = models.IntegerField(null=True, blank=True, verbose_name=u'最大打开文件数')
    uptime = models.IntegerField(null=True, blank=True, verbose_name=u'在线时间（天）')

    def __unicode__(self):
        return '%s - %s' % (self.in_ip, self.host_name)

    class Meta:
        verbose_name = u'服务器信息'
        verbose_name_plural = verbose_name

class Service(models.Model):
    '''
                服务
    '''
    server = models.ForeignKey(Server, verbose_name=u'服务器')
    port = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'端口')
    service_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'服务名')

    def __unicode__(self):
        return '%s - %s - %s' % (self.server.in_ip, self.port, self.service_name)

    class Meta:
        verbose_name = u'服务'
        verbose_name_plural = verbose_name
