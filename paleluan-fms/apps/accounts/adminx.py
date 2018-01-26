# -*- coding:utf-8 -*-
__author__ = 'jummy'

import xadmin
from xadmin import views
from .models import Project,Contact

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "神州数码"
    site_footer = "神州数码"
    # menu_style = "accordion"


class ProjectAdmin(object):
    list_display = ['name','description']
    list_filter = ['name','description']
    search_fields = ['name','description']


class ContactAdmin(object):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']



xadmin.site.register(Project,ProjectAdmin)
xadmin.site.register(Contact,ContactAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

