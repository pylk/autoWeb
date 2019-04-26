# coding=utf-8
from AutoFramework.core.pom import BasePage
from selenium.webdriver.common.by import By


class LoginOutObj(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginOutObj, self).__init__(*args, **kwargs)
        self.userName = (By.XPATH, "//input[@id='loginName']")
        self.passWord = (By.XPATH, "//input[@id='password']")
        self.loginButton = (By.XPATH, "//a[text()='GO']")
        self.loginCheckPoint = (By.XPATH, "//a[text()='欢迎您：管理员']")

    def Login(self, userName, passWord):
        self.type(userName, self.userName)
        self.type(passWord, self.passWord)
        self.click(self.loginButton)
        self.checkPoint_contain(self.loginCheckPoint, "管理员")


class NavigateObj(BasePage):
    '''各种导航对象'''

    def __init__(self, *args, **kwargs):
        super(NavigateObj, self).__init__(*args, **kwargs)
        # 问题反馈
        # 问题列表
        self.questionList = (By.XPATH, "//a[text()='问题列表']")

        # 信息发布
        self.infoPublish = (By.XPATH, "//a[text()='信息发布']")
        # 群组维护
        self.groupMaintaince = (By.XPATH, "//a[text()='群组维护']")

        # 事件消息发布
        self.eventMsgPub = (By.XPATH, "//a[text()='事件消息发布']")
        self.eventMsgRecord = (By.XPATH, "//a[text()='事件消息记录']")
        self.eventMsgModify = (By.XPATH, "//a[text()='事件消息修改']")

        # 值班填报
        self.dutyfill = (By.XPATH, "//a[text()='值班填报']")
        # 值班填报子菜单
        self.waterpowerfill = (By.XPATH, "//a[text()='水电抄表']")
        self.sunpowerfill = (By.XPATH, "//a[text()='光伏抄表']")
        self.coalfill = (By.XPATH, "//a[text()='煤矿抄表']")
        self.firepowerfill = (By.XPATH, "//a[text()='值班填报']//following-sibling::*//a[text()='火电']")
        self.DutyFill_firePower = (By.XPATH, "/html/body/div[2]/div[1]/ul/li[9]/ul/li[1]/ul/li[1]/a")
        self.waterpower = (By.XPATH, "//a[text()='水电值班填报']")
        self.DutyFill_firePower_search = (By.XPATH, "/html/body/div[2]/div[1]/ul/li[9]/ul/li[1]/ul/li[2]/a")
        self.sunpower = (By.XPATH, "//a[text()='光伏值班填报']")
        self.Duty_firePower_modify = (By.XPATH, "//a[text()='火电']/..//following-sibling::*/a[text()='火电抄表修改']")

        # 实时监视
        self.monitoring = (By.XPATH, "//a[text()='实时监视']")
        self.comprehensiveOverview = (By.XPATH, "//a[text()='综合总览']")
        self.stateOverview = (By.XPATH, "//a[text()='状态总览']")
        self.coalproduction = (By.XPATH, "//a[text()='煤矿生产情况']")
        self.cementproduction = (By.XPATH, "//a[text()='水泥生产情况']")
        self.fireproduction = (By.XPATH, "//a[text()='火电生产情况']")
        self.sunproduction = (By.XPATH, "//a[text()='光伏生产情况']")
        self.waterproduction = (By.XPATH, "//a[text()='水电生产情况']")

        # 值班填报
        self.dutycfill = (By.XPATH, "//a[text()='值班填报']")
        # 值班填报子菜单
        self.waterpowerfill = (By.XPATH, "//a[text()='水电抄表']")
        self.sunpowerfill = (By.XPATH, "//a[text()='光伏抄表']")
        self.coalfill = (By.XPATH, "//a[text()='煤矿抄表']")

        # 配置管理
        self.configManag = (By.XPATH, "//a[text()='配置管理']")
        self.metrixConfig = (By.XPATH, "//a[text()='指标配置']")
        self.metrixMaintance = (By.XPATH, "//a[text()='指标维护']")
        # 报警服务
        self.alertService = (By.XPATH, "//a[text()='报警服务']")
        # self.initPoint=(By.XPATH,"//a[text()='测点初始化']")
        self.initPoint = (By.XPATH, "//a[text()='添加测点']")
        self.alertConfig = (By.XPATH, "//a[text()='报警配置']")
        self.alertRecord = (By.XPATH, "//a[text()='报警记录']")

        self.simlateQuantityAlertConfig = (By.XPATH, "//a[text()='模拟量报警配置']")
        self.switcherQuantityAlertConfig = (By.XPATH, "//a[text()='开关量报警配置']")
        self.simulateQuantityThreaholdConfig = (By.XPATH, "//a[text()='模拟量阈值配置']")
        self.simulateQuantityThreaholdModiy = (By.XPATH, "//a[text()='模拟量阈值修改']")

        self.simulateQuantityAlertRecord = (By.XPATH, "//a[text()='模拟量报警记录']")
        self.switcherQuantityAlertRecord = (By.XPATH, "//a[text()='开关量报警记录']")

        # self.doNotFreshAlert = (By.XPATH, "//a[text()='不刷新报警']")
        # self.dataNotFreshPage= (By.XPATH, "//a[text()='数据不刷新监视页面']")
        self.doNotFreshAlert = (By.XPATH, "//a[text()='不刷新测点报警']")
        self.dataNotFreshPage = (By.XPATH, "//a[text()='不刷新监视页面']")
        self.pointDetailPage = (By.XPATH, "//a[text()='测点详情页面']")
        self.notFreshTimeConfig = (By.XPATH, "//a[text()='不刷新时间配置']")

        # 数据管理
        self.dataManagement = (By.XPATH, "//a[text()='数据管理']")
        # 综合报表-火电
        self.overallReport = (By.XPATH, "//a[text()='综合报表']")
        self.overallReport_firePower = (
        By.XPATH, "//a[text()='综合报表']/following-sibling::*//descendant::*//a[text()='火电']")
        self.overallReport_firePower_dailyReport = (
        By.XPATH, "//a[text()='火电']/following-sibling::*//descendant::*/a[text()='日报']")
        # 综合报表-火电-日报
        self.firePower_Daily = (By.XPATH, "//a[text()='火电板块日报表']")
        self.jinyuanFirePower_daily = (By.XPATH, "//a[text()='金元火电生产日报表']")
        self.dailyPowerGenerate = (By.XPATH, "//a[text()='日发电量及负荷报表']")
        self.singleGroupPowerGenerate = (By.XPATH, "//a[text()='单机电量报表']")
        self.coalStateDaily = (By.XPATH, "//a[text()='煤情日报']")
        self.powerBural_coalStateDaily = (By.XPATH, "//a[text()='(电监办)电煤情况日报表']")
        self.electronic_coalDaily = (By.XPATH, "//a[text()='(经信委)电煤日报表']")
        # 综合报表-火电-周报
        self.overallReport_firePower_weeklyReport = (By.XPATH, "//a[text()='周报']")
        self.weeklyReport_jinyuan = (By.XPATH, "//a[text()='金元周报']")
        # 综合报表-火电-月报
        self.overallReport_firePower_monthlyReport = (By.XPATH, "//a[text()='月报']")
        self.monthlyReport_coalCheck = (By.XPATH, "//a[text()='燃煤盘存校核月报']")
        self.monthlyReport_electralCoalStatic = (By.XPATH, "//a[text()='电煤统计日报表']")
        self.monthlyReport_elecGenerateStatic = (By.XPATH, "//a[text()='发电量情况统计报表']")
        # 综合报表-火电-综合报表
        self.overallReport_firePower_overallReport = (
        By.XPATH, "//a[text()='月报']/../following-sibling::*/a[text()='综合报表']")
        self.overallReport_elecGenerateReport = (By.XPATH, "//a[text()='发电量及负荷综合报表']")
        self.overallReport_coalStatGeneralReport = (By.XPATH, "//a[text()='煤情综合报表']")
        self.overallReport_elecCoalGeneralReport = (By.XPATH, "//a[text()='(经信委)电煤综合报表']")
        self.overallReport_electGenrateMatrixReport = (By.XPATH, "//a[text()='发电生产指标报表']")
        self.overallReport_nonStopeReport = (By.XPATH, "//a[text()='非停总表']")
        self.overallReport_nonStopeStatisticReport = (By.XPATH, "//a[text()='非停统计表']")
        self.overallReport_openCloseReport = (By.XPATH, "//a[text()='开停报表']")
        # 综合报表-水电
        self.overallReport_waterPower = (By.XPATH, "//a[text()='综合报表']/..//following-sibling::*/a[text()='水电']")
        # 综合报表-水电-水电板块日报表
        self.overallReport_waterPower_dailyReport = (By.XPATH, "//a[text()='水电板块日报表']")
        # 综合报表-水电-水电机组报表
        self.overallReport_waterPower_unit = (By.XPATH, "//a[text()='水电机组报表']")
        # 综合报表-水电-水电电站报表
        self.overallReport_waterPower_powerStation = (By.XPATH, "//a[text()='水电电站报表']")
        # 综合报表-水电-水情报表
        self.overallReport_waterPower_situation = (By.XPATH, "//a[text()='水情报表']")
        # 综合报表-水电-水电单机报表
        self.overallReport_waterPower_singleHostReport = (By.XPATH, "//a[text()='水电单机报表']")

        # 综合报表-光伏
        # self.overallReport_sunPower = (By.XPATH, "//a[text()='光伏']")
        self.overallReport_sunPower = ('xpath', '//*[@id="cssmenu"]/ul/li[2]/ul/li[2]/ul/li[3]/a')
        # 综合报表-光伏-光伏日报表
        self.overallReport_sunPower_daily = (By.XPATH, "//a[text()='光伏板块日报表']")
        # 综合报表-煤矿
        self.overallReport_coalPower = (By.XPATH, "//a[text()='综合报表']/..//following-sibling::*/a[text()='煤矿']")
        # 综合报表-煤矿-日表
        self.overallReport_coalPower_daily = (By.XPATH, "//a[text()='煤矿板块日报表']")

        # 综合报表-综合产业
        self.overallReport_overall = (By.XPATH, "//a[text()='综合报表']/..//following-sibling::*/a[text()='综合产业']")
        # 综合报表-综合产业-日报
        self.overallReport_overalld_daily = (By.XPATH, "//a[text()='综合产业日报表']")
        ##月度指标报表
        self.monthlyIndex = (By.XPATH, "//a[contains(.,'月度指标报表')]")

        self.fillState = (By.XPATH, "//a[text()='填报情况']")

        # 数据填报
        self.dataFill = (By.XPATH, "//a[text()='数据填报']")
        self.dataFill_firePower = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='火电']")
        self.dataFill_firePower_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='火电']//following-sibling::*//a[text()='填报']")
        self.dataFill_firePower_fill_dailyReport = (By.XPATH, "//a[text()='电量日报(7点以前)']")
        self.dataFill_firePower_fill_generalReport = (By.XPATH, "//a[text()='综合日报(8点以前)']")
        self.dataFill_firePower_fill_coalReport = (By.XPATH, "//a[text()='煤量日报(7点以前)']")
        self.dataFill_firePower_fill_anualPlan = (By.XPATH, "//a[text()='年计划填报']")
        self.dataFill_firePower_fill_planElecDuplicate = (By.XPATH, "//a[text()='96点计划电量(复制)']")
        self.dataFill_firePower_fill_planElecFill = (By.XPATH, "//a[text()='96点计划电量填报']")
        self.dataFill_firePower_fill_coalFill = (By.XPATH, "//a[text()='煤量填报(经信委)']")
        self.dataFill_firePower_fill_firePowerGroupStatusFill = (By.XPATH, "//a[text()='火电机组状态变更填报']")
        self.dataFill_firePower_verify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='火电']//following-sibling::*//a[text()='审核']")
        self.dataFill_firePower_verify_elecVerify = (By.XPATH, "//a[text()='电量日填报审核']")
        self.dataFill_firePower_verify_generalReportFillVerify = (By.XPATH, "//a[text()='综合日填报审核']")
        self.dataFill_firePower_verify_coalDailyVerify = (By.XPATH, "//a[text()='煤量日填报审核']")
        self.dataFill_firePower_verify_coalQuantity = (By.XPATH, "//a[text()='煤量审核(经信委)']")
        self.dataFill_firePower_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='火电']//following-sibling::*//a[text()='修改']")
        self.dataFill_firePower_modify_elecDailyModify = (By.XPATH, "//a[text()='电量日填报修改']")
        self.dataFill_firePower_modify_generalDailyModify = (By.XPATH, "//a[text()='综合日填报修改']")
        self.dataFill_firePower_modify_coalDailyModify = (By.XPATH, "//a[text()='煤量日填报修改']")
        self.dataFill_firePower_modify_anaualModify = (By.XPATH, "//a[text()='年计划修改']")
        self.dataFill_firePower_modify_planElecModify = (By.XPATH, "//a[text()='96点计划电量修改']")
        self.dataFill_firePower_modify_coalQuantityModify = (By.XPATH, "//a[text()='煤量修改(经信委)']")
        self.dataFill_firePower_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='火电']//following-sibling::*//a[text()='查询']")
        self.dataFill_firePower_search_elecDailySearch = (By.XPATH, "//a[text()='电量日填报查询']")
        self.dataFill_firePower_search_generalDailySearch = (By.XPATH, "//a[text()='综合日填报查询']")
        self.dataFill_firePower_search_coalDailySearch = (By.XPATH, "//a[text()='煤量日填报查询']")
        self.dataFill_firePower_search_planElecSearch = (By.XPATH, "//a[text()='96点计划电量查询']")
        self.dataFill_firePower_search_coalSearch = (By.XPATH, "//a[text()='煤量查询(经信委)']")

        self.dataFill_waterPower = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='水电']")
        self.dataFill_waterPower_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='填报']")
        self.dataFill_waterPower_fill_hostStatusChange = (By.XPATH, "//a[text()='机组状态变更填报']")
        self.dataFill_waterPower_fill_readNum = (By.XPATH, "//a[text()='读数填报']")
        self.dataFill_waterPower_fill_anual = (By.XPATH,
                                               "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='填报']/following-sibling::*//a[text()='年计划填报']")
        self.dataFill_waterPower_verify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='审核']")
        self.dataFill_waterPower_verify_readNum = (By.XPATH, "//a[text()='读数审核']")
        self.dataFill_waterPower_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='修改']")
        self.dataFill_waterPower_modify_readNum = (By.XPATH, "//a[text()='读数修改']")
        self.dataFill_waterPower_modify_hostStatusModify = (By.XPATH, "//a[text()='机组状态修改']")
        self.dataFill_waterPower_modify_annualPlanModify = (By.XPATH,
                                                            "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='修改']/following-sibling::*//a[text()='年计划修改']")
        self.dataFill_waterPower_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='水电']//following-sibling::*//a[text()='查询']")
        self.dataFill_waterPower_search_readNumSearch = (By.XPATH, "//a[text()='读数查询']")
        self.dataFill_waterPower_search_hostStatusChangeSearch = (By.XPATH, "//a[text()='机组状态变更查询']")

        self.dataFill_sunPower = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']")
        self.dataFill_sunPower_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='填报']")
        self.dataFill_sunPower_fill_dailyFill = (By.XPATH,
                                                 "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='日填报']")
        self.dataFill_sunPower_fill_anualFill = (By.XPATH,
                                                 "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='年计划填报']")
        self.dataFill_sunPower_verify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='审核']")
        self.dataFill_sunPower_verify_dailyVerify = (By.XPATH, "//a[text()='日填报审核']")
        self.dataFill_sunPower_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='修改']")
        self.dataFill_sunPower_modify_dailyModify = (By.XPATH, "//a[text()='日填报修改']")
        self.dataFill_sunPower_modify_anualModify = (By.XPATH,
                                                     "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='年计划修改']")
        self.dataFill_sunPower_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='光伏']//following-sibling::*//a[text()='查询']")
        self.dataFill_sunPower_search_daily = (By.XPATH, "//a[text()='日填报查询']")

        self.dataFill_coalPower = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']")
        self.dataFill_coalPower_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='填报']")
        self.dataFill_coalPower_fill_dailyFill = (By.XPATH, "//a[text()='煤矿日填报']")
        self.dataFill_coalPower_fill_anualFill = (By.XPATH, "//a[text()='年计划填报']")
        self.dataFill_coalPower_fill_vasElecFill = (By.XPATH, "//a[text()='瓦斯发电日填报']")
        self.dataFill_coalPower_fill_costIndex = (By.XPATH, "//a[contains(.,'成本指标月填报')]")
        self.dataFill_coalPower_verify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='审核']")
        self.dataFill_coalPower_verify_dailyVerify = (By.XPATH,
                                                      "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='审核']//following-sibling::*//a[text()='日填报审核']")
        self.dataFill_coalPower_verify_vasElectVerify = (By.XPATH, "//a[text()='瓦斯发电填报审核']")
        self.dataFill_coalPower_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='修改']")
        self.dataFill_coalPower_modify_dailyModify = (By.XPATH,
                                                      "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='日填报修改']")
        self.dataFill_coalPower_modify_anualModify = (By.XPATH,
                                                      "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='年计划填报修改']")
        self.dataFill_coalPower_modify_vasElecModify = (By.XPATH,
                                                        "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='瓦斯发电填报修改']")
        self.dataFill_coalPower_modify_costIndexModify = (By.XPATH,
                                                          "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='月成本指标修改']")
        self.dataFill_coalPower_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='查询']")
        self.dataFill_coalPower_search_daily = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='煤矿']//following-sibling::*//a[text()='查询']//following-sibling::*//a[text()='日填报查询']")
        self.dataFill_coalPower_search_vasElecSearch = (By.XPATH, "//a[text()='瓦斯发电填报查询']")
        self.dataFill_coalPower_search_costIndexSearch = (By.XPATH, "//a[contains(.,'月成本指标查询')]")

        self.dataFill_overall = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']")
        self.dataFill_overall_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']")
        self.dataFill_overall_fill_dailyFill = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='日填报']")

        self.dataFill_overall_fill_cement_monthFill = (By.XPATH,
                                                       "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='水泥月填报']")
        self.dataFill_overall_fill_mn_dailyFill = (By.XPATH,
                                                   "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='锰系合金日填报']")
        self.dataFill_overall_fill_mn_monthFill = (By.XPATH,
                                                   "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='锰系合金月填报']")
        self.dataFill_overall_fill_hotel_dailyFill = (By.XPATH,
                                                      "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='酒店日填报']")
        self.dataFill_overall_fill_hotel_monthFill = (By.XPATH,
                                                      "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='酒店月成本填报']")

        self.dataFill_overall_fill_anualFill = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='填报']//following-sibling::*//a[text()='年计划填报']")
        self.dataFill_overall_verify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='审核']")
        self.dataFill_overall_verify_fillVerify = (By.XPATH, "//a[text()='填报审核']")

        self.dataFill_overall_mnDaily_fillVerify = (By.XPATH,
                                                    "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='审核']//following-sibling::*//a[text()='锰系合金日报审核']")
        self.dataFill_overall_hotelDaily_fillVerify = (By.XPATH,
                                                       "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='审核']//following-sibling::*//a[text()='酒店日填报审核']")

        self.dataFill_overall_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']")
        self.dataFill_overall_modify_daily = (By.XPATH,
                                              "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='日填报修改']")

        self.dataFill_overall_modify_cenmentMonth = (By.XPATH,
                                                     "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='水泥月报修改']")
        self.dataFill_overall_modify_mnDaily = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='锰系合金日报修改']")
        self.dataFill_overall_modify_mnMonth = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='锰系合金月报修改']")
        self.dataFill_overall_modify_hotelDaily = (By.XPATH,
                                                   "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='酒店日填报修改']")
        self.dataFill_overall_modify_hotelMonth = (By.XPATH,
                                                   "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='修改']//following-sibling::*//a[text()='酒店月成本修改']")

        self.dataFill_overall_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='查询']")
        self.dataFill_overall_search_daily = (By.XPATH,
                                              "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='查询']//following-sibling::*//a[text()='日填报查询']")

        self.click_dataFill_yearplansearch = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']")
        self.click_dataFill_yearplan_of_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']//following-sibling::*//a[text()='查询']")
        self.click_dataFill_yearplan_of_modify = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']//following-sibling::*//a[text()='修改']")
        self.click_dataFill_yearplan_of_fill = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']//following-sibling::*//a[text()='填报']")

        self.click_dataFill_yearplan_search = (By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']")
        self.click_dataFill_yearplan_of_search = (
        By.XPATH, "//a[text()='数据填报']//following-sibling::*//a[text()='年计划']//following-sibling::*//a[text()='查询']")

        self.dataFill_overall_search_cenmentMonth = (By.XPATH,
                                                     "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='查询']//following-sibling::*//a[text()='水泥月报查询']")
        self.dataFill_overall_search_mnMonth = (By.XPATH,
                                                "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='查询']//following-sibling::*//a[text()='锰系合金月报查询']")
        self.dataFill_overall_search_hotelMonth = (By.XPATH,
                                                   "//a[text()='数据填报']//following-sibling::*//a[text()='综合产业']//following-sibling::*//a[text()='查询']//following-sibling::*//a[text()='酒店月成本查询']")

        # 值班填报
        self.dutyFill = (By.XPATH, "//a[text()='值班填报']")
        self.firePower = (By.XPATH, "//a[text()='值班填报']//following-sibling::*//a[text()='火电']")
        self.coal = ("xpath", '//*[@id="cssmenu"]/ul/li[8]/ul/li[4]/a')
        self.firePower_fill = (By.XPATH, "//a[text()='火电抄表填报']")
        self.firePower_search = (By.XPATH, "//a[text()='火电抄表查询']")
        self.firePower_modify = (By.XPATH, "//a[text()='火电抄表修改']")
        self.firePower_duty_fill = (By.XPATH, "//a[text()='火电值班填报']")
        self.firePower_duty_search = (By.XPATH, "//a[text()='火电值班查询']")
        self.firePower_duty_modify = (By.XPATH, "//a[text()='火电值班修改']")
        self.firePower_duty_record_search = (By.XPATH, "//a[text()='火电值班记录查询']")
        self.waterCopyPower = (By.XPATH, "//a[text()='水电抄表']")
        self.sunCopyPower = (By.XPATH, "//a[text()='光伏抄表']")
        self.coalCopyPower = (By.XPATH, "//a[text()='煤矿抄表']")
        self.dutyfill_waterPower = ("xpath", '//*[@id="cssmenu"]/ul/li[8]/ul/li[2]/a')  # 值班填报-水电
        self.waterDutyFill = (By.XPATH, "//a[text()='水电值班填报']")
        self.dutyfill_sunpower = ("xpath", '//*[@id="cssmenu"]/ul/li[8]/ul/li[3]/a')  # 值班填报-光伏
        self.sunDutyFill = (By.XPATH, "//a[text()='光伏值班填报']")
        self.coalDutyFill = (By.XPATH, "//a[text()='煤矿值班填报']")
        self.waterpower1 = (By.XPATH, "//*[@id='cssmenu']//ul//li[8]//a[text()='水电']")  # 增加值班填报-说表移动到水电

        # 2018/08/06新增
        self.dataFill_firePower_fill_coalAndCoalQulityFill = (By.XPATH, "//a[text()='燃煤及煤质填报']")
        self.dataFill_firePower_verify_coalAndCoalQulityVerify = (By.XPATH, "//a[text()='燃煤及煤质审核']")
        self.dataFill_firePower_verify_coalAndCoalQulityModify = (By.XPATH, "//a[text()='燃煤及煤质修改']")
        self.dataFill_firePower_verify_coalAndCoalQulitySearch = (By.XPATH, "//a[text()='燃煤及煤质查询']")
        self.dataFill_firePower_fill_coalStaticMonthReportFill = (By.XPATH, "//a[text()='耗煤盘存月报']")
        self.dataFill_firePower_modify_coalStaticMonthReportModify = (By.XPATH, "//a[text()='耗煤盘存月报修改']")
        self.dataFill_firePower_groupStatsChange = (By.XPATH, "//a[text()='机组状态变更']")
        self.dataFill_firePower_groupStatsChange_fill = (By.XPATH, "//a[text()='变更填报']")
        self.dataFill_firePower_groupStatsChange_confirm = (By.XPATH, "//a[text()='变更确认']")
        self.dataFill_firePower_groupStatsChange_modify = (By.XPATH, "//a[text()='变更修改']")
        self.dataFill_firePower_groupStatsChange_delete = (By.XPATH, "//a[text()='变更删除']")
        self.dataFill_firePower_groupStatsChange_records = (By.XPATH, "//a[text()='变更记录']")
        self.dataFill_firePower_groupStatsChange_maintaince = (By.XPATH, "//a[text()='变更类型维护']")

    # 2018/08/06新增
    def click_dataFill_firePower_fill_coalAndCoalQulityFill(self):
        self.click(self.dataFill_firePower_fill_coalAndCoalQulityFill)

    def click_dataFill_firePower_verify_coalAndCoalQulityVerify(self):
        self.click(self.dataFill_firePower_verify_coalAndCoalQulityVerify)

    def click_dataFill_firePower_modify_coalAndCoalQulityModify(self):
        self.click(self.dataFill_firePower_verify_coalAndCoalQulityModify)

    def click_dataFill_firePower_search_coalAndCoalQulitySearch(self):
        self.click(self.dataFill_firePower_verify_coalAndCoalQulitySearch)

    def click_dataFill_firePower_fill_coalStaticMonthReportFill(self):
        self.click(self.dataFill_firePower_fill_coalStaticMonthReportFill)

    def click_dataFill_firePower_modify_coalStaticMonthReportModify(self):
        self.click(self.dataFill_firePower_modify_coalStaticMonthReportModify)

    def click_dataFill_firePower_groupStatsChange(self):
        self.click(self.dataFill_firePower_groupStatsChange)

    def click_dataFill_firePower_groupStatsChange_fill(self):
        self.click(self.dataFill_firePower_groupStatsChange_fill)

    def click_dataFill_firePower_groupStatsChange_confirm(self):
        self.click(self.dataFill_firePower_groupStatsChange_confirm)

    def click_dataFill_firePower_groupStatsChange_modify(self):
        self.click(self.dataFill_firePower_groupStatsChange_modify)

    def click_dataFill_firePower_groupStatsChange_delete(self):
        self.click(self.dataFill_firePower_groupStatsChange_delete)

    def click_dataFill_firePower_groupStatsChange_records(self):
        self.click(self.dataFill_firePower_groupStatsChange_records)

    def click_dataFill_firePower_groupStatsChange_maintaince(self):
        self.click(self.dataFill_firePower_groupStatsChange_maintaince)

        # 大屏展示
        self.large_screen_display = ("xpath", '//*[text()="大屏展示"]')
        self.data_maintian = ("xpath", '//*[text()="数据维护"]')
        self.jy_data_maintian = ("xpath", '//*[text()="金元数据维护"]')
        self.jy_data_modify = ("xpath", '//*[text()="金元数据修改"]')
        self.jy_data_query = ("xpath", '//*[text()="金元数据查询"]')
        self.map_text_modify = ("xpath", '//*[text()="地图文字修改"]')
        self.firePower_data_maintian = ("xpath", '//*[text()="火电数据维护"]')
        self.firePower_data_modify = ("xpath", '//*[text()="火电数据修改"]')
        self.firePower_data_query = ("xpath", '//*[text()="火电数据查询"]')
        self.coal_data_maintian = ("xpath", '//*[text()="煤矿数据维护"]')
        self.coal_data_modify = ("xpath", '//*[text()="煤矿数据修改"]')
        self.coal_data_query = ("xpath", '//*[text()="煤矿数据查询"]')

        # 问题反馈
        self.questionFeedback = (By.XPATH, "//a[text()='问题反馈']")
        self.questionFeedback_auit = ("xpath", "//*[text()='问题反馈审核']")
        self.questionFeedback_add = ("xpath", "//*[text()='问题反馈填报']")
        self.questionFeedback_confirm = ("xpath", "//*[text()='开发确认']")

    # 大屏展示
    def click_large_screen_display(self):
        self.click(self.large_screen_display)

    def click_data_maintian(self):
        self.click(self.data_maintian)

    def click_jy_data_maintian(self):
        self.click(self.jy_data_maintian)

    def click_jy_data_modify(self):
        self.click(self.jy_data_modify)

    def click_jy_data_query(self):
        self.click(self.jy_data_query)

    def click_map_text_modify(self):
        self.click(self.map_text_modify)

    def click_firePower_data_maintian(self):
        self.click(self.firePower_data_maintian)

    def click_firePower_data_modify(self):
        self.click(self.firePower_data_modify)

    def click_firePower_data_query(self):
        self.click(self.firePower_data_query)

    def click_coal_data_maintian(self):
        self.click(self.coal_data_maintian)

    def click_coal_data_modify(self):
        self.click(self.coal_data_query)

    # 问题反馈
    def click_question_feedback(self):
        self.click(self.questionFeedback)

    def click_question_feedback_add(self):
        self.click(self.questionFeedback_add)

    def click_question_feedback_auit(self):
        self.click(self.questionFeedback_auit)

    def click_question_feedback_comfirm(self):
        self.click(self.questionFeedback_confirm)

    # 值班填报
    def click_waterpower1(self):
        self.click(self.waterpower1)

    def click_dutyFill(self):
        self.click(self.dutyFill)

    def click_dutyFill_coal(self):
        self.click(self.coal)

    def click_dutyFillfirePower(self):
        self.click(self.firePower)

    def click_dutyFillfirePower_fill(self):
        self.click(self.firePower_fill)

    def click_dutyFillfirePower_search(self):
        self.click(self.firePower_search)

    def click_dutyFillfirePower_modify(self):
        self.click(self.firePower_modify)

    def click_dutyFillfirePower_duty_fill(self):
        self.click(self.firePower_duty_fill)

    def click_dutyFillfirePower_duty_search(self):
        self.click(self.firePower_duty_search)

    def click_dutyFillfirePower_duty_modify(self):
        self.click(self.firePower_duty_modify)

    def click_dutyFillfirePower_duty_record_search(self):
        self.click(self.firePower_duty_record_search)

    def click_waterCopyPower(self):
        self.click(self.waterCopyPower)

    def click_sunCopyPower(self):
        self.click(self.sunCopyPower)

    def click_coalCopyPower(self):
        self.click(self.coalCopyPower)

    def click_waterDutyFill(self):
        self.click(self.waterDutyFill)

    def click_sunDutyFill(self):
        self.click(self.sunDutyFill)

    def click_coalDutyFill(self):
        self.click(self.coalDutyFill)

    def click_dutyFill_sunPower(self):
        self.click(self.dutyfill_sunpower)

    def click_dutyFill_wataerPower(self):
        self.click(self.dutyfill_waterPower)

    # 数据填报
    def click_dataFill(self):
        self.click(self.dataFill)

    # 火电
    def click_dataFill_firePower(self):
        self.click(self.dataFill_firePower)

    def click_dataFill_firePower_fill(self):
        self.click(self.dataFill_firePower_fill)

    def click_dataFill_firePower_fill_dailyReport(self):
        self.click(self.dataFill_firePower_fill_dailyReport)

    def click_dataFill_firePower_fill_generalReport(self):
        self.click(self.dataFill_firePower_fill_generalReport)

    def click_dataFill_firePower_fill_coalReport(self):
        self.click(self.dataFill_firePower_fill_coalReport)

    def click_dataFill_firePower_fill_anualPlan(self):
        self.click(self.dataFill_firePower_fill_anualPlan)

    def click_dataFill_firePower_fill_planElecDuplicate(self):
        self.click(self.dataFill_firePower_fill_planElecDuplicate)

    def click_dataFill_firePower_fill_planElecFill(self):
        self.click(self.dataFill_firePower_fill_planElecFill)

    def click_dataFill_firePower_fill_coalFill(self):
        self.click(self.dataFill_firePower_fill_coalFill)

    def click_dataFill_firePower_fill_firePowerGroupStatusFill(self):
        self.click(self.dataFill_firePower_fill_firePowerGroupStatusFill)

    def click_dataFill_firePower_verify(self):
        self.click(self.dataFill_firePower_verify)

    def click_dataFill_firePower_verify_elecVerify(self):
        self.click(self.dataFill_firePower_verify_elecVerify)

    def click_dataFill_firePower_verify_generalReportFillVerify(self):
        self.click(self.dataFill_firePower_verify_generalReportFillVerify)

    def click_dataFill_firePower_verify_coalDailyVerify(self):
        self.click(self.dataFill_firePower_verify_coalDailyVerify)

    def click_dataFill_firePower_verify_coalQuantity(self):
        self.click(self.dataFill_firePower_verify_coalQuantity)

    def click_dataFill_firePower_modify(self):
        self.click(self.dataFill_firePower_modify)

    def click_dataFill_firePower_modify_elecDailyModify(self):
        self.click(self.dataFill_firePower_modify_elecDailyModify)

    def click_dataFill_firePower_modify_generalDailyModify(self):
        self.click(self.dataFill_firePower_modify_generalDailyModify)

    def click_dataFill_firePower_modify_coalDailyModify(self):
        self.click(self.dataFill_firePower_modify_coalDailyModify)

    def click_dataFill_firePower_modify_anaualModify(self):
        self.click(self.dataFill_firePower_modify_anaualModify)

    def click_dataFill_firePower_modify_planElecModify(self):
        self.click(self.dataFill_firePower_modify_planElecModify)

    def click_dataFill_firePower_modify_coalQuantityModify(self):
        self.click(self.dataFill_firePower_modify_coalQuantityModify)

    def click_dataFill_firePower_search(self):
        self.click(self.dataFill_firePower_search)

    def click_dataFill_firePower_search_elecDailySearch(self):
        self.click(self.dataFill_firePower_search_elecDailySearch)

    def click_dataFill_firePower_search_generalDailySearch(self):
        self.click(self.dataFill_firePower_search_generalDailySearch)

    def click_dataFill_firePower_search_coalDailySearch(self):
        self.click(self.dataFill_firePower_search_coalDailySearch)

    def click_dataFill_firePower_search_planElecSearch(self):
        self.click(self.dataFill_firePower_search_planElecSearch)

    def click_dataFill_firePower_search_coalSearch(self):
        self.click(self.dataFill_firePower_search_coalSearch)

    # 水电
    def click_dataFill_waterPower(self):
        self.click(self.dataFill_waterPower)

    def click_dataFill_waterPower_fill(self):
        self.click(self.dataFill_waterPower_fill)

    def click_dataFill_waterPower_fill_hostStatusChange(self):
        self.click(self.dataFill_waterPower_fill_hostStatusChange)

    def click_dataFill_waterPower_fill_readNum(self):
        self.click(self.dataFill_waterPower_fill_readNum)

    def click_dataFill_waterPower_fill_anual(self):
        self.click(self.dataFill_waterPower_fill_anual)

    def click_dataFill_waterPower_verify(self):
        self.click(self.dataFill_waterPower_verify)

    def click_dataFill_waterPower_verify_readNum(self):
        self.click(self.dataFill_waterPower_verify_readNum)

    def click_dataFill_waterPower_modify(self):
        self.click(self.dataFill_waterPower_modify)

    def click_dataFill_waterPower_modify_readNum(self):
        self.click(self.dataFill_waterPower_modify_readNum)

    def click_dataFill_waterPower_modify_hostStatusModify(self):
        self.click(self.dataFill_waterPower_modify_hostStatusModify)

    def click_dataFill_waterPower_modify_annualPlanModify(self):
        self.click(self.dataFill_waterPower_modify_annualPlanModify)

    def click_dataFill_waterPower_search(self):
        self.click(self.dataFill_waterPower_search)

    def click_dataFill_waterPower_search_readNumSearch(self):
        self.click(self.dataFill_waterPower_search_readNumSearch)

    def click_dataFill_waterPower_search_hostStatusChangeSearch(self):
        self.click(self.dataFill_waterPower_search_hostStatusChangeSearch)

    # 光伏
    def click_dataFill_sunPower(self):
        self.click(self.dataFill_sunPower)

    def click_dataFill_sunPower_fill(self):
        self.click(self.dataFill_sunPower_fill)

    def click_dataFill_sunPower_fill_dailyFill(self):
        self.click(self.dataFill_sunPower_fill_dailyFill)

    def click_dataFill_sunPower_fill_anualFill(self):
        self.click(self.dataFill_sunPower_fill_anualFill)

    def click_dataFill_sunPower_verify(self):
        self.click(self.dataFill_sunPower_verify)

    def click_dataFill_sunPower_verify_dailyVerify(self):
        self.click(self.dataFill_sunPower_verify_dailyVerify)

    def click_dataFill_sunPower_modify(self):
        self.click(self.dataFill_sunPower_modify)

    def click_dataFill_sunPower_modify_dailyModify(self):
        self.click(self.dataFill_sunPower_modify_dailyModify)

    def click_dataFill_sunPower_modify_anualModify(self):
        self.click(self.dataFill_sunPower_modify_anualModify)

    def click_dataFill_sunPower_search(self):
        self.click(self.dataFill_sunPower_search)

    def click_dataFill_sunPower_search_daily(self):
        self.click(self.dataFill_sunPower_search_daily)

    # 煤电
    def click_dataFill_coalPower(self):
        self.click(self.dataFill_coalPower)

    def click_dataFill_coalPower_fill(self):
        self.click(self.dataFill_coalPower_fill)

    def click_dataFill_coalPower_fill_dailyFill(self):
        self.click(self.dataFill_coalPower_fill_dailyFill)

    def click_dataFill_coalPower_fill_anualFill(self):
        self.click(self.dataFill_coalPower_fill_anualFill)

    def click_dataFill_coalPower_fill_vasElecFill(self):
        self.click(self.dataFill_coalPower_fill_vasElecFill)

    def click_dataFill_coalPower_fill_costIndex(self):
        """
        点击成本指标月填报
        :return:
        """
        self.click(self.dataFill_coalPower_fill_costIndex)

    def click_dataFill_coalPower_verify(self):
        self.click(self.dataFill_coalPower_verify)

    def click_dataFill_coalPower_verify_dailyVerify(self):
        self.click(self.dataFill_coalPower_verify_dailyVerify)

    def click_dataFill_coalPower_verify_vasElectVerify(self):
        self.click(self.dataFill_coalPower_verify_vasElectVerify)

    def click_dataFill_coalPower_modify(self):
        self.click(self.dataFill_coalPower_modify)

    def click_dataFill_coalPower_modify_dailyModify(self):
        self.click(self.dataFill_coalPower_modify_dailyModify)

    def click_dataFill_coalPower_modify_anualModify(self):
        self.click(self.dataFill_coalPower_modify_anualModify)

    def click_dataFill_coalPower_modify_vasElecModify(self):
        self.click(self.dataFill_coalPower_modify_vasElecModify)

    def click_dataFill_coalPower_modify_costIndexModify(self):
        """
        点击修改月成本指标填报
        :return:
        """
        self.click(self.dataFill_coalPower_modify_costIndexModify)

    def click_dataFill_coalPower_search(self):
        self.click(self.dataFill_coalPower_search)

    def click_dataFill_coalPower_search_daily(self):
        self.click(self.dataFill_coalPower_search_daily)

    def click_dataFill_coalPower_search_vasElecSearch(self):
        self.click(self.dataFill_coalPower_search_vasElecSearch)

    def click_dataFill_coalPower_search_costIndexSearch(self):
        """
        点击月成本指标查询
        :return:
        """
        self.click(self.dataFill_coalPower_search_costIndexSearch)

    # 综合产业
    def click_dataFill_overall(self):
        self.click(self.dataFill_overall)

    def click_dataFill_overall_fill(self):
        self.click(self.dataFill_overall_fill)

    def click_dataFill_overall_fill_dailyFill(self):
        self.click(self.dataFill_overall_fill_dailyFill)

    def click_dataFill_overall_fill_cementMonthFill(self):
        """
        点击水泥月填报
        :return:
        """
        self.click(self.dataFill_overall_fill_cement_monthFill)

    def click_dataFill_overall_fill_mn_dailyFill(self):
        """
        点击锰金合系日填报
        :return:
        """
        self.click(self.dataFill_overall_fill_mn_dailyFill)

    def click_dataFill_overall_fill_mn_monthFill(self):
        """
        点击锰金合系月填报
        :return:
        """
        self.click(self.dataFill_overall_fill_mn_monthFill)

    def click_dataFill_overall_fill_hotel_dailyFill(self):
        """
        点击酒店日填报
        :return:
        """
        self.click(self.dataFill_overall_fill_hotel_dailyFill)

    def click_dataFill_overall_fill_hotel_monthFill(self):
        """
        点击酒店月填报
        :return:
        """
        self.click(self.dataFill_overall_fill_hotel_monthFill)

    def click_dataFill_overall_fill_anualFill(self):
        self.click(self.dataFill_overall_fill_anualFill)

    def click_dataFill_overall_verify(self):
        self.click(self.dataFill_overall_verify)

    def click_dataFill_overall_verify_fillVerify(self):
        self.click(self.dataFill_overall_verify_fillVerify)

    def click_dataFill_overall_mnDaily_fillVerify(self):
        """
        点击锰系日填报审核
        :return:
        """
        self.click(self.dataFill_overall_mnDaily_fillVerify)

    def click_dataFill_overall_hotelDaily_fillVerify(self):
        """
        点击酒店日填报审核
        """
        self.click(self.dataFill_overall_hotelDaily_fillVerify)

    def click_dataFill_overall_modify(self):
        self.click(self.dataFill_overall_modify)

    def click_dataFill_overall_modify_daily(self):
        self.click(self.dataFill_overall_modify_daily)

    def click_dataFill_overall_modify_anual(self):
        self.click(self.dataFill_overall_modify_anual)

    def click_dataFill_overall_modify_cenmentMonth(self):
        """
        点击水泥月填报修改
        :return:
        """
        self.click(self.dataFill_overall_modify_cenmentMonth)

    def click_dataFill_overall_modify_mnDaily(self):
        """
        点击锰系合金日填报修改
        """
        self.click(self.dataFill_overall_modify_mnDaily)

    def click_dataFill_overall_modify_mnMonth(self):
        """
        点击锰系合金月填报修改
        """
        self.click(self.dataFill_overall_modify_mnMonth)

    def click_dataFill_overall_modify_hotelDaily(self):
        """
        点击酒店日填报修改
        """
        self.click(self.dataFill_overall_modify_hotelDaily)

    def click_dataFill_overall_modify_hotelMonth(self):
        """
        点击酒店月填报修改
        """
        self.click(self.dataFill_overall_modify_hotelMonth)

    def click_dataFill_overall_search(self):
        self.click(self.dataFill_overall_search)

    def click_dataFill_overall_search_daily(self):
        self.click(self.dataFill_overall_search_daily)

    def click_dataFill_overall_search_cenmentMonth(self):
        """
        点击水泥月填报查询
        """
        self.click(self.dataFill_overall_search_cenmentMonth)

    def click_dataFill_overall_search_mnMonth(self):
        """
        点击锰系合金月填报查询
        """
        self.click(self.dataFill_overall_search_mnMonth)

    def click_dataFill_overall_search_hotelMonth(self):
        """
        点击酒店月填报查询
        """
        self.click(self.dataFill_overall_search_hotelMonth)

    def click_dataFill_yearplan(self):
        self.click(self.click_dataFill_yearplansearch)

    def click_dataFill_yearplanofmodify(self):
        self.click(self.click_dataFill_yearplan_of_modify)

    def click_dataFill_yearplanoffill(self):
        self.click(self.click_dataFill_yearplan_of_fill)

    # 数据管理
    # 周
    def click_overallReport_firePower_weeklyReport(self):
        self.click(self.overallReport_firePower_weeklyReport)

    def click_weeklyReport_jinyuan(self):
        self.click(self.weeklyReport_jinyuan)

    # 月
    def click_overallReport_firePower_monthlyReport(self):
        self.click(self.overallReport_firePower_monthlyReport)

    def click_monthlyReport_coalCheck(self):
        self.click(self.monthlyReport_coalCheck)

    def click_monthlyReport_electralCoalStatic(self):
        self.click(self.monthlyReport_electralCoalStatic)

    def click_monthlyReport_elecGenerateStatic(self):
        self.click(self.monthlyReport_elecGenerateStatic)

    # 综合
    def click_overallReport_firePower_overallReport(self):
        self.click(self.overallReport_firePower_overallReport)

    def click_overallReport_elecGenerateReport(self):
        self.click(self.overallReport_elecGenerateReport)

    def click_overallReport_coalStatGeneralReport(self):
        self.click(self.overallReport_coalStatGeneralReport)

    def click_overallReport_elecCoalGeneralReport(self):
        self.click(self.overallReport_elecCoalGeneralReport)

    def click_overallReport_electGenrateMatrixReport(self):
        self.click(self.overallReport_electGenrateMatrixReport)

    def click_overallReport_nonStopeReport(self):
        self.click(self.overallReport_nonStopeReport)

    def click_overallReport_nonStopeStatisticReport(self):
        self.click(self.overallReport_nonStopeStatisticReport)

    def click_overallReport_openCloseReport(self):
        self.click(self.overallReport_openCloseReport)

    def click_dataManagement(self):
        self.click(self.dataManagement)

    def click_overallReport(self):
        self.click(self.overallReport)

    def click_overallReport_firePower(self):
        self.click(self.overallReport_firePower)

    # 日
    def click_overallReport_firePower_dailyReport(self):
        self.click(self.overallReport_firePower_dailyReport)

    def click_firePower_Daily(self):
        self.click(self.firePower_Daily)

    def click_jinyuanFirePower_daily(self):
        self.click(self.jinyuanFirePower_daily)

    def click_dailyPowerGenerate(self):
        self.click(self.dailyPowerGenerate)

    def click_singleGroupPowerGenerate(self):
        self.click(self.singleGroupPowerGenerate)

    def click_coalStateDaily(self):
        self.click(self.coalStateDaily)

    def click_powerBural_coalStateDaily(self):
        self.click(self.powerBural_coalStateDaily)

    def click_electronic_coalDaily(self):
        self.click(self.electronic_coalDaily)

    def click_firePower(self):
        self.click(self.overallReport_firePower)

    # 水电
    def click_waterPower(self):
        self.click(self.overallReport_waterPower)

    def click_overallReport_waterPower_dailyReport(self):
        self.click(self.overallReport_waterPower_dailyReport)

    def click_overallReport_waterPower_unit(self):
        self.click(self.overallReport_waterPower_unit)

    def click_overallReport_waterPower_powerStation(self):
        self.click(self.overallReport_waterPower_powerStation)

    def click_overallReport_waterPower_situation(self):
        self.click(self.overallReport_waterPower_situation)

    def click_overallReport_waterPower_singleHostReport(self):
        self.click(self.overallReport_waterPower_singleHostReport)

    # 煤矿
    def click_overallReport_coalPower(self):
        self.click(self.overallReport_coalPower)

    def click_overallReport_coalPower_daily(self):
        self.click(self.overallReport_coalPower_daily)

    # 综合产业
    def click_overallReport_overall(self):
        self.click(self.overallReport_overall)

    def click_overallReport_overalld_daily(self):
        self.click(self.overallReport_overalld_daily)

    def click_sunPower(self):
        self.click(self.overallReport_sunPower)

    # self.overallReport_sunPower_daily
    def click_overallReport_sunPower_dailyReport(self):
        self.click(self.overallReport_sunPower_daily)

    def click_coalPower(self):
        self.click(self.dataFill_coalPower)

    def click_overall(self):
        self.click(self.dataFill_overall)

    # 月度指标报表
    def click_monthlyIndex(self):
        self.click(self.monthlyIndex)

        # 值班填报

    def click_dutycopy(self):
        self.click(self.dutycfill)
        self.justWait(10)

    # 值班填报水电抄表
    def click_dutywaterpower(self):
        self.click(self.waterpowerfill)
        self.justWait(10)

    # 值班填报水电
    def click_dutywaterpower(self):
        self.click(self.waterpowerfill)
        self.justWait(30)

    # 值班填报光伏抄表
    def click_sunshinepower(self):
        self.click(self.sunpowerfill)
        self.justWait(10)

    # 值班填报煤矿抄表
    def click_coalpower(self):
        self.click(self.coalfill)
        self.justWait(10)

    # 值班填报火电抄表
    def click_firepowerfill(self):
        self.click(self.firepowerfill)
        self.click(self.DutyFill_firePower)
        self.justWait(10)

    # 值班填报光伏
    def click_sunshinepower(self):
        self.click(self.sunpowerfill)
        self.justWait(10)

    # 值班填报煤矿
    def click_coalpower(self):
        self.click(self.coalfill)
        self.justWait(10)

    # 值班填报水电填报
    def click_dutywater(self):
        self.click(self.waterpower)
        self.justWait(10)

    # 值班填报火电抄表查询
    def click_firepowerfill_search(self):
        self.click(self.firepowerfill)
        self.click(self.DutyFill_firePower_search)
        self.justWait(10)

    # 火电值班查询
    def click_firepowerduty_modify(self):
        self.click(self.firepowerfill)
        self.click(self.Duty_firePower_modify)
        self.justWait(10)

    # 值班填报光伏填报
    def click_dutysunpower(self):
        self.click(self.sunpower)
        self.justWait(10)

    # 实时监视
    def click_monitoring(self):
        self.click(self.monitoring)
        self.justWait(10)

    # 实时监视子菜单
    #综合总览
    def click_comprehensiveOverview(self):
        self.click(self.comprehensiveOverview)
        self.justWait(10)
    #状态总览
    def click_stateOverview(self):
        self.click(self.stateOverview)
        self.justWait(10)

    # 煤矿生产情况
    def click_coalproduction(self):
        self.click(self.coalproduction)
        self.justWait(10)

    # 水泥生产情况
    def click_cementproduction(self):
        self.click(self.cementproduction)
        self.justWait(10)

    # 火电生产情况
    def click_firepowerproduction(self):
        self.click(self.fireproduction)
        self.justWait(10)

    # 光伏生产情况
    def click_sunpowerproduction(self):
        self.click(self.sunproduction)
        self.justWait(10)

    # 水电生产情况
    def click_waterpowerproduction(self):
        self.click(self.waterproduction)
        self.justWait(10)

    # 报警管理

    def click_switcherQuantityAlertConfig(self):
        self.move_to_element(self.switcherQuantityAlertConfig)
        self.click(self.switcherQuantityAlertConfig)
        self.justWait(1)

    def click_dataNotFreshPage(self):
        self.move_to_element(self.dataNotFreshPage)
        self.click(self.dataNotFreshPage)
        self.justWait(1)

    def click_pointDetailPage(self):
        self.move_to_element(self.pointDetailPage)
        self.click(self.pointDetailPage)
        self.justWait(1)

    def click_notFreshTimeConfig(self):
        self.move_to_element(self.notFreshTimeConfig)
        self.click(self.notFreshTimeConfig)
        self.justWait(1)

    def click_alertRecord(self):
        self.move_to_element(self.alertRecord)
        self.click(self.alertRecord)
        self.justWait(1)

    def click_simulateQuantityAlertRecord(self):
        self.move_to_element(self.simulateQuantityAlertRecord)
        self.click(self.simulateQuantityAlertRecord)
        self.justWait(1)

    def click_switcherQuantityAlertRecord(self):
        self.move_to_element(self.switcherQuantityAlertRecord)
        self.click(self.switcherQuantityAlertRecord)
        self.justWait(1)

    def click_alertService(self):
        self.move_to_element(self.alertService)
        self.click(self.alertService)
        self.justWait(1)

    def click_initPoint(self):
        self.move_to_element(self.initPoint)
        self.click(self.initPoint)
        self.justWait(1)

    def click_alertConfig(self):
        self.move_to_element(self.alertConfig)
        self.click(self.alertConfig)
        self.justWait(1)

    def click_doNotFreshAlert(self):
        self.move_to_element(self.doNotFreshAlert)
        self.click(self.doNotFreshAlert)
        self.justWait(1)

    def click_simlateQuantityAlertConfig(self):
        self.move_to_element(self.simlateQuantityAlertConfig)
        self.click(self.simlateQuantityAlertConfig)
        self.justWait(1)

    def click_switcherQuantityAlertConfig(self):
        self.move_to_element(self.switcherQuantityAlertConfig)
        self.click(self.switcherQuantityAlertConfig)
        self.justWait(1)

    def click_simulateQuantityThreaholdConfig(self):
        self.move_to_element(self.simulateQuantityThreaholdConfig)
        self.click(self.simulateQuantityThreaholdConfig)
        self.justWait(1)

    def click_simulateQuantityThreaholdModiy(self):
        self.move_to_element(self.simulateQuantityThreaholdModiy)
        self.click(self.simulateQuantityThreaholdModiy)
        self.justWait(1)

    def click_configMange(self):
        self.move_to_element(self.configManag)
        self.click(self.configManag)
        self.justWait(1)

    def click_metrixConfig(self):
        self.move_to_element(self.metrixConfig)
        self.click(self.metrixConfig)
        self.justWait(1)

    def click_metrixMaintance(self):
        self.move_to_element(self.metrixMaintance)
        self.click(self.metrixMaintance)
        self.justWait(1)

    def click_questionFeedBack(self):
        self.move_to_element(self.questionFeedback)
        self.click(self.questionFeedback)
        self.justWait(1)

    def click_questionList(self):
        self.move_to_element(self.questionList)
        self.click(self.questionList)
        self.justWait(1)

    def click_infoPublish(self):
        self.move_to_element(self.infoPublish)
        self.click(self.infoPublish)
        self.justWait(1)

    def click_groupMaintaince(self):
        self.move_to_element(self.groupMaintaince)
        self.click(self.groupMaintaince)
        self.justWait(1)

    def click_eventMsgPub(self):
        self.move_to_element(self.eventMsgPub)
        self.click(self.eventMsgPub)
        self.justWait(1)

    def click_eventMsgRecord(self):
        self.move_to_element(self.eventMsgRecord)
        self.click(self.eventMsgRecord)
        self.justWait(1)

    def click_eventMsgModify(self):
        self.move_to_element(self.eventMsgModify)
        self.click(self.eventMsgModify)
        self.justWait(1)


class CommConfirmDialogObj(BasePage):
    '''公共类 确认框，等待显示框对象'''

    def __init__(self, *args, **kwargs):
        super(CommConfirmDialogObj, self).__init__(*args, **kwargs)

        # 消息弹出框
        self.popupBox = (By.XPATH, "//div[@type='dialog']")
        # 消息值位置
        self.msg = (By.XPATH, "//div[@type='dialog']/div[2]")
        # 确定按钮
        self.determine = (By.XPATH, "//div[@type='dialog']//a[text()='确定']")
        # 确认按钮
        self.confirm = (By.XPATH, "//div[@type='dialog']//a[text()='确认']")

    # 2次确认，并设置两次确认中，检查点设置
    def submit_confirmCheck2times(self, checkText1, checkText2):
        self.waitUntil(self.confirm, 10)
        self.checkPoint_contain(self.msg, checkText1)
        self.shot("确认框截图")
        self.click(self.confirm)
        self.waitUntil(self.determine, 10)
        self.checkPoint_contain(self.msg, checkText2)
        self.shot("确认框截图")
        self.click(self.determine)

    # 1次确认，并设置两次确认中，检查点设置
    def submit_confirmCheck1times(self, checkText1):
        self.waitUntil(self.popupBox, 10)
        self.checkPoint_contain(self.msg, checkText1)
        self.shot("确认框截图")
        self.click(self.confirm)

    def submit_determineCheck1times(self, checkText1):
        self.waitUntil(self.popupBox, 10)
        self.checkPoint_contain(self.msg, checkText1)
        self.shot("确认框截图")
        self.click(self.determine)

    # 仅点击确认，不设置检查点
    def click_confirmButton(self):
        self.shot("确认框截图")
        self.click(self.confirm)
