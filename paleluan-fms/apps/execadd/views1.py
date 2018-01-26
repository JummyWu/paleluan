
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from commons.paginator import paginator


import pymysql
import xlrd
from datetime import date,time

from execadd.models import ExecFile,UploadFile
import os

def execadd_list(request):

    data = {}
    execfile = ExecFile.objects.order_by('id')


    data = paginator(request, execfile)
    print(data)
    request.breadcrumbs((('首页', '/'),('exec数据',reverse('execadd_list'))))

    return render_to_response('execadd/index1.html', data)




def upload(request):
    return render(request,'upload.html')


def upload_file(request):

    fafafa = request.FILES.get('fafafa')
    print(fafafa)


    img_path = os.path.join('static/exec/',fafafa.name)
    print('img_path:',img_path)
    with open(img_path,'wb') as f:
        for item in fafafa.chunks():
            f.write(item)

    print(img_path)

    ret = {'code':True,'data':img_path}


    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test2',charset='utf8')
    # 创建游标
    cursor = conn.cursor()

    book = xlrd.open_workbook(img_path)
    # sheet = book.sheet_names()[0]
    sheet = book.sheet_by_index(0)
    # sheet = book.sheet_by_name('1')book.sheet_by_index(1)
    print("sheet_name:",sheet)
    # print(sheet3)
    #
    row_ = sheet.nrows
    col_ = sheet.ncols

    all_content = []
    for i in range(1, row_):
        row_content = []
        for j in range(col_):

            ctype = sheet.cell(i, j).ctype
            value = sheet.cell(i, j).value

            if ctype == 3:
                date = xlrd.xldate.xldate_as_datetime(value, 0)
                if date.year > 1996:
                    value = '%s/%s/%s' % (date.year, date.month, date.day)
                else:
                    value = '%s:%s:%s' % (date.hour, date.minute, date.second)

            elif ctype == 2 and value:
                value = int(value)
            elif ctype == 1 and value:
                value = value.replace('\n', ' ')
            else:
                value = value
            row_content.append(value)
        all_content.append(tuple(row_content))
        list_data = row_content
    # for i in range(len(all_content)):
    #     print(all_content[i])

    cursor.executemany("insert into execadd_execfile(majors,worktype,contentc,datet,starttime,lengtime,networkn,department_name,head,announeoms,singleeoms,enforcer,remark) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",all_content)
    # cursor.execute("insert into execadd_execfile(majors,worktype,contentc,datet,starttime,lengtime,networkn,department_name,head,announeoms,singleeoms,enforcer,remark) values('IP888','故障处66理','处理EOMS系统故障工单','2019/03/09','10:00:00','1:30:00	','现网SR\\现网BRAS','互联网支撑室/何忠荣','何忠荣','无','CMCC-GD-GZCLX-20170724-011724 CMCC-GD-GZCLX-20170724-011724','刘敏荣','23')")

    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    list_datas =  ExecFile.objects.all()
    print(list_datas)

    return render(request,'execeadd_table.html')


