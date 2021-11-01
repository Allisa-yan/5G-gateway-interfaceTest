# -*- coding: utf-8 -*-
# @Time : 2021/11/1 15:48
# @Author : zhangyan
# @File : read_testcase.py  工具类：读取测试用例

class ReadTestCase(object):
    # 初始化方法
    def __init__(self):
        # excel数据对应列
        cell_config = {
            "case_id": 1,
            "module": 2,
            "case_desc": 3,
            "api_name": 4,
            "path": 5,
            "method": 6,
            "headers": 7,
            "param_type": 8,
            "params": 9,
            "except": 10,
            "is_run": 11,
            "result": 12,
            "desc": 13
        }
