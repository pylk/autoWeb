# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj,LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_monthFill

class Test_overall__mn_monthFill_search(unittest.TestCase):
    """
    酒店月填报-查询功能验证
    """
    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj=Moudle_dataFill_overall_mn_monthFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])
    def Test_overall__mn_monthFill_modify(self):
        """
        酒店月填报-查询功能验证
        """
        #点击数据管理
        self.naviObj.click_dataManagement()
        #点击数据填报
        self.naviObj.click_dataFill()
        #点击综合产业
        self.naviObj.click_overall()
        #点击查询
        self.naviObj.click_dataFill_overall_search()
        #点击酒店月填报查询
        self.naviObj.click_dataFill_overall_search_hotelMonth()
        time.sleep(2)
        self.title=self.mdObj.get_page_title()
        self.mdObj.assertEqual(self.title,"贵州金元运营监管平台")

        time.sleep(2)

    def tearDown(self):
        self.d.close()


