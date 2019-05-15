from socket import *
import json

# 注册
def register(user, password1, password2, name):
    # 创建套接字
    sockfd = socket()

    # 发起连接
    server_addr = ("127.0.0.1",8888)
    sockfd.connect(server_addr)

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
    # 创建套接字
    sockfd = socket()

    # 发起连接
    server_addr = ("127.0.0.1",8888)
    sockfd.connect(server_addr)

    # 收发消息
    while True:
        data = {"style": "E", "uid": user, "uname": name, "upwd": password1}
        request = json.dumps(data).encode()

        if not data:
            break
        sockfd.send(request)
        data = sockfd.recv(1024)
        print("From server:",data.decode())
        return data.decode()
    sockfd.close()







