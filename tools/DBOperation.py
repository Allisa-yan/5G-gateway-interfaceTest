# -*- coding: utf-8 -*-
# @Time : 2021/11/25 13:35
# @Author : zhangyan
# @File : DBOperation.py  数据库相关操作
import pymysql


class DBOperation(object):

    # 数据库操作
    def operate_db(self, host, user, password, db,sql):
        # 获取数据库连接对象
        db = pymysql.connect(host=host, user=user, password=password, database=db, charset="utf8")
        # 获取游标对象
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 获取结果并返回
        print(cursor.fetchone())
        # 关闭游标对象
        cursor.close()
        # 关闭连接对象
        db.close()


if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = 'root123'
    database = '5g_gateway_client'
    sql='select * from testcases'
    OperateDB().operate_db(host, user, password, database,sql)
