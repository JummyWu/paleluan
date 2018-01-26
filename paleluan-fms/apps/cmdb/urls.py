# -*- coding: UTF-8 -*-
"""skyoms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cmdb import views, api

urlpatterns = [

    url(r'^server_list/$', views.server_list, name='server_list'),
    url(r'^server_add_page/$', views.server_add_page, name='server_add_page'),
    url(r'^server_add/$', views.server_add, name='server_add'),
    url(r'^server_edit_page/(?P<id>\d+)/$', views.server_edit_page, name='server_edit_page'),
    url(r'^server_edit/$', views.server_edit, name='server_edit'),
    # url(r'^server_detail/(?P<id>\d+)/$', views.server_detail, name='server_detail'),
    url(r'^server_delete/$', views.server_delete, name='server_delete'),
    url(r'^search$', api.server_search, name='server_search'),


    url(r'^server_group/$', views.server_group, name='server_group'),
    url(r'^group_add/$', views.group_add, name='group_add'),
    url(r'^group_edit/$', views.group_edit, name='group_edit'),
    url(r'^group_delete/$', views.group_delete, name='group_delete'),
    url(r'^group_search$', api.group_search, name='group_search'),



    url(r'^server_idc/$', views.server_idc, name='server_idc'),
    url(r'^idc_add/$', views.idc_add, name='idc_add'),
    url(r'^idc_edit/$', views.idc_edit, name='idc_edit'),
    url(r'^idc_delete/$', views.idc_delete, name='idc_delete'),
    url(r'^idc_search$', api.idc_search, name='idc_search'),


    url(r'^postmachineinfo/$', views.postmachineinfo, name='postmachineinfo'),

]
