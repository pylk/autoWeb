#-*- coding:utf-8 -*-
# author:isyuan
# datetime:25/03/2019 17:14
# software: PyCharm

import os
import time
import unittest
from unittest import SkipTest

import HTMLReport
from AutoFramework.testcase.test_baiduLogin import Test_baidu_login
from selenium import webdriver
from AutoFramework.utils.configReader import YamlReader
from AutoFramework.HTMLTestRunnerCN.python3x import HTMLTestReportCN
from AutoFramework.utils.configReader import LOG_PATH, CHROMEDRIVER

# class MySuite(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome(executable_path=CHROMEDRIVER)
#
#
#     def tardown(self):
#         #清除缓存
#         self.driver.refresh()
#         self.driver.quit()


if __name__ == "__main__":
    rp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    rpath=r"C:\Software\pycharm\stu\python\scripts\AutoWeb\AutoFramework\testReport"
    filePath=rpath+"\\"+rp+"Report_CN.html"
    # 构造测试集
    suite1=unittest.TestLoader().loadTestsFromTestCase(Test_baidu_login)
    suite=unittest.TestSuite([suite1])
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='isyuan'
    )
    # 运行测试用例
    runner.run(suite)
    # 关闭文件，否则会无法生成文件
    fp.close()
