# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20171108_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idc',
            options={'verbose_name': '机房', 'verbose_name_plural': '机房'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name': '服务器信息', 'verbose_name_plural': '服务器信息'},
        ),
        migrations.AlterModelOptions(
            name='servergroup',
            options={'verbose_name': '资产', 'verbose_name_plural': '资产'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '服务', 'verbose_name_plural': '服务'},
        ),
    ]