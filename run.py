#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from client import initdb
from client import insert_db
from client import usersd    
from client import menu    

h="127.0.0.1"
u="root"
p="asas1212"
dbConn=initdb.ConnetDb(h,u,p)
cursor=dbConn.cursor()
user_chois=usersd.constantStart()
def LoginCheck():
    user_name,user_passwd=usersd.constantStr()
    result,userId=usersd.Login(user_name,user_passwd,dbConn)
    return result,userId

if user_chois==1:
    #输入登录名，密码
    result,userId=LoginCheck()
    while True:
        if result!=0:
            result,userId=LoginCheck()
            if result==0:
                continue
        else:
            menu.MenuAction(userId,dbConn)
else:
    user_name,user_passwd=usersd.constantStr()
    userId=usersd.Region(user_name,user_passwd,dbConn)
    menu.MenuAction(userId,dbConn)