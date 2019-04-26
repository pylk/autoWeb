# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj,LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_monthFill

class Test_overall__mn_monthFill_modify(unittest.TestCase):
    """
    锰系合金月填报-修改功能验证
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
        锰系合金月填报-修改功能验证
        """
        #点击数据管理
        self.naviObj.click_dataManagement()
        #点击数据填报
        self.naviObj.click_dataFill()
        #点击综合产业
        self.naviObj.click_overall()
        #点击修改
        self.naviObj.click_dataFill_overall_modify()
        #点击锰系合金月填报修改
        self.naviObj.click_dataFill_overall_modify_mnMonth()
        #点击组织树中的综合产业
        self.mdObj.click_orgTree()
        #点击锰系合金
        self.mdObj.click_mxhj()
        time.sleep(2)
        
        #验证填报是否可修改
        self.valueList=[self.mdObj.sencondMonth_peopleCost,self.mdObj.sencondMonth_makeCost,self.mdObj.sencondMonth_fullCost]
        if self.mdObj.isClickable(self.mdObj.modifyButton):
            self.mdObj.mn_monthFill_input_inTable(22,22,22)
            self.mdObj.click_modifyButton()
        elif self.valueList:
            self.mdObj.shot("填报未审核")
            print("填报未审核")
        else:
            self.mdObj.shot("填报未提交")
            print("填报未提交")


        time.sleep(2)

    def tearDown(self):
        self.d.close()


