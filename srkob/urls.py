# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from srkob import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^genre/$', views.genre, name ='genre'),
        url(r'^register/$', views.register, name='register'),
<<<<<<< HEAD
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
<<<<<<< HEAD
        url(r'^genre_details/(?P<genre_name_url>\w+)/$', views.genre_details, name='genre_details'),
        url(r'^book_details/(?P<book_name_url>\w+)/$', views.book_details, name='book_details'),              
        url(r'^user_profile/$', views.user_profile, name='user_profile'),
        url(r'^rent_details/$', views.user_profile, name='rent_details'),
        url(r'^search/$', views.search, name='search'),)
=======
        url(r'^genre_details/(?P<genre_name_url>\w+)/$', views.genre_details, name='genre_details'),           
		url(r'^book_details/(?P<book_name_url>\w+)/$', views.book_details, name='book_details'),)    
=======
        url(r'^genre_details/(?P<genre_name_url>\w+)/$', views.genre_details, name='genre_details'),)  # New!


>>>>>>> f807e813e81bb82e502257923495b6216a0ba557
>>>>>>> b0ac0410d8acb8012e960cf6db1910b8aca88c54
