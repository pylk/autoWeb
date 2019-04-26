#coding=utf-8
from AutoFramework.testobject.comm_obj import LoginOutObj
import unittest
from AutoFramework.utils.configReader import YamlReader,getDriver


class Test_corp_login(unittest.TestCase):
    def setUp(self):
        self.d= getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login=LoginOutObj(self.d)
        self.conf=YamlReader().data

    def test_corplogin(self):
        u'''
        登陆
        '''
        user=self.conf['global']['corp']['user']
        passwd=self.conf['global']['corp']['pass']
        self.login.Login(user,passwd)
        # self.login.getLogger.info("##########this is for login module.....")


    def tearDown(self):
        self.d.quit()

