# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from landing.views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),

]
