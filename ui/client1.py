from socket import *
import json
from threading import Thread
from ui import *



# 创建套接字
sockfd = socket()

# 发起连接
server_addr = ("127.0.0.1",8888)
sockfd.connect(server_addr)
def recv(sockfd):
    while True:
        data = sockfd.recv(1024)
        print(data.decode())
        recv_message()
def send(data,user):
    print(data)
    data = {"style": "M", "uid": user,"data": data}
    # sockfd.send(data.encode())
    data = json.dumps(data).encode()
    sockfd.send(data)
# 注册
def register(user, password1, password2, name):
    # # 创建套接字
    # sockfd = socket()
    #
    # # 发起连接
    # server_addr = ("127.0.0.1",8888)
    # sockfd.connect(server_addr)

    # 收发消息
    while True:
        data = {"style": "R", "uid": user, "uname": name, "upwd": password1}
        request = json.dumps(data).encode()

        if not data:
            break
        sockfd.send(request)
        data = sockfd.recv(1024)
        print("From server:",data.decode())
        return data.decode()
    sockfd.close()


# 登录
def login(user, password1, password2, name):
    # # 创建套接字
    # sockfd = socket()
    #
    # # 发起连接
    # server_addr = ("127.0.0.1",8888)
    # sockfd.connect(server_addr)

    # 收发消息
    while True:
        data = {"style": "E", "uid": user, "uname": name, "upwd": password1}
        request = json.dumps(data).encode()

        if not data:
            break
        sockfd.send(request)
        data = sockfd.recv(1024)
        a = json.loads(data.decode())
        # print("From server:",data.decode())
        print(a)
        # 创建新的线程
        t = Thread(target=recv, args=(sockfd,))
        t.setDaemon(True)  # 分支线程会随主线程退出
        t.start()

        return a
    sockfd.close()








