# -*- coding:utf-8 -*-
import random
import re
from AutoFramework.core.pom import BasePage

from selenium.webdriver.common.by import By


class Moudle_dataFill_overall_cenmentMonth(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_overall_cenmentMonth, self).__init__(*args, **kwargs)
        # 综合产业组织树定位
        self.orgTree = (By.XPATH, "//span[text()='综合产业']/../../span[1]")
        self.wljd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='万丽酒店']")
        self.zyjd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='中悦酒店']")
        self.syhg = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        self.mxhj = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='锰系合金']")

        ##########-水泥月填报元素定位-#########

        # 二月人工成本
        self.sencondMonth_peopleCost = (By.XPATH, ".//*[@id='people2']")
        # 二月制造成本
        self.sencondMonth_makeCost = (By.XPATH, ".//*[@id='make2']")
        # 二月完全成本
        self.sencondMonth_fullCost = (By.XPATH, ".//*[@id='full2']")

        # 保存按钮
        self.saveButton = (By.XPATH, ".//*[@id='saveButton']")
        # 提交按钮
        self.submitButton = (By.XPATH, ".//*[@id='subButton']")
        # 修改按钮
        self.modifyButton = (By.XPATH, ".//*[@id='ModButton']")

    def click_orgTree(self):
        # 点击组织树中的综合产业
        self.click(self.orgTree)

    def click_wljd(self):
        self.click(self.wljd)

    def click_zyjd(self):
        self.click(self.zyjd)

    def click_syhg(self):
        self.click(self.syhg)

    def click_mxhj(self):
        self.click(self.mxhj)

    def click_saveButton(self):
        # 点击保存按钮
        self.click(self.saveButton)

    def click_submitButton(self):
        # 点击提交按钮
        self.click(self.submitButton)

    def click_modifyButton(self):
        # 点击修改按钮
        self.click(self.modifyButton)

    def get_pValue(self):
        """
        获取sencondMonth_peopleCost输入值
        """
        return self.getValue(self.sencondMonth_peopleCost)

    def get_mValue(self):
        """
        获取sencondMonth_makeCost输入值
        """
        return self.getValue(self.sencondMonth_makeCost)

    def get_fValue(self):
        """
        获取sencondMonth_fullCost输入值
        """
        return self.getValue(self.sencondMonth_fullCost)

    def cement_monthFill_input_inTable(self, num1, num2, num3):
        """
        水泥月填报数据输入
        """
        self.type(num1, self.sencondMonth_peopleCost)
        self.type(num2, self.sencondMonth_makeCost)
        self.type(num3, self.sencondMonth_fullCost)


class Moudle_dataFill_overall_mn_dailyFill(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_overall_mn_dailyFill, self).__init__(*args, **kwargs)
        # 综合产业组织树定位
        self.orgTree = (By.XPATH, "//span[text()='综合产业']/../../span[1]")
        self.wljd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='万丽酒店']")
        self.zyjd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='中悦酒店']")
        self.syhg = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        self.mxhj = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='锰系合金']")

        ##########-锰系合金日填报元素定位-#########

        # 产量
        self.outPut = (By.XPATH, ".//*[@id='yield']")
        # 销量
        self.salesVolume = (By.XPATH, ".//*[@id='salesVolume']")
        # 销价
        self.sellingPrice = (By.XPATH, ".//*[@id='sellingPrice']")

        self.mn_bc = (By.XPATH, ".//*[@id='bc']")
        self.mn_tj = (By.XPATH, ".//*[@id='tj']")
        self.mn_xg = (By.XPATH, ".//*[@id='xg']")
        self.mn_sp = (By.XPATH, ".//*[@id='sp']")

        self.list = [self.salesVolume, self.outPut, self.sellingPrice]

    def click_orgTree(self):
        # 点击组织树中的综合产业
        self.click(self.orgTree)

    def click_wljd(self):
        self.click(self.wljd)

    def click_zyjd(self):
        self.click(self.zyjd)

    def click_syhg(self):
        self.click(self.syhg)

    def click_mxhj(self):
        self.click(self.mxhj)

    def click_bc(self):
        self.click(self.mn_bc)

    def click_tj(self):
        self.click(self.mn_tj)

    def click_xg(self):
        self.click(self.mn_xg)

    def click_sp(self):
        self.click(self.mn_sp)

    def mn_dailyFill_input_inTable(self, num1, num2, num3):
        """
        锰系合金日填报数据输入
        """
        self.type(num1, self.outPut)
        self.type(num2, self.salesVolume)
        self.type(num3, self.sellingPrice)

    def get_listValue(self):
        self.listValue = list(map(self.getValue, self.list))
        return self.listValue


class Moudle_dataFill_overall_mn_monthFill(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_overall_mn_monthFill, self).__init__(*args, **kwargs)
        # 综合产业组织树定位
        self.orgTree = (By.XPATH, "//span[text()='综合产业']/../../span[1]")
        self.wljd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='万丽酒店']")
        self.zyjd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='中悦酒店']")
        self.syhg = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        self.mxhj = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='锰系合金']")

        ##########-锰系合金月填报元素定位-#########

        # 二月人工成本
        self.sencondMonth_peopleCost = (By.XPATH, ".//*[@id='people2']")
        # 二月制造成本
        self.sencondMonth_makeCost = (By.XPATH, ".//*[@id='make2']")
        # 二月完全成本
        self.sencondMonth_fullCost = (By.XPATH, ".//*[@id='full2']")

        self.xg = (By.XPATH, "//div[@class='layui-layer-content']")

        # self.table = (By.XPATH,"//table[@class='new-table new-tablehead-bj']")

        # 保存按钮
        self.saveButton = (By.XPATH, ".//*[@id='saveButton']")
        # 提交按钮
        self.submitButton = (By.XPATH, ".//*[@id='subButton']")
        # 修改按钮
        self.modifyButton = (By.XPATH, ".//*[@id='ModButton']")

    # def input(self,text):
    #     self.table_InputInTableByRow(self.table,(By.XPATH,"//table[@class='new-table new-tablehead-bj']//tr/td[2]"),1,text)
    def click_orgTree(self):
        # 点击组织树中的综合产业
        self.click(self.orgTree)

    def click_wljd(self):
        self.click(self.wljd)

    def click_zyjd(self):
        self.click(self.zyjd)

    def click_syhg(self):
        self.click(self.syhg)

    def click_mxhj(self):
        self.click(self.mxhj)

    def click_saveButton(self):
        # 点击保存按钮
        self.click(self.saveButton)

    def click_submitButton(self):
        # 点击提交按钮
        self.click(self.submitButton)

    def click_modifyButton(self):
        # 点击修改按钮
        self.click(self.modifyButton)

    def mn_monthFill_input_inTable(self, num1, num2, num3):
        """
        锰系合金月填报数据输入
        """
        self.type(num1, self.sencondMonth_peopleCost)
        self.type(num2, self.sencondMonth_makeCost)
        self.type(num3, self.sencondMonth_fullCost)

    def get_value(self, selecoter):
        return self.getValue(selecoter)


class Moudle_dataFill_overall_hotel_dailyFill(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_overall_hotel_dailyFill, self).__init__(*args, **kwargs)
        # 综合产业组织树定位
        self.orgTree = (By.XPATH, "//span[text()='综合产业']/../../span[1]")
        self.wljd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='万丽酒店']")
        self.zyjd = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='中悦酒店']")
        self.syhg = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='绥阳化工']")
        self.mxhj = (By.XPATH, "//span[text()='综合产业']/../following-sibling::*//span[text()='锰系合金']")

        ##########-酒店日填报元素定位-#########

        # 入住率
        self.occupancyRate = (By.XPATH, ".//*[@id='occupancyRate']")
        # 平均房价
        self.averageHousePrice = (By.XPATH, ".//*[@id='averageHousePrice']")
        # 房客收入
        self.sellingPrice = (By.XPATH, ".//*[@id='roomIncome']")

        # 餐饮收入
        self.foodBeverageIncome = (By.XPATH, ".//*[@id='foodBeverageIncome']")
        # 其他业务收入
        self.otherBusinessIncome = (By.XPATH, ".//*[@id='otherBusinessIncome']")
        # 总收入
        self.totalIncome = (By.XPATH, ".//*[@id='totalIncome']")

        # 电耗量
        self.electricityConsumption = (By.XPATH, ".//*[@id='electricityConsumption']")

        # 水耗量
        self.waterConsumption = (By.XPATH, ".//*[@id='waterConsumption']")
        # 天然气耗量
        self.naturalConsumption = (By.XPATH, ".//*[@id='naturalConsumption']")

        self.mn_bc = (By.XPATH, ".//*[@id='bc']")
        self.mn_tj = (By.XPATH, ".//*[@id='tj']")
        self.mn_xg = (By.XPATH, ".//*[@id='xg']")
        self.mn_sp = (By.XPATH, ".//*[@id='sp']")

        self.list = [self.occupancyRate, self.averageHousePrice, self.sellingPrice, self.foodBeverageIncome,
                     self.otherBusinessIncome, self.totalIncome, self.electricityConsumption, self.waterConsumption,
                     self.naturalConsumption]
        self.dict = {x: random.randint(1, 1) for x in self.list}

    def click_orgTree(self):
        # 点击组织树中的综合产业
        self.click(self.orgTree)

    def click_wljd(self):
        self.click(self.wljd)

    def click_zyjd(self):
        self.click(self.zyjd)

    def click_syhg(self):
        self.click(self.syhg)

    def click_mxhj(self):
        self.click(self.mxhj)

    def click_bc(self):
        self.click(self.mn_bc)

    def click_tj(self):
        self.click(self.mn_tj)

    def click_xg(self):
        self.click(self.mn_xg)

    def click_sp(self):
        self.click(self.mn_sp)

    def get_listValue(self):
        self.listValue = list(map(self.getValue, self.list))
        return self.listValue

    def hotel_dailyFill_input_inTable(self):
        """
        酒店日填报数据输入
        """
        for k, v in self.dict.items():
            self.type(v, k)


class Moudle_dataFill_overall_hotel_monthFill(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_overall_hotel_monthFill, self).__init__(*args, **kwargs)

        ##########-酒店月填报元素定位-#########
        self.table = (By.XPATH, "//tbody[@id='month_hotel_table']/..")
        self.tag = (By.XPATH, ".//*[@id='month_hotel_table']")
        self.year = (By.XPATH, ".//*[@id='year']")

        #定义填报元素集合
        self.people = {".//*[@id='people" + str(x) + "']" for x in range(1, 13)}
        self.live = {".//*[@id='live" + str(x) + "']" for x in range(1, 13)}
        self.food = {".//*[@id='food" + str(x) + "']" for x in range(1, 13)}
        self.guest = {".//*[@id='guest" + str(x) + "']" for x in range(1, 13)}
        self.yearpeople = {".//*[@id='yearpeople" + str(x) + "']" for x in range(1, 13)}
        self.yearlive = {".//*[@id='yearlive" + str(x) + "']" for x in range(1, 13)}
        self.yearfood = {".//*[@id='yearfood" + str(x) + "']" for x in range(1, 13)}
        self.yearguest = {".//*[@id='yearguest" + str(x) + "']" for x in range(1, 13)}

        self.els = self.people | self.live | self.food | self.guest | self.yearpeople | self.yearlive | self.yearfood | self.yearguest
        self.els = self.sortEle(self.els)
        self.eList = [(By.XPATH, x) for x in self.els]

        # 保存按钮
        self.saveButton = (By.XPATH, ".//*[@id='saveButton']")
        # 提交按钮
        self.submitButton = (By.XPATH, ".//*[@id='subButton']")
        # 修改按钮
        self.modifyButton = (By.XPATH, ".//*[@id='ModButton']")

        self.search = (By.XPATH, "//input[@value='查询']")

        self.js = "document.getElementById('year').removeAttribute('readonly');"

    def sortEle(self, ls):
        #元素按数字排序
        self.ls = ''.join(ls)
        self.re_digits = re.compile(r'(\d+)')
        self.pieces = self.re_digits.split(self.ls)  # 切成数字和非数字
        self.e = [int(x) for x in self.pieces[1::2]]  # 将数字部分转成整数
        self.newList = sorted(ls, key=lambda p: p)  # 将前面的函数作为key来排序
        return self.newList

    def input_yValue(self, yValue):
        #输入年份值
        self.js_value = "document.getElementById('year').value={};".format(yValue)
        self.js_execute(self.js_value)

    def click_saveButton(self):
        # 点击保存按钮
        self.click(self.saveButton)

    def click_submitButton(self):
        # 点击提交按钮
        self.click(self.submitButton)

    def click_modifyButton(self):
        # 点击修改按钮
        self.click(self.modifyButton)

    def click_search(self):
        self.click(self.search)

    def input_inTable(self, text):
        self.table_InputInTableByRow(self.table, (By.XPATH, "//tbody[@id='month_hotel_table']/..//td[3]/input"), 1,
                                     text)
