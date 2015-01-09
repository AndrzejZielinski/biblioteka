# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from srkob import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^genre/$', views.genre, name ='genre'),
        url(r'^register/$', views.register, name='register'),
        url(r'^genre_details/(?P<genre_name_url>\w+)/$', views.genre_details, name='genre_details'),)  # New!


