# -*- coding:utf-8 -*-
import time
import unittest
import random
from AutoFramework.testobject.comm_obj import NavigateObj, LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_hotel_monthFill


class Test_overall_hotel_monthFill_modify(unittest.TestCase):
    """
    酒店月填报-修改功能验证
    """

    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj = Moudle_dataFill_overall_hotel_monthFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])

    def Test_overall_hotel_monthFill_modify(self):
        """
        酒店月填报-修改功能验证
        """
        # 点击数据管理
        self.naviObj.click_dataManagement()
        # 点击数据填报
        self.naviObj.click_dataFill()
        # 点击综合产业
        self.naviObj.click_overall()
        # 点击修改
        self.naviObj.click_dataFill_overall_modify()
        # 点击酒店月成本修改
        self.naviObj.click_dataFill_overall_modify_hotelMonth()
        time.sleep(2)

        if self.mdObj.isClickable(self.mdObj.modifyButton):
            self.mdObj.type(111,random.sample(self.mdObj.eList,1)[0])#随机修改一个元素值
            self.mdObj.click_modifyButton()
        else:
            self.mdObj.getLogger.info("填报未填写，无法修改")





    def tearDown(self):
        self.d.close()
