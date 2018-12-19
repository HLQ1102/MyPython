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
# create_dep = '''create table departments(dep_id int,
# dep_name varchar(20) UNIQUE NULL , PRIMARY KEY (dep_id))'''

# create_emp = '''create table employers(emp_id INT,
# emp_name VARCHAR(20),
# gender VARCHAR(6),
# email VARCHAR(50),
# phone char(11),
# dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id))'''

create_sal = '''create table salary(auto_id INT,
data DATE,
emp_id INT,
basic INT,
awards INT,
PRIMARY KEY(auto_id),
FOREIGN KEY(emp_id) REFERENCES employers(emp_id))'''

# create_sal = '''create table salary(auto_id INT ,
# date DATE ,
# emp_id INT ,
# basic INT ,
# awards INT ,
# PRIMARY KEY(auto_id) ,
# FOREIGN KEY(emp_id) REFERENCES employers(emp_id)
# )'''
# cursor.execute(create_dep)
# cursor.execute(create_emp)
cursor.execute(create_sal)
conn.commit()
cursor.close()
conn.close()
