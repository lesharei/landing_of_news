# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-14 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_news_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='pic',
        ),
    ]
