# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.

from accounts.models import User


class UploadFile(models.Model):
    filename = models.FileField(upload_to="./upload/%Y/%m")
    user_u = models.ForeignKey(User,verbose_name=u'谁上传的文件')
    date_t = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = u"上传文件"
        verbose_name_plural = verbose_name


class ExecFile(models.Model):

    majors= models.CharField(max_length=20,verbose_name=u'专业',null=True)
    worktype=models.CharField(max_length=20,verbose_name=u'工作类型',null=True)
    contentc = models.CharField(max_length=64,verbose_name=u'工作内容',null=True)#blank=True,editable=True,
    datet = models.DateField(verbose_name=u'日期',null=True,default=True,editable=True)   ###auto_now=False,auto_now_add=True,
    starttime=models.TimeField(verbose_name=u'开始时间',null=True,default=True,editable=True)
    lengtime=models.TimeField(verbose_name=u'时间长度',null=True,default=True,editable=True)
    networkn = models.CharField(max_length=128,verbose_name=u'涉及网元',null=True)
    department_name = models.CharField(max_length=64,verbose_name=u'工作发起人(部门/名字)',null=True)
    head =models.CharField(max_length=20,verbose_name=u'互联网室负责人',null=True)
    announeoms = models.CharField(max_length=20, verbose_name=u'涉及的EOMS公告号',null=True)
    singleeoms=models.CharField(max_length=2048,verbose_name=u'涉及的EOMS单号',null=True)
    enforcer = models.CharField(max_length=20,verbose_name=u'工作实施人',null=True)
    remark=  models.CharField(max_length=20,verbose_name=u'备注',null=True)

    class Meta:
        verbose_name = u"excel表格信息"
        verbose_name_plural = verbose_name