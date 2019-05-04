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

    def main():
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
        


