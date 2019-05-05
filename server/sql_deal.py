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
        return True

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


    def commit():

         self.db_conn.commit()


def get_user(user_id):
    fields = ['id', 'username', 'nickname']
    row = c.execute('SELECT ' + ','.join(fields) + ' FROM users WHERE id=?', [user_id]).fetchall()
    if len(row) == 0:
        return None
    else:
        user = dict(zip(fields, row[0]))
        user['online'] = user_id in user_id_to_sc
        return user