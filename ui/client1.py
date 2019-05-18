from socket import *
import json
from threading import Thread
from ui import *
class Client:
    def __init__(self):
        self.msglist = []
        # 创建套接字
        self.sockfd = socket()
        # 发起连接
        self.server_addr = ("127.0.0.1", 8888)
        self.sockfd.connect(self.server_addr)

    def recv(self,sockfd):
        while True:
            data = sockfd.recv(1024)
            request = json.loads(data.decode())

            print("收到信息",request)
            self.msglist.append(request)
            print(self.msglist)
    def send(self,data,user,):
        print(data)
        data = {"style": "M", "uid": user,"data": data}
        # sockfd.send(data.encode())
        data = json.dumps(data).encode()
        self.sockfd.send(data)
    # 注册
    def register(self,user, password1, password2, name):
    # # 创建套接字
    # sockfd = socket()
    # # 发起连接
    # server_addr = ("127.0.0.1",8888)
    # sockfd.connect(server_addr)
    # 收发消息
        data = {"style": "R", "uid": user, "uname": name, "upwd": password1}
        request = json.dumps(data).encode()
        self.sockfd.send(request)
        data = self.sockfd.recv(1024)
        print("From server:",data.decode())
        return data.decode()
    # sockfd.close()


    # 登录
    def login(self,user, password1, password2, name):
    # # 创建套接字
    # sockfd = socket()
    #
    # # 发起连接
    # server_addr = ("127.0.0.1",8888)
    # sockfd.connect(server_addr)

        data = {"style": "E", "uid": user, "uname": name, "upwd": password1}
        request = json.dumps(data).encode()

        self.sockfd.send(request)
        data = self.sockfd.recv(1024)
        a = json.loads(data.decode())
        # print("From server:",data.decode())
        print(a)
        # 创建新的线程
        t = Thread(target=self.recv, args=(self.sockfd,))
        t.setDaemon(True)  # 分支线程会随主线程退出
        t.start()

        return a
# sockfd.close()








