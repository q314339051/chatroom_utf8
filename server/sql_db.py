"""
    sql模块
"""
from connfig import *
import pymysql
import sys

"""
    开始服务器后，先判断是否存在chat数据库,
    如果存在，则创建表，如果表存在，则返回ok
    如果chat数据库不存在，则创建chat数据库，然后建立表

"""
class ConnSql(object):
    def __init__(self):
        self.db_conf = DbConf()


    # @staticmethod
    def sql_init(self):
        """
            初始化数据库
        """
        self.open_conn()
        re = self.create_chatdb()
        if re == True:
            self.create_user_tb()
            # self.create_his_tb()
        else:
            print("存在数据库chat，请检查数据库是否正确")
            

    def open_conn(self):
        """
            连接数据库
        :return:
        """
        try:
            # 建立连接对象
            self.db_conn = pymysql.connect(self.db_conf.host, self.db_conf.user, self.db_conf.passwd,
                                           charset='utf8')
        except Exception as e:
            print("连接数据库错误")
            print(e)
            sys.exit("数据库连接失败，程序退出")
            
        # else:
        #     print("连接数据库成功")

        # 创建游标
        self.cur = self.db_conn.cursor()
        return True

    def create_chatdb(self):
        """
            访问或创建chat库
        """
        try:
            self.cur.execute("create database chat default charset=utf8")
        except Exception as e:
            print(e)
            return False
        else:
            print("创建chat成功")
            return True

    def create_user_tb(self):
        """
            创建用户表
        """
        # 进入chat数据库
        self.cur.execute("use chat;")
        # print("进入数据库成功")
        sql = """create table user (id int primary key auto_increment,uid varchar(32) not 
        null ,uname varchar(32) not null,upwd varchar(32) not null);"""
        # 创建user表
        self.cur.execute(sql)
        print("创建user表成功")
        return True

    def create_his_tb(self):
        """
            创建历史记录
        """
        pass

    def insert_user(self,uid,uname,upwd):
        """
            创建用户
        """
        sql = "insert into user (uid ,uname,upwd) values ('%s','%s')"%(uid,uname,upwd)
        try:
            self.cur.execute(sql)
            self.db_conn.commit()
            return True
        except:
            self.db_conn.rollback()
            return False

        
    def query_user_by_name(self,uid):
        """
            查询用户表
        """
        sql = "select * from user where uid = '%s'"%uid
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r != None:
            return False
        else:
            return True

    def verify_login(self,uid,upwd):
        """
            验证用户登录
        """
        sql = "select * from user where uid = '%s' and upwd = '%s'" %(uid,upwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r != None:
            return True
        else:
            return False






if __name__ == '__main__':
    db = ConnSql()
    db.sql_init()
    










# class DBhelper:
#     def __init__(self):
#         """
#             构造方法
#         """
#         # 数据库连接对象
#         self.db_conn = None
#         self.db_conf = DbConf()

#     def open_conn(self):
#         """
#             连接数据库
#         :return:
#         """
#         try:
#             # 建立连接对象
#             self.db_conn = pymysql.connect(self.db_conf.host, self.db_conf.user, self.db_conf.passwd,
#                                            self.db_conf.dbname)
#         except Exception as e:
#             print("连接数据库错误")
#             print(e)
#         else:
#             print("连接数据库成功")
#         return True

#     def close_conn(self):
#         """
#             关闭数据库连接
#         :return:
#         """
#         try:
#             self.db_conn.close()
#         except Exception as e:
#             print("关闭数据库错误")
#             print(e)
#         else:
#             print("关闭数据库成功")


#     def commit():

#          self.db_conn.commit()


# def get_user(user_id):
#     fields = ['id', 'username', 'nickname']
#     row = c.execute('SELECT ' + ','.join(fields) + ' FROM users WHERE id=?', [user_id]).fetchall()
#     if len(row) == 0:
#         return None
#     else:
#         user = dict(zip(fields, row[0]))
#         user['online'] = user_id in user_id_to_sc
#         return user