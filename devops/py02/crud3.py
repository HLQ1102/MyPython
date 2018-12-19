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

delete_emp = 'delete from departments WHERE dep_id = 2'
cursor.execute(delete_emp)

# update_dep = 'update departments set dep_name=%s WHERE dep_name=%s'
# data = ('运维部', 'hr')
# cursor.execute(update_dep, data)


conn.commit()
cursor.close()
conn.close()
