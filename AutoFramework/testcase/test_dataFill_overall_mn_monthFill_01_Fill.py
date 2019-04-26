# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj,LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_monthFill

class Test_overall__mn_monthFill(unittest.TestCase):
    """
    锰系合金月填报-填报功能验证
    """
    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj=Moudle_dataFill_overall_mn_monthFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])
    def Test_overall__mn_monthFill(self):
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
        #点击锰系合金月填报
        self.naviObj.click_dataFill_overall_fill_mn_monthFill()
        #点击组织树中的综合产业
        self.mdObj.click_orgTree()
        #点击锰系合金
        self.mdObj.click_mxhj()
        time.sleep(2)
        #判断填报是否已提交
        self.list=[self.mdObj.sencondMonth_peopleCost,self.mdObj.sencondMonth_makeCost,self.mdObj.sencondMonth_fullCost]
        for i in self.list:
            if not self.mdObj.get_value(i):
                self.mdObj.mn_monthFill_input_inTable(22,22,22)
                self.mdObj.click_saveButton()
                self.pValue = self.mdObj.getValue(i)
                #验证保存数据是否与输入一致
                self.assertEqual(int(self.pValue), 22)
                self.mdObj.click_saveButton()
                self.mdObj.click_submitButton()
            else:
                print("填报已提交")
                break





        time.sleep(2)

    def tearDown(self):
        self.d.close()


