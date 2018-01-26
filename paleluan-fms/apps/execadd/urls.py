from __future__ import unicode_literals
from django.conf.urls import url
from execadd import views

urlpatterns = [

    url(r'^listadd$', views.execadd_list, name='execadd_list'),

    # 上传文件
    # url(r'^upload_exec/$', views.upload, name='execadd_name'),
    url(r'^upload_file_add/$', views.upload_file, name='execadd_file'),


]


