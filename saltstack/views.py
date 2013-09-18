# Create your views here.
# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
import salt
import subprocess
import os
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
#from opsadmin.models import saltstack
def saltstack(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username=req.session.get('username')
    #ret=subprocess.Popen('salt "node2" test.ping',shell=True,stdout=subprocess.PIPE).stdout.read()
    error = False
    ret_msg=[]
    ret_cmd_msg=[]
    ret_err=[]
    ret_nohost=''
    ret_nocmd=''
    ret_badcmd=''
    ret_bad=''
    if req.method == "POST":
        print req.POST
        host=req.POST.getlist('cmd_run_command_host')
        cmd=req.POST.get('cmd_run_command_cmd')
        print len(host),'oooo'
        print req.POST.get('chechk_alive_host_name').split(',')
        print req.POST.get('check_alive_host_cmd')
        if host[0] == '':
            host=req.POST.get('chechk_alive_host_name').split(',')
            cmd=req.POST.get('check_alive_host_cmd')
        print len(host),host,cmd
        #ret=salt.client.LocalClient().cmd('node2','cmd.run',['ping -c 4 8.8.8.8'])
        bad_cmd=['rm','shutdown','cat /etc/passwd']
        if host[0] !='' and cmd != "" and cmd not in bad_cmd:
           # node_list=node.split(',')
            for node in host:
                print node
                allow_cmd=['test.ping','test.version']
                print "*"*45
                print node,cmd
                if cmd in allow_cmd:
                    try:
                        print '111%%%%%%%%%%%%%%%%%%%%%%'
                        msg=salt.client.LocalClient().cmd_full_return(node,cmd)
                        msg=str(node)+" "*24+str(msg[node]['ret'])
                        print msg
                        ret_msg.append(msg)
                        print ret_msg,'[[[[[[[[[[[[[['
                    except:
                        msg=str(node)+" "*24+"False"
                        print msg,'msg'
                        ret_err.append(msg)
                        print ret_err,'ret'
                        print '222%%%%%%%%%%%%%%%%%%%%%%'
                else:
                    try:
                        ret=salt.client.LocalClient().cmd(node,'cmd.run',[cmd])
                        print "=================="
                        if len(ret)<1:
                            err=str(node)+" "*24+'minions is not running'
                            ret_err.append(err)
                            print ret_err
                        #ret=str(node)+" "*24+str(ret[node])
                        ret_cmd_msg=str(node)+":\n"+"="*24+"\n"+str(ret[node])
                        print node,ret[node]
                        print ret
                        print "err============================="
                    except:
                        err=str(node)+" "*24+"The command is error\n"
                        ret_err.append(err)
                        print ret_err
                #ret=node+':\n'+u'ret[node]['ret']'
                print ret_msg
                print ret_err
                print "++++++++++++====+++"
        elif host == "":
            ret_bad="hostname is can not null"
            error=True
        elif cmd == "":
            ret_bad="command is can not null"
            error=True
        elif cmd  in bad_cmd:
            ret_bad="the command is not allow to use"
            error=True
        return render_to_response('saltstack.html',{"ret_msg":ret_msg,"ret_cmd_msg":ret_cmd_msg,"error":error,"ret_err":ret_err,'ret_bad':ret_bad,'ret_nocmd':ret_nocmd,'ret_badcmd':ret_badcmd},context_instance=RequestContext(req))


    elif req.method == "GET":
        print req.META['REMOTE_ADDR'],req.META['HTTP_USER_AGENT']

        ###############################grains info####################################
        node='node2'
        cmd='grains.items'
        grains_info=salt.client.LocalClient().cmd_full_return(node,cmd)[node]['ret']
        id=grains_info['id']
        host=grains_info['host']
        domain=grains_info['domain']
        fqdn=grains_info['fqdn']
        nodename=grains_info['nodename']
        localhost=grains_info['localhost']
        server_id=grains_info['server_id']
        master=grains_info['master']
        ipv4=grains_info['ipv4']
        saltversion=grains_info['saltversion']
        pythonversion=grains_info['pythonversion']
        shell=grains_info['shell']
        defaultencoding=grains_info['defaultencoding']
        defaultlanguage=grains_info['defaultlanguage']
        os=grains_info['os']
        os_family=grains_info['os_family']
        kernel=grains_info['kernel']
        kernelrelease=grains_info['kernelrelease']
        ps=grains_info['ps']
        virtual=grains_info['virtual']
        cpu_model=grains_info['cpu_model']
        cpuarch=grains_info['cpuarch']
        num_cpus=grains_info['num_cpus']
        cpu_flags=grains_info['cpu_flags']
        num_gpus=grains_info['num_gpus']
        gpus=grains_info['gpus']
        mem_total=grains_info['mem_total']
        ip=grains_info['ipv4']
        path=grains_info['path']
        saltpath=grains_info['saltpath']
        pythonpath=grains_info['pythonpath']
        ###############################grains info####################################
        ###################################master_config################################
        f=open('/etc/salt/master','r')
        sshd_config=f.read()
        f.close()
        ##################################master_config################################
        ret = ""
        return render_to_response('saltstack.html',{"username":username,"sshd_config":sshd_config,"result_data":ret,"error":error,"path":path,"id":id,"host":host,"domain":domain,"fqdn":fqdn,"nodename":nodename,"localhost":localhost,"server_id":server_id,"master":master,"ipv4":ipv4,"saltversion":saltversion,"pythonversion":pythonversion,"shell":shell,"defaultencoding":defaultencoding,"defaultlanguage":defaultlanguage,"os":os,"os_family":os_family,"kernel":kernel,"kernelrelease":kernelrelease,"ps":ps,"virtual":virtual,"cpu_model":cpu_model,"cpuarch":cpuarch,"num_cpus":num_cpus,"cpu_flags":cpu_flags,"num_gpus":num_gpus,"gpus":gpus,"mem_total":mem_total,"ipv4":ipv4,"path":path,"saltpath":saltpath,"pythonpath":pythonpath},context_instance=RequestContext(req))
    return render_to_response('saltstack.html',{"result_data":ret,"error":error},context_instance=RequestContext(req))
def minions(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('minion.html',context_instance=RequestContext(req))

def salt_key(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    proc = subprocess.Popen('salt-key', stdout=subprocess.PIPE)
    salt_key = proc.stdout.read().replace('\n','<br>')
    #return render_to_response('saltstack.html',{"salt_key":salt_key},context_instance=RequestContext(req))
    return HttpResponse(salt_key)

@csrf_protect
@csrf_exempt
def saltstack_master_config(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if req.is_ajax():
        if req.method == "POST":
            #response=HttpResponse()
            #response['Content-Type']="text/javascript"
            data=req.POST['name']
            print data
            try:
                f=open('/etc/salt/master','r+')
                f.write(data)
                f.close
            except:
                pass
        if req.method == "GET":
            try:
                f=open('/etc/salt/master','r')
                data=f.read()
                f.close
            except:
                data="The file /etc/salt/master is not exist"
    elif not req.is_ajax():
        print "-----------"
        return render_to_response('saltstack.html')
    return HttpResponse(data)

@csrf_protect
@csrf_exempt
def saltstack_master_group(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    data='method is not allowed'
    if not os.path.isdir('/etc/salt/master.d'):
        os.mkdir('/etc/salt/master.d')
    if not os.path.exists('/etc/salt/master.d/node.conf'):
        f=open('/etc/salt/master.d/node.conf','w')
        f.write('You should setting group in /etc/salt/master.d/node.conf')
        f.close
    if req.is_ajax():
        if req.method == "POST":
            data=req.POST['name']
            print data
            try:
                f=open('/etc/salt/master.d/node.conf','r+')
                f.write(data)
                f.close
                print "add group"
            except:
                pass
        if req.method == "GET":
            try:
                f=open('/etc/salt/master.d/node.conf')
                data=f.read()
                f.close
            except:
                data="The file /etc/salt/master.d/node.conf is not exist "
    return HttpResponse(data)

@csrf_protect
@csrf_exempt
def saltstack_top_sls(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    data='method is not allowed'
    if not os.path.isdir('/srv/salt'):
        os.mkdir('/srv/salt')
    if not os.path.exists('/srv/salt/top.sls'):
        f=open('/srv/salt/top.sls','w')
        f.write('You should modify the /srv/salt/top.sls')
        f.close
    if req.is_ajax():
        if req.method == "POST":
            data=req.POST['name']
            print data
            try:
                f=open('/srv/salt/top.sls','r+')
                f.write(data)
                f.close
            except:
                pass
        if req.method == "GET":
            try:
                f=open('/srv/salt/top.sls')
                data=f.read()
                f.close
            except:
                data="The file /srv/salt/top.sls is not exist "
    return HttpResponse(data)

def ssh_remote_manager(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    try:
        import paramiko
    except:
        subprocess.call('yum install -y python-paramiko',shell=True)|subprocess.call('easy_install paramiko',shell=True)
    import sys,os
    if req.method == "GET":
        CMD=req.GET.get('ssh_cmd')
        #print CMD
        CMD='w'
        username = "zswu"
        host = '127.0.0.1'
        port = 60022
        pkey_file = "/home/zswu/.ssh/id_rsa"

        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(pkey_file)

        s.connect(host,port,username,pkey=key,timeout=5)
        print CMD
        stdin,stdout,stderr = s.exec_command(CMD)
        cmd_result = stdout.read(),stderr.read()
    return HttpResponse(cmd_result) #context_instance=RequestContext(req))


@csrf_protect
@csrf_exempt
def os_path_edit(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    data='method is not allowed'
    if req.is_ajax():
        if req.method == "POST":
            path=req.POST['os_path_edit_path']
            data=req.POST['os_path_edit_path_text']
            print data
            try:
                f=open(path,'r+')
                f.write(data)
                f.close
            except:
                data="The file "+path+" is not exist "
        if req.method == "GET":
            path=req.GET['os_path_edit_path']
            try:
                f=open(path,'r')
                data=f.read()
                f.close
            except:
                data="The file "+path+" is not exist "
    return HttpResponse(data)
