# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(max_length=32, null=True, verbose_name='用户')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP')),
                ('port', models.CharField(max_length=32, null=True, verbose_name='端口')),
                ('cmd', models.CharField(max_length=128, null=True, verbose_name='命令')),
                ('user', models.CharField(max_length=32, null=True, verbose_name='操作者')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '历史命令',
                'db_table': 'history',
                'verbose_name': '历史命令',
            },
        ),
        migrations.CreateModel(
            name='toolsscript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='工具名称')),
                ('tool_script', models.TextField(blank=True, null=True, verbose_name='脚本')),
                ('tool_run_type', models.IntegerField(choices=[(0, 'shell'), (1, 'python'), (2, 'yml')], default=0, verbose_name='脚本类型')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='工具说明')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '工具',
                'db_table': 'toolsscript',
                'verbose_name': '工具',
            },
        ),
    ]
