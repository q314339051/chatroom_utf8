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
from sql_deal import *
from response import *




class Server(object):

    def __init__(self):
        pass

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
        s = create_socket()
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


def do_request(c):
    """
        服务端接收请求处理
    """
    while True:
        data,addr = c.recvfrom(1024)
        msgList = data.decode().split(' ')
        # 区分请求类型
        if msgList[0] == 'L':
            # 登录请求
            Do_login(c,msgList[1],addr)

        elif msgList[0] =='R':
            # 注册请求
            do_register()

        elif msgList[0] =='F':
            # 添加好友请求
            do_joinfriend()

        elif msgList[0] =='C':
            # 创建群聊房间
            do_create_romm()

        elif msgList[0] == 'M':
            # 私聊
            text = ' '.join(msgList[2:])
            do_priv_chat(s,msgList[1],text)

        elif msgList[0] == 'N':
            # 群聊
            text = ' '.join(msgList[2:])
            do_group_chat(s,msgList[1],text)

        elif msgList[0] == 'Q':
            # 处理用户退出
            do_quit(s,msgList[1])
        


