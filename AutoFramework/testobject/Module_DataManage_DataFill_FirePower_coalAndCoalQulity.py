#encode:utf-8
from selenium.webdriver.common.by import By
from AutoFramework.core.pom import BasePage


class Module_DataManage_DataFill_FirePower_Fill_coalAndCoalQulityFill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Fill_coalAndCoalQulityFill,self).__init__(*args,**kwargs)

        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.xishui=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        #夜班
        self.nightDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use1']")
        self.nightDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful1']")
        self.nightDutySave=(By.XPATH,'''//button[@onclick="saveAndSubmit('10')"]''')
        self.nightDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('11')"]''')
        #早班
        self.earlyDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use2']")
        self.earlyDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful2']")
        self.earlyDutySave=(By.XPATH,'''//button[@onclick="saveAndSubmit('20')"]''')
        self.earlyDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('21')"]''')
        #白班
        self.dayDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use3']")
        self.dayDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful3']")
        self.dayDutySave=(By.XPATH,'''//button[@onclick="saveAndSubmit('30')"]''')
        self.dayDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('31')"]''')
        #中班
        self.middleDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use4']")
        self.middleDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful4']")
        self.middleDutySave=(By.XPATH,'''//button[@onclick="saveAndSubmit('40')"]''')
        self.middleDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('41')"]''')

    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)

    def click_nightDutySave(self):
        self.click(self.nightDutySave)
    def click_nightDutySubmit(self):
        self.click(self.nightDutySubmit)
    def click_earlyDutySave(self):
        self.click(self.earlyDutySave)
    def click_earlyDutySubmit(self):
        self.click(self.earlyDutySubmit)
    def click_dayDutySave(self):
        self.click(self.dayDutySave)
    def click_dayDutySubmit(self):
        self.click(self.dayDutySubmit)
    def click_middleDutySave(self):
        self.click(self.middleDutySave)
    def click_middleDutySubmit(self):
        self.click(self.middleDutySubmit)
    def input_nightDutyCoalQuality(self, value):
        self.type(value, self.nightDutyCoalQuality)
    def input_nightDutyCoalheat(self, value):
        self.type(value, self.nightDutyCoalheat)
    def input_earlyDutyCoalQuality(self, value):
        self.type(value, self.earlyDutyCoalQuality)
    def input_earlyDutyCoalheat(self, value):
        self.type(value, self.earlyDutyCoalheat)
    def input_dayDutyCoalQuality(self, value):
        self.type(value, self.dayDutyCoalQuality)
    def input_dayDutyCoalheat(self, value):
        self.type(value, self.dayDutyCoalheat)
    def input_middleDutyCoalQuality(self, value):
        self.type(value, self.middleDutyCoalQuality)
    def input_middleDutyCoalheat(self, value):
        self.type(value, self.middleDutyCoalheat)




class Module_DataManage_DataFill_FirePower_Verify_coalAndCoalQulity(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Verify_coalAndCoalQulity,self).__init__(*args,**kwargs)

        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.xishui=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        #夜班
        self.nightDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use1']")
        self.nightDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful1']")
        self.nightDutyVerify=(By.XPATH,'''//button[@onclick="check('13')"]''')
        # self.nightDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('11')"]''')
        #早班
        self.earlyDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use2']")
        self.earlyDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful2']")
        self.earlyDutyVerify=(By.XPATH,'''//button[@onclick="check('23')"]''')
        # self.earlyDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('21')"]''')
        #白班
        self.dayDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use3']")
        self.dayDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful3']")
        self.dayDutyVerify=(By.XPATH,'''//button[@onclick="check('33')"]''')
        # self.dayDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('31')"]''')
        #中班
        self.middleDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use4']")
        self.middleDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful4']")
        self.middleDutyVerify=(By.XPATH,'''//button[@onclick="check('43')"]''')
        # self.middleDutySubmit = (By.XPATH, '''//button[@onclick="saveAndSubmit('41')"]''')

    def get_nightDutyCoalQuality(self):
        return self.getValue(self.nightDutyCoalQuality)
    def get_earlyDutyCoalQuality(self):
        return self.getValue(self.earlyDutyCoalQuality)
    def get_dayDutyCoalQuality(self):
        return self.getValue(self.dayDutyCoalQuality)
    def get_middleDutyCoalQuality(self):
        return self.getValue(self.middleDutyCoalQuality)


    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)

    def click_nightDutyVerify(self):
        self.click(self.nightDutyVerify)
    def click_earlyDutyVerify(self):
        self.click(self.earlyDutyVerify)
    def click_dayDutyVerify(self):
        self.click(self.dayDutyVerify)
    def click_middleDutyVerify(self):
        self.click(self.middleDutyVerify)

    def input_nightDutyCoalQuality(self, value):
        self.type(value, self.nightDutyCoalQuality)
    def input_nightDutyCoalheat(self, value):
        self.type(value, self.nightDutyCoalheat)
    def input_earlyDutyCoalQuality(self, value):
        self.type(value, self.earlyDutyCoalQuality)
    def input_earlyDutyCoalheat(self, value):
        self.type(value, self.earlyDutyCoalheat)
    def input_dayDutyCoalQuality(self, value):
        self.type(value, self.dayDutyCoalQuality)
    def input_dayDutyCoalheat(self, value):
        self.type(value, self.dayDutyCoalheat)
    def input_middleDutyCoalQuality(self, value):
        self.type(value, self.middleDutyCoalQuality)
    def input_middleDutyCoalheat(self, value):
        self.type(value, self.middleDutyCoalheat)




class Module_DataManage_DataFill_FirePower_Modify_coalAndCoalQulity(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Modify_coalAndCoalQulity,self).__init__(*args,**kwargs)

        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.xishui=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        #夜班
        self.nightDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use1']")
        self.nightDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful1']")
        self.nightDutyModify=(By.XPATH,'''//button[@onclick="modify('14')"]''')
        #早班
        self.earlyDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use2']")
        self.earlyDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful2']")
        self.earlyDutyModify=(By.XPATH,'''//button[@onclick="modify('24')"]''')
        #白班
        self.dayDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use3']")
        self.dayDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful3']")
        self.dayDutyModify=(By.XPATH,'''//button[@onclick="modify('34')"]''')
        #中班
        self.middleDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use4']")
        self.middleDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful4']")
        self.middleDutyModify=(By.XPATH,'''//button[@onclick="modify('44')"]''')

    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)

    def click_nightDutyModify(self):
        self.click(self.nightDutyModify)
    def click_earlyDutyModify(self):
        self.click(self.earlyDutyModify)
    def click_dayDutyModify(self):
        self.click(self.dayDutyModify)
    def click_middleDutyModify(self):
        self.click(self.middleDutyModify)

    def input_nightDutyCoalQuality(self, value):
        self.type(value, self.nightDutyCoalQuality)
    def input_nightDutyCoalheat(self, value):
        self.type(value, self.nightDutyCoalheat)
    def input_earlyDutyCoalQuality(self, value):
        self.type(value, self.earlyDutyCoalQuality)
    def input_earlyDutyCoalheat(self, value):
        self.type(value, self.earlyDutyCoalheat)
    def input_dayDutyCoalQuality(self, value):
        self.type(value, self.dayDutyCoalQuality)
    def input_dayDutyCoalheat(self, value):
        self.type(value, self.dayDutyCoalheat)
    def input_middleDutyCoalQuality(self, value):
        self.type(value, self.middleDutyCoalQuality)
    def input_middleDutyCoalheat(self, value):
        self.type(value, self.middleDutyCoalheat)


class Module_DataManage_DataFill_FirePower_Search_coalAndCoalQulity(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_FirePower_Search_coalAndCoalQulity,self).__init__(*args,**kwargs)

        self.firePowerTree=(By.XPATH,"//span[text()='火电']/../../span[1]")
        self.xishui=(By.XPATH,"//span[text()='火电']/../following-sibling::*//span[text()='习水电厂']/../span[text()='习水电厂']")
        #夜班
        self.nightDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use1']")
        self.nightDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful1']")
        self.nightDutyModify=(By.XPATH,'''//button[@onclick="modify('14')"]''')
        #早班
        self.earlyDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use2']")
        self.earlyDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful2']")
        self.earlyDutyModify=(By.XPATH,'''//button[@onclick="modify('24')"]''')
        #白班
        self.dayDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use3']")
        self.dayDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful3']")
        self.dayDutyModify=(By.XPATH,'''//button[@onclick="modify('34')"]''')
        #中班
        self.middleDutyCoalQuality=(By.XPATH,"//input[@id = 'coal_use4']")
        self.middleDutyCoalheat=(By.XPATH,"//input[@id = 'coal_useful4']")
        self.middleDutyModify=(By.XPATH,'''//button[@onclick="modify('44')"]''')

    def click_firePowerTree(self):
        self.click(self.firePowerTree)
    def click_xishui(self):
        self.click(self.xishui)

    def get_nightDutyCoalQuality(self):
        return self.getValue(self.nightDutyCoalQuality)
    def get_earlyDutyCoalQuality(self):
        return self.getValue(self.earlyDutyCoalQuality)
    def get_dayDutyCoalQuality(self):
        return self.getValue(self.dayDutyCoalQuality)
    def get_middleDutyCoalQuality(self):
        return self.getValue(self.middleDutyCoalQuality)

    def input_nightDutyCoalQuality(self, value):
        self.type(value, self.nightDutyCoalQuality)
    def input_nightDutyCoalheat(self, value):
        self.type(value, self.nightDutyCoalheat)
    def input_earlyDutyCoalQuality(self, value):
        self.type(value, self.earlyDutyCoalQuality)
    def input_earlyDutyCoalheat(self, value):
        self.type(value, self.earlyDutyCoalheat)
    def input_dayDutyCoalQuality(self, value):
        self.type(value, self.dayDutyCoalQuality)
    def input_dayDutyCoalheat(self, value):
        self.type(value, self.dayDutyCoalheat)
    def input_middleDutyCoalQuality(self, value):
        self.type(value, self.middleDutyCoalQuality)
    def input_middleDutyCoalheat(self, value):
        self.type(value, self.middleDutyCoalheat)