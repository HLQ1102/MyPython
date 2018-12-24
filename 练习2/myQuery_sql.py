from myNew_sql import Student, Stubasic, Session
from sqlalchemy import and_

session = Session()

# search = 'select * from student'
result = session.query(Student.stu_name, Stubasic.stu_shuxue).join(Stubasic, Stubasic.stu_id==Student.stu_num)
print(result.all())
for i1, i2 in result.all():
    print('%s 的数学成绩：%s' % (i1, i2))
# print(result.first())
# print(result)

session.close()

