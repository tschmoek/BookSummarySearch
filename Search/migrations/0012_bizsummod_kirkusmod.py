# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-03 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0011_auto_20170527_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='BizSumMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True, unique=True)),
                ('url', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KirkusMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True, unique=True)),
                ('url', models.TextField(null=True)),
            ],
        ),
    ]
