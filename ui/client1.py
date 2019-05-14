from socket import *
import json

def client(user, passsword1, passsword2, name):
    # 创建套接字
    sockfd = socket()

    # 发起连接
    server_addr = ("127.0.0.1",8888)
    sockfd.connect(server_addr)

    # 收发消息
    while True:
        data = {"style": "E", "uid": user, "uname": name, "upwd": passsword1}
        request = json.dumps(data).encode()

        if not data:
            break
        sockfd.send(request)
        data = sockfd.recv(1024)
        print("From server:",data.decode())
        return data.decode()
    sockfd.close()








