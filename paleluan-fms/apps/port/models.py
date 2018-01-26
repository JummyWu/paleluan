from django.db import models

# Create your models here.


class ssh_port(models.Model):
    name = models.CharField(max_length=40,verbose_name=u'虚拟机名字')
    device_type = models.CharField(max_length=30,verbose_name=u'板卡')
    ip = models.GenericIPAddressField(max_length=20,verbose_name=u'IP')
    username = models.CharField(max_length=30,verbose_name=u'用户名')
    password = models.CharField(max_length=50,verbose_name=u'链接密码')
    port = models.CharField(max_length=8,verbose_name=u'端口')
    secret = models.CharField(max_length=20,verbose_name=u'密匙')
    verbose = models.CharField(max_length=25,default='False',verbose_name=u'默认')

    class Meta:
        verbose_name = u'链接机子的信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        name = self.name


class ssh_command(models.Model):
    name = models.ForeignKey(ssh_port,verbose_name=u'虚拟机')
    command = models.CharField(max_length=200,verbose_name=u'命令')

    class Meta:
        verbose_name = u'命令'
        verbose_name_plural = verbose_name