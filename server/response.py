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
            解析信息
        """
        pass
    

        # 查询数据库


    def do_register(self,c,request,addr):
        """
            处理用户注册
            1.接收客户请求
            2.验证密码是否正确，不正确，返回失败
            3.密码正确，对账号进行验证，如果账号存在，返回失败
            4.如果账号成功，则将用户信息写入数据库
        """
        uid = request["uid"]
        res = self.sql.query_user_by_name(uid):
        if res == True:
            c.send(b'OK')
            uname = request['uname']
            passwd = request['uspwd']
            self.sql.insert_user(self,uid,uname,passwd)
        else:
            c.send("账号已存在".encode())


        

        
        




    
