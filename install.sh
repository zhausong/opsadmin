#!/bin/bash
#author:itnihao
#http://www.itnihao.com


rpm -q epel-release
[ "$?" != 0 ] && rpm -ivh rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm  && yum install -y Django14
[ "$?" != 0 ] &&  easy_install django==1.4.5
yum install -y MySQL-python
