# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-12 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20161012_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfplseazon',
            name='firstteam',
            field=models.SmallIntegerField(choices=[(0, ''), (1, '\u0410\u043c\u043a\u0430\u0440'), (2, '\u0410\u043d\u0436\u0438'), (3, '\u0410\u0440\u0441\u0435\u043d\u0430\u043b'), (4, '\u0417\u0435\u043d\u0438\u0442'), (5, '\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440'), (6, '\u041a\u0440\u044b\u043b\u044c\u044f \u0421\u043e\u0432\u0435\u0442\u043e\u0432'), (7, '\u041b\u043e\u043a\u043e\u043c\u043e\u0442\u0438\u0432'), (8, '\u041e\u0440\u0435\u043d\u0431\u0443\u0440\u0433'), (9, '\u0420\u043e\u0441\u0442\u043e\u0432'), (10, '\u0420\u0443\u0431\u0438\u043d'), (11, '\u0421\u043f\u0430\u0440\u0442\u0430\u043a'), (12, '\u0422\u0435\u0440\u0435\u043a'), (13, '\u0422\u043e\u043c\u044c'), (14, '\u0423\u0440\u0430\u043b'), (15, '\u0423\u0444\u0430'), (16, '\u0426\u0421\u041a\u0410')], default=0),
        ),
        migrations.AlterField(
            model_name='rfplseazon',
            name='secondteam',
            field=models.SmallIntegerField(choices=[(0, ''), (1, '\u0410\u043c\u043a\u0430\u0440'), (2, '\u0410\u043d\u0436\u0438'), (3, '\u0410\u0440\u0441\u0435\u043d\u0430\u043b'), (4, '\u0417\u0435\u043d\u0438\u0442'), (5, '\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440'), (6, '\u041a\u0440\u044b\u043b\u044c\u044f \u0421\u043e\u0432\u0435\u0442\u043e\u0432'), (7, '\u041b\u043e\u043a\u043e\u043c\u043e\u0442\u0438\u0432'), (8, '\u041e\u0440\u0435\u043d\u0431\u0443\u0440\u0433'), (9, '\u0420\u043e\u0441\u0442\u043e\u0432'), (10, '\u0420\u0443\u0431\u0438\u043d'), (11, '\u0421\u043f\u0430\u0440\u0442\u0430\u043a'), (12, '\u0422\u0435\u0440\u0435\u043a'), (13, '\u0422\u043e\u043c\u044c'), (14, '\u0423\u0440\u0430\u043b'), (15, '\u0423\u0444\u0430'), (16, '\u0426\u0421\u041a\u0410')], default=0),
        ),
    ]
