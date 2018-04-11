# -*- coding: utf-8 -*-
import socket
import re
import os
import sys
import crypt

def __password():
    localIP = socket.gethostbyname(socket.gethostname())
    a = re.split('[.]', localIP)
    addr = a[3]
    ps = "Zhb2018!@#$%^" + addr
    # ps = "Zhb2018)(*&^" + addr
    return ps

def changepass():
    localIP = socket.gethostbyname(socket.gethostname())
    new_passwd = crypt.crypt(__password(), "ab")
    change_passwd = "usermod -p %s root" % (new_passwd)
    os.system(change_passwd)
    return "Congratulation!, password for %s is %s " % (localIP, __password())
    # sys.exit()


