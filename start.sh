#!/bin/bash
#author:itnihao
#http://www.itnihao.com


case $1 in
start)
     nohup python  manage.py runserver 0.0.0.0:8080  &
     echo "server is start on 0.0.0.0:8080"
     ;;
stop)
     ps -ef |awk '/0.0.0.0:8080/&& !/awk/ {print $2}'|xargs kill -9
     ;;
*)
     echo "Usage $0 {start|stop}"
     ;;
esac
