# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170904_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', verbose_name='创建者'),
        ),
    ]