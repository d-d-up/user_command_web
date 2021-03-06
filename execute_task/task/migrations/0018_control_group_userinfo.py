# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_task_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, verbose_name='权限对应代码')),
                ('name', models.CharField(max_length=32, verbose_name='权限名称')),
            ],
            options={
                'verbose_name_plural': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='组名')),
                ('to_control', models.ManyToManyField(blank=True, to='task.Control', verbose_name='权限选择')),
            ],
            options={
                'verbose_name_plural': '权限组表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('passwd', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('to_control', models.ManyToManyField(blank=True, to='task.Control', verbose_name='权限的选择')),
                ('to_group', models.ManyToManyField(blank=True, to='task.Group', verbose_name='组的选择')),
            ],
            options={
                'verbose_name_plural': '用户权限',
            },
        ),
    ]
