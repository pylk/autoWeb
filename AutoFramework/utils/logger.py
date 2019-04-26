# coding=utf-8
import logging
import os.path
import os
import time
import inspect
from AutoFramework.utils.configReader import LOG_PATH
from functools import wraps
from AutoFramework.utils.common import getMethodName, getModuleName, getLastMethodName
import pysnooper
global log_path


class Logger(object):
    @pysnooper.snoop()
    def __init__(self, logger=""):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)#设置log输出级别

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        log_path = LOG_PATH
        log_name = log_path + os.sep + rq + '.log'
        formatter = logging.Formatter('%(asctime)s - %(name)s -%(lineno)d - %(levelname)s - %(message)s')

        # 文件句柄
        fh = logging.FileHandler(log_name, mode='a', encoding='utf-8')
        fh.setLevel(logging.INFO)#设置log写入级别依赖log输出级别self.logger.setLevel

        # 流式句柄，输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)

    # self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


# 返回模块级日志实例
# logger = Logger(logger="main").getlog()


def log(msg, level='info'):
    '''
    日志装饰器，没有用到
    :param msg:
    :param level:
    :return:
    '''

    def use_logging(func):
        def wrapper(*args, **kwargs):
            logger = Logger(logger=func.__module__ + "--" + func.__name__).getlog()
            if level == 'info':
                logger.info(msg)
            elif level == 'error':
                logger.error(msg)
            elif level == 'warning':
                logger.warning(msg)
            else:
                print("no such log level")
            return func(*args, **kwargs)

        return wrapper

    return use_logging


@log("this is 3+4")
def add(a, b):
    print(a + b)


if __name__ == '__main__':
    logger = Logger(logger="mainlog").getlog()
    logger.info('this is info')
    logger.debug("this is debug")
    logger.warning('this is warning')
    logger.error('this is error')
add(3,4)
