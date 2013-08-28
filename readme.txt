项目介绍:opsadmin运维平台,是一个整合saltstack，zabbix，cobbler，资产管理系统，审计系统于一体的运维管理平台
         集合各种优秀的运维工具，整合最佳的运维技术，实现自动化运维
官方网站：http://www.itnihao.com
预览地址：http://www.itnihao.com/opsadmin/opsadmin-view.html
说    明：本项目由于处于开发阶段，各项功能逐步完善中。
开发语言: python,django,html,css,js
当前版本：0.1
更新日期：2013-08-27

  欢迎大家参与本项目。
1.需要安装软件包
Django14 MySQL-python
shell#bash install.sh
shell#rpm -ivh rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
shell#yum install -y salt-master salt-minions salt
shell#/etc/init.d/salt-master restart
shell#/etc/init.d/salt-minions restart
（需配置salt，此处就不说了）
shell#yum install -y Django14
shell#easy_install django-admin-bootstrapped(美化django后台){如果没有此命令请安装python-setuptools的rpm包}
或者是采用easy_install安装django
shell#easy_install django==1.4.5
2.mysql的配置
#创建mysql数据库
mysql>create database opsadmin character set utf8;
mysql>grant all privileges on opsadmin.* to opsadmin@localhost identified by 'opsadmin';
mysql>flush privileges;
shell#vim  opsadmin/settings.py  #如需更改mysql连接信息，找到以下配置
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'opsadmin',                    #数据库名称
     'USER': 'opsadmin',                    #数据库用户名
     'PASSWORD': 'opsadmin',                #数据库密码
     'HOST': 'localhost',                   #数据库地址
     'PORT': '3306',                        #数据库端口
 }
3.生成数据库
shell#python manage.py syncdb
运行此命令，会生成数据库表，过程中提示是否创建管理员用户，选择y，默认是root用户，如果需要更改，则输入自己的用户名，接下来输入密码
4.开启服务
shell#python  manage.py runserver 0.0.0.0:8080
5.访问站点
http://X.X.X.X:8080
6.由于此项目未完全完成，很多功能没完成，代码会存在不兼容的地方
    6.1 salt-master需要和django在一台机器 
    6.2 目前salt的grains只用了一台机器node2，没有写成通用的，后面会改为通用的
    6.3 其他未完善的地方还有很多，当前相等于一个模型，大约完成40%功能
7.美化后台管理admin
    #pip install django-admin-bootstrapped
    #vim settings.py
    INSTALLED_APPS = (
        'django_admin_bootstrapped',		<==在'django.contrib.admin'的上面
        'django.contrib.admin',
    )

