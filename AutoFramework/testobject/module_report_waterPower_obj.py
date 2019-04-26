# -*- coding:utf-8 -*-
import os
from datetime import datetime, timedelta
from AutoFramework.core.pom import BasePage

from selenium.webdriver.common.by import By


class Moudle_report_waterPower_Unit(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_report_waterPower_Unit, self).__init__(*args, **kwargs)
        # 水电板块日报表
        self.waterDaily = (By.XPATH, "//a[@onclick='fun_a()']")
        # 水情报表
        self.waterSituation = (By.XPATH, "//a[@onclick='fun_b()']")
        # 水电电站报表
        self.waterpowerStation = (By.XPATH, "//a[@onclick='fun_c()']")
        # 报表导出按钮
        self.downLoad = (By.XPATH, "//p[contains(.,'输出')]")
        self.yesterday = datetime.strftime(datetime.today() - timedelta(days=1), "%Y%m%d")
        self.fileName = '水电机组情况表' + self.yesterday + '.xls'
        self.fileNames = ['水电机组情况表' + self.yesterday + ' (' + str(x) + ')' + '.xls' for x in range(1, 100)]
        self.fileNames.append(self.fileName)

    def click_waterDaily(self):
        self.click(self.waterDaily)

    def click_waterpowerStation(self):
        self.click(self.waterpowerStation)

    def click_waterSituation(self):
        self.click(self.waterSituation)

    def click_downLoad(self):
        """下载报表"""
        self.click(self.downLoad)
        self.getLogger.info("{}:下载成功".format(self.fileName))

    def remove_downloadFile(self):
        """删除报表"""
        self.pwd = os.getcwd()
        self.fPath = os.path.abspath(os.path.dirname(self.pwd))
        self.dPath = os.path.join(self.fPath, r'testData')
        self.filePath = [os.path.join(self.dPath, p) for p in self.fileNames]
        for i in self.filePath:
            if os.path.exists(i):
                os.remove(i)
                self.getLogger.info("{}:删除成功".format(i))


class Moudle_report_waterPower_powerStation(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_report_waterPower_powerStation, self).__init__(*args, **kwargs)
        # 水电板块日报表
        self.waterDaily = (By.XPATH, "//a[@onclick='fun_a()']")
        # 水情报表
        self.waterSituation = (By.XPATH, "//a[@onclick='fun_b()']")
        # 水电机组报表
        self.waterUnit = (By.XPATH, "//a[@onclick='fun_c()']")
        # 报表导出按钮
        self.downLoad = (By.XPATH, "//p[contains(.,'输出')]")
        self.yesterday = datetime.strftime(datetime.today() - timedelta(days=1), "%Y%m%d")
        self.fileName = '发电情况表' + self.yesterday + '.xls'
        #将导出文件名（包含重复下载或上次删除失败的文件）组装成列表
        self.fileNames = ['发电情况表' + self.yesterday + ' (' + str(x) + ')' + '.xls' for x in range(1, 100)]
        self.fileNames.append(self.fileName)

    def click_waterDaily(self):
        self.click(self.waterDaily)

    def click_waterUnit(self):
        self.click(self.waterUnit)

    def click_waterSituation(self):
        self.click(self.waterSituation)

    def click_downLoad(self):
        """下载报表"""
        self.click(self.downLoad)
        self.getLogger.info("{}:下载成功".format(self.fileName))

    def remove_downloadFile(self):
        """删除报表"""
        self.pwd = os.getcwd()
        self.fPath = os.path.abspath(os.path.dirname(self.pwd))
        self.dPath = os.path.join(self.fPath, r'testData')
        self.filePath = [os.path.join(self.dPath, p) for p in self.fileNames]
        for i in self.filePath:
            if os.path.exists(i):
                os.remove(i)
                self.getLogger.info("{}:删除成功".format(i))


class Moudle_report_waterPower_Situation(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_report_waterPower_Situation, self).__init__(*args, **kwargs)
        # 水电板块日报表
        self.waterDaily = (By.XPATH, "//a[@onclick='fun_a()']")
        # 水电机组报表
        self.waterUnit = (By.XPATH, "//a[@onclick='fun_b()']")
        # 水电电站报表
        self.waterPowerStation = (By.XPATH, "//a[@onclick='fun_c()']")
        # 报表导出按钮
        self.downLoad = (By.XPATH, "//p[contains(.,'输出')]")
        self.yesterday = datetime.strftime(datetime.today() - timedelta(days=1), "%Y%m%d")
        self.fileName = '水情报表日报' + '.xls'
        self.fileNames = ['水情报表日报' + ' (' + str(x) + ')' + '.xls' for x in range(1, 100)]
        self.fileNames.append(self.fileName)

    def click_waterDaily(self):
        self.click(self.waterDaily)

    def click_waterUnit(self):
        self.click(self.waterUnit)

    def click_waterPowerStation(self):
        self.click(self.waterPowerStation)

    def click_downLoad(self):
        """下载报表"""
        self.click(self.downLoad)
        self.getLogger.info("{}:下载成功".format(self.fileName))

    def remove_downloadFile(self):
        """删除报表"""
        self.pwd = os.getcwd()
        self.fPath = os.path.abspath(os.path.dirname(self.pwd))
        self.dPath = os.path.join(self.fPath, r'testData')
        self.filePath = [os.path.join(self.dPath, p) for p in self.fileNames]
        for i in self.filePath:
            if os.path.exists(i):
                os.remove(i)
                self.getLogger.info("{}:删除成功".format(i))


class Moudle_report_waterPower_singleHostReport(BasePage):
    def __init__(self, *args, **kwargs):
        super(Moudle_report_waterPower_singleHostReport, self).__init__(*args, **kwargs)
        # 开机次数
        self.power_on = (By.XPATH, "//a[contains(.,'开机次数')]")
        # 停机次数
        self.shutdown = (By.XPATH, "//a[contains(.,'停机次数')]")
        # 运行小时
        self.hours_run = (By.XPATH, "//a[contains(.,'运行小时')]")
        # 冷备用小时
        self.cold_standby = (By.XPATH, "//a[contains(.,'冷备用小时')]")
        # 热备用小时
        self.hot_standby = (By.XPATH, "//a[contains(.,'热备用小时')]")
        # 检修小时
        self.overhaul_hours = (By.XPATH, "//a[contains(.,'检修小时')]")
        # 发电量
        self.power_generation = (By.XPATH, "//a[@href='javascript:queryWaterSingleFdl();']")
        # 报表导出按钮
        self.downLoad = (By.XPATH, "//p[contains(.,'输出')]")
        self.year = datetime.strftime(datetime.today(), "%Y")

        self.fileName = '单机报表(开机次数)' + self.year + '.xls'
        self.fileNames = ['单机报表(开机次数)' + self.year + ' (' + str(x) + ')' + '.xls' for x in range(1, 100)]
        self.fileNames.append(self.fileName)

    def click_power_on(self):
        self.click(self.power_on)

    def click_shutdown(self):
        self.click(self.shutdown)

    def click_hours_run(self):
        self.click(self.hours_run)

    def click_cold_standby(self):
        self.click(self.cold_standby)

    def click_hot_standby(self):
        self.click(self.hot_standby)

    def click_overhaul_hours(self):
        self.click(self.overhaul_hours)

    def click_power_generation(self):
        self.click(self.power_generation)

    def click_downLoad(self):
        """下载报表"""
        self.click(self.downLoad)
        self.getLogger.info("{}:下载成功".format(self.fileName))

    def remove_downloadFile(self):
        """删除报表"""
        self.pwd = os.getcwd()
        self.fPath = os.path.abspath(os.path.dirname(self.pwd))
        self.dPath = os.path.join(self.fPath, r'testData')
        self.filePath = [os.path.join(self.dPath, p) for p in self.fileNames]
        for i in self.filePath:
            if os.path.exists(i):
                os.remove(i)
                self.getLogger.info("{}:删除成功".format(i))

