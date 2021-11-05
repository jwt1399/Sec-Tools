# -*- coding:utf-8 -*-
import os
import logging
from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))   # 当前目录 【os.path.abspath：返回绝对路径】
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)           # 根目录 【os.pardir：当前目录的父目录】
LOG_PATH = os.path.join(ROOT_PATH, './loginfo/log/')        # 存放log文件的目录


class LogHandler(logging.Logger):
    """日志处理程序"""
    def __init__(self, name, level=DEBUG, stream=False, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __setFileHandler__(self, level=None):
        """
        set file handler
        :param level:
        :return:
        """
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留60天
        # filename：日志文件名
        # when：日志文件按什么维度切分。'S'-秒；'M'-分钟；'H'-小时；'D'-天；'W'-周
        #       这里需要注意，如果选择 D-天，那么这个不是严格意义上的'天'，而是从你
        #       项目启动开始，过了24小时，才会从新创建一个新的日志文件，
        #       如果项目重启，这个时间就会重置。所以这里选择'MIDNIGHT'-是指过了午夜
        #       12点，就会创建新的日志。
        # interval：是指等待多少个单位 when 的时间后，Logger会自动重建文件。
        # backupCount：是保留日志个数。默认的0是不会自动删除掉日志。
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=60, encoding='utf-8')
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        set stream handler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        #日志格式
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def resetName(self, name):
        """
        reset name
        :param name:
        :return:
        """
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()


if __name__ == '__main__':
    log = LogHandler('test')
    log.info('this is a test msg')