from AutoFramework.core.pom import BasePage
import random
import datetime,time

class module_large_screen_display_com(BasePage):
    def __init__(self,*args,**kwargs):
        super(module_large_screen_display_com, self).__init__(*args, **kwargs)

        #菜单元素
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

    # 移除时间控件只读属性和onfocus属性
    # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
    def remove_time_control_readonly(self, label, name, value, attrName):
        for x in attrName:
            js = "$('%s[%s=%s]').removeAttr('%s')" % (label, name, value, x)
            # print(js)
            self.getDriver().execute_script(js)

    #选择指标年份
    def select_index_year(self,index_year_selector):
        now = datetime.datetime.now()
        year = datetime.datetime.strftime(now, "%Y")
        year=int(year)-1
        year=str(year)+"年"
        self.selectByText(index_year_selector,year)

    #输入指标日期
    def select_index_datetime(self,date_selector,day=1):
        now = datetime.datetime.now()
        input_date=now - datetime.timedelta(days=day)
        input_date = datetime.datetime.strftime(input_date, "%Y-%m-%d").strip()
        self.type(input_date,date_selector)

    def switch_to_fram(self,fram_selector):
        #ele=self.find_element(fram_selector)
        self.switchFrame(self.find_element(fram_selector))

    def switch_to_default(self):
        self.switchBackFromIframe()

    def click_operation(self,click_ele):
        self.click(click_ele)

    # 定位到表格元素后，输入数据的公共方法
    def input_values(self, inputs):
        for one in inputs:
            num = random.randint(1, 1000)
            one.clear()
            one.send_keys(num)

    #针对单独元素，输入字符或数字
    def input_index_value(self,text,index_selector):
        self.type(text,index_selector)

    #定位一组表格元素，并逐一在表格中填值
    def input_index_values(self,index_values_selector):
        inputs = self.find_elements(index_values_selector)
        self.input_values(inputs)

    # 获取元素文本
    def get_ele_info(self, selector):
        return self.get_element_text(selector)

    # 判断元素是否存在
    def is_element_exist(self, selector):
        try:
            self.find_element(selector)
            return True
        except:
            return False

    # 判断元素的属性中是否包含xx字符串
    def is_attribute_exist(self, ele_selector, attr_name, attr_value):
        ele = self.find_element(ele_selector)
        if attr_value not in ele.get_attribute(attr_name):
            return True
        else:
            return False

    #选择年份，填写指标的值
    def select_year_to_add_values(self,index_date_selector,index_submit_button,attr_name,attr_value,
                                  index_values_selector_list,type='year'):
        '''
        :param index_date_selector: 指标时间选择器
        :param index_submit_button: 指标提交按钮选择器
        :param attr_name: 提交按钮html元素行中某一属性
        :param attr_value: attr_value中包含的字符串值
        :param index_values_selector_list: 指标值选择器列表
        :param type：时间类型，year为年，day为天
        :return:
        '''
        for i in range(0, 100):
            if type=='year':
                now = datetime.datetime.now()
                year=datetime.datetime.strftime(now, "%Y")
                year=int(year)-1*i
                year='%s年'%str(year)
                self.selectByText(index_date_selector,year)
            elif type=='day':
                now = datetime.datetime.now()
                input_date = now - datetime.timedelta(1+i*1)
                input_date = datetime.datetime.strftime(input_date, "%Y-%m-%d").strip()
                self.type(input_date, index_date_selector)
            else:
                raise Exception("参数type输入错误！")
            time.sleep(1)
            submit_button_useable=self.is_attribute_exist(index_submit_button, attr_name, attr_value)
            if submit_button_useable:
                for x in index_values_selector_list:
                    self.input_index_values(x)
                break
            else:
                continue

    # 选择年份，填写指标的值
    def select_datetime_to_add_values(self, index_year_selector, index_submit_button, attr_name, attr_value,
                                  index_values_selector_list,type='year'):
        '''
        :param index_year_selector: 指标年份选择器
        :param index_submit_button: 指标提交按钮选择器
        :param attr_name: 提交按钮html元素行中某一属性
        :param attr_value: attr_value中包含的字符串值
        :param index_values_selector_list: 指标值选择器列表
        :return:
        '''
        for i in range(0, 100):
            now = datetime.datetime.now()
            year = datetime.datetime.strftime(now, "%Y")
            year = int(year) - 1 * i
            year = '%s年' % str(year)
            self.selectByText(index_year_selector, year)
            time.sleep(1)
            submit_button_useable = self.is_attribute_exist(index_submit_button, attr_name, attr_value)
            if submit_button_useable:
                for x in index_values_selector_list:
                    self.input_index_values(x)
                break
            else:
                continue

    # 随机删除图片
    def delete_picture_random(self, delete_picture_button):
        delete_buttons = self.find_elements(delete_picture_button)
        count = len(delete_buttons)
        if count >= 1:
            l = range(0, count)
            randNum = random.choice(l)
            delete_buttons[randNum].click()
            # print('删除了一张图片！')
        else:
            pass
            # print('没有图片可删除！')

class module_large_screen_display_jy(module_large_screen_display_com):
    '''大屏展示-数据维护-金元'''
    def __init__(self,*args,**kwargs):
        super(module_large_screen_display_jy,self).__init__(*args,**kwargs)

        #金元数据维护
        #利润情况
        self.profit_situation_year=("id","connditionYear") #利润情况选择年份
        self.firePower_profit_values=("xpath",'//*[contains(@id,"hdcondition") and contains(@check,"null")]') #火电利润
        self.waterPower_profit_values = ("xpath", '//*[contains(@id,"sdcondition") and contains(@check,"null")]')  # 水电利润
        self.sunPower_profit_values = ("xpath", '//*[contains(@id,"gfcondition") and contains(@check,"null")]')  # 光伏利润
        self.coal_profit_values = ("xpath", '//*[contains(@id,"mkcondition") and contains(@check,"null")]')  # 煤矿利润
        self.zc_profit_values = ("xpath", '//*[contains(@id,"sncondition") and contains(@check,"null")]')  # 综产利润
        self.profit_submit_button=("id","connditionButton") #利润情况提交、修改按钮

        #-----------------------------------------------------------------
        #eva
        self.eva_year=("id","evaYear") #选择eva年份
        self.eva_1=('id','season1') #第一季度
        self.eva_values=("xpath",'//*[contains(@id,"season")]') #各季度eva
        self.eva_submit_button=("id","evaButton") #eva提交、修改按钮

        # -----------------------------------------------------------------
        #装机容量
        self.capacity_year=("id","capacityYear") #装机容量年份
        self.firePower_capcity=("id","fireElectric") #火电
        self.waterPower_capcity = ("id", "waterElectric")  # 水电
        self.sunPower_capcity=("id","newSource") #光伏
        self.coal_capcity = ("id", "coal")  # 瓦斯
        self.capacity_submit_button=("id","capacityButton") #装机容量提交、修改按钮

        # -----------------------------------------------------------------
        #产业利润
        self.industry_profit_year=("id","profitYear") #产业利润年份
        self.firePower_industry_profit_values=("xpath",'//*[contains(@id,"hdprofit") and contains(@check,"null")]') #火电产业利润
        self.waterPower_industry_profit_values=("xpath", '//*[contains(@id,"sdprofit") and contains(@check,"null")]')# 水电产业利润
        self.sunPower_industry_profit_values=("xpath", '//*[contains(@id,"gfprofit") and contains(@check,"null")]') #新能源产业利润
        self.coal_industry_profit_values=("xpath", '//*[contains(@id,"mkprofit") and contains(@check,"null")]') # 煤矿产业利润
        self.zc_industry_profit_values=("xpath", '//*[contains(@id,"snprofit") and contains(@check,"null")]') #综产产业利润
        self.industry_profit_submit_button=("id","profitButton") #产业利润提交、修改按钮

        # -----------------------------------------------------------------
        #实际资产结构
        self.real_asset_structure_year=("id","actualStuctYear") #实际资产结构年份
        self.firePower_real_asset_values=("xpath",'//*[contains(@id,"hdactual") and contains(@check,"null")]') #火电实际资产
        self.waterPower_real_asset_values=("xpath",'//*[contains(@id,"sdactual") and contains(@check,"null")]') #水电实际资产
        self.sunPower_real_asset_values=("xpath",'//*[contains(@id,"gfactual") and contains(@check,"null")]')  #光伏实际资产
        self.coal_real_asset_values =("xpath",'//*[contains(@id,"mkactual") and contains(@check,"null")]') #煤矿实际资产
        self.zc_real_asset_values =("xpath",'//*[contains(@id,"snactual") and contains(@check,"null")]') #综产实际资产
        self.real_asset_submit_button=("id","actualStuctButton") #实际资产结构提交、修改按钮

        #----------------------------------------------------------------
        #查询
        self.query_info=("xpath",'/html/body/div[2]/div[9]/h1')  #大屏贵州金元数据维护页面

class large_screen_display_map_text(module_large_screen_display_com):
    '''大屏展示-数据维护-地图文字修改'''
    def __init__(self,*args,**kwargs):
        super(large_screen_display_map_text,self).__init__(*args,**kwargs)
        self.jy=("id","jinyuan")  #金元产业发展介绍情况
        self.fire=("id","fire")   #火电产业发展介绍情况
        self.water=("id","water") #水电产业发展介绍情况
        self.gf=("id","light")    #光伏产业发展介绍情况
        self.coal=("id","coal")   #煤矿产业发展介绍情况
        self.modify_button=("id","saveMapInfo") #修改按钮

class large_screen_display_firePower(module_large_screen_display_com):
    '''大屏展示-数据维护-火电'''
    def __init__(self,*args,**kwargs):
        super(large_screen_display_firePower,self).__init__(*args,**kwargs)
       #填报、修改
        self.ifram =('xpath','/html/body/div[4]/iframe')
        self.time_comfirm_button=('id','dpOkInput') #各指标查询日期确定按钮
        #装机容量
        self.capacity_year=('id','capacityYear') #装机容量年份
        self.capacity_values=("xpath","//*[contains(@id,'capacity') and contains(@check,'null')]") #装机容量

        #发电量
        self.fdl_datetime=('id','fdlYear') #发电量日期
        self.fdl_values = ("xpath", "//*[contains(@id,'fdl') and contains(@check,'null')]")   #发电量

        #进煤量
        self.jml_datetime=('id','lmlYear') #发电日期
        self.jml_values = ("xpath", "//*[contains(@id,'lml') and contains(@check,'null')]")   #进煤量

        #存煤量
        self.cml_datetime = ('id', 'cmlYear')  # 发电日期
        self.cml_values=("xpath","//*[contains(@id,'cml') and contains(@check,'null')]")      #存煤量

        #各指标提交按钮
        self.capacity_submit_button=('id','capacityInstallEquipment') #装机容量提交按钮、修改按钮
        self.fdl_submit_button = ('id', 'fdlInstallEquipment')  # 装机容量提交按钮、修改按钮
        self.jml_submit_button = ('id', 'lmlInstallEquipment')  # 装机容量提交按钮、修改按钮
        self.cml_submit_button = ('id', 'cmlInstallEquipment')  # 装机容量提交按钮、修改按钮

        self.industry_introduction=('id','desc')  #产业发展情况介绍
        self.picture_upload=('xpath','//*[@name="file"]') #文件上传按钮
        self.delete_picture_button=('xpath',"//*[@class='pictureOK-li']/a") #图片删除按钮
        self.save_button=('id','save') #保存按钮

        #查询
        self.title=('xpath','/html/body/div[2]/div[9]/h1') #页面标题

class large_screen_display_coal(module_large_screen_display_com):
    '''大屏展示-数据维护-煤矿'''
    def __init__(self,*args,**kwargs):
        super(large_screen_display_coal,self).__init__(*args,**kwargs)

        #填报、修改
        self.industry_introduction = ('id', 'desc')  # 产业发展情况介绍
        self.picture_upload = ('xpath', '//*[@name="file"]')  # 文件上传按钮
        self.delete_picture_button = ('xpath', "//*[@class='pictureOK-li']/a")  # 图片删除按钮
        self.save_button = ('id', 'save')  # 保存按钮

        #查询
        self.title=('xpath','/html/body/div[2]/div[9]/h1') #页面标题











