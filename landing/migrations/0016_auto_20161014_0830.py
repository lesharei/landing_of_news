# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-14 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0015_auto_20161014_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.CharField(choices=[(models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/button.png'), models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/button.png')), (models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/visual1.jpg'), models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/visual1.jpg')), (models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/visual2.png'), models.ImageField(default='../core/static/img/button.png', upload_to='../core/static/img/visual2.png'))], default='n', max_length=200),
        ),
    ]
