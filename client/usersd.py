def constantStart():
    print('*'*20,'欢迎使用学生选课系统',"*"*20)
    print('*'*62)
    print('1:登录\n2:注册')
    user_chois=int(input('请输入要做的操作：'))
    return user_chois
    
def constantStr():
    user_name=input('请输入登录名:')
    user_passwd=input('请输入登录密码:') 
    return user_name,user_passwd

def Login(user_name,user_passwd,dbConn):
    cursor=dbConn.cursor()
    queryPWDSql=("""SELECT passwd,id FROM information where name = "%s" """ % (user_name))
    cursor.execute(queryPWDSql)
    #取出全部数据
    result=cursor.fetchall()
    if len(result)>0:
        if user_passwd==result[0][0]:
            print("登录成功")
            return 0,result[0][1]
    else:
        print('您输入的密码不正确，请重新输入')
        return 1,0

def Region(user_name,user_passwd,dbConn):
    dbConnCursor=dbConn.cursor()
    dbConnCursor.execute("""SELECT name from information where name="%s" """ % (user_name))
    #取出全部数据
     #取出全部数据
    result=dbConnCursor.fetchall()
    if len(result)>0:
        print('您输入的登录名已存在，请重新输入')
        return 0,
    else:
        #添加登录信息到用户登录表中    
        student_informat=("INSERT INTO information (name,passwd) VALUES (%s,%s)")
        dbConnCursor.execute(student_informat,(user_name, user_passwd))
        dbConn.commit()
        print(dbConnCursor.lastrowid)
        return dbConnCursor.lastrowid
        # #添加信息新信息到学生表中
def updateclass(userid,dbConn):
    dbConnCursor=dbConn.cursor()
    ravamp=int(input('请输入要修改的课程编号：'))
    print(ravamp)
    newrevamp=int(input('请输入修改后的课程编号'))
    print(newrevamp)
    dbConnCursor.execute('''UPDATE student SET class_id = REPLACE(class_id, {ravamp}, {newrevamp})
         WHERE user_id={userid} '''.format(ravamp=ravamp,newrevamp=newrevamp,userid=userid))
    dbConn.commit()






