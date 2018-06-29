# -*- coding: utf-8 -*-
__author__ = 'hzl'
__date__ = '202018/6/28 16:15'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from onestart_rest import views

urlpatterns = [
    url('^snippets/$', views.snippet_list),
    url('^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)  ## 作用是提供一种简单干净的方式来应用特定的格式
