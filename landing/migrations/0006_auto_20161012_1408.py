# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-12 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20161012_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='type_of_news',
            field=models.SmallIntegerField(choices=[(0, 'Ordinar'), (1, 'Other')], default=0),
        ),
    ]
