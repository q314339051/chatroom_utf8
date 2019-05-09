"""
    处理用户请求模块
"""

from sql_db import *

class Response(object):
    """
        处理客户端响应
    """
    slef.sql = ConnSql()


    def do_login(self,c,request,addr):
        """
            处理客户登录
            1.接收客户信息，解析
            2.验证客户账号跟密码
        """
        uid  = request['uid']
        upwd = request['upwd']
        res = self.sql.verify_login(uid,upwd):
        if res == True:
            c.send(b'OK')
        else:
            c.send('账号或密码有误'.encode())
          


    def do_register(self,c,request,addr):
        """
            处理用户注册
            1.接收客户请求
            2.对账号进行验证，如果账号存在，返回失败
            3.如果账号成功，则将用户信息写入数据库
        """
        uid = request["uid"]
        res = self.sql.query_user_by_name(uid):
        if res == True:
            c.send(b'OK')
            uname = request['uname']
            upwd = request['upwd']
            # 创建用户信息
            self.sql.insert_user(self,uid,uname,upwd)
        else:
            c.send("账号已存在".encode())


        

        
        




    
