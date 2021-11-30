# -*- coding: utf-8 -*-
# @Time : 2021/9/28 13:43
# @Author : zhangyan
# @File : api_requests.py.py   所有请求方法封装
import requests


class ApiRequests(object):
    # get方法（查询）
    def send_get(self, url, data, headers):
        return requests.get(url=url, headers=headers, data=data).json()

    # post方法（新增）
    def send_post(self, url, data, headers):
        return requests.get(url=url, headers=headers, data=data).json()

    # put方法（更新）
    def send_put(self, url, data, headers):
        return requests.get(url=url, headers=headers, data=data).json()

    # delete方法（删除）
    def send_delete(self, url, data, headers):
        return requests.get(url=url, headers=headers, data=data).json()

    # 请求方法主调用
    def rend_requests(self,url,data,headers,method):
        if method == 'get':
            return self.send_get(url,data,headers)
        elif method == 'post':
            return self.send_post(url,data,headers)
        elif method == 'put':
            return self.send_put(url, data, headers)
        elif method == 'delete':
            return self.send_delete(url, data, headers)


# 调用运行方法
if __name__ == '__main__':
    ApiRequests().rend_requests()
