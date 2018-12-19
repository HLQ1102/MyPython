from dbconn import Departments, Session, Employees
session = Session()
#
# hr = Departments(dep_id=1, dep_name='hr')
# op = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')

# wjg = (10, '王建港', 'man', 'wjg@tedu.com',      '18299984673', 2)
# xr  = (11, '谢瑞', 'man', 'xierui@tedu.com',    '15288825455', 2)
# ywj = (12, '严文杰', 'man', 'yanwen@tedu.com',  '15645672589', 2)
# xsh = (13, '肖书恒', 'man', 'xiaoshu@tedu.com', '12487545552', 2)
# lx  = (14, '刘鑫', 'waman', 'liuxin@tedu.com',  '13856942135', 1)

wjg = Employees(emp_id=11, emp_name='王建港', gender='man', phone='18299984673', dep_id=2)
xr = Employees(emp_id=12, emp_name='谢瑞', gender='man', phone='15288825455', dep_id=2)
ywj = Employees(emp_id=13, emp_name='严文杰', gender='man', phone='15645672589', dep_id=2)
xsh = Employees(emp_id=14, emp_name='肖书恒', gender='man', phone='12487545552', dep_id=2)
lx = Employees(emp_id=15, emp_name='刘鑫', gender='waman', phone='13856942135', dep_id=1)


# session.add(hr)
# session.add_all([op, dev, qa])
session.add_all([wjg, ywj, xr, xsh, lx])
session.commit()
session.close()


from dbconn import Departments, Session, Employees

session = Session()

# hr = Departments(dep_id=1, dep_name='hr')
# op = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# session.add(hr)
# session.add_all([op, dev, qa])
########################
gw = Employees(emp_id=10, emp_name='高伟', gender='男', email='gaowei@163.com', phone='15012345678', dep_id=2)
hl = Employees(emp_id=11, emp_name='何林', gender='男', email='hl@qq.com', phone='13512344321', dep_id=2)
zs = Employees(emp_id=12, emp_name='张思', gender='男', email='zs@qq.com', phone='15098761234', dep_id=2)
zj = Employees(emp_id=13, emp_name='周婕', gender='女', email='zj@163.com', phone='17600112233', dep_id=4)
ws = Employees(emp_id=20, emp_name='王顺', gender='男', email='ws@sohu.com', phone='18900998877', dep_id=3)
zy = Employees(emp_id=25, emp_name='张羽', gender='男', email='zy@163.com', phone='13366778899', dep_id=1)
py = Employees(emp_id=30, emp_name='潘越', gender='男', email='py@sohu.com', phone='13256789876', dep_id=3)
zzy = Employees(emp_id=42, emp_name='张之毅', gender='男', email='zzy@126.com', phone='13898765678', dep_id=4)
ll = Employees(emp_id=45, emp_name='林灵', gender='男', email='ll@aliyun.com', phone='13789896786', dep_id=1)
bsf = Employees(emp_id=48, emp_name='白松峰', gender='男', email='bsf@163.com', phone='13987654321', dep_id=2)
xej = Employees(emp_id=50, emp_name='夏二姣', gender='女', email='xej@qq.com', phone='15098567800', dep_id=2)
session.add_all([gw, hl, zs, zj, ws, zy, py, zzy, ll, bsf, xej])

session.commit()
session.close()
