# -*- coding: utf-8 -*-
# @Time : 2021/9/28 13:43
# @Author : zhangyan
# @File : api_requests.py.py   请求方法调用封装
import requests


class ApiRequests(object):
    # 初始化方法：从json字典中获取请求依赖的参数
    def __init__(self, case):
        # 获取请求url，需要拼接域名url
        self.url = host + case.get("path")

        # 获取请求方法

        # 获取请求头

        # 获取参数类型（新增、更新使用）

        # 获取参数

    # get方法（查询）

    # post方法（新增）

    # put方法（更新）

    # delete方法（删除）

    # 调用运行方法
