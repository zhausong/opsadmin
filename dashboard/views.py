# Create your views here.
#coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django import forms
from dashboard.models import User
import os

def index(req):
    '''验证用户是否通过认证 '''
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    '''获取登录用户名'''
    username=req.session.get('username')
    print username
    return render_to_response('index.html',{'username':username})
def login(req):
    if req.method == "POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        if username is not None and password is not None:
            user=auth.authenticate(username=username,password=password)
            print username,password
            if user is not None and user.is_active:
                auth.login(req,user)
                #设置用户的session
                req.session['username']=username
                return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/login/',context_instance=RequestContext(req))
    '''判断是否已经登录'''
    if req.user.is_authenticated() and req.session['username'] is not None:
        return HttpResponseRedirect('/index/')
        
    return  render_to_response('login.htm',context_instance=RequestContext(req))

def logout(req):
    session = req.session.get('username',False)
    if session:
        print "delete session",req.session.get('username')
        auth.logout(req)
        #del req.session['username']        
        #return render_to_response('logout.html',{'username':session})
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')


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

