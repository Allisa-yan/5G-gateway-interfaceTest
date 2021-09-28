# -*- coding: utf-8 -*-
# @Time : 2021/9/28 10:16
# @Author : zhangyan
# @File : api_system_log.py.py  系统设置-系统日志 接口类

# 导包
import requests


# 新建对象类，即：日志列表查询类（）
class ApiSystemLog(object):
    # 新建方法：查询日志列表方法
    def api_get_system_log(self, url, data):
        # headers定义
        headers = {"Content-Type": "application/json"}

        # data定义(动态传参)
        data = {}

        # 调用get方法，返回响应对象
        return requests.post(url, headers=headers, json=data)
