#coding=utf-8
import os
import time
import unittest
from unittest import SkipTest

import HTMLReport
from selenium import webdriver
from AutoFramework.utils.configReader import YamlReader
from AutoFramework.testcase.d_corp_addSource import CorpAddSource_Action
from AutoFramework.testcase.d_corp_delSource import CorpDelSource_Action
from AutoFramework.testcase.d_corp_login import CorpLogin_Action
from AutoFramework.testcase.d_corp_logout import CorpLogout_Action
from AutoFramework.testcase.d_corp_syncSource import CorpSyncSource_Action
from AutoFramework.utils.configReader import LOG_PATH, CHROMEDRIVER


class MySuite(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    conf=YamlReader().data
    caseList=conf['suite']['oper']
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    #     cls.driver.get("http://192.168.1.30:8081/ds-web-gt/index.html#/login")
    #     time.sleep(2)
    #     CorpLogin_Action(cls.driver).run()
    #     CorpAddSource_Action(cls.driver).run()
    #     CorpSyncSource_Action(cls.driver).run()
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     CorpDelSource_Action(cls.driver).run()
    #     CorpLogout_Action(cls.driver).run()
    #
    # def test_01_CorpLogin(self):
    #     '''这个测试是用来登陆企业端'''
    #     CorpLogin_Action(self.driver).run()
    #
    # # @SkipTest
    # def test_02_CorpSyncSource(self):
    #     '''同步源点'''
    #     CorpAddSource_Action(self.driver).run()
    #     CorpSyncSource_Action(self.driver).run()
    #     CorpDelSource_Action(self.driver).run()
    #     CorpSyncSource_Action(self.driver).run()
    #
    # # @SkipTest
    # def test_04_CorpSyncSource_1(self):
    #     CorpSyncSource_Action(self.driver).run()
    # # @SkipTest
    # def test_02_CorpAddSource(self):
    #     '''单个源点添加'''
    #     CorpAddSource_Action(self.driver).run()
    # @SkipTest
    # def test_03_CorpDelSource(self):
    #     CorpDelSource_Action(self.driver).run()
    # # @SkipTest
    # def test_05_CorpLogout(self):
    #     '''退出'''
    #     CorpLogout_Action(self.driver).run()


# path = os.path.dirname(__file__)
# outfile = os.path.join(path, 'mySuite.py')
# run(argv=['nosetests', '-v', '--with-html-output', '--html-out-file=report.html', outfile], plugins=[HtmlOutput()])
if __name__=="__main__":
    curTime=time.strftime("%Y%m%d%H%M%S",time.localtime())
    path = os.path.dirname(LOG_PATH+os.sep)
    # shutil.rmtree(path)
    # os.mkdir(path)
    name='testReport'+str(curTime)
    suite=unittest.TestSuite()
    # suite.addTest(MySuite("test_01_CorpLogin"))
    # suite.addTest(MySuite("test_02_CorpSyncSource"))
    # # suite.addTest(MySuite("test_05_CorpLogout"))
    # # suite.addTest(MySuite("test_03_CorpDelSource"))
    # suite.addTest(MySuite("test_04_CorpSyncSource_1"))
    # suite.addTest(MySuite("test_05_CorpLogout"))
    runner=HTMLReport.TestRunner(name,path)
    runner.run(suite)







