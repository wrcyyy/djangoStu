# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : djangoStu
@Time    : 2021/3/4 16:46
@Auth    : wrc
@Email   : wangrc@inhand.com.cn
@File    : urls.py
@IDE     : PyCharm
------------------------------------
"""
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
