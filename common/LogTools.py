import logging
import os
from common import constant
from common.ConfTools import DoConf


class DoLogs:

    def __init__(self, loggin_name):
        conf = DoConf(constant.globe_conf_dir)
        # 定义一个日志收集器
        self.log = logging.getLogger(loggin_name)
        if not self.log.handlers:
            # 设置日志器级别
            self.log.setLevel(conf.get_value('log_level', 'debug'))
            # 设置日志输出格式
            famatter = logging.Formatter(conf.get_value('log_format', 'format'))

            # 设置日志控制台输出
            hdr = logging.StreamHandler()
            hdr.setLevel(conf.get_value('log_level', 'error'))
            hdr.setFormatter(famatter)

            # 设置日志文件输出
            fdr = logging.FileHandler(os.path.join(constant.log_dir, 'log_info.log'), encoding='utf-8')
            fdr.setLevel(conf.get_value('log_level', 'info'))
            fdr.setFormatter(famatter)

            # 添加处理器到日志器中
            self.log.addHandler(hdr)
            self.log.addHandler(fdr)
