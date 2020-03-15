from client import insert_db
from client import usersd
def MenuAction(userid,dbConn):
    # cursor=dbConn.cursor()
    student_chois=input('请选择要做的操作：\n1:查询选课信息\n2:修改选课信息\n3:选择新课\n4:删除已选课程')
    if student_chois=='1' :
        insert_db.GetStudentSelfData(userid,dbConn)
    elif student_chois=='2':
        #调用查看所有课程的函数ALLlesson
        insert_db.GetStudentSelfData(userid,dbConn)
        insert_db.ALLlesson(dbConn)
        usersd.updateclass(userid,dbConn)
    elif student_chois=='3':
        insert_db.ALLlesson(dbConn)
        insert_db.NEWStudentSelfDate(userid,dbConn)
    elif student_chois=='4':
    #调用查看学生课程的函数 
        delnum=[input('请输入要删除的课程编号')]
        print(delnum)
    else:
        print('您的输入有误请重新输入')