# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    url(r'^in/$', views.import_data, name='import_data'),
)
