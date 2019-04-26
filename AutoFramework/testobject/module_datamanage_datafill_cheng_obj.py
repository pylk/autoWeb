#coding=utf-8
import datetime
import time

from AutoFramework.core.pom import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

class Module_DataManage_DataFill_coal_yearplan_modify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_coal_yearplan_modify,self).__init__(*args,**kwargs)
        #年计划

        self.click_coal_Button=(By.XPATH,"//*[@id='coal']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.modify1Button = (By.XPATH, "//*[@id='updatelhMButton']")

        self.modify2Button = (By.XPATH, "//*[@id='updatemdbMButton']")

    def click_coal_modifyButton(self):
        self.click(self.click_coal_Button)

    def click_modifyButton1(self):
        self.click(self.modify1Button)

    def click_modifyButton2(self):
        self.click(self.modify2Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets=(By.XPATH,"//*[@id='M_lh_tbody']/*//input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"==one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1,100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='M_mdb_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))


    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

class Module_DataManage_DataFill_metalmn_yearplan_modify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_metalmn_yearplan_modify,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_metalmn_Button=(By.XPATH,"//*[@id='metalmn']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.modifyButton = (By.XPATH, "//*[@id='updateOverallButton']")

    def click_midifyButton(self):
        self.click(self.modifyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='mengTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))
    def click_metalmn_modifyButton(self):
        self.click(self.click_metalmn_Button)

    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

class Module_DataManage_DataFill_cement_yearplan_modify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_cement_yearplan_modify,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_overall_Button=(By.XPATH,"//*[@id='overall']/a")


        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.time=(By.XPATH,"//input[@id='queryTime']")

        self.modifyButton = (By.XPATH, "//*[@id='updateOverallButton']")

    def click_midifyButton(self):
        self.click(self.modifyButton)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def click_overall_modifyButton(self):
        self.click(self.click_overall_Button)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='overall_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

class Module_DataManage_DataFill_waterpower_yearplan_modify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_waterpower_yearplan_modify,self).__init__(*args,**kwargs)
        #年计划查询
        self.click_water_Button=(By.XPATH,"//*[@id='water']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.time=(By.XPATH,"//input[@id='queryTime']")

        self.modify1Button = (By.XPATH, "//*[@id='updateSfdlButton']")

        self.modify2Button = (By.XPATH, "//*[@id='updateSfdlPurposeButton']")

        self.modify3Button = (By.XPATH, "//*[@id='updateSdlSButton']")

        self.modify4Button = (By.XPATH, "//*[@id='updateUseHoursSButton']")

        self.modify5Button = (By.XPATH, "//*[@id='updateElecRateSButton']")

    def click_modifyButton1(self):
        self.click(self.modify1Button)

    def click_modifyButton2(self):
         self.click(self.modify2Button)

    def click_modifyButton3(self):
        self.click(self.modify3Button)

    def click_modifyButton4(self):
         self.click(self.modify4Button)

    def click_modifyButton5(self):
         self.click(self.modify5Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='S_fdl_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='S_fdlPurpose_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable3(self):
        targets = (By.XPATH, "//*[@id='S_sdl_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable4(self):
        targets = (By.XPATH, "//*[@id='S_useHours_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable5(self):
        targets = (By.XPATH, "//*[@id='S_elecRate_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def click_waterpower_modifyButton(self):
        self.click(self.click_water_Button)

class Module_DataManage_DataFill_hotel_yearplan_modify(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_hotel_yearplan_modify,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_hotel_Button=(By.XPATH,"//*[@id='hotel']/a")

        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.modify1Button = (By.XPATH, "//*[@id='wanlicoalcommitwl3']")

        self.modify2Button = (By.XPATH, "//*[@id='zycoalcommitwl3']")

    def click_modifyButton1(self):
        self.click(self.modify1Button)

    def click_modifyButton2(self):
         self.click(self.modify2Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='wlhotelTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='zyhotelTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def click_hotel_modifyButton(self):
        self.click(self.click_hotel_Button)

class Module_DataManage_DataFill_coal_yearplan_fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_coal_yearplan_fill,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_coal_Button=(By.XPATH,"//*[@id='coal']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.table=(By.XPATH,"//table[@id='tableNew']")

        self.time=(By.XPATH,"//input[@id='queryTime']")

        self.save1Button = (By.XPATH, "//*[@id='savelhMButton']")

        self.sumbit1Button = (By.XPATH, "//*[@id='sumbitlhMButton']")

        self.save2Button = (By.XPATH, "//*[@id='savemdbMButton']")

        self.sumbit2Button = (By.XPATH, "//*[@id='sumbitmdbMButton']")

    def click_saveButton1(self):
        self.click(self.save1Button)

    def click_sumbitButton1(self):
        self.click(self.sumbit1Button)

    def click_saveButton2(self):
        self.click(self.save2Button)

    def click_sumbitButton2(self):
        self.click(self.sumbit2Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def click_coal_fillButton(self):
        self.click(self.click_coal_Button)

    def input_inTable1(self):
        targets=(By.XPATH,"//*[@id='M_lh_tbody']/*//input")
        targetsOjb=self.find_elements(targets)
        for one in targetsOjb:
            if "readonly"==one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1,100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='M_mdb_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))


    def input_modifyData(self,value):
        # self.type(Keys.BACKSPACE,self.modifyValue)
        self.type(value,self.modifyValue)

class Module_DataManage_DataFill_metalmn_yearplan_fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_metalmn_yearplan_fill,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_metalmn_Button=(By.XPATH,"//*[@id='metalmn']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.modifyButton = (By.XPATH, "//*[@id='updateOverallButton']")


    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='mengTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))
    def click_metalmn_fillButton(self):
        self.click(self.click_metalmn_Button)

class Module_DataManage_DataFill_cement_yearplan_fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_cement_yearplan_fill,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_overall_Button=(By.XPATH,"//*[@id='overall']/a")


        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.time=(By.XPATH,"//input[@id='queryTime']")

        self.modifyButton = (By.XPATH, "//*[@id='updateOverallButton']")

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def click_overall_fillButton(self):
        self.click(self.click_overall_Button)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='overall_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

class Module_DataManage_DataFill_waterpower_yearplan_fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_waterpower_yearplan_fill,self).__init__(*args,**kwargs)
        #年计划查询
        self.click_water_Button=(By.XPATH,"//*[@id='water']/a")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.time=(By.XPATH,"//input[@id='queryTime']")

        self.save1Button = (By.XPATH, "//*[@id='saveSfdlButton']")

        self.save2Button = (By.XPATH, "//*[@id='saveSfdlPurposeButton']")

        self.save3Button = (By.XPATH, "//*[@id='saveSdlSButton']")

        self.save4Button = (By.XPATH, "//*[@id='saveUseHoursSButton']")

        self.save5Button = (By.XPATH, "//*[@id='saveElecRateSButton']")

        self.sumbit1Button = (By.XPATH, "//*[@id='sumbitSfdlButton']")

        self.sumbit2Button = (By.XPATH, "//*[@id='sumbitSfdlPurposeButton']")

        self.sumbit3Button = (By.XPATH, "//*[@id='sumbitSdlSButton']")

        self.sumbit4Button = (By.XPATH, "//*[@id='sumbitUseHoursSButton']")

        self.sumbit5Button = (By.XPATH, "//*[@id='sumbitElecRateSButton']")

    def click_saveButton1(self):
        self.click(self.save1Button)

    def click_saveButton2(self):
         self.click(self.save2Button)

    def click_saveButton3(self):
        self.click(self.save3Button)

    def click_saveButton4(self):
         self.click(self.save4Button)

    def click_saveButton5(self):
         self.click(self.save5Button)

    def click_sumbitButton1(self):
        self.click(self.sumbit1Button)

    def click_sumbitButton2(self):
         self.click(self.sumbit2Button)

    def click_sumbitButton3(self):
        self.click(self.sumbit3Button)

    def click_sumbitButton4(self):
         self.click(self.sumbit4Button)

    def click_sumbitButton5(self):
         self.click(self.sumbit5Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='S_fdl_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='S_fdlPurpose_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable3(self):
        targets = (By.XPATH, "//*[@id='S_sdl_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable4(self):
        targets = (By.XPATH, "//*[@id='S_useHours_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable5(self):
        targets = (By.XPATH, "//*[@id='S_elecRate_tbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def click_waterpower_fillButton(self):
        self.click(self.click_water_Button)

class Module_DataManage_DataFill_hotel_yearplan_fill(BasePage):
    def __init__(self,*args,**kwargs):
        super(Module_DataManage_DataFill_hotel_yearplan_fill,self).__init__(*args,**kwargs)
        #年计划查询

        self.click_hotel_Button=(By.XPATH,"//*[@id='hotel']/a")

        self.submitButton=(By.XPATH,"//button[text()='提交']")

        self.modifyValue=(By.XPATH,"//input[@id='powerGenertion']")

        self.modify1Button = (By.XPATH, "//*[@id='wanlicoalcommitwl3']")

        self.modify2Button = (By.XPATH, "//*[@id='zycoalcommitwl3']")

    def click_modifyButton1(self):
        self.click(self.modify1Button)

    def click_modifyButton2(self):
         self.click(self.modify2Button)

    def input_time(self,day=1):
        self.js_inputRemoveReadOnly(self.time[1],'readOnly')
        now=datetime.datetime.now()
        preDay=now-datetime.timedelta(days=day)
        # strDay=datetime.datetime.strftime(preDay)
        self.type(preDay.strftime('%YYYY'),self.time)

    def input_inTable1(self):
        targets = (By.XPATH, "//*[@id='wlhotelTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def input_inTable2(self):
        targets = (By.XPATH, "//*[@id='zyhotelTbody']/*//input")
        targetsOjb = self.find_elements(targets)
        for one in targetsOjb:
            if "readonly" == one.get_attribute("readonly"):
                print("abc")
                continue
            else:
                one.send_keys(random.randint(1, 100))

    def click_hotel_fillButton(self):
        self.click(self.click_hotel_Button)