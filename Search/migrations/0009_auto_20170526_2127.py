# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0008_auto_20170526_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blinkmod',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blinkmod',
            name='url',
            field=models.TextField(null=True),
        ),
    ]