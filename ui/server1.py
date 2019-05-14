from socket import *
from threading import Thread
import json
import pymysql

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


def handle(connfd):
    print("Connect from:", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        request = json.loads(data)
        print(request)

        if not request:
            break
        if request["style"] == "R":
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "123456", "chatroom",charset='utf8')

            # 使用cursor()方法获取操作游标
            cursor = db.cursor()

            # SQL 插入语句
            sql = """INSERT INTO users VALUES ('%s', '%s', '%s');"""%(request["uid"],request["uname"],request["upwd"])

            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()

            # 关闭数据库连接
            db.close()
        elif request["style"] == "E":
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "123456", "chatroom",charset='utf8')

            # 使用cursor()方法获取操作游标
            cursor = db.cursor()

            # SQL 查询语句
            sql = "SELECT * FROM users \
                   WHERE id = '666';"
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                print(results)
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
        connfd.send(b"OK")
    connfd.close()


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(ADDR)
s.listen(3)

# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue

    # 创建新的线程处理客户端
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 分支线程会随主线程退出
    t.start()
