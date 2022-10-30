# -*- coding:utf-8 -*-
from configparser import ConfigParser

from common import constant


class DoConf:

    def __init__(self, files):
        self.cf = ConfigParser()
        self.cf.read(files, encoding='utf-8')
        switch = self.cf.get('switch', 'on')
        if switch == "dev":
            self.cf.read(constant.conf_test_dir, encoding='utf-8')
        elif switch == "uat":
            self.cf.read(constant.conf_uat_dir, encoding='utf-8')
        elif switch == "prod":
            self.cf.read(constant.conf_prod_dir, encoding='utf-8')
        else:
            print("没有匹配到对应的文件")

    # 获取配置文件
    def get_value(self, sections, options):
        value = self.cf.get(sections, options)
        return value

    def get_float_value(self, sections, options):
        value = self.cf.getfloat(sections, options)
        return value

    # 写入配置文件
    def write_value(self, sections, options, value, files):
        self.cf.set(sections, options, value)
        with open(files, 'w') as configfile:
            self.cf.write(configfile)


if __name__ == '__main__':
    print(DoConf(constant.globe_conf_dir).get_value("log_level", "debug"))