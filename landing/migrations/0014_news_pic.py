# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-14 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_remove_news_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.CharField(choices=[('n', ''), ('football', models.ImageField(upload_to='../core/static/img/visual1.jpg')), ('hockey', models.ImageField(upload_to='../core/static/img/visual2.png'))], default='n', max_length=200),
        ),
    ]