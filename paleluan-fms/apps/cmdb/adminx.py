# -*- coding:utf-8 -*-
__author__ = 'jummy'

import xadmin
from .models import ServerGroup,IDC,Server,Service


class ServerGroupAdmin(object):
    list_display = ['name','created_by','date_created','comment']
    search_fields = ['name','created_by','comment']
    list_filter = ['name','created_by','date_created','comment']

class IDCAdmin(object):
    list_display = ['name', 'bandwidth', 'contact', 'phone','address','intranet','extranet','date_created','operator','created_by','comment']
    search_fields = ['name', 'bandwidth', 'contact', 'phone','address','intranet','extranet','operator','created_by','comment']
    list_filter = ['name', 'bandwidth', 'contact', 'phone','address','intranet','extranet','date_created','operator','created_by','comment']

class ServerAdmin(object):
    list_display = ['in_ip', 'idc', 'groups', 'ex_ip', 'project_name', 'host_name', 'service_name', 'position', 'ctime', 'author', 'cpu_model',
                    'cpu_cores','cpu_count','mem','disk','os_version','os_kernel','status','max_open_files','uptime']
    search_fields = ['in_ip', 'idc', 'groups', 'ex_ip', 'project_name', 'host_name', 'service_name', 'position',  'author', 'cpu_model',
                    'cpu_cores','cpu_count','mem','disk','os_version','os_kernel','status','max_open_files']
    list_filter = ['in_ip', 'idc', 'groups', 'ex_ip', 'project_name', 'host_name', 'service_name', 'position', 'ctime', 'author', 'cpu_model',
                    'cpu_cores','cpu_count','mem','disk','os_version','os_kernel','status','max_open_files','uptime']

class ServiceAdmin(object):
    list_display = ['server','port', 'service_name']
    search_fields = ['server','port', 'service_name']
    list_filter = ['server','port', 'service_name']


xadmin.site.register(ServerGroup,ServerGroupAdmin)
xadmin.site.register(IDC,IDCAdmin)
xadmin.site.register(Server,ServerAdmin)
xadmin.site.register(Service,ServiceAdmin)





