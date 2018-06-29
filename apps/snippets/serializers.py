# -*- coding: utf-8 -*-
from django.contrib.auth.models import User,Group
from apps.snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES
from apps.snippets.models import Snippet

__author__ = 'hzl'
__date__ = '202018/6/27 20:49'

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')