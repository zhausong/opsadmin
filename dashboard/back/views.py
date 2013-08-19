# Create your views here.
#coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django import forms
from dashboard.models import User
import os

class UserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

def index(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        username=req.session.get('username','anybody')
        return render_to_response('index.html',{'username':username})
def login(req):
    if req.method == "POST":
         username=req.POST.get('username')
         password=req.POST.get('password')
         #user=User.objects.filter(username=username,password=password)
         user=auth.authenticate(username=username,password=password)
         print user
         print username,password
         if user:
             req.session['username']=username
             if req.session['username'] == '':
                 return HttpResponseRedirect('/login/',context_instance=RequestContext(req))
             else:
                 return HttpResponseRedirect('/index/')
         else:
             if User.objects.filter(username=username):
                 return HttpResponseRedirect('/login/',context_instance=RequestContext(req))
             else:
                 return HttpResponseRedirect('/register/',context_instance=RequestContext(req))
    else:
        uf=UserForm()  
    return render_to_response('login.htm',context_instance=RequestContext(req))



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
            return HttpResponseRedirect('/login/',context_instance=RequestContext(req))
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
