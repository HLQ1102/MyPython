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

# query1 = 'select * from employers'
# cursor.execute(query1)
# result = cursor.fetchone()
# result1 = cursor.fetchmany(4)
# result2 = cursor.fetchall()
#################################
query1 = 'select a.emp_id, a.emp_name,b.dep_name FROM employers AS a JOIN departments AS b ON a.dep_id = b.dep_id'
cursor.execute(query1)
result = cursor.fetchone()
print(result)
print('-' * 30)
result1 = cursor.fetchone()
print(result1)
result2 = cursor.fetchone()
print('-' * 30)
print(result2)


conn.commit()
cursor.close()
conn.close()
