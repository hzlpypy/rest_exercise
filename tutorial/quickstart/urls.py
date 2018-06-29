# -*- coding: utf-8 -*-
__author__ = 'hzl'
__date__ = '202018/6/28 15:16'

from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]

