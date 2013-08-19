#!/usr/bin/env python
import salt.utils

def test1():
    cmd='ping -c 4 8.8.8.8'
    ret=__salt__['cmd.run'](cmd)
    print ret
test1()
