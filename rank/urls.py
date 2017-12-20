# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^search/', views.search, name='search'),
    #url(r'^$', views.login, name='login'),
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^$', views.show_product, name='show_product'),
    url(r'^commentcreate/(?P<product_slug>[-\w]+)/(?P<order_id>[-\w]+)/$',views.comment_create,name='comment_create'),
    url(r'^show/', 
        views.show_product, 
        name='show_product'),
        #url(r'^remove/(?P<product_id>\d+)/$',
    url(r'^showme/', 
        views.show_me, 
        name='show_me'),
    url(r'^(?P<restaurant_slug>[-\w]+)/$', 
        views.show_product, 
        name='product_list_by_restaurant'),
   
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 
        views.product_detail, 
        name='product_detail')]

    
   # r'^remove/(?P<product_id>\d+)/$'
   # url(r'^show_product/(?P<restaurant_name>[-\w]+)/$', 
       # views.show_product, 
       # name='show_product'),
        