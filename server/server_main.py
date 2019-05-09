# -*- coding:utf-8 -*-
"""
    chatroom project for server
    env:python3.5
    exc:for socket and Procrss 
"""
from socket import *
import sys,os
import pymysql
import signal
from multiprocessing import Process 
from connfig import *
from sql_db import *
from response import *
import json



class Server(object):

    def __init__(self):
        # 运行main
        self.main()
        # 实例化响应对象
        slef.response = Response()

    def create_socket(self):
        """
            创建tcp套接字
        """
        s = socket()
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
        s.bind((SERVER_IP,PORT))
        s.listen(5)
        return s

    def main(self):
        # 创建套接字
        s = create_socket()
        # 数据库初始化
        ConnSql.sql_init()

        # 处理僵尸进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)

        while True:
            try:
                c, addr = s.accept()
                print("Connect from ", addr)
            except KeyboardInterrupt:
                s.close()
                sys.exit("服务器退出")
            except Exception as e:
                print(e)
                continue
            # 创建子进程
            pid = os.fork()
            if pid == 0:
                s.close()
                do_request(c)  # 处理客户端请求
                sys.exit()
            else:
                c.close()

    @staticmethod
    def do_request(c):
        """
            服务端接收请求处理
        """
        while True:
            data,addr = c.recvfrom(1024)
            request = json.loads(data)
            # 区分请求类型
            if request['style'] == 'Q':
                # 处理用户退出
                c.close()
                return
            elif request['style'] == 'L':
                # 登录请求
                self.response.do_login(c,request,addr)
            elif request['style'] =='R':
                # 注册请求
                self.response.do_register(c,request,addr)
            elif request['style'] =='F':
                # 添加好友请求
                do_joinfriend(c,request,addr)

            elif request['style'] =='C':
                # 创建群聊房间
                do_create_romm(c,request,addr)

            elif request['style'] == 'M':
                # 私聊
                do_priv_chat(c,request,addr)

            elif request['style'] == 'N':
                # 群聊
                text = ' '.join(msgList[2:])
                do_group_chat(s,msgList[1],text)

        
        

if __name__ == '__main__':
    run = Server()
