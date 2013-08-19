# Create your views here.
# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from opsadmin.models import Idcmanager


class IdcmanagerForm(forms.Form):
    hostname=forms.CharField()
    ip=forms.CharField()
    serialnumber=forms.CharField()
    sshport=forms.IntegerField()
    status=forms.IntegerField()
    location=forms.CharField()
    idcname=forms.CharField()
    ostype=forms.CharField()
    cpu=forms.CharField()
    harddisk=forms.CharField()
    memory=forms.CharField()
    buytime=forms.CharField()
    qualitytime=forms.CharField()
    detail=forms.CharField()


def idc(req):
    context={}
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username=req.session.get('username')
    if req.method == "POST":
       idcmanager=Idcmanager()
       idcmanager.hostname=req.POST.get('hostname')
       idcmanager.ip=req.POST.get('ip')
       idcmanager.serialnumber=req.POST.get('serialnumber')
       idcmanager.sshport=req.POST.get('sshport')
       idcmanager.status=req.POST.get('status')
       idcmanager.location=req.POST.get('location')
       idcmanager.idcname=req.POST.get('idcname')
       idcmanager.ostype=req.POST.get('ostype')
       idcmanager.cpu=req.POST.get('cpu')
       idcmanager.harddisk=req.POST.get('harddisk')
       idcmanager.memory=req.POST.get('memory')
       idcmanager.buytime=req.POST.get('buytime')
       idcmanager.qualitytime=req.POST.get('qualitytime')
       idcmanager.detail=req.POST.get('detail')

       idcmanager.save()
    return render_to_response('idc-manager.html',{'username':username},context_instance=RequestContext(req))

def get_host_info(req):
    if req.method == "GET":
       import MySQLdb
       db = MySQLdb.connect(user='opsadmin', db='opsadmin', passwd='opsadmin', host='localhost')
       cursor=db.cursor()
       cursor.execute('select * from opsadmin_idcmanager') 
       data=cursor.fetchall()
       db.close()
       print data          
       hostname=['']
       ip=['']
       serialnumber=['']
       sshport=['']
       status=['']
       location=['']
       idcname=['']
       ostype=['']
       cpu=['']
       harddisk=['']
       memory=['']
       buytime=['']
       qualitytime=['']
       detail=['']
       for v in data:
           hostname_list=v[1]
           ip_list=v[2]
           serialnumber_list=v[3]
           sshport_list=v[4]
           status_list=v[5]
           location_list=v[6]
           idcname_list=v[7]
           ostype_list=v[8]
           cpu_list=v[9]
           harddisk_list=v[10]
           memory_list=v[11]
           buytime_list=v[12]
           qualitytime_list=v[13]
           detail_list=v[14]

           hostname.append(hostname_list)
           ip.append(ip_list)
           serialnumber.append(serialnumber_list)
           sshport.append(sshport_list)
           status.append(status_list)
           location.append(location_list)
           idcname.append(idcname_list)
           ostype.append(ostype_list)
           cpu.append(cpu_list)
           harddisk.append(harddisk_list)
           memory.append(memory_list)
           buytime.append(buytime_list)
           qualitytime.append(qualitytime_list)
           detail.append(detail_list)

           print hostname

       #for i in data:
       #    print i
       #print data
    return render_to_response('idc-manager.html',{"hostname":hostname,"ip":ip,"serialnumber":serialnumber,"sshport":sshport,"status":status,"location":location,"idcname":idcname,"ostype":ostype,"cpu":cpu,"harddisk":harddisk,"memory":memory,"buytime":buytime,"qualitytime":qualitytime,"detail":detail},context_instance=RequestContext(req))


def test(req):
       if not req.user.is_authenticated():
            return HttpResponseRedirect('/login/')
       import MySQLdb
       import json
       db = MySQLdb.connect(user='opsadmin', db='opsadmin', passwd='opsadmin', host='localhost')
       #output data is a tuple
       #cursor=db.cursor()
       #output data is a dict
       cursor=db.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('select * from opsadmin_idcmanager')
       data=cursor.fetchall()
       db.close()
       data=[x for x in data]       
       #data=str(data).replace('\'','\\\'')
       data=json.dumps(data).decode('utf-8')
       print data
       #return render_to_response('back/json.test.ok.idc-manager.html',{"data":data},context_instance=RequestContext(req))
       return render_to_response('idc-manager.html',{"data":data},context_instance=RequestContext(req))
def add_tab(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    import json
    f=open('/home/zswu/python/django/opsadmin/static/getCustomers','r')
    data=f.read()
    #data=json.dumps(f1).replace('\\','')
    return HttpResponse(data)
    #return render_to_response('add_tab.txt',{"data":data})

def table_add_del(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('table_add_del.html')
