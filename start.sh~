#!/bin/bash


case $1 in
start)
     nohup python  manage.py runserver 0.0.0.0:8090  &
     echo "server is start on 0.0.0.0:8090"
     ;;
stop)
     ps -ef |awk '/0.0.0.0:8090/&& !/awk/ {print $2}'|xargs kill -9
     ;;
*)
     echo "Usage $0 {start|stop}"
     ;;
esac
