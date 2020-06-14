"""定义了应用的url模式"""
from django.urls import path,re_path

from . import views

urlpatterns = [
        # 主页
        path('', views.index, name='index'),

        # 显示所有Topic的页面
        path('topics/', views.topics, name='topics'),

        # 显示特定的Topic下的所有Entry
        re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

        # 显示添加新topic的表单
        path('new_topic/', views.new_topic, name='new_topic'),

        # 显示添加新Entry的表单
        re_path(r'new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

        # 编辑条目的页面
        re_path(r'edit_entry/(?P<entry_id>\d+)/', views.edit_entry,name='edit_entry'),
        ]
