from selenium import webdriver
import time
import os

from AutoFramework.utils.configReader import LOG_PATH


class ScreenShoter(object):
    '''
    截图类，目前没有用，已经独立封装在BasePage中了

    '''
    def __init__(self,selenium_driver):
        self.driver=selenium_driver

    def shot(self,stepName):
        time.sleep(1)
        stepName=stepName
        suffix='.png'
        ctime=time.strftime("%Y%m%d%H%M%S",time.localtime())
        path=LOG_PATH+os.sep
        self.driver.save_screenshot(path+ctime+stepName+suffix)

if __name__=="__main__":
    d=webdriver.Safari()
    ScreenShoter(d).shot('empty')