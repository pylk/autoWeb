# -*- coding:utf-8 -*-
import time
import unittest
import datetime
from AutoFramework.testobject.comm_obj import NavigateObj, LoginOutObj
from AutoFramework.utils.configReader import YamlReader, getDriver
from AutoFramework.testobject.module_dataFill_overall_obj import Moudle_dataFill_overall_hotel_monthFill


class Test_overall_hotel_monthFill(unittest.TestCase):
    """
    酒店月填报-填报功能验证
    """

    def setUp(self):
        self.d = getDriver()
        self.d.get(YamlReader().data['global']['corp']['url'])
        self.login = LoginOutObj(self.d)
        self.mdObj = Moudle_dataFill_overall_hotel_monthFill(self.d)
        self.naviObj = NavigateObj(self.d)
        self.login.Login(YamlReader().data['global']['corp']['user'], YamlReader().data['global']['corp']['pass'])

    def Test_overall_hotel_dailyFill(self):
        """
        酒店月填报-填报功能验证
        """
        # 点击数据管理
        self.naviObj.click_dataManagement()
        # 点击数据填报
        self.naviObj.click_dataFill()
        # 点击综合产业
        self.naviObj.click_overall()
        # 点击填报
        self.naviObj.click_dataFill_overall_fill()
        # 点击酒店月填报
        self.naviObj.click_dataFill_overall_fill_hotel_monthFill()
        time.sleep(2)
        # 判断填报是否已填写,若未全部填写则填写未填写部分，若全都被填写则填写上一年
        for i in range(50):
            now = datetime.datetime.now()
            year = datetime.datetime.strftime(now, "%Y")
            self.mdObj.js_execute(self.mdObj.js)
            self.mdObj.input_yValue(int(year) - i * 1)
            self.mdObj.click_search()
            time.sleep(1)
            if self.mdObj.isClickable(self.mdObj.saveButton):
                for e in self.mdObj.eList:
                    if self.mdObj.getAttribute(e, 'readonly') == 'true':
                        self.mdObj.getLogger.info("{},已被填写".format(e))
                    else:
                        self.mdObj.type(1, e)
                        self.mdObj.getLogger("{},正在填写".format(e))
                self.mdObj.click_saveButton()
                self.mdObj.click_submitButton()
                break
            else:
                continue

    def tearDown(self):
        self.d.close()
