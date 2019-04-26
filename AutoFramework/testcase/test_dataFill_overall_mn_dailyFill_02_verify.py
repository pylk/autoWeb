# -*- coding:utf-8 -*-
import time
import unittest
from AutoFramework.testobject.comm_obj import NavigateObj, LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_mn_dailyFill


class Test_overall__mn_dailyFill_verify(unittest.TestCase):
    """
    锰系合金日填报-审核功能验证
    """

    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj = Moudle_dataFill_overall_mn_dailyFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])

    def Test_overall__mn_dailyFill_verify(self):
        """
        锰系合金日填报-审核功能验证
        """
        # 点击数据管理
        self.naviObj.click_dataManagement()
        # 点击数据填报
        self.naviObj.click_dataFill()
        # 点击综合产业
        self.naviObj.click_overall()
        # 点击审核
        self.naviObj.click_dataFill_overall_verify()
        # 点击锰系合金日填报审核
        self.naviObj.click_dataFill_overall_mnDaily_fillVerify()
        # 点击组织树中的综合产业
        self.mdObj.click_orgTree()
        # 点击锰系合金
        self.mdObj.click_mxhj()
        time.sleep(2)

        # 验证填报是否可审核
        self.valueList=self.mdObj.get_listValue()
        if self.mdObj.isClickable(self.mdObj.mn_sp):
            self.mdObj.click_sp()
        elif not self.valueList:
            self.mdObj.getLogger.info("填报未提交，无法审核")
        else:
            self.mdObj.getLogger.info("填报已审核")

        time.sleep(2)

    def tearDown(self):
        self.d.close()
