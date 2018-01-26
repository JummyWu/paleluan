# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 13:37
from __future__ import unicode_literals

import content.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='故障简述')),
                ('level', models.IntegerField(choices=[(0, '非常严重'), (1, '严重'), (2, '中等'), (3, '一般'), (4, '无影响')], verbose_name='故障级别')),
                ('effect', models.TextField(blank=True, verbose_name='故障影响')),
                ('reasons', models.TextField(blank=True, null=True, verbose_name='故障原因')),
                ('solution', models.TextField(blank=True, null=True, verbose_name='解决方案')),
                ('status', models.IntegerField(choices=[(0, '处理中'), (1, '已恢复'), (2, '改进中'), (3, '已完结')], verbose_name='故障状态')),
                ('improve', models.IntegerField(choices=[(0, '开发'), (1, '运维'), (2, '机房'), (3, '网络运营商'), (4, '第三方')], verbose_name='主导改进')),
                ('content', models.TextField(blank=True, verbose_name='故障分析')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fms_project', to='accounts.Project', verbose_name='影响项目')),
            ],
            options={
                'permissions': (('get_content', '查看故障列表'), ('add_content', '添加故障'), ('edit_content', '编辑故障'), ('del_content', '删除故障')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, null=True, storage=content.storage.images_storage(), upload_to='img/%Y/%m/%d')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='故障类型')),
            ],
            options={
                'permissions': (('add_type', '添加故障类型'), ('edit_content', '编辑故障类型'), ('del_content', '删除故障类型')),
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fms_type', to='content.Type', verbose_name='故障类型'),
        ),
    ]
