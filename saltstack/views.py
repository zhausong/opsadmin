# Create your views here.
# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
import salt
import subprocess
#from opsadmin.models import saltstack
def saltstack(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username=req.session.get('username')
    #ret=subprocess.Popen('salt "node2" test.ping',shell=True,stdout=subprocess.PIPE).stdout.read()
    error = False
    ret=""
    if req.method == "POST":
        node=req.POST.get('cmd_run_command_host')
        cmd=req.POST.get('cmd_run_command_cmd')
        alivenode=req.POST.get('chechk_alive_host_name')
        alivecmd=req.POST.get('check_alive_host_cmd')
        print node,cmd
        print alivenode,alivecmd
        #if alivenode != "" or alivecmd != "":
        #     return HttpResponseRedirect('/check_host_alive/')
        #ret=salt.client.LocalClient().cmd('node2','cmd.run',['ping -c 4 8.8.8.8'])
        #ret=ret['node2']
        if node != "" and cmd != "":
            bad_cmd=['rm','shutdown','cat /etc/passwd']
            if node != "" and cmd != "" and cmd not in bad_cmd:
                try:
                    ret=salt.client.LocalClient().cmd(node,'cmd.run',[cmd])
                    ret=node+':\n'+ret[node]
                except:
                    ret=node+u' running  '+cmd+u' is error，please make sure the network is ok'
                    error=True
            elif node == "" or cmd == "" :
                ret="input is can't null"
                error=True
            elif cmd  in bad_cmd:
                ret="the command is not allow to use"
                error=True
            return render_to_response('saltstack.html',{"result_data":ret,"error":error},context_instance=RequestContext(req))

        if alivenode  != "" and alivecmd != "":
            node=alivenode
            cmd=alivecmd
            allow_cmd=['test.ping','test.version']
            if cmd in allow_cmd:
                try:
                    ret=salt.client.LocalClient().cmd_full_return(node,cmd)
                    ret=str(node)+" "*24+str(ret[node]['ret'])
                except:
                    ret=str(node)+" "*24+"False"
                    error=True
            elif node == "" or cmd == "" :
                ret="input is can't null"
                error=True
            else:
                ret="The command is not allowed to use"
                error=True
            return render_to_response('saltstack.html',{"result_data":ret,"error":error},context_instance=RequestContext(req)) 
    #print ret
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
        ###################################sshd_config################################
        f=open('/etc/salt/master.bak','r')
        sshd_config=f.read()
        ###################################sshd_config################################
        ret = ""
        return render_to_response('saltstack.html',{"username":username,"sshd_config":sshd_config,"result_data":ret,"error":error,"path":path,"id":id,"host":host,"domain":domain,"fqdn":fqdn,"nodename":nodename,"localhost":localhost,"server_id":server_id,"master":master,"ipv4":ipv4,"saltversion":saltversion,"pythonversion":pythonversion,"shell":shell,"defaultencoding":defaultencoding,"defaultlanguage":defaultlanguage,"os":os,"os_family":os_family,"kernel":kernel,"kernelrelease":kernelrelease,"ps":ps,"virtual":virtual,"cpu_model":cpu_model,"cpuarch":cpuarch,"num_cpus":num_cpus,"cpu_flags":cpu_flags,"num_gpus":num_gpus,"gpus":gpus,"mem_total":mem_total,"ipv4":ipv4,"path":path,"saltpath":saltpath,"pythonpath":pythonpath},context_instance=RequestContext(req))
    return render_to_response('saltstack.html',{"result_data":ret,"error":error},context_instance=RequestContext(req))
def minions(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('minion.html',context_instance=RequestContext(req))
#def saltstack_alive_host(req):
#    error = False
#    if req.method == "POST":
#        node=req.POST.get('chechk_alive_host_name')
#        cmd=req.POST.get('check_alive_host_cmd')  
#        allow_cmd=['test.ping']
#        if cmd in allow_cmd:
#            try:
#                ret=salt.client.LocalClient().cmd_full_return(node,'test.ping')
#                ret=str(node)+" "*24+str(ret[node]['ret'])
#            except:
#                ret=str(node)+" "*24+"False"
#                error=True
#        elif node == "" or cmd == "" :
#            ret="input is can't null"
#            error=True
#        else:
#            ret="The command is not allowed to use"
#            error=True
#    elif req.method == "GET":
#        ret = ""
#    return render_to_response('saltstack.html',{"result_data":ret,"error":error},context_instance=RequestContext(req))
def salt_key(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    proc = subprocess.Popen('salt-key', stdout=subprocess.PIPE)
    salt_key = proc.stdout.read().replace('\n','<br>')
    #return render_to_response('saltstack.html',{"salt_key":salt_key},context_instance=RequestContext(req))
    return HttpResponse(salt_key)
def saltstack_master_config(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    try:
        f=open('/etc/salt/master','r')
        data=f.read()
    except:
        data="The file /etc/salt/master is not exist"
    return HttpResponse(data)
def saltstack_master_group(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    try:
        f=open('/etc/salt/master.d/node.conf')
        data=f.read()
    except:
        data="The file /etc/salt/master.d/node.conf is not exist "
    return HttpResponse(data)
def saltstack_top_sls(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    try:
        f=open('/srv/salt/top.sls')
        data=f.read()
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
        CMD='cat /tmp/myapp.conf'
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
