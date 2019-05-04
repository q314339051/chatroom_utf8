"""
    sql模块
"""
from connfig import *
import pymysql


class DBhelper:
    def __init__(self):
        """
            构造方法
        """
        # 数据库连接对象
        self.db_conn = None
        self.db_conf = DbConf()

    def open_conn(self):
        """
            连接数据库
        :return:
        """
        try:
            # 建立连接对象
            self.db_conn = pymysql.connect(self.db_conf.host, self.db_conf.user, self.db_conf.passwd,
                                           self.db_conf.dbname)
        except Exception as e:
            print("连接数据库错误")
            print(e)
        else:
            print("连接数据库成功")

    def close_conn(self):
        """
            关闭数据库连接
        :return:
        """
        try:
            self.db_conn.close()
        except Exception as e:
            print("关闭数据库错误")
            print(e)
        else:
            print("关闭数据库成功")