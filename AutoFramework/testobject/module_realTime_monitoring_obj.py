# -*- coding:utf-8 -*-
from AutoFramework.core.pom import BasePage

from selenium.webdriver.common.by import By


class Moudle_realTime_monitoring(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_realTime_monitoring, self).__init__(*args, **kwargs)
        self.firePower = (By.XPATH, "//a[@title='火电']")
        self.waterPower = (By.XPATH, "//a[@title='水电']")
        self.sunPower = (By.XPATH, "//a[@title='光伏']")
        self.coalPower = (By.XPATH, "//a[@title='煤矿']")
        self.overall = (By.XPATH, "//a[@title='综合产业']")
        self.Product = (By.XPATH,"//div[@class='st_right']/child::h1")#[火电、水电、水电、光伏、水泥]生产情况

    def click_firePower(self):
        self.click(self.firePower)

    def click_waterPower(self):
        self.click(self.waterPower)

    def click_sunPower(self):
        self.click(self.sunPower)

    def click_coalPower(self):
        self.click(self.coalPower)

    def click_overall(self):
        self.click(self.overall)







