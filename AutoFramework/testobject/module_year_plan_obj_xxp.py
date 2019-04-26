from AutoFramework.core.pom import BasePage
import random
import datetime
from AutoFramework.utils.configReader import YamlReader, getDriver, DATA_PATH
import os
import time

class module_year_plan_common(BasePage):
    '''光伏年计划'''
    def __init__(self,*args,**kwargs):
        super(module_year_plan_common,self).__init__(*args,**kwargs)
        #菜单元素
        self.data_manage=("xpath","//*[text()='数据管理']")
        self.data_fill=("xpath","//*[text()='数据填报']")
        self.year_plan=("xpath","//*[text()='年计划']")
        self.fill=("xpath",'//*[@id="cssmenu"]/ul/li[2]/ul/li[1]/ul/li[7]/ul/li[1]/a')  #填报
        self.modify=('xpath','//*[@id="cssmenu"]/ul/li[2]/ul/li[1]/ul/li[7]/ul/li[2]/a')#修改
        self.query=('xpath','//*[@id="cssmenu"]/ul/li[2]/ul/li[1]/ul/li[7]/ul/li[3]/a') #查询)
        self.select_year_query_button=('xpath','/html/body/div[2]/div[9]/div[2]/div/div[3]/button') #选择年份旁边的'查询'按钮

        self.select_year=('id','queryTime') #选择年份
        self.query_button=('xpath','/html/body/div[2]/div[9]/div[2]/div/div[3]/button') #查询按钮
        self.sunPower_anual_plan=('xpath','//*[@id="sun"]/a')    #光伏年计划
        self.firePower_anual_plan=("xpath",'//*[@id="hfire"]/a') #火电年计划

    # 菜单操作
    def click_data_manage(self):  #数据管理
        self.click(self.data_manage)
    def click_data_fill(self):    #数据填报
        self.click(self.data_fill)
    def click_year_plan(self):    #年计划
        self.click(self.year_plan)

    #填报
    def click_fill(self):
        self.click(self.fill)
    #修改
    def click_modify(self):
        self.click(self.modify)
    #查询
    def click_query(self):
        self.click(self.query)

    #点击火电年计划
    def click_firePower_anual_plan(self):
        self.click(self.firePower_anual_plan)

    # 移除时间控件只读属性和onfocus属性
    # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
    def remove_time_control_readonly(self, label, name, value, attrName):
        for x in attrName:
            js = "$('%s[%s=%s]').removeAttr('%s')" % (label, name, value, x)
            # print(js)
            self.getDriver().execute_script(js)

    # 输入年份
    # def input_date(self, year=1):
    #     now = datetime.datetime.now()
    #     preDay = now - datetime.timedelta(days=day)
    #     self.type(datetime.datetime.strftime(preDay, "%Y"), self.select_year)

    #输入年份
    def input_date(self, year=2018):
        self.type(year, self.select_year)

    # 选择年份后，点击查询按钮
    def click_year_query_button(self):
        self.click(self.select_year_query_button)

    # 选择上传文件
    def select_upload_file(self,file_name,select_upload_file_ele,import_button_ele,close_button_ele):
        '''select_upload_file_ele --选择上传文件的元素
           import_button_ele--导入按钮元素
           close_button_ele--关闭按钮元素'''
        file_path = os.path.join(DATA_PATH, file_name)
        if os.path.exists(file_path):
            self.upload_file(select_upload_file_ele, file_path)  # 选择上传文件
            self.click(import_button_ele)  # 选择上传文件后点击"导入"按钮
            self.click(close_button_ele)  # 导入数据后关闭上传文件的弹窗


   #判断元素是否存在
    def is_element_exist(self, selector):
        try:
            self.find_element(selector)
            return True
        except:
            return False

    #将右侧滚动条拉到最下方
    def drop_scroll_bar(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.getDriver().execute_script(js)

class module_year_plan_sunPoewr(module_year_plan_common):
    '''光伏年计划'''
    def __init__(self, *args, **kwargs):
        super(module_year_plan_sunPoewr, self).__init__(*args, **kwargs)
        #填报-------------------------------------------------------
        #5个指标公有的：点击导入按钮后，选择文件的元素、导入元素、关闭元素定位
        self.select_upload_file_button = ('id', 'filealarm')  # 选择上传文件
        self.upload_import_button = ('xpath', '/html/body/div[2]/div[10]/div[2]/button[1]')  # 上传文件导入按钮
        self.upload_close_button = ('xpath', '/html/body/div[2]/div[10]/div[2]/button[2]')  # 上传文件导入关闭按钮

        #发电量
        self.fdl_import_button=('id','sunfdlimport') #导入按钮
        self.fdl_save_button=('id','sunfdlsave')     #保存按钮
        self.fdl_submit_button=('id','sunfdlcommit') #提交按钮

        #发电量奋斗目标
        self.fdlf_import_button=("id","sunfdlfimport")     #导入按钮
        self.fdlf_save_button = ('id', 'sunfdlfsave')      # 保存按钮
        self.fdlf_submit_button = ('id', 'sunfdlfcommit')  # 提交按钮

        # 综合厂用电率
        self.zhcydl_import_button = ("id", "sunzhcydlimport")  # 导入按钮
        self.zhcydl_save_button = ('id', 'sunzhcydlsave')     # 保存按钮
        self.zhcydl_submit_button = ('id', 'sunzhcydlcommit')  # 提交按钮

        #售电量
        self.sdl_import_button = ("id", "sunsdlimport")  # 导入按钮
        self.sdl_save_button = ('id', 'sunsdlsave')     # 保存按钮
        self.sdl_submit_button = ('id', 'sunsdlcommit')  # 提交按钮

        # 利用小时
        self.lyxs_import_button = ("id", "sunlyxhimport")  # 导入按钮
        self.lyxs_save_button = ('id', 'sunlyxhsave')     # 保存按钮
        self.lyxs_submit_button = ('id','sunlyxhcommit')   # 提交按钮

        #修改---------------------------------------------
        #发电量
        self.fdl_modify_button=("id","sunfdlupdate") #修改按钮
        self.fdl_gzjy_1_month=('xpath','//*[@id="sunplanfdlbody"]/tr[1]/td[3]/div/input') #贵州金元1月的值
        self.fdl_xbl_12_month=('xpath','//*[@id="sunplanfdlbody"]/tr[10]/td[14]/div/input') #象鼻岭光伏12月的值

        #发电量奋斗目标
        self.fdlf_gzjy_1_month=('xpath','//*[@id="sunplanfdlfbody"]/tr[1]/td[3]/div/input')#贵州金元1月的值
        self.fdlf_xbl_12_month=('xpath','//*[@id="sunplanfdlfbody"]/tr[9]/td[14]/div/input') #象鼻岭能源12月的值
        self.fdlf_modify_button=('id','sunfdlfupdate') #修改按钮

        #综合厂用电率
        self.zhcydl_gzjy_1_month=('xpath','//*[@id="sunplanzhcydlbody"]/tr[1]/td[3]/div/input')#贵州金元1月
        self.zhcydl_zlz_12_month=('xpath','//*[@id="sunplanzhcydlbody"]/tr[7]/td[14]/div/input')#中梁子12月
        self.zhcydl_modify_button=('id','sunzhcydlupdate') #修改按钮

        #售电量
        self.sdl_wn_1_month=('xpath','//*[@id="sunplansdlbody"]/tr[3]/td[3]/div/input') #威宁1月
        self.sdl_pj_12_month=('xpath','//*[@id="sunplansdlbody"]/tr[4]/td[14]/div/input') #平津12月
        self.sdl_modify_button=('id','sunsdlupdate')

        #l利用小时
        self.lyxs_sj_1_month=('xpath','//*[@id="sunplanlyxhbody"]/tr[2]/td[3]/div/input')#洒金1月
        self.lyxs_jhf_12_month=('xpath','//*[@id="sunplanlyxhbody"]/tr[8]/td[14]/div/input') #金海湖12月
        self.lyxs_modify_button=('id','sunlyxhupdate') #修改按钮

        #查询---------------------------------------------------
        self.fdl=('xpath','//*[@id="sun"]/div/div[1]/h2') #发电量的标题
        self.lyxs=('xpath','//*[@id="sun"]/div/div[5]/h2') #利用小时的标题


    #发电量指标填报--------------------------------
    #点击导入按钮
    def click_fdl_import_button(self):
        self.click(self.fdl_import_button)
    #点击保存按钮
    def click_fdl_save_button(self):
        self.click(self.fdl_save_button)
    #点击提交按钮
    def click_fdl_submit_button(self):
        self.click(self.fdl_submit_button)
    #选择上传文件
    def fdl_select_upload_file(self):
        file_name='planYear_sunpower.xlsx'
        self.select_upload_file(file_name,self.select_upload_file_button,self.upload_import_button,self.upload_close_button)

    #各指标填报界面公有的方法----------------------------
    #点击导入按钮
    def click_import_button(self,import_ele):
        self.click(import_ele)
    # 点击保存按钮
    def click_save_button(self,save_ele):
        self.click(save_ele)
    # 点击提交按钮
    def click_submit_button(self,submit_ele):
        self.click(submit_ele)

    #选择年份后对各指标上传文件-------------------------------------
    def select_year_to_import_file(self,submit_button,import_button,file_name,select_upload_file_button,
                                   upload_import_button,upload_close_button):
        '''
        :param submit_button: 提交按钮
        :param import_button: 导入按钮
        :param file_name:上传的文件名
        :param select_upload_file_button: 选择上传文件
        :param upload_import_button: 点击窗口的导入按钮
        :param upload_close_button: 点击窗口的关闭按钮
        :return:
        '''
        for i in range(0, 50):
            now = datetime.datetime.now()
            year=datetime.datetime.strftime(now, "%Y")
            self.input_date(int(year) - 1 * i)
            self.click_year_query_button()
            # if not self.is_element_exist(submit_button):
            #     self.drop_scroll_bar()
            time.sleep(1)
            if self.is_element_exist(submit_button):
                self.click_import_button(import_button)  # 点击导入按钮
                # file_name = 'planYear_sunpower.xlsx'
                self.select_upload_file(file_name, select_upload_file_button,upload_import_button,upload_close_button)  # 上传发电量附件
                break
            else:
                continue

    # 选择年份后对各指标上传文件,针对下半页面指标的上传---------------------------------
    def select_year_to_import_file_s(self, submit_button, import_button, file_name,select_upload_file_button,
                                   upload_import_button, upload_close_button):
        '''
        :param submit_button: 提交按钮
        :param import_button: 导入按钮
        :param select_upload_file_button: 选择上传文件
        :param upload_import_button: 点击窗口的导入按钮
        :param upload_close_button: 点击窗口的关闭按钮
        :return:
        '''
        for i in range(0, 50):
            now = datetime.datetime.now()
            year = datetime.datetime.strftime(now, "%Y")
            self.input_date(int(year) - 1 * i)
            self.click_year_query_button()
            if not self.is_element_exist(submit_button):
                self.drop_scroll_bar()
            time.sleep(1)
            if self.is_element_exist(submit_button):
                #print('find submit button')
                self.click_import_button(import_button)  # 点击导入按钮
                #print('click import button')
                # file_name = 'planYear_sunpower.xlsx'
                self.select_upload_file(file_name, select_upload_file_button, upload_import_button,
                                        upload_close_button)  # 上传发电量附件
                break
            else:
                #print('not find submit button')
                continue

    #修改页的操作--------------------------------------
    #修改值
    def input_value(self,modify_ele):
        randNum=random.randint(1,100)
        self.type(randNum,modify_ele)
    #点击修改按钮
    def click_modify_button(self,modify_button_ele):
        #print(str(modify_button_ele))
        self.click(modify_button_ele)

    #查询页操作
    def get_index_title_info(self,query_index_title):
        return self.get_element_text(query_index_title)

class module_year_plan_firePoewr(module_year_plan_sunPoewr):
    '''火电年计划'''
    def __init__(self, *args, **kwargs):
        super(module_year_plan_firePoewr, self).__init__(*args, **kwargs)
        #填报-------------------------------------------------------
        # 7个指标公有的：点击导入按钮后，选择文件的元素、导入元素、关闭元素定位
        # self.select_upload_file_button = ('id', 'filealarm')  # 选择上传文件
        # self.upload_import_button = ('xpath', '/html/body/div[2]/div[10]/div[2]/button[1]')  # 上传文件导入按钮
        # self.upload_close_button = ('xpath', '/html/body/div[2]/div[10]/div[2]/button[2]')  # 上传文件导入关闭按钮

        #发电量
        self.fdl_import_button=("id","hfirefdlimport")  #导入按钮
        self.fdl_save_button=("id","hfirefdlsave")      #保存按钮
        self.fdl_submit_button=("id","hfirefdlcommit")  #提交按钮

        #发电量奋斗目标
        self.fdlf_import_button = ("id", "hfirefdlfimport")  # 导入按钮
        self.fdlf_save_button = ("id", "hfirefdlfsave")      # 保存按钮
        self.fdlf_submit_button = ("id", "hfirefdlfcommit")  # 提交按钮

        #上网电量
        self.swdl_import_button = ("id", "hfiresdlimport")  # 导入按钮
        self.swdl_save_button = ("id", "hfiresdlsave")      # 保存按钮
        self.swdl_submit_button = ("id", "hfiresdlcommit")  # 提交按钮

        # 综合厂用电率
        self.zhcydl_import_button = ("id", "hfirezhcydlimport")  # 导入按钮
        self.zhcydl_save_button = ("id", "hfirezhcydlsave")      # 保存按钮
        self.zhcydl_submit_button = ("id", "hfirezhcydlcommit")  # 提交按钮

        # 售热量
        self.srl_import_button = ("id", "hfiresrlimport")  # 导入按钮
        self.srl_save_button = ("id", "hfiresrlsave")      # 保存按钮
        self.srl_submit_button = ("id", "hfiresrlcommit")  # 提交按钮

        # 供电标煤耗
        self.gdbmh_import_button = ("id", "hfiregdbmhimport")  # 导入按钮
        self.gdbmh_save_button = ("id", "hfiregdbmhsave")      # 保存按钮
        self.gdbmh_submit_button = ("id", "hfiregdbmhcommit")  # 提交按钮

        # 利用小时
        self.lyxs_import_button = ("id", "hfirelyxhimport")  # 导入按钮
        self.lyxs_save_button = ("id", "hfirelyxhsave")      # 保存按钮
        self.lyxs_submit_button = ("id", "hfirelyxhcommit")  # 提交按钮

        #修改-----------------------------------------------
        #发电量
        self.fdl_modify_button=('id','hfirefdlupdate')  #修改按钮
        self.fdl_jy_1_month=('xpath','//*[@id="hfireplanfdlbody"]/tr[1]/td[3]/div/input')   #金元1月的值
        self.fdl_ny_12_month=('xpath','//*[@id="hfireplanfdlbody"]/tr[2]/td[14]/div/input') #纳雍12月的值

        #发电量奋斗目标
        self.fdlf_modify_button=('id','hfirefdlfupdate') #修改按钮
        self.fdlf_jy_1_month = ('xpath', '//*[@id="hfireplanfdlfbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.fdlf_qx_12_month=('xpath','//*[@id="hfireplanfdlfbody"]/tr[3]/td[14]/div/input')  #黔西电厂12月的值

        #上网电量
        self.swdl_modify_button=('id','hfirewsdlupdate') #修改按钮
        self.swdl_jy_1_month = ('xpath', '//*[@id="hfireplanswdlbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.swdl_qx4_12_month = ('xpath', '//*[@id="hfireplanswdlbody"]/tr[4]/td[14]/div/input')  # 黔西#4 12月的值

        #综合厂用电率
        self.zhcydl_modify_button=('id','hfirezhcydlupdate') #修改按钮
        self.zhcydl_jy_1_month = ('xpath', '//*[@id="hfireplanzhcydlbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.zhcydl_qx5_12_month = ('xpath', '//*[@id="hfireplanswdlbody"]/tr[5]/td[14]/div/input')  # 黔西#5 12月的值

        # 售热量
        #self.srl_modify_button = ('id', 'hfiresrlupdate')  # 修改按钮
        self.srl_modify_button = ('xpath', '//*[@id="hfiresrlupdate"]')  # 修改按钮
        self.srl_jy_1_month = ('xpath', '//*[@id="hfireplansrlbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.srl_qb_12_month = ('xpath', '//*[@id="hfireplansrlbody"]/tr[6]/td[14]/div/input')  # 黔北 12月的值

        # 供电标煤耗
        self.gdbmh_modify_button = ('id', 'hfiregdbmhupdate')  # 修改按钮
        self.gdbmh_jy_1_month = ('xpath', '//*[@id="hfireplangdbmhbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.gdbmh_xs_12_month = ('xpath', '//*[@id="hfireplangdbmhbody"]/tr[7]/td[14]/div/input') # 习水 12月的值

        # 利用小时
        self.lyxs_modify_button = ('id', 'hfirelyxhupdate')  # 修改按钮
        self.lyxs_jy_1_month = ('xpath', '//*[@id="hfireplanlyxhbody"]/tr[1]/td[3]/div/input')  # 金元1月的值
        self.lyxs_yx_12_month = ('xpath', '//*[@id="hfireplanlyxhbody"]/tr[8]/td[14]/div/input')  #鸭溪 12月的值

        #查询-----------------------------------
        self.fdl=('xpath','//*[@id="addHfdlPlanForm"]/table/thead/tr[1]/th[2]/div')   #发电量标题
        self.lyxs=('xpath','//*[@id="addHlyxhPlanForm"]/table/thead/tr[1]/th[2]/div') #利用小时标题


       
