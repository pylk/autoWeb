# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj,LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_dailyFill

class Test_overall__mn_dailyFill(unittest.TestCase):
    """
    锰系合金日填报-填报功能验证
    """
    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj=Moudle_dataFill_overall_mn_dailyFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])
    def Test_overall_mn_dailyFill(self):
        """
        锰系合金日填报-填报功能验证
        """
        #点击数据管理
        self.naviObj.click_dataManagement()
        #点击数据填报
        self.naviObj.click_dataFill()
        #点击综合产业
        self.naviObj.click_overall()
        #点击填报
        self.naviObj.click_dataFill_overall_fill()
        #点击锰系合金日填报
        self.naviObj.click_dataFill_overall_fill_mn_dailyFill()
        #点击组织树中的综合产业
        self.mdObj.click_orgTree()
        #点击锰系合金
        self.mdObj.click_mxhj()
        time.sleep(2)
        #输入验证数据
        self.mdObj.mn_dailyFill_input_inTable(2,2,3)
        #判断填报是否已填写
        if self.mdObj.isClickable(self.mdObj.mn_bc):
            self.mdObj.click_bc()
            self.output = self.mdObj.getValue(self.mdObj.outPut)
            # 验证已输入数据
            self.assertEqual(int(self.output), 2)
            self.mdObj.click_tj()
        else:
            print("填报已提交")




        time.sleep(2)

    def tearDown(self):
        self.d.close()


