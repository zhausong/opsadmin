# Create your views here.
#coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from opsadmin.models import User
from opsadmin.models import Idcmanager
from opsadmin.models import Ostype
import os

class UserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

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


def index(req):
    username=req.session.get('username','anybody')
    return render_to_response('index.html',{'username':username})
def login(req):
    if req.method == "POST":
         username=req.POST.get('username')
         password=req.POST.get('password')
         user=User.objects.filter(username=username,password=password)
         print user
         print username,password
         if user:
             req.session['username']=username
             if req.session['username'] == '':
                 return HttpResponseRedirect('/login/')
             else:
                 return HttpResponseRedirect('/index/')
         else:
             if User.objects.filter(username=username):
                 return HttpResponseRedirect('/login/')
             else:
                 return HttpResponseRedirect('/register/')
    else:
        uf=UserForm()  
    return render_to_response('login.htm',{'uf':uf},context_instance=RequestContext(req))



def register(req):
    context={}
    if req.method == "POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        password_two=req.POST.get('password_two')
        print username,password,password_two
        user=User.objects.filter(username=username)
        if user:
            req.session['username']=username
            return HttpResponse('用户名已经被占用')
        elif password == password_two:
            print "----"
            user = User()
            user.username=username
            user.password=password
            print "--------"
            user.save()
            print username,password,password_two
            #return HttpResponse(u'恭喜你!注册成功，您的用户名为'+username)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse(u'您两次输入的密码不匹配，请重新输入') 
    else:
         uf=UserForm()
    return render_to_response('register.html',context_instance=RequestContext(req))

def logout(req):
    session = req.session.get('username',False)
    if session:
        del req.session['username']
        #return render_to_response('logout.html',{'username':session})
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')
def idc(req):
    context={}
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
    return render_to_response('idc-manager.html')

def ostype(req):
     if req.method == "POST":
         ostype=Ostype()
         ostype.ostype=req.POST.get('ostype')
         ostype.save()
     return render_to_response('idc-ostype.html')
