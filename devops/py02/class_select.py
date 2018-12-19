import pymysql

conn = pymysql.connect(       # 创建链接
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'nsd1807',
        charset = 'utf8'
    )
cursor = conn.cursor()      # 创建游标

# create_dep = '''create table departments(dep_id int,           # 创建职工类型表
# dep_name varchar(20) UNIQUE NULL , PRIMARY KEY (dep_id))'''
# cursor.execute(create_dep)

# create_emp = '''create table employers(emp_id INT,             # 创建职工基本信息表
# emp_name VARCHAR(20),
# gender VARCHAR(6),
# email VARCHAR(50),
# phone char(11),
# dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id))'''
# cursor.execute(create_emp)

# create_sal = '''create table salary(auto_id INT,           # 创建工资表
# data DATE,
# emp_id INT,
# basic INT,
# awards INT,
# PRIMARY KEY(auto_id),
# FOREIGN KEY(emp_id) REFERENCES employers(emp_id))'''  # 外键
# cursor.execute(create_sal)

insert_emp = 'insert into employers VALUE(%s, %s, %s, %s, %s, %s)'
wjg = (10, '王建港', 'man', 'wjg@tedu.com',      '18299984673', 2)
xr  = (11, '谢瑞', 'man', 'xierui@tedu.com',    '15288825455', 2)
ywj = (12, '严文杰', 'man', 'yanwen@tedu.com',  '15645672589', 2)
xsh = (13, '肖书恒', 'man', 'xiaoshu@tedu.com', '12487545552', 2)
lx  = (14, '刘鑫', 'waman', 'liuxin@tedu.com',  '13856942135', 1)
emps = [xr, ywj, xsh, lx]
cursor.execute(insert_emp, wjg)  # 插入一条记录
cursor.executemany(insert_emp, emps)  # 插入多条记录

show_table = 'select * from employers'  # 编辑sql命令
cursor.execute(show_table)          # 执行sql命令, 游标cursor指向查询结果的第一条
result1 = cursor.fetchone()         # 读取一条查询结果
print(result1)

result2 = cursor.fetchmany(2)       # 读取2条查询结果
print(result1)

result3 = cursor.fetchall()         # 读取剩下的所有的结果
print(result3)

conn.commit()          # 如果执行了增删改, 则需要该命令提交执行结果
cursor.close()         # 关闭游标
conn.close()           # 关闭链接

