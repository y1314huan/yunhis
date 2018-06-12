# coding:utf-8
#1、挂号接诊、查看收费明细。2、结束就诊医生完善病例。3、检验工作台。4、检查工作
#台。5、治疗。6、患者管理的查询功能。7、修改基础信息。8、病史信息修改，体检信息修改、添加患者、患
#者的禁用/启用。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
from commonshare.his_common import His
from commonshare.his_common import browser

p = His()
today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
print (today.strftime('%Y-%m-%d'))
print (n_days.strftime('%Y-%m-%d'))


class TestHis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        p.setUp()
    @classmethod
    def tearDownClass(cls):
        p.tearDown()
    #登录
    def test001(self):
        p.login()
    #预约挂号
    def test002(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/div[3]/aside/section/ul/li[2]/ul/li[1]/a')).click()  # 点击预约挂号
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="registerName_input"]')).send_keys(u"董焕焕")#输入姓名
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="appointment_nav"]/ul')).click()  # 点击空白处
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="telephonNum"]')).send_keys("18611059298")#输入手机号
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="sexWoman"]')).click()#选择女
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="registAgeInput"]')).send_keys(25)#输入年龄
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-costTypeName-container"]')).click()#点击费别处的请选择
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"VIP")#在费别处输入VIP
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择VIP
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="atureFlage"]')).click()#勾选保险支付
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-InsureCompanyList-container"]')).click()#点击保险信息处的请选择
        time.sleep(1)
        WebDriverWait(browser, 10).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"兴业银行")#输入兴业银行
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)  # 选择兴业银行
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="registInsureNum"]')).send_keys(123456)#输入保险号
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="appointment_nav"]/ul')).click()  # 点击空白处
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="register_deductible"]')).send_keys(u"99.99")#输入自付款
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="register_CoInsurance"]')).send_keys(u"0.87654321")#输入自付比例
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="register_copayment"]')).send_keys(u'0.88')#输入定额手续费
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="register_insure_remark"]')).send_keys(u"每年最高报销100万")#输入备注
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-zhenfee_select-container"]')).click()#点击诊费处的请选择
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"常规诊费")#输入常规诊费
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择常规诊费
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="appointment_nav"]/ul')).click()  # 点击空白处
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-Order_startTime-container"]')).click()#点击就诊时间的开始时间
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"8:00")#就诊时间的开始时间输入9:00
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#就诊时间的开始时间选择9:00
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-Order_endTime-container"]')).click()#点击结束时间
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"8:30")#在结束时间输入10:00
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择10:00
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="1002"]')).click()#就诊事项选择打针
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="1004"]')).click()  # 就诊事项选择取药
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="1006"]')).click()  # 就诊事项选择推拿
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="itemsNose"]')).send_keys(u"青霉素过敏")#备注处输入青霉素过敏
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="pationtDtailBtn"]/small')).click()#患者详细信息处点击展开
        target = WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="addressDetail"]'))
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到地址处
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="medicareCardNum"]')).send_keys(123456)
        time.sleep(1)
        s1 = Select(WebDriverWait(browser, 30).until(lambda x: x.find_element("id", "credentialType")))#下拉框的选择
        s1.select_by_index("1")#下拉框的选择军官证
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="credentialTypeNum"]')).send_keys(1234567890)#输入军官证号
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-country-container"]')).click()#点击民族处的国籍
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"中国")#在国籍处输入中国
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择中国
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-national-container"]')).click()#点击民族
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"维吾尔族")#输入维吾尔族
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择维吾尔族
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="maritalStatus"]')).click()#点击婚姻状态处的请选择
        time.sleep(1)
        t1 = Select(WebDriverWait(browser, 30).until(lambda x: x.find_element("id", "maritalStatus")))   # 下拉框的选择
        t1.select_by_index("1")  # 下拉框的选择已婚
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="work"]')).send_keys(u"测试工程师")#输入职业
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="companyName"]')).send_keys(u"泓华国际医疗控股有限公司")#输入工作单位
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-province-container"]')).click()#选择住址处的省
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"北京")#
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-city-container"]')).click()#选择住址处的市
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"北京市")#
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="select2-district-container"]')).click()#选择住址处的区
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(u"朝阳区")#
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="addressDetail"]')).send_keys(u"北辰东路北辰汇宾大厦B座19层")#填写详细地址
        target = WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="weight"]'))# 滑动到体重处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到体重处
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="temperature"]')).send_keys(37)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="heartRateNow"]')).send_keys(70)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="breatheNow"]')).send_keys(80)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="pulseRateNow"]')).send_keys(90)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="BP_hight"]')).send_keys(120)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="BP_low"]')).send_keys(90)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="height"]')).send_keys(160)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="weight"]')).send_keys(60)
        target = WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="historyShowBtn"]'))#滑动到病史信息
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="historyShowBtn"]/small')).click()#点击病史信息处的展开
        time.sleep(1)
        target = WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="allergiesHistory"]')) # 滑动到过敏史处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到过敏史处
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="historyOfPresentIllness"]')).send_keys(u"偏头痛")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="personalHistory"]')).send_keys(u"失眠、多梦")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="allergiesHistory"]')).send_keys(u"青霉素过敏")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="pastHistory"]')).send_keys(u"失眠、多梦")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="familyHistory"]')).send_keys(u"近视眼")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="addRegister_save"]')).click()#点击保存
        print ("预约挂号成功")

 # 接诊
    def test003(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/div[3]/aside/section/ul/li[2]/ul/li[2]/a')).click()# 点击医生工作台
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]')).click()# 点击接诊
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="chielfComplaint"]')).send_keys(u"感冒、发烧、咳嗽、嗓子疼")  # 输入主诉
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="saveForCommonMedicalRecord"]/a')).click()#点击存为常用病例
        browser.current_window_handle # 此行代码用来定位当前页面
        time.sleep(5)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="layui-layer11"]/div[2]/div/ul/li[1]/input')).send_keys(u"感冒")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="saveHisTem"]')).click()#在病例名称弹窗处点击保存
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="doctorAdvice"]')).send_keys(u"多喝水，好好休息")#填写处理意见
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath",'//*[@id="saveForCommondoctorAdvice"]/a')).click()  #点击存为存为常用处理意见
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath( '//*[@id="layui-layer14"]/div[2]/div/ul/li[1]/input')).clear()#清除输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath( '//*[@id="layui-layer14"]/div[2]/div/ul/li[1]/input')).send_keys(u"处理意见模板保存")#填写处理意见名称
        WebDriverWait(browser, 30).until(lambda x: x.find_element("id", "saveDocterSeeTem")).click()#点击处理意见弹窗中的保存
        print ("填写病例成功")

    # 接诊界面填写检验项目
    def test004(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a')).click()#点击检验项目
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]')).click()  # 点击检验项目处的请选择
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"过敏原检测(食物组)")  #输入过敏原检测(食物组)
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择过敏原检测(食物组)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]')).click()  # 点击检验项目处的请选择
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"ABO血型")  #输入ABO血型
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择ABO血型
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_save"]')).click()  # 点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_presprint"]')).click()#点击打印
        time.sleep(1)
        browser.back()#点击返回
        print ("填写检验项目成功")


    # 接诊界面填写检查项目
    def test005(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a')).click()## 点击检查项目
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="checkoutBox"]/div[1]/div/span[2]/span[1]/span')).click()  # 点击检查项目处的请选择
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"多普勒听胎心")#输入多普勒听胎心
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择多普勒听胎心
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]')).click()  # 点击检查项目处的请选择
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"泌尿系超声")#输入泌尿系超声
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)#选择泌尿系超声
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="saveCheckoutItems"]')).click()  # 点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="checkoutPresprint"]')).click()  #点击打印
        time.sleep(1)
        browser.back()#浏览器返回
        print ("填写检查项目成功")
    # 接诊界面填写治疗项目
    def test006(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a')).click()  # 点击治疗
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherFee"]')).send_keys(u"隔物灸法")  # 输入治疗项目"隔物灸法"
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]')).click()  # 选择某项治疗"隔物灸法"
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="selectedInspectListBox"]/form/div/div[3]/input')).clear()  # 清除治疗项目"隔物灸法"的频次输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="selectedInspectListBox"]/form/div/div[3]/input')).send_keys(10)  # 输入治疗项目"隔物灸法"的频次为10次
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherFee"]')).send_keys(u"颈椎正骨治疗")  # 输入治疗项目"颈椎正骨治疗"
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]')).click()  # 选择某项治疗"颈椎正骨治疗
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_save"]')).click()  #点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_presprint"]')).click()  #点击打印
        time.sleep(1)
        browser.back()
        print ("填写治疗项目成功")

    # 接诊界面填写西药
    def test007(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a')).click()  # 点击西药处方
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadicine"]')).send_keys(u"阿奇霉素注射液")  # 在处方药品处输入阿
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p')).click()  # 选择阿奇霉素注射液
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadicine"]')).send_keys(u"硫酸庆大霉素注射液")  # 在处方药品处输入硫酸庆大霉素注射液
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]')).click()  # 硫酸庆大霉素注射液
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="saveForComenPres"]')).click()#点击存为常用处方
        time.sleep(1)
        browser.current_window_handle#获取当前界面
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="saveConPresName"]')).send_keys(u"感冒、发烧")#输入处方模板的名称
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="presSave"]')).click()  #保存处方模板
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input')).send_keys(u"一次性换药包")#输入耗材一次性换药包
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]')).click()#选择耗材一次性换药包
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div/div/div/span/input')).clear()#清除耗材的数量
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div/div/div/span/input')).send_keys(2)#填写好猜的数量为2
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input')).send_keys(u"一次性纱布块")#输入耗材一次性纱布块
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]')).click()  #选择一次性纱布块
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select')).click()  # 点击诊费输入框
        time.sleep(1)
        InputType = Select(WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select')))
        InputType.select_by_value("10001000012")#诊费由常规诊费   ￥500改成急诊诊费   ￥1000
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("#addOtherFee")).send_keys(u"代煎费")  # 其他费用
        time.sleep(3)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("#addOtherRelateList > p > span.name.name-text")).click()  # 选择代煎费
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("#prescription_save")).click()  # 点击处方处的保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescription_print"]')).click()#点击打印
        time.sleep(1)
        browser.back()
        time.sleep(1)
        print ("填写西药处方成功")

    # 接诊界面填写中草药
    def test008(self):#填写草药处方
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("#seeDoctoring_nav > ul > li.herbal-pres > a")).click()  # 点击草药处方
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"荆芥")  # 在草药输入框中输入“荆芥”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择荆芥
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“荆芥”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"防风")  # 在草药输入框中输入“防风”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择防风
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“防风”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"羌活")  # 在草药输入框中输入“羌活”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择羌活
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“羌活”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"独活")  # 在草药输入框中输入“独活”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择独活
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“独活”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"川芎")  # 在草药输入框中输入“川芎”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择川芎
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“川芎”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"醋北柴胡")  # 在草药输入框中输入“醋北柴胡”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择醋北柴胡
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“醋北柴胡”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"前胡")  # 在草药输入框中输入“前胡”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择前胡
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“前胡”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"桔梗")  # 在草药输入框中输入“桔梗”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择桔梗
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“桔梗”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"麸炒枳壳")  # 在草药输入框中输入“麸炒枳壳”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择麸炒枳壳
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“麸炒枳壳”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"土茯苓")  # 在草药输入框中输入“土茯苓”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择土茯苓
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(30)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“土茯苓”30g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"炙甘草")  # 在草药输入框中输入“炙甘草”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  # 选择炙甘草
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  # 清除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(15)  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  # 添加草药“炙甘草”15g
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input')).send_keys(6)#剂数填写6剂
        target = WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea'))#滑动到处方输入框
        browser.execute_script("arguments[0].scrollIntoView();", target)#滑动到处方输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea')).send_keys(u"饭后服用，每天2次。")
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("p.save-for-prescription-templat")).click()#点击存为常用处方
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("li > input[type=\"text\"]")).clear()#清除处方模板输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector("li > input[type=\"text\"]")).send_keys(u"草药模板")#输入处方模板名称
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="presTanchuang"]/ul/li[3]/button')).click()#在处方模板名称弹窗中点击保存
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalPres_save"]')).click()#点击保存
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="contaleBtn"]/button[3]')).click()#点击打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_id("lookDetail")).click()#点击查看收费明细
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_class_name("layui-layer-setwin")).click()#关闭收费明细



    # 结束就诊、完善病例
    def test009(self):
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="ajax-content"]/div[1]/div[2]/p[2]/a')).click()#点击结束就诊
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="offMadicalMess"]/div/a/button')).click()#点击是
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="patient_state_tab"]/li[3]')).click()  #点击已完成
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/a[2]')).click()  #点击完善病例
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="chielfComplaint"]')).send_keys(u"完善病例")  #修改主诉
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="doctorAdvice"]')).send_keys(u"完善病例")  #修改处理意见
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a')).click()#点击检验项目
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspece_reportList_content"]/div[2]/div[1]/div/div/img')).click()  #删除检验项目
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]')).click()  #点击添加检验项目
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"抗缪勒试管激素")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[2]')).click()  #选择“抗缪勒试管激素”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_save"]')).click()  #点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_presprint"]')).click()  #点击打印
        time.sleep(1)
        browser.back()
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a')).click()  #点击检查项目
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="checkoutReportBox"]/div[1]/div[1]/div/img')).click()  #点击删除
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]')).click()  #点击检查项目
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(u"经颅多普勒超声 ¥1500")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('/html/body/span/span/span[1]/input')).send_keys(Keys.ENTER)  #选择经颅多普勒超声 ¥1500
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="saveCheckoutItems"]')).click()  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="checkoutPresprint"]')).click()  #点击打印
        time.sleep(1)
        browser.back()  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a')).click()  #点击治疗
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspece_reportList_content"]/form[1]/div/div[7]/p/img')).click()  #点击删除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherFee"]')).send_keys(u"无痛麻醉费")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]')).click()  #选择“无痛麻醉费”
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_save"]')).click()  #点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="inspect_presprint"]')).click()  #点击打印
        time.sleep(2)
        browser.back()  #
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a')).click()  #点击处方
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="madicineList_content"]/form[2]/div/img')).click()  #删除药品
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadicine"]')).send_keys(u"达克宁")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]')).click()  #选择硝酸咪康唑阴道软胶囊
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div[2]/div/img')).click()  #删除耗材
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input')).send_keys(u"碘伏棉签")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]')).click()  #选择碘伏棉签
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select')).click()  #点击诊费
        InputType = Select(WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select')))
        InputType.select_by_value("10001000011")  # 诊费由急诊诊费   ￥1000改成复诊诊费
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="otherFeeContent"]/form/img')).click()  #删除其他费用
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherFee"]')).send_keys(u"中药费")  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]')).click()  #选择"中药费	"
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescription_save"]')).click()  #点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="prescription_print"]')).click()  #点击打印
        time.sleep(1)
        browser.back()  #
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[6]/a')).click()  #点击草药处方
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[1]/ul/li[11]')).click()  #点击炙甘草
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[1]/ul/li[11]/span[4]')).click()  #点击删除
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input')).send_keys(u"黄芩")  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]')).click()  #选择黄芩
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).clear()  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input')).send_keys(u"20")  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img')).click()  #点击新增
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input')).clear()  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input')).send_keys(u"10")  #改成10剂
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalKind_01"]')).click()  #选择外敷
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea')).send_keys(u"修改备注")  #
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="herbalPres_save"]')).click()  #点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="contaleBtn"]/button[3]')).click()  #点击打印
        time.sleep(1)
        browser.back()  #
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="lookDetail"]')).click()  # 点击查看收费明细
        time.sleep(1)
        browser.current_window_handle
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="layui-layer5"]/span[1]/a')).click()  #点击关闭
        time.sleep(1)






    # 检验工作台
    def test010(self):  # 检验工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="Jiu_Zhen"]/li[3]/a').click()  # 点击检验工作台
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="inspect_patient_content"]/div[1]/div[2]/a').click()  # 点击开始检验
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspectSavePrint"]').click()  # 点击保存与打印
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspectSystm_patientCart_tab"]/li[3]/span[2]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_patient_content"]/div[1]/div[2]/a').click()  # 点击查看
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="againPrint"]').click()  # 点击打印报告
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)

    # 治疗工作台
    def test011(self):
        browser.find_element_by_xpath('//*[@id="Jiu_Zhen"]/li[6]/a').click()  # 点击治疗
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()#点击开始治疗
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/span')))  #
        ys.click()  # #点击执行
        time.sleep(3)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_link_text(u"确认").click()#点击确定
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="treatPrint"]').click()  # 点击查看并打印
        time.sleep(2)
        browser.back()
        time.sleep(2)


    # 检查工作台
    def test012(self):  # 检查工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="Jiu_Zhen"]/li[4]/a').click()# 点击检查工作台
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()  # 点击开始检查
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="chDes"]').send_keys(u"头疼、发烧、咳嗽、眩晕")  # 输入描述信息
        browser.find_element_by_xpath('//*[@id="chResult"]').send_keys(u"感冒")  # 输入结论
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutSavePrint"]').click()  # 点击保存与打印
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inSaveYes"]').click()  # 点击继续
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patientCart_tab"]/li[3]/span[2]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div/div[2]/a').click()  # 点击查看
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkAgainPrint"]').click()  # 点击打印报告
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)


# 患者管理
    def test013(self):  # 患者管理
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[3]/a').click()#点击患者管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').send_keys(u"董焕焕")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchP"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').clear()  #清除输入框
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').send_keys(u"18611059298")  #输入手机号
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchP"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').clear()  #清除输入框
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').send_keys(u"190001768")  #输入病历号
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchP"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="str_info"]').clear()  #清除输入框
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="searchP"]').click()  #点击查询
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="data-search"]/div/div/div[3]/div[1]/div/a/span').click()  #点击查看健康档案
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div/div[1]/section/div[1]/h3/u').click()  #基础信息点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="sexinput1"]').click()  #性别改为男
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="idcard_proving"]').clear()  #身份证号清空
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="btn_one"]').click()  #点击保存
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="bottom_ziliao1"]/p')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #滑动到体检信息
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="xiu"]').click()  #病史信息处点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form3"]/ul/li[1]/p').send_keys(u"、失眠")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="btn_two"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div/div[1]/section/div[5]/h3/u').click()  #体检信息点击修改
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form4"]/ul/li[1]/p[2]/input').clear()  #清除体重
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form4"]/ul/li[1]/p[2]/input').send_keys(u"50")  #
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="btn_three"]')  #滑动到保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="clinic_patient"]/ul/li[2]/a').click()  #点击就诊记录
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/section/div[1]/p/a[1]').click()  #点击展开
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/section/div[1]/p/a[1]').click()  #点击收起
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="clinic_patient"]/ul/li[3]/a').click()  #点击预约信息
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/table/tbody/tr/td[5]/span').click()  #点击查看详情
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer9"]/span[1]/a')))  #
        ys.click()  #点击关闭
        time.sleep(2)


        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[3]/a/span[1]').click()  #点击患者管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="data-search"]/div/div/div[2]/form/div[6]').click()  #点击患添加
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"添加患者")  # 输入患者姓名
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="check_form"]/ul/li[5]/span').click()  # 点击患者情况
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="check_form"]/ul/li[2]/input').send_keys(u"18611059298")  # 输入手机号
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="sexW"]').click()  # 选择女
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ages"]').send_keys(u"25")  # 点击年龄输入25岁
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="check_form"]/ul/li[5]/textarea').send_keys(u"感冒、发烧") #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="keepCheckBtn"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="data-search"]/div/div/div[3]/div[1]/div/a/span').click()  #点击查看健康档案
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/i').click()  #点击禁用
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'forbidden_ok')))  #
        ys.click()  ##点击确定
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/i').click()  # 点击启用
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'forbidden_ok')))  #
        ys.click()  ##点击确定
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="gobackTo"]/i').click()  #点击返回
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()