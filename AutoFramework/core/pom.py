# coding=utf-8
import inspect
import os
from HTMLReport import *
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from AutoFramework.utils.common import getModuleName, getMethodName, getLastMethodName
from AutoFramework.utils.configReader import LOG_PATH
from AutoFramework.utils.logger import Logger
import selenium,unittest
import time
from datetime import datetime,timedelta
from functools import wraps


logger=Logger(__name__).getlog()


def addShoter(driver):
    def decorateShoter(func):
        @wraps(func)
        def wrapperShoter(driver):
            try:
                res = func(driver)
                driver.shot(driver, func.__name__)
                return res
            except:
                driver.shot(driver, func.__name__)
                time.sleep(2)
                raise
        return wrapperShoter
    return decorateShoter


# class Shoter():
#     def __init__(self,driver):
#         self.driver = driver
#     def __call__(self,func):
#         @wraps(func)
#         def wrapperShoter(*args,**kwargs):
#             try:
#                 return func(*args,**kwargs)
#             except:
#                 setpName=func.__name__
#                 suffix = '.png'
#                 ctime = time.strftime("%Y%m%d%H%M%S", time.localtime())
#                 path = LOG_PATH + os.sep
#                 self.driver.save_screenshot(path + ctime + setpName + getLastMethodName(3) + suffix)
#                 raise
#         return wrapperShoter


def addLogger(func):
    @wraps(func)
    def wrapperLog(*args, **kwargs):
        res=func(*args, **kwargs)
        logger.info('正在操作函数:' + func.__name__)
        return res
    return wrapperLog

def addTimer(func):
    @wraps(func)
    def wrapperTimer(*args, **kwargs):
        startTime = datetime.now()

        res = func(*args, **kwargs)

        endTime = datetime.now()
        consumeTime = endTime - startTime
        logger.info(func.__name__ + '消耗' + str(consumeTime.seconds) + '秒')
        return res
    return wrapperTimer



class BasePage(unittest.TestCase):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self,seleniumdriver):
        super(BasePage,self).__init__()
        self.driver = seleniumdriver


    #添加截图
    def shot(self,stepName):
        stepName=stepName
        suffix='.png'
        ctime=time.strftime("%Y%m%d%H%M%S",time.localtime())
        path=LOG_PATH+os.sep
        self.driver.save_screenshot(path+ctime+stepName+getLastMethodName(3)+suffix)
        self.getLogger.info(stepName)


    def getURL(self):
        return self.driver.current_url

    @property
    def getLogger(self):
        logger2 = logger
        return logger2

    def getDriver(self):
        return self.driver

    def getCurrWindowHandle(self):
        return self.driver.current_window_handle

    def getAllWindowHandles(self):
        return self.driver.window_handles

    def switchWindow(self,windowName):
        try:
            self.driver.switch_to.window(windowName)
            self.shot('成功_切换window')
        except:
            self.shot('失败_切换window失败')
            # self.getLogger.error('切换window失败')

    def switchBackFromIframe(self):
        try:
            self.driver.switch_to.default_content()
            self.shot('成功_切换回iframe')
        except:
            self.shot('失败_切换回iframe失败')
            # self.getLogger.error('切换回iframe失败')

    def closeWindow(self):
        try:
            self.driver.close()
            self.shot('成功_关闭window')
        except:
            self.shot('失败_关闭window')
            # self.getLogger.error('关闭window出错')

    def switchFrame(self,frameRef):
        try:
            self.driver.switch_to.frame(frameRef)
            self.shot('成功_切换iframe')
        except:
            self.shot('失败_切换iframe')
            # self.getLogger.error('切换iframe失败')

    
    def switchAlertAccept(self):
        time.sleep(2)
        try:
            self.getDriver().switch_to.alert.accept()
            self.shot('成功_点击接受警告弹出框')
        except NoAlertPresentException as e:
            self.shot('失败_点击接受警告弹出框')
            self.getLogger.warning("警告：没有警告框弹出 %s", e)
        except UnexpectedAlertPresentException as e:
            self.shot('失败_点击接受警告弹出框')
            self.getLogger.warning("警告：未期待的警告框 %s", e)
        except Exception as e :
            self.getLogger.warning("警告：未期待的警告框 %s", e)

    def switchAlertSendEnter(self):
        time.sleep(2)
        try:
            self.getDriver().switch_to.alert.send_keys(Keys.ENTER)
            self.shot('成功_点击回车')
        except NoAlertPresentException as e:
            self.shot('失败_点击回车')
            self.getLogger.warning("警告：没有警告框弹出 %s", e)
        except UnexpectedAlertPresentException as e:
            self.shot('失败_点击回车')
            self.getLogger.warning("警告：未期待的警告框 %s", e)
        except Exception as e :
            self.getLogger.warning("警告：未期待的警告框 %s", e)

    
    
    def switchAlertDecline(self):
        time.sleep(2)
        try:
            self.driver.switch_to.alert.dismiss()
            self.shot('成功_点击拒绝警告弹出框')
        except NoAlertPresentException as e:
            self.shot('失败_点击拒绝警告弹出框')
            self.getLogger.warning("警告：没有警告框弹出 %s", e)
        except UnexpectedAlertPresentException as e:
            self.shot('失败_点击拒绝警告弹出框')
            self.getLogger.warning("警告：未期待的警告框 %s", e)
        except Exception as e :
            self.getLogger.warning("警告：未期待的警告框 %s", e)

    #推出浏览器
    
    
    def quit_browser(self):
        try:
            self.driver.quit()
            self.shot('成功_浏览器退出')
        except:
            self.shot('失败_浏览器退出')
            # self.getLogger.info("操作：浏览器推出")

    # 浏览器前进操作
    
    
    def forward(self):
        try:
            self.driver.forward()
            self.shot('成功_点击浏览器前进')
        except:
            self.shot('失败_点击浏览器前进')
            # self.getLogger.info("操作：点击浏览器前进")

    # 浏览器后退操作
    
    
    def back(self):
        try:
            self.driver.back()
            self.shot('成功_点击浏览器后退')
        except:
            self.shot('失败_点击浏览器后退')
        # self.getLogger.info("操作：点击浏览器后退")

    # 隐式等待
    
    
    def wait(self, seconds):
        try:
            self.driver.implicitly_wait(seconds)
            self.getLogger.info("操作：等待 %d 秒." % seconds)
        except:
            self.shot("失败_等待"+seconds+"秒")

    # 点击关闭当前窗口
    
    
    def close(self):
        try:
            self.driver.close()
            self.shot("成功_关闭并推出浏览器")
            # self.getLogger.info("操作：关闭并推出浏览器")
        except Exception as e:
            self.shot('失败_关闭并推出浏览器')
            # self.getLogger.error("失败_不能退出浏览器 %s",e)
            self.fail("失败_不能退出浏览器")

    #下拉选框按值
    
    
    def selectByText(self,selector,optionValue):
        try:
            element=self.find_element(selector)
            s1 = Select(element)
            s1.select_by_visible_text(optionValue)
            self.shot('成功_文本操作下拉选框')
        except Exception as e:
            self.shot('失败_文本操作下拉选框')
            # self.getLogger.error("失败_下拉选框失败 %s", e)
            self.fail("失败_文本操作下拉选框")

    # 下拉选框,按序号
    def selectByIndex(self,selector,index):
        try:
            element = self.find_element(selector)
            s1 = Select(element)
            s1.select_by_index(index)
            self.shot('成功_索引操作下拉选框')
        except Exception as e:
            self.shot('失败_索引操作下拉选框')
            # self.getLogger.error("失败_下拉选框失败 %s", e)
            self.fail("失败_下拉选框失败")

    # 下拉选框，按标签内value
    def selectByInnerValue(self, selector, value):
        try:
            element = self.find_element(selector)
            s1 = Select(element)
            s1.select_by_value(value)
            self.shot('成功_内值操作下拉选框')
        except Exception as e:
            # self.getLogger.error("失败_下拉选框失败 %s", e)
            self.shot('失败内置操作下拉选框')
            self.fail("失败_下拉选框失败")



    #定位元素方法

    def find_elements(self,selector):
        by, value = selector
        element = None
        if self.waitUntil(selector, 8):
            try:
                if by == "id" or by == "By.ID":
                    element = self.driver.find_elements_by_id(value)
                elif by == "name" or by == "By.NAME":
                    element = self.driver.find_elements_by_name(value)
                elif by == "class_name" or by == "By.CLASS_NAME":
                    element = self.driver.find_elements_by_class_name(value)
                elif by == "link_text" or by == "By.LINK_TEXT":
                    element = self.driver.find_elements_by_link_text(value)
                elif by == "partial_link_text" or by == "By.PARTIAL_LINK_TEXT":
                    element = self.driver.find_elements_by_partial_link_text(value)
                elif by == "tag_name" or by == "By.TAG_NAME":
                    element = self.driver.find_elements_by_tag_name(value)
                elif by == "xpath" or by == "By.XPATH":
                    element = self.driver.find_elements_by_xpath(value)
                elif by == "css" or by == "By.CSS_SELECTOR":
                    element = self.driver.find_elements_by_css_selector(value)
                else:
                    raise Exception("你选择的元素查找方式有误")
                self.shot("成功：元素查找 "+str(selector)+"")
                # self.getLogger.info("成功：元素查找 %s", selector)
                return element
            except NoSuchElementException as e:
                self.getLogger.error("失败_NoSuchElementException: %s" % e)
                self.shot("失败_查找元素失败")
                self.fail("查找元素失败")
        else:
            self.getLogger.error("失败_元素等待后未出现: %s" % selector)
            self.fail("查找元素失败")

    # 定位元素方法
    
    
    def find_element(self,selector):
        by,value=selector
        element=None
        if self.waitUntil(selector,8):
            try:
                if by=="id" or by=="By.ID":
                    element=self.driver.find_element_by_id(value)
                elif by=="name"or by=="By.NAME":
                    element=self.driver.find_element_by_name(value)
                elif by=="class_name"or by=="By.CLASS_NAME":
                    element=self.driver.find_element_by_class_name(value)
                elif by=="link_text" or by=="By.LINK_TEXT":
                    element = self.driver.find_element_by_link_text(value)
                elif by=="partial_link_text" or by=="By.PARTIAL_LINK_TEXT":
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by=="tag_name" or by=="By.TAG_NAME":
                    element = self.driver.find_element_by_tag_name(value)
                elif by=="xpath" or by=="By.XPATH":
                    element = self.driver.find_element_by_xpath(value)
                elif by=="css" or by=="By.CSS_SELECTOR":
                    element=self.driver.find_element_by_css_selector(value)
                else:
                    raise Exception("你选择的元素查找方式有误")
                self.shot("成功：元素查找 " + str(selector) + "")
                # self.getLogger.info("成功：元素查找 %s",selector)
                return element
            except NoSuchElementException as e:
                self.getLogger.error("失败_NoSuchElementException: %s" % e)
                self.shot("失败_查找元素失败")
                self.fail("查找元素失败")
        else:
            self.getLogger.error("失败_元素等待后未出现: %s" % selector)
            self.fail("查找元素失败")


    #文件上传 input标签上传
    def upload_file(self,selector,filepath):
        try:
            button=self.find_element(selector)
            if os.path.exists(filepath):
                button.send_keys(filepath)
                self.shot("成功_文件上传 ")
            else:
                self.getLogger.error("文件不存在")
                self.shot("失败_文件上传")
                self.fail("要导入的文件不存在，路径是："+filepath)
        except:
            self.shot("失败_文件上传")

    # 输入
    
    
    def type(self, text, selector ):
        el = self.find_element(selector)
        el.clear()
        try:
            text=str(text)
            el.send_keys(text)
            self.getLogger.info("操作：在输入框输入了 \' %s \' ",text)
            self.shot("成功_输入框输入")
        except Exception as e:
            self.getLogger.error("失败_不能输入 %s 到输入框" % e)
            self.shot('失败_输入框输入失败')
            self.fail("输入框不能输入")

    # 输入
    
    
    def typeWithOutClear(self, text, selector):
        el = self.find_element(selector)
        # el.clear()
        try:
            text = str(text)
            el.send_keys(text)
            self.getLogger.info("操作：在输入框输入了 \'%s\' ", text)
            self.shot("成功_输入框输入")
        except Exception as e:
            self.getLogger.error("失败_不能输入 %s 到输入框" % e)
            self.shot('失败_输入框输入失败')
            self.fail("输入框不能输入")



    # 清除文本框
    
    
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            self.getLogger.info("操作：输入前清空输入框")
        except Exception as e:
            self.getLogger.error("失败_不能清空输入框： %s", e)
            self.shot("失败_清空输入框失败")
        self.fail("输入框不能清空")

    # def click(self,selector):
    #     element = self.find_element(selector)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     element.click()

    
    
    def just_click(self,selector):
        try:
            el=self.find_element(selector)
            el.click()
            self.shot("成功_点击操作")
        except:
            self.shot("失败_点击操作")

    
    
    def rightClick(self,selector):
        try:
            el=self.find_element(selector)
            self.move_to_element(selector)
            ActionChains(self.driver).context_click(el).perform()
            self.shot("成功_右键操作")
        except:
            self.shot("失败_右键操作")
            self.fail("失败_右键操作")
    
    def doubleClick(self,selector):
        try:
            el=self.find_element(selector)
            self.move_to_element(selector)
            ActionChains(self.driver).double_click(el).perform()
            self.shot("成功_双击操作")
        except:
            self.shot("失败_双击操作")
            self.fail("失败_双击操作")

    # 点击元素
    
    
    def click(self, selector):
        if self.waitUntilClickable(selector):
            el = self.find_element(selector)
            self.move_to_element(selector)
            try:
                el.click()
                self.shot("成功_点击")
            except UnexpectedAlertPresentException as e:
                self.switchAlertAccept()
            except Exception as e:
                self.getLogger.error("失败_点击失败 %s",selector)
                self.shot("失败_点击失败")
                self.fail("失败_点击失败")

        else:
            self.getLogger.error("失败_不能够点击元素 %s", selector)
            self.shot("失败_不能够点击元素")
            self.fail("失败_点击失败")

   # 获得网页标题
    
    
    def get_page_title(self):
        self.getLogger.info("当前页面的标题为： %s",self.driver.title)
        return self.driver.title

    #获取元素页面显示值
    
    
    def get_element_text(self, elem):
        el=self.find_element(elem)
        text=el.text
        self.getLogger.info("当前页面元素文本为： %s " , text)
        return text

    #直接等待秒
    @staticmethod
    def sleep(seconds=1):
        time.sleep(seconds)

    #显式等待
    
    
    def justWait(self,time=2):
        self.getLogger.info("显式等待 %d 秒" % (time))
        self.driver.implicitly_wait(time)

    #等对象出现
    
    
    def waitUntil(self,selector,time=3):
        self.getLogger.info("操作：等待 %d 秒 直到 %s 出现" % (time,selector))
        try:
            element=WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(selector))
            if element:
                return True
        except Exception as e:
            self.getLogger.error("失败_%s元素未出现",selector)
            self.fail("对象等待失败")
        # finally:
        #     self.shot("失败_元素等待未出现")


    #等待元素消失
    #

    def waitUntilDisappear(self,selector,time=5):
        self.getLogger.info("操作：等待 %d 秒 直到 %s 消失" % (time, selector))
        try:
            res = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(selector))
            if not res==False:
                return res
            else:
                self.fail("等待 %d 秒 直到 %s 没有消失消失" % (time, selector))
        except Exception as e:
            self.getLogger.error("失败_%s元素等待点击失败",selector)
            self.shot("失败_元素等待未出现")
            self.fail("对象等待点击失败")

    #移动到元素
    
    
    def move_to_element(self, selector):
        time.sleep(1)
        # if self.waitUntilInvisible(selector):
        el=self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
                    # ActionChains(self.base_driver).drag_and_drop(el_source, el_target).perform()
                    # else:
                    # ActionChains(self.base_driver).click_and_hold(el_source).perform()
                    # ActionChains(self.base_driver).move_to_element(el_target).perform()
                    # ActionChains(self.base_driver).release(el_target).perform()
            self.getLogger.info("操作：鼠标移动到 %s", selector)
        except Exception as e:
            self.getLogger.error("鼠标移动失败 %s", selector)
            self.shot("失败_鼠标移动失败")
        # else:
        #     self.getLogger.error("失败_鼠标移动失败 %s", selector)
        #     self.shot("失败_鼠标移动失败")

    #等待元素可以点击
    
    
    def waitUntilClickable(self,selector,time=5):
        self.getLogger.info("操作：等待 %d 秒 直到 %s 可以点击" % (time,selector))
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(selector))
            if not element==False:
                return True
            else:
                return False
        except Exception as e:
            self.getLogger.error("失败_%s元素等待点击失败",selector)
            self.shot("失败_元素等待未出现")
            self.fail("对象等待点击失败")

    # 等待元素消失
    
    
    def waitUntilInvisible(self, selector, time=5):
        self.getLogger.info("操作：等待 %d 秒 直到 %s 可以点击" % (time, selector))
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(selector))
            if not element == False:
                return True
        except Exception as e:
            self.getLogger.error("失败_%s元素等待点击失败", selector)
            self.shot("失败_元素等待未出现")
            self.fail("对象等待点击失败")

    #检查页面文本元素 相等
    
    
    def checkPoint_equal(self,selector,expectText):
        realText = ""
        try:
            if self.find_element(selector):
                realText=self.get_element_text(selector)

                if realText==expectText:
                # assert_equal(realText,expectText,"页面检查"+realText+"和"+expectText+"是否相等")
                    self.getLogger.info("成功_页面检查元素 %s",selector)
                    self.shot("成功_页面检查")
                else:
                    self.getLogger.info("失败_页面检查元素 %s",selector)
                    self.shot("失败_页面检查")
                    self.fail("失败_页面包含检查失败")
        except Exception as e:
            self.getLogger.error("失败_页面检查失败_%s",selector)
            self.shot("失败_页面检查失败")
            self.fail("页面检查，文本不相等: "+realText)

    #检查页面文本元素 包含
    
    
    def checkPoint_contain(self,selector,expectText):
        realText=""
        try:
            if self.find_element(selector):
                realText=self.get_element_text(selector)
                if realText=="":
                    realText=self.getText(selector)

                if expectText in realText:
                # assert_equal(realText,expectText,"页面检查"+realText+"和"+expectText+"是否相等")
                    self.getLogger.info("成功_页面检查元素 %s",selector)
                    self.shot("成功_页面检查")
                else:
                    self.getLogger.info("失败_页面检查元素 %s",selector)
                    self.shot("失败_页面检查")
                    self.fail("失败_页面包含检查失败")
        except Exception as e:
            self.shot("失败_页面检查失败")
            self.getLogger.error("失败_页面检查失败_%s",selector)
            self.fail("失败_页面包含检查失败_"+realText)

    #获取弹出框
    
    
    def getAlertDialog(self):
        alert = self.driver.switch_to_alert
        return alert

    #获取元素页面文本
    
    
    def getText(self,selecoter):
        txt=self.find_element(selecoter).text
        self.getLogger.info("对话框内容为%s",txt)
        return txt

    #获取元素页面值
    
    
    def getValue(self,selecoter):
        item=self.find_element(selecoter)
        txt=item.get_attribute('value')
        self.getLogger.info("对话框内容为%s",txt)
        return txt

    # 获取元素属性值
    def getAttribute(self,selector,attributeName):
        item = self.find_element(selector)
        txt = item.get_attribute(attributeName)
        self.getLogger.info("对象%s 属性的值为：%s" %(selector[1],txt))
        return txt

    #点击对话框确认按钮
    
    
    def confirmDialog(self,selecoter):
        self.find_element(selecoter).accept()

#   判断是否启用
    
    
    def isEnabled(self,selector):
        element=self.find_element(selector)
        self.getLogger.info(str(selector)+str(element.is_enabled()))
        if element.is_enabled()==True:
            return True
        else:
            return False

    #判断是否显示
    
    
    def isDisplayed(self,selector):
        element=self.find_element(selector)
        self.getLogger.info(element.is_displayed())
        if element.is_displayed()==True:
            return True
        else:
            return False

    #判断是否可以点击
    
    
    def isClickable(self,selector):
        try:
            element=self.find_element(selector)
            self.wait(2)
            if element.is_displayed()==True:#需要检查元素是否有此对象
                if element.is_enabled()==True:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            self.shot("失败_元素当前不能点击"+str(e))
            self.getLogger.warn("警告：不能判断元素是否可以点击 %s",selector)
            self.fail("失败_元素不能点击")

    def get_element_inner_text(self, elem):
        pass

    #判断是否可见
    
    
    def is_element_visible(self, element):
        driver = self.driver
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except:
            flag = False
        return flag

    #获取表格行数
    
    
    def table_getRowNum(self,table_selector):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            self.getLogger.info("表格有%s行", len(tableRow))

        except Exception as e:
            self.shot("失败_获取表格行数")
            self.getLogger.error("失败_获取表格行数")
            self.getLogger.error(e)
            self.fail("失败_获取表格行数")
        return len(tableRow)-1

    #行数表格选取
    
    
    def table_SelectByCordinates(self,table_selector,rowindex):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            for i in range(0, len(tableRow)):
                    # for j in range(0, len(tableCol)+1):
                if i==rowindex-1:
                    tableRow[i].find_element_by_xpath("//td/button[1]").click()
                    self.shot("操作_表格按照行列号选择")
                    break

        except Exception as e:
            self.shot("失败_表格选择")
            self.getLogger.error("失败_表格选取失败")
            self.getLogger.error(e)
            self.fail("失败_表格按行列号选取失败")

    #表格行号选取
    #
    def table_SelectByIndex(self,table_selector,rowindex):
        try:
            # print("#############################")
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            for i in range(1, len(tableRow)):
                # print(i)
                if i==rowindex:
                    # self.getLogger.error("#########已进入表格")
                    tableRow[i].find_element_by_tag_name("input").click()
                    self.shot("操作_表格选择")
                    break
        except Exception as e:
            self.shot("失败_表格选择")
            self.getLogger.error("失败_输入的表格行号或者列号非法"+str(e))
            self.fail("失败_表格按行选取失败")

    #表格由值点击
    #
    def table_clickInTableByRow(self,table_selector,selector,rowIndex):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            for i in range(1, len(tableRow)+1):
                # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[j].text)
                if i==rowIndex:
                    way,value=selector
                    # print(tableRow[i].find_element_by_xpath(value).text)
                    tableRow[i].find_element_by_xpath(value).click()
                    self.shot("操作_表格点击操作")
                    break
        except UnexpectedAlertPresentException as e:
            self.switchAlertAccept()
        except Exception as e:
            self.shot("失败_表格内操作")
            self.getLogger.error("失败:表格内操作")
            self.fail("失败_表格内操作")

    # 表格由值输入
    #
    def table_InputInTableByRow(self, table_selector, selector, rowIndex,txt):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            for i in range(1, len(tableRow) + 1):
                # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[i].text)
                if i == rowIndex:
                    way, value = selector
                    # print(tableRow[i].find_element_by_xpath(value).text)
                    tableRow[i].find_element_by_xpath(value).clear()
                    tableRow[i].find_element_by_xpath(value).send_keys(txt)
                    self.shot("操作_表格点击操作")
                    break

        except Exception as e:
            self.shot("失败_表格内操作")
            self.getLogger.error("失败:表格内操作")
            self.fail("失败_表格内操作")

    # #表格由列名选择
    # def table_inputInTableByColumnName(self,table_selector,columnName,rowIndex):
    #     try:
    #         table = self.find_element(table_selector)
    #         tableRow = table.find_elements_by_tag_name("tr")
    #         tableCol = tableRow[0].find_elements_by_tag_name("th")
    #         self.getLogger.info("表格有%s行", len(tableRow))
    #         self.getLogger.info("表格有%s列", len(tableCol))
    #
    #         columnNum=None
    #
    #         for i in range(0, tableCol):
    #             print(self.getText(tableCol[i]))
    #             # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[j].text)
    #             if tableCol[i].getText()==columnName:
    #                 print(tableCol[i].getText(tableCol[i]))
    #                 columnNum=i
    #                 break
    #
    #         for i in range(1, len(tableRow) + 1):
    #             if i==rowIndex:
    #                 way,value=columnName
    #                 # print(tableRow[i].find_element_by_xpath(value).text)
    #                 tableRow[i].find_element_by_xpath(value).click()
    #                 self.shot("操作：表格点击操作")
    #                 break
    #     except Exception as e:
    #         self.shot("失败_表格内操作")
    #         self.getLogger.error("失败:表格内操作")
    #         self.fail("失败_表格内操作")



    #由值表格选取
    #
    def table_SelectByValue(self,table_selector,value):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            for i in range(1, len(tableRow)):
                for j in range(0, len(tableCol)):
                    # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[j].text)
                    if (tableRow[i].find_elements_by_tag_name("td"))[j].text==value:
                        tableRow[i].find_element_by_tag_name("input").click()
                        self.shot("操作_表格选择")
                        break
        except Exception as e:
            self.shot("失败_表格选择")
            self.getLogger.error("失败_输入的值没有在表格中 %s",value)
            self.fail("失败_表格按值选取失败")

    #获取表格所有数据
    #
    def table_getAllData(self,table_selector):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            row=len(tableRow)
            col=len(tableCol)
            self.getLogger.info("表格有%s行", row)
            self.getLogger.info("表格有%s列", col)
            list=[]

            for i in range(1, row):
                rowContent = []
                for j in range(0, col):
                    temp=""
                    # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[j].text)
                    temp = (tableRow[i].find_elements_by_tag_name("td"))[j].text
                    # self.getLogger.info("内容："+temp)
                    rowContent.append(temp)
                self.getLogger.info(",".join(rowContent))
                list.append(rowContent)
            return list
        except Exception as e:
            self.shot("失败_表格内容获取失败")
            self.getLogger.error("失败_表格内容获取")
            self.fail("失败_表格内容获取失败")

            # 获取表格所有数据

    def table_getAllData2(self, table_selector):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("th")
            row = len(tableRow)
            col = len(tableCol)
            self.getLogger.info("表格有%s行", row)
            self.getLogger.info("表格有%s列", col)
            list = []

            for i in range(1, row-1):
                rowContent = []
                for j in range(0, col):
                    temp = ""
                    # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[j].text)
                    temp = (tableRow[i].find_elements_by_tag_name("td"))[j].text
                    # self.getLogger.info("内容："+temp)
                    rowContent.append(temp)
                self.getLogger.info(",".join(rowContent))
                list.append(rowContent)
            return list
        except Exception as e:
            self.shot("失败_表格内容获取失败")
            self.getLogger.error("失败_表格内容获取")
            self.fail("失败_表格内容获取失败")

    
    
    def js_exec(self,xpath):
        js='evaluator = new XPathEvaluator(); result = evaluator.evaluate("'+xpath+'", document.documentElement, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);document.getElementById(result.singleNodeValue.id).click()'
        # print(js)
        time.sleep(2)
        self.driver.execute_script(js)

    def js_execute(self,jscode):
        self.driver.execute_script(jscode)


    def js_inputRemoveReadOnly(self,xpath,attrName):
        js = 'evaluator = new XPathEvaluator(); result = evaluator.evaluate("' + xpath + '", document.documentElement, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);document.getElementById(result.singleNodeValue.id).removeAttribute("'+attrName+'")'
        time.sleep(2)
        self.driver.execute_script(js)

    def jquery_removeProperty(self, label, nameOrId, value, attrName):
        #"$('input[name=search').removeAttr('onfocus')"
        for x in attrName:
            js = "$('%s[%s=%s]').removeAttr('%s')" % (label, nameOrId, value, x)
            # print(js)
            self.driver.execute_script(js)



# 表格由值输入
    #
    def table_InputAllInTable(self, table_selector, selector, datas):
        try:
            table = self.find_element(table_selector)
            tableRow = table.find_elements_by_tag_name("tr")
            tableCol = tableRow[0].find_elements_by_tag_name("td")
            self.getLogger.info("表格有%s行", len(tableRow))
            self.getLogger.info("表格有%s列", len(tableCol))

            way, value = selector

            for i in range(1, len(tableRow) + 1):
                # print("查找到的值有：",(tableRow[i].find_elements_by_tag_name("td"))[i].text)
                if "input-disabled" != tableRow[i].find_element_by_xpath(value).get_attribute("class"):
                    # print(tableRow[i].find_element_by_xpath(value).text)
                    tableRow[i].find_element_by_xpath(value).clear()
                    tableRow[i].find_element_by_xpath(value).send_keys()

        except Exception as e:
            self.shot("失败_表格内操作")
            self.getLogger.error("失败_表格内操作")
            self.fail("失败_表格内操作")

if __name__=="__main__":
    b=BasePage(webdriver)


