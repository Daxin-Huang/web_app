from django.urls import path,re_path

from . import views

urlpatterns = [
        # 主页
        path('', views.index, name='index'),

        # 显示所有Topic的页面
        path('topics/', views.topics, name='topics'),

        # 显示特定的Topic下的所有Entry
        re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        ]
