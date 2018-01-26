# -*- coding:utf-8 -*-
__author__ = 'jummy'

from  .models import ExecFile
import xadmin

class ExecFileAdmin(object):
    list_display = ['majors','worktype','contentc','datet','starttime','lengtime','networkn','department_name','head','announeoms','singleeoms','enforcer','remark']
    list_filter = ['majors','worktype','contentc','datet','networkn','department_name','head','announeoms','singleeoms','enforcer','remark']
    search_fields=['majors','worktype','contentc','datet','starttime','lengtime','networkn','department_name','head','announeoms','singleeoms','enforcer','remark']



xadmin.site.register(ExecFile,ExecFileAdmin)

