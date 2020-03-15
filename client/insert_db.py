#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import prettytable as pt

def CreateInforMationTable(me_cursor):
    #创建登录信息表，包含id，登录名，密码
    me_cursor.execute(
        '''CREATE TABLE OA.information(id int not null auto_increment primary key,
        name varchar(255) not null, 
        password varchar(8) not null)
        ''')
    print("创建登录信息表，包含id，登录名，密码 success")
    #创建课程表
def CreateLesson(me_cursor):
    me_cursor.execute(
        '''CREATE TABLE OA.lesson(id int not null auto_increment primary key,
        name varchar(255) not null )''')



#添加新的信息到登录信息表中
# def AppendInforMation(me_cursor):
#     student_informat=("INSERT INTO information(name,password) values(%s,%s)")
#     me_cursor.execute(student_informat,(user_name,user_passwd))
#     me_connection.commit()
#     print(me_cursor.lastrowid) 

#查看学生的选课情况()
def GetStudentSelfData(userid,dbConn):
    cursor=dbConn.cursor()
    querySQL=("""SELECT class_id FROM student where user_id = "%s" """ % (userid))
    cursor.execute(querySQL)
    #取出全部数据
    result=cursor.fetchall()
    if len(result)>0:
        querySubjectSQL=("""SELECT class_id,subject FROM lesson where class_id in (%s) """ % (result[0][0]))
        cursor.execute(querySubjectSQL)
        #取出全部数据
        result=cursor.fetchall()
        print('*'*20,'我的课程表',"*"*20)
        tb=pt.PrettyTable()
        tb.field_names=['课程编号','课程名']
        for classList in result:
            tb.add_row([classList[0],classList[1]])
        print(tb)
        return

    

def ALLlesson(dbConn):
    cursor=dbConn.cursor()
    cursor.execute('SELECT class_id,subject from lesson')
    result=cursor.fetchall()
    print('-'*20,'全部课程表',"-"*20)
    tb = pt.PrettyTable()
    tb.field_names = ["课程编号", "课程名字"]
    for classList in result:
        tb.add_row([classList[0],classList[1]])
    print(tb)
    return result




def NEWStudentSelfDate(userid,dbConn):
    newclass=input('请输入要选的课程编号')
    dbConnCursor=dbConn.cursor()
    newselfdate=(""" INSERT INTO student (user_id ,class_id) values (%s,%s)""")
    dbConnCursor.execute(newselfdate,(userid,newclass))
    dbConn.commit()

def DELselfclass(userid,dbConn):
    delnum=[input('请输入要删除的课程编号')]
    for num in delnum:
        


