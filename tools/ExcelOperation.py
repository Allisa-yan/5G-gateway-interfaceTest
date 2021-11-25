# -*- coding: utf-8 -*-
# @Time : 2021/11/25 15:47
# @Author : zhangyan
# @File : ExcelOperation.py  excel表相关操作
import os

class ExcelOperation(object):
    # 初始化方法
    def __init__(self):
        # 动态获取文件路径
        # print(os.path.abspath())  # 获取当前文件的绝对路径
        # print(os.path.dirname(os.path.abspath(__file__))) # 获取当前文件的上一级目录的绝对路径
        # print(os.path.)

        print(os.getcwd())

    # 读取excel文件方法
    def read_excel(self):
        pass

    # 写入excel文件方法
    def write_excel(self):
        pass


if __name__ == '__main__':
    # file_name = "5GClient_testcase.xlsx"
    ExcelOperation()