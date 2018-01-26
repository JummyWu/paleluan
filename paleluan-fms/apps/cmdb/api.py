# -*- coding: utf-8 -*-
'''
    Author: smallmi
    Blog: http://www.smallmi.com
'''
from django.shortcuts import render, render_to_response, reverse
from django.http import HttpResponse, HttpResponseRedirect
from commons.paginator import paginator
from cmdb.models import Server, ServerGroup, IDC
from django.db.models import Q


def server_search(request):
    data = {}
    search = request.GET.get("search")
    content = Server.objects.filter(
        Q(in_ip__icontains=search) | Q(project_name__icontains=search) | Q(service_name__icontains=search) | Q(
            position__icontains=search) | Q(host_name__icontains=search) | Q(author__fullname__icontains=search))
    data = paginator(request, content)
    return render_to_response('cmdb/server_table.html', data)


def group_search(request):
    data = {}
    search = request.GET.get("search")
    content = ServerGroup.objects.filter(
        Q(name__icontains=search) | Q(comment__icontains=search) | Q(created_by__fullname__icontains=search))
    data = paginator(request, content)
    return render_to_response('cmdb/group_table.html', data)


def idc_search(request):
    data = {}
    search = request.GET.get("search")
    content = IDC.objects.filter(
        Q(name__icontains=search) | Q(contact__icontains=search) | Q(phone__icontains=search) | Q(
            operator__icontains=search) | Q(created_by__fullname__icontains=search))
    data = paginator(request, content)
    return render_to_response('cmdb/idc_table.html', data)
