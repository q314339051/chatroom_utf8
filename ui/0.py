import pymysql


# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "chatroom",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = """select user_id,user_pwd,user_name from users
where user_id in (select user_id2 as user_id from friends where user_id1 = '111')
or user_id in (select user_id1 as user_id from friends where user_id2 = '111');"""
dict1 = {}
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    for i in range(len(results)):
        dict1[i] = results[i]
    if len(results) == 0:


        # 关闭数据库连接
        db.close()

    # for row in results:
    #     fname = row[0]
    #     lname = row[1]
    #     age = row[2]
    #     sex = row[3]
    #     income = row[4]
    #     # 打印结果
    #     print
    #     "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
    #     (fname, lname, age, sex, income)
except:
    print("Error: unable to fecth data")


# 关闭数据库连接
db.close()
print(dict1)
for i in range(len(dict1)):
    print(dict1[i][0],dict1[i][1],dict1[i][2])
