# -*- coding:utf-8 -*-  



from AutoFramework.core.pom import BasePage

from selenium.webdriver.common.by import By


class Moudle_dataFill_coal_costIndex(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_dataFill_coal_costIndex, self).__init__(*args, **kwargs)
        self.linHua_modifyButton = (By.XPATH, ".//*[@id='ModButton']")
        self.muDanBa_modifyButton = (By.XPATH, ".//*[@id='ModButtonm']")

    def click_linHua_modifyButton(self):
        # 点击林华煤矿修改按钮
        self.click(self.linHua_modifyButton)

    def click_muDanBa_modifyButton(self):
        # 点击木担坝煤矿修改按钮
        self.click(self.muDanBa_modifyButton)

    def linHua_input_inTable(self, num1, num2, num3):
        """
        输入林华煤矿二月份的修改数据
        """
        # 林华煤矿二月人工成本
        self.linHua_sencondMonth_peopleCost = (By.XPATH, ".//*[@id='people2']")
        # 林华煤矿二月制造成本
        self.linHua_sencondMonth_makeCost=(By.XPATH, ".//*[@id='make2']")
        # 林华煤矿二月完全成本
        self.linHua_sencondMonth_fullCost=(By.XPATH, ".//*[@id='full2']")

        self.type(num1, self.linHua_sencondMonth_peopleCost)
        self.type(num2, self.linHua_sencondMonth_makeCost)
        self.type(num3, self.linHua_sencondMonth_fullCost)

    def muDanBa_input_inTable(self, num1, num2, num3):
        """
        输入木担坝煤矿二月份修改数据
        """
        # 木担坝煤矿二月人工成本
        self.muDanBa_sencondMonth_peopleCost = (By.XPATH, ".//*[@id='peoplem2']")
        # 木担坝煤矿二月制造成本
        self.muDanBa_sencondMonth_makeCost=(By.XPATH, ".//*[@id='makem2']")
        # 木担坝煤矿二月完全成本
        self.muDanBa_sencondMonth_fullCost=(By.XPATH, ".//*[@id='fullm2']")

        self.type(num1, self.muDanBa_sencondMonth_peopleCost)
        self.type(num2, self.muDanBa_sencondMonth_makeCost)
        self.type(num3, self.muDanBa_sencondMonth_fullCost)
