# -*- coding: utf-8 -*-
# @Time : 2021/11/25 13:35
# @Author : zhangyan
# @File : db_operation.py  数据库相关操作
import pymysql

from util.config_operation import ConfigOperation


class DBOperation(object):
    # 初始化数据库参数
    def __init__(self):
        db_config = ConfigOperation("config.ini")
        self.host = db_config.read_config("local_mysql", "host")
        self.user = db_config.read_config("local_mysql", "user")
        self.password = db_config.read_config("local_mysql", "password")
        self.database = db_config.read_config("local_mysql", "db")

    # 数据库连接
    def link_db(self):
        # 获取数据库连接对象
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db, charset="utf8")
        # 获取游标对象
        cursor = db.cursor()

    # 数据库操作
    def excute_sql(self,sql):
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取结果并返回
        print(self.cursor.fetchone())

    # 关闭数据库
    def close_db(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭连接对象
        self.db.close()


if __name__ == '__main__':
    # host = 'localhost'
    # user = 'root'
    # password = 'root123'
    # database = '5g_gateway_client'
    # sql = 'select * from testcases'
    # DBOperation().operate_db(host, user, password, database, sql)
    pass
