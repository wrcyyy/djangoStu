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
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
