from dbconn import Departments, Session, Employees
from sqlalchemy import and_, or_

session = Session()
query1 = session.query(Departments)
# print(query1)
# print(list(query1))
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query2 = session.query(Departments.dep_id, Departments.dep_name)
# print(query2)
# print(list(query2))
# for dep in query2:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in query3:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query4 = session.query(Departments).order_by(Departments.dep_id)[:2]
# for dep in query4:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query5 = session.query(Departments).filter(Departments.dep_id==2)
# print(query5)
# print(list(query5))
# for dep in query5:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query6 = session.query(Departments).filter(Departments.dep_id==3).filter(Departments.dep_name=='开发部')
# print(query6)
# print(list(query6))
# for dep in query6:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))

query7 = session.query(Departments).filter(~Departments.dep_id.in_([1, 3]))
# print(query7)
# print(query7.count())
# for dep in query7:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#     print(dep)

query8 = session.query(Employees).filter(or_(Employees.emp_id==12,Employees.emp_name=='王建港'))
# print(query8)
# for emp in query8:
#     print('%s: %s ' %(emp.emp_name, emp.emp_id))

query9 = session.query(Employees).filter(Employees.emp_id==12)
# print(query9.scalar())
# for emp in query9:
#     print('%s' % emp)

query10 = session.query(Departments.dep_name,).filter(Departments.dep_id==3)
# print(query10)   #
# for dep in query10:
#     print('%s,' % (dep))

query11 = session.query(Departments.dep_id, Employees.emp_name).filter(Departments.dep_id==Employees.dep_id)
# print(query11.first())
# ex = query11.all()  # 连表查询返回的对象取内容不方便,使用all()返回列笔列表
# for hh in ex:
#     print(hh[1])

query12 = session.query(Departments).filter(Departments.dep_name=='hr')
print(query12.first())
# dep = query12.one()       # 使用one()保证返回的值只有一行
# dep.dep_name = '人力资源'  #  修改
# print(dep)

query13 = session.query(Departments).order_by(Departments.dep_id.desc()).first()  # 排序后获取第一行的记录
print('%s' % query13.dep_name)                                 # desc()降序排列, asc()升序排列

query14 = session.query(Employees).get(12)  # get(12) 获取主键是12的记录
print(query14)
emp = query1.first()
print(emp)
# session.delete(emp)



session.commit()
session.close()
