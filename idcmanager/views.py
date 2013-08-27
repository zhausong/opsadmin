# Create your views here.
# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from opsadmin.models import Idcmanager
from opsadmin.models import Idcnamelist
from opsadmin.models import Location
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


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
    import MySQLdb
    db = MySQLdb.connect(user='opsadmin', db='opsadmin', passwd='opsadmin', host='localhost',charset='utf8')
    cursor=db.cursor()
    #cursor.execute("SET NAMES 'gb2312'")
    cursor.execute('select * from opsadmin_idcnamelist')
    idcnamelist=cursor.fetchall()
    cursor.execute('select * from opsadmin_location')
    locationlist=cursor.fetchall()
    cursor.execute('select id,nodename,ipv4,sshport,status,location,idcname,is_virtual,serialnumber,cpu_model,harddisk,memory,ostype,buytime,qualitytime,detail from opsadmin_idcmanager')
    idcmanager_host_info=cursor.fetchall()
    db.close

    if req.method == "POST":
       print req.POST
       idcmanager=Idcmanager()
       idcmanager.nodename=req.POST.get('hostname')
       idcmanager.ipv4=req.POST.get('ip')
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
    if req.method == "GET":
        #data=Idcnamelist.objects.all()
        #idcnamelist_dict=Idcnamelist.objects.order_by("id")
        #idcnamelist=idcnamelist_dict.values()
        #idcnamelist=Idcnamelist.objects.values()
        get='test'
    return render_to_response('idc-manager.html',{'username':username,'idcnamelist':idcnamelist,'locationlist':locationlist,'idcmanager_host_info':idcmanager_host_info},context_instance=RequestContext(req))

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


@csrf_protect
@csrf_exempt
def add_idc_name(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    data='method is not allowed'
    print req.POST
    if req.is_ajax():
        if req.method == "POST":
            name=req.POST['name']
            date=req.POST['date']
            detail=req.POST['detail']
            #print name,date,detail
            #data=name
            is_idcname_in_list=Idcnamelist.objects.filter(idcname=name)
            if is_idcname_in_list:
                data=name+' already in database'
            else: 
                idcnamelist=Idcnamelist(idcname=name,usetime=date,detail=detail)
                idcnamelist.save()
                data=name+' Successful  to add databae '
        if req.method == "GET":
            #data=Idcnamelist.objects.all()
            data=Idcnamelist.objects.values()
            print data
            print "idcnamelist"
    return HttpResponse(data)



@csrf_protect
@csrf_exempt
def add_location_name(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    data='method is not allowed'
    print req.POST
    if req.is_ajax():
        if req.method == "POST":
            name=req.POST['locationname']
            detail=req.POST['locationdetail']
            print name,detail
            data=name
            is_location_in_list=Location.objects.filter(location=name)
            print "*"*30
            if is_location_in_list:
                data=name+' already in database'
            else:
                location=Location(location=name,detail=detail)
                location.save()
                data=name+' Successful  to add databae '
        if req.method == "GET":
            #data=Idcnamelist.objects.all()
            data=Location.objects.values()
            print data
            print "Location"
    return HttpResponse(data)
