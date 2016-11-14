# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.db import models

# Create your models here.
TYPE_OF_TITLE = (
    ('', ''),
    ('Американский футбол','Американский футбол'),
    ('Баскетбол','Баскетбол'),
    ('Бейсбол','Бейсбол'),
    ('Биатлон','Биатлон'),
    ('Бильярд','Бильярд'),
    ('Боевые искусства','Боевые искусства'),
    ('Бокс','Бокс'),
    ('Воллейбол','Воллейбол'),
    ('Гольф','Гольф'),
    ('Дарст', 'Дарст'),
    ('Крикет','Крикет'),
    ('Лыжный спорт','Лыжный спорт'),
    ('Настольный теннис','Настольный теннис'),
    ('Регби', 'Регби'),
    ('Теннис', 'Теннис'),
    ('Футбол', 'Футбол'),
    ('Формула 1','Формула 1'),
    ('Хоккей', 'Хоккей'),
)
TYPE_OF_NEWS = (
    (0, 'Ordinary'),
    (1, 'Important'),
)

Noned = ''
Amkar = 'Амкар'
Anzhi = 'Анжи'
Arsenal = 'Арсенал'
Zenit = 'Зенит'
Krasnodar = 'Краснодар'
KrSov = 'Крылья Советов'
Lokomotiv = 'Локомотив'
Orenburg = 'Оренбург'
Rostov = 'Ростов'
Rubin = 'Рубин'
Spartak = 'Спартак'
Terek = 'Терек'
Tom = 'Томь'
Ural = 'Урал'
Ufa = 'Уфа'
CSKA = 'ЦСКА'

TYPE_OF_TEAM = (
    (Noned, ''),
    (Amkar, 'Амкар'),
    (Anzhi, 'Анжи'),
    (Arsenal, 'Арсенал'),
    (Zenit, 'Зенит'),
    (Krasnodar, 'Краснодар'),
    (KrSov, 'Крылья Советов'),
    (Lokomotiv, 'Локомотив'),
    (Orenburg, 'Оренбург'),
    (Rostov, 'Ростов'),
    (Rubin, 'Рубин'),
    (Spartak, 'Спартак'),
    (Terek, 'Терек'),
    (Tom, 'Томь'),
    (Ural, 'Урал'),
    (Ufa, 'Уфа'),
    (CSKA, 'ЦСКА'),
)
TYPE_OF_TOUR = tuple([(v, v) for v in range(0, 31)])




class News(models.Model):
    title = models.CharField(max_length=200, default='', choices=TYPE_OF_TITLE)
    shorttext = models.CharField(max_length=2000)
    fulltext = models.CharField(max_length=10000)
    type_of_news = models.SmallIntegerField(default=0, choices=TYPE_OF_NEWS)




    def __unicode__(self):
        return "%s" % self.title


class RfplSeazon(models.Model):
    firstteam = models.CharField(max_length=200, default=Noned, choices=TYPE_OF_TEAM)
    secondteam = models.CharField(max_length=200, default=Noned, choices=TYPE_OF_TEAM)
    dateofmatch = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return "%s %s" % (self.firstteam, self.secondteam)


