import pymysql

conn = pymysql.connect(
    host='192.168.1.50',
    user='root',
    passwd='123456',
    port=3306,
    charset='utf8',
    db='xiao'
)

cursor = conn.cursor()

cursor.execute('show tables')
result = cursor.fetchall()
print(result)
create_base  = 'create table stu_base(stu_id INT ,stu_name CHAR(10), stu_gender CHAR(5))'
create_base1 = '''create table tongxun(id INT ,
stu_id INT, 
phone CHAR(11),
PRIMARY KEY(`id`),
CONSTRAINT `f_ck` FOREIGN KEY(`stu_id`) REFERENCES `stu_base`(`stu_id`)
)'''
cursor.execute(create_base1)

# cursor.execute('show create table student')
# print(cursor.fetchall())


conn.commit()
cursor.close()
conn.close()
