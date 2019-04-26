# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj, LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_dailyFill


class Test_overall__mn_dailyFill_modify(unittest.TestCase):
    """
    锰系合金日填报-修改功能验证
    """

    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj = Moudle_dataFill_overall_mn_dailyFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])

    def Test_overall__mn_dailyFill_modify(self):
        """
        锰系合金日填报-修改功能验证
        """
        # 点击数据管理
        self.naviObj.click_dataManagement()
        # 点击数据填报
        self.naviObj.click_dataFill()
        # 点击综合产业
        self.naviObj.click_overall()
        # 点击修改
        self.naviObj.click_dataFill_overall_modify()
        # 点击锰系合金日填报修改
        self.naviObj.click_dataFill_overall_modify_mnDaily()
        # 点击组织树中的综合产业
        self.mdObj.click_orgTree()
        # 点击锰系合金
        self.mdObj.click_mxhj()
        time.sleep(2)

        # 修改填报
        self.listValue = self.mdObj.get_listValue()
        if self.mdObj.isClickable(self.mdObj.mn_xg):
            for i in self.mdObj.list:
                self.mdObj.type(2, i)
                self.assertEqual(int(self.mdObj.getValue(i)), 2)
            self.mdObj.click_xg()
            self.mdObj.getLogger.info("修改成功")

        elif self.listValue:
            self.mdObj.getLogger.info("填报未审核,无法修改")
        else:
            self.mdObj.getLogger.info("填报未提交，无法修改")

        time.sleep(2)

    def tearDown(self):
        self.d.close()
