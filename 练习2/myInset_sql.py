from myNew_sql import Student, Stubasic, Session

session = Session()


xwj = Student(stu_num=12, stu_name='肖伍九', denger='男')
wjg = Student(stu_num=13, stu_name='王建港', denger='男')
xr = Student(stu_num=14, stu_name='谢瑞', denger='男')

# session.add(xwj)
session.add_all([wjg, xr])
xwj = Stubasic(num=1, stu_id=12, stu_yuwen=132, stu_shuxue=143)
wjg = Stubasic(stu_id=13, stu_yuwen=128, stu_shuxue=157)
xr = Stubasic(stu_id=14, stu_yuwen=139, stu_shuxue=121)
session.add(xwj)
session.add_all([wjg, xr])
session.commit()
session.close()



