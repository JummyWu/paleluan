#-*- coding: utf-8 -*-
'''
    Author: smallmi
    Blog: http://www.smallmi.com
'''
from django.conf.urls import url,include
from django.contrib import admin
from content import urls,views
from django.conf.urls.static import static
from django.conf import settings
from content import views as content_views
from dashboard import views as dashboard_views
import xadmin

urlpatterns = [
    url(r'^$',dashboard_views.index, name="index"),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'fms/', include('content.urls')),

    url(r'cmdb/', include('cmdb.urls')),
    url(r'tasks/', include('tasks.urls')),

    url(r'^type/add$', views.type_add,name='type_add'),
    url(r'^type/del/(?P<id>\d+)$', views.type_del,name='type_del'),

    url(r'^get/email$',views.get_email, name='get_email'),
    url(r'^send/emails$',views.send_mails, name='send_mails'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^images/upload$', content_views.upload_images, name='upload_images'),

    # 上传文件
    url(r'execadd/', include('execadd.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
