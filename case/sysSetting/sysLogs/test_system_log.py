# -*- coding: utf-8 -*-
# @Time : 2021/9/28 10:16
# @Author : zhangyan
# @File : api_system_log.py.py  系统设置-系统日志 测试类

# 导包：unittest框架、ApiSystemLog
import unittest
from api.m_sysSetting.m_sysLogs.api_system_log import ApiSystemLog


# 新建测试类：让unittest认识到这是一条测试用例
class TestSystemLog(unittest.TestCase):
    # 新建测试方法
    def test_system_log(self):
        # 暂存数据url...（之后参数化从data文件夹中读取）
        url = ""
        data = ""

        # 调用api类，获取响应结果
        res = ApiSystemLog().api_get_system_log(url, data)
        print("响应结果：", res.json())

        # 断言响应信息
        self.assertEquals("OK", res.json()['message'])
        self.assertEquals(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
