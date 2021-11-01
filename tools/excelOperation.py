# -*- coding: utf-8 -*-
# @Time : 2021/11/1 15:44
# @Author : zhangyan
# @File : excelOperation.py   封装所有excel操作方法
import os


class ExcelOperation(object):
    # 初始化
    def __init__(self,filename):
        # 动态获取文件路径
        self.file_path = os.path.dirname(__file__)
        # 打开

    # 读取excel
    def read_excel(self):
        pass

    # 写入excel
    def write_excel(self):
        pass
