import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1807',
    charset='utf8'
)
cursor = conn.cursor()
# insert_dep1 = 'insert into departments VALUE(%s, %s)'
# hr = (1, 'hr')
# other_deps = [(2, '运维部'), (3, '开发部'), (4, '测试部')]
# cursor.execute(insert_dep1, hr)
# cursor.executemany(insert_dep1, other_deps)

insert_emp = 'insert into employers VALUE(%s, %s, %s, %s, %s, %s)'
wjg = (10, '王建港', 'man', 'wjg@tedu.com',      '18299984673', 2)
xr  = (11, '谢瑞', 'man', 'xierui@tedu.com',    '15288825455', 2)
ywj = (12, '严文杰', 'man', 'yanwen@tedu.com',  '15645672589', 2)
xsh = (13, '肖书恒', 'man', 'xiaoshu@tedu.com', '12487545552', 2)
lx  = (14, '刘鑫', 'waman', 'liuxin@tedu.com',  '13856942135', 1)
emps = [wjg, xr, ywj, xsh, lx]
# for i in alist:
#     cursor.executemany(insert_emp, i)
# cursor.execute(insert_emp, wjg)
# cursor.execute(insert_emp, xr)
# cursor.execute(insert_emp, xsh)
# cursor.execute(insert_emp, ywj)
# cursor.execute(insert_emp, lx)
cursor.executemany(insert_emp, emps)
conn.commit()
cursor.close()
conn.close()
