"""
    sql模块
"""
from connfig import *
import pymysql


"""
    开始服务器后，先判断是否存在chat数据库,
    如果存在，则创建表，如果表存在，则返回ok

    如果chat数据库不存在，则创建chat数据库，然后建立表

"""
class ConnSql:
    def __init__(self):
        self.db_conf = DbConf()


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
            return False
            print(e)
        else:
            print("连接数据库成功")
        return True

    def visit_chatdb(self):
        """
            访问或创建chat库
        """
        # 创建游标
        self.cur = self.db_conn.cursor()
        try:
            self.cur.execute("create database chat default charset=utf8")
        except Exception as e:
            print(e)
            return False
        else:
            print("创建chat成功")
        return False

    def create_user_db(self):
        






if __name__ == '__main__':
    db = ConnSql()
    db.open_conn()
    db.visit_chatdb()










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