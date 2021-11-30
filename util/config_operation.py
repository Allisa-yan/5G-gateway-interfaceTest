# -*- coding: utf-8 -*-
# @Time : 2021/11/29 10:44
# @Author : zhangyan
# @File : config_operation.py  所有配置文件相关操作
import configparser
import os


class ConfigOperation(object):
    # 初始化方法
    def __init__(self, filename):
        # 动态获取文件路径
        self.filepath = os.path.join(os.path.dirname(os.getcwd()), "config", filename)
        # 创建配置文件对象
        self.conf = configparser.ConfigParser()
        # 读取配置文件
        self.conf.read(self.filepath)
        # .sections()方法返回所有section名列表['section1','section2',...]
        self.secs = self.conf.sections()

    # 读取配置文件
    def read_config(self, section, key):
        # options = self.cf.options(option_name)
        items = self.conf.items(section)  # 获取某section的所有键值对[('key','value'),('key','value'),...]
        print(items)
        host = self.conf.get(section, key)  # 获取某section的键名为xxx的值
        print(host)

    # 写入配置文件
    def write_config(self, section, dataConfig):
        try:
            # 如果插入section不存在，则直接插入
            if section not in self.secs:
                self.conf.add_section(section)
                for k, v in dataConfig.items():
                    self.conf.set(section, k, str(v))
                # 写入文件
                with open(self.filepath, 'w') as f:
                    self.conf.write(f)
        except Exception as e:
            print(e)

    # 删除配置文件
    def delete_config(self):
        pass


if __name__ == '__main__':
    # ConfigOperation("config.ini").read_config("host", "host")
    # ConfigOperation("config.ini").read_config("mysql", "host")
    dataConfig = {"abc": 1234, "root": 123}
    ConfigOperation("config.ini").write_config("abs", dataConfig)
    ConfigOperation("config.ini").write_config("aaaaaaaaa", dataConfig)
