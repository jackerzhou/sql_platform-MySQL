import MySQLdb,sys,string,time,datetime,uuid
from django.contrib.auth.models import User
from myapp.models import Db_name,Db_account,Db_instance,Oper_log,Task
from myapp.form import LoginForm,Captcha
from django.db.models import Count

def get_main_chart():
    log = Oper_log.objects.values('sqltype').annotate(num=Count('sqltype')).order_by("-num")
    collist=[]
    datalist = []
    for i in log:
        collist.append(i['sqltype'])
        datalist.append(i['num'])
    return datalist,collist


def get_task_chart():
    #today
    log = Task.objects.filter(create_time__gte=datetime.date.today()).values('status').annotate(num=Count('status')).order_by("-num")
    collist=[]
    datalist = []
    for i in log:
        collist.append(i['status'])
        datalist.append(i['num'])
    return datalist,collist
#'executed','executed failed','check not passed','check passed','running'

def get_task_bingtu():
    log = Task.objects.values('status').annotate(num=Count('status')).order_by("-num")
    collist=[]
    datalist = []
    for i in log:
        dict={}
        dict['value'] =i['num']
        dict['name'] = i['status']
        datalist.append(dict)
    return datalist