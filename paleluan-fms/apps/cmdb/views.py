# -*- coding: UTF-8 -*-
import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from cmdb.models import Server, Service
from controller.public.pagination import *
from controller.core.ansiblehelp import *
from django.http import HttpResponse
from django.shortcuts import render
from commons.paginator import paginator
from cmdb.models import *
import json
from django.contrib.auth.decorators import permission_required,login_required
# from permissions import check_permission
# Create your views here.

PAGE_SIZE = 10  # 每页显示条数
current_page_total = 10  # 分页下标


@login_required
def index(request):
    user = request.user
    if user.is_superuser:
        role = '超级管理员'
    elif user.is_anonymous():
        role = '匿名用户'
    else:
        role = '普通用户'
    request.role = role
    return render_to_response('base/index.html', {'request': request})

# def time_count(content, start_time, end_time):
#
#     start_time = time.strptime(str(start_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
#     end_time = time.strptime(
#         str(end_time).split('+')[0], "%Y-%m-%d %H:%M:%S")
#     timestamp = int(time.mktime(end_time)) - int(time.mktime(start_time))
#
#     setattr(content, 'time', str(timestamp // 3600) + '小时' + str(timestamp % 3600 // 60) + '分')

@login_required
@permission_required('content.get_content',raise_exception=True)
def server_list(request):
    data = {}
    server = Server.objects.order_by('id')
    data = paginator(request, server)
    request.breadcrumbs((('首页', '/'), ('资产列表', reverse('server_list'))))

    return render_to_response('cmdb/index.html', data)


@login_required
@permission_required('content.get_content',raise_exception=True)
def server_group(request):
    data = {}
    server = ServerGroup.objects.order_by('id')
    data = paginator(request, server)
    request.breadcrumbs((('首页', '/'), ('资产组列表', reverse('server_group'))))

    return render_to_response('cmdb/group.html', data)


@login_required
@permission_required('content.get_content',raise_exception=True)
def server_idc(request):
    data = {}
    server = IDC.objects.order_by('id')
    data = paginator(request, server)
    request.breadcrumbs((('首页', '/'), ('IDC列表', reverse('server_idc'))))

    return render_to_response('cmdb/idc.html', data)

def server_add_page(request):
    # 新增机器页面
    return render_to_response('cmdb/server_add.html', locals(), context_instance=RequestContext(request))


def server_add(request):
    # 新增机器

    user = request.user
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    server = Server()
    server.author_id = user.id
    server.project_name = data['project_name']
    server.service_name = data['service_name']
    server.in_ip = data['in_ip']
    server.ex_ip = data['ex_ip']
    server.position = data['position']
    try:
        server.save()
    except:
        response.write(json.dumps(u'新增失败'))
    else:
        response.write(json.dumps(u'成功'))
    return response


def group_add(request):
    # 新增资产组

    user = request.user
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    group = ServerGroup()
    group.created_by_id = user.id
    group.name = data['group_name']
    group.comment = data['group_comment']
    try:
        group.save()
    except:
        response.write(json.dumps(u'新增失败'))
    else:
        response.write(json.dumps(u'成功'))
    return response


def idc_add(request):
    # 新增IDC

    user = request.user
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    idc = IDC()
    idc.created_by_id = user.id
    idc.name = data['idc_name']
    idc.contact = data['idc_contact']
    idc.phone = data['idc_phone']
    idc.address = data['idc_address']
    idc.intranet = data['idc_intranet']
    idc.extranet = data['idc_extranet']
    idc.operator = data['idc_operator']
    try:
        idc.save()
    except:
        response.write(json.dumps(u'新增失败'))
    else:
        response.write(json.dumps(u'成功'))
    return response


def server_edit_page(request, id):
    pass
    # 编辑机器页面
    # server = Server.objects.get(pk=id)
    # return render_to_response('cmdb/server_edit.html', locals(), context_instance=RequestContext(request))


def server_edit(request):
    # 编辑机器
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    # print data
    # for i in data:
    #     print i, data[i]
    id = data['id']
    project_name = data['project_name']
    service_name = data['service_name']
    position = data['position']
    in_ip = data['in_ip']
    ex_ip = data['ex_ip']

    server = Server.objects.get(pk=id)
    server.project_name = project_name
    server.service_name = service_name
    server.position = position
    server.in_ip = in_ip
    server.ex_ip = ex_ip
    server.save()

    response.write(json.dumps(u'成功'))
    return response


def group_edit(request):
    # 编辑机器
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    id = data['id']
    group_name = data['group_name']
    group_comment = data['group_comment']

    group = ServerGroup.objects.get(pk=id)
    group.name = group_name
    group.comment = group_comment
    group.save()

    response.write(json.dumps(u'成功'))
    return response


def idc_edit(request):
    # 编辑IDC

    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    id = data['id']

    idc = IDC.objects.get(pk=id)
    idc.name = data['idc_name']
    idc.contact = data['idc_contact']
    idc.phone = data['idc_phone']
    idc.address = data['idc_address']
    idc.intranet = data['idc_intranet']
    idc.extranet = data['idc_extranet']
    idc.operator = data['idc_operator']
    try:
        idc.save()
    except:
        response.write(json.dumps(u'失败'))
    else:
        response.write(json.dumps(u'成功'))
    return response


def server_delete(request):
    # 删除机器信息
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    id = int(data['id'])
    Server.objects.get(pk=id).delete()

    response.write(json.dumps(u'成功'))
    return response


def group_delete(request):
    # 删除资产组
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    id = int(data['id'])
    ServerGroup.objects.get(pk=id).delete()

    response.write(json.dumps(u'成功'))
    return response


def idc_delete(request):
    # 删除IDC
    response = HttpResponse()
    data = json.loads(request.POST.get('data', ''))

    id = int(data['id'])
    IDC.objects.get(pk=id).delete()

    response.write(json.dumps(u'成功'))
    return response


def postmachineinfo(request):
    # 提交服务器信息
    response = HttpResponse()
    data = json.loads(request.GET.get('data', ''))
    id = int(data['id'])
    print('update--->')
    server = Server.objects.get(pk=id)
    data = get_info(server.in_ip)
    server.os_version = data['sysinfo']
    server.host_name = data['host_name']
    server.os_kernel = data['os_kernel']
    server.cpu_model = data['cpu']
    server.cpu_count = data['cpu_count']
    server.cpu_cores = data['cpu_cores']
    server.mem = data['mem']
    server.disk = data['disk']
    server.status = True
    server.max_open_files = get_ulimit(server.in_ip)
    server.uptime = get_uptime(server.in_ip)
    server.save()

    # set_service_port(server)  # 设置服务端口信息
    response.write(json.dumps(u'成功'))
    return response


def set_service_port(server):
    # 设置服务端口信息
    services = Service.objects.filter(server=server)
    result = get_service_port(server.in_ip)

    new_srv_name = result.keys()  # 客户端抓取的数据
    old_srv_name = [obj.service_name for obj in services]  # 数据库查询的数据

    add_services = list(set(new_srv_name) - set(old_srv_name))  # 新增的服务
    delete_services = list(set(old_srv_name) - set(new_srv_name))  # 删除的服务
    update_services = list(set(new_srv_name) & set(old_srv_name))  # 更新的服务

    add_data = {}  # 新增服务和端口号
    update_data = {}  # 更新的服务和端口号
    for value in result:
        if value in add_services:
            add_data[value] = result[value]
        if value in update_services:
            update_data[value] = result[value]

    # 新增服务
    for ad in add_data:
        values = add_data[ad]
        for val in values:
            Service.objects.create(server=server, service_name=ad, port=val)

    # 删除服务
    for delt in delete_services:
        Service.objects.filter(server=server, service_name=delt).delete()

    # 更新服务
    for update in update_data:
        new = update_data[update]  # 需要更新的服务的端口
        services = Service.objects.filter(server=server, service_name=update)
        old = [srv.port for srv in services]  # 旧的服务的端口

        adds = list(set(new) - set(old))  # 增加的端口
        deletes = list(set(old) - set(new))  # 删除的端口

        for add in adds:
            Service.objects.create(server=server, service_name=update, port=add)
        for delete in deletes:
            Service.objects.filter(server=server, service_name=update, port=delete).delete()
