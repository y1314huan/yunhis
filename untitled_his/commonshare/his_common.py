# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()  # chromedriver.exe文件的路径


class His():
    def setUp(self):
        global browser
        browser.maximize_window()
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        # # ## 测试地址
        # browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # 准正式地址

        print ("setUp")
    def tearDown(self):
        # browser.quit()
        print ("TearDown")
    #登录
    def login(self):

        global browser
        u"""这里写了一个登陆的方法，账号和密码参数化"""
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="username"]')).send_keys("17444444444")  # 输入用户名
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="password"]')).clear()  # 清空密码输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="password"]')).send_keys("444444")  # 输入密码
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="loginBtn"]')).click()  # 点击登录
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="#clinics"]/li[2]')).click()  # 选择诊所

    def book(self):#预约挂号
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/div[3]/aside/section/ul/li[3]/a/span[1]')).click()  # 点击预约挂号
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
        time.sleep(1)
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
    def accepts(self):#接诊
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '/html/body/div[3]/aside/section/ul/li[4]/a/span[1]')).click()# 点击医生工作台
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]')).click()# 点击接诊
    def cases(self):#填写病例
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="chielfComplaint"]')).send_keys(u"感冒、发烧、咳嗽、嗓子疼")  # 输入主诉
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="saveForCommonMedicalRecord"]/a')).click()#点击存为常用病例
        browser.current_window_handle # 此行代码用来定位当前页面
        time.sleep(3)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_css_selector('#layui-layer12 > div.layui-layer-content > div > ul > li:nth-child(1) > input[type="text"]')).send_keys(u"感冒")
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="saveHisTem"]')).click()#在病例名称弹窗处点击保存
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="doctorAdvice"]')).send_keys(u"多喝水，好好休息")#填写处理意见
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath",'//*[@id="saveForCommondoctorAdvice"]/a')).click()  #点击存为存为常用处理意见
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="layui-layer15"]/div[2]/div/ul/li[1]/input')).clear()#清除输入框
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", '//*[@id="layui-layer15"]/div[2]/div/ul/li[1]/input')).send_keys(u"处理意见模板保存")#填写处理意见名称
        WebDriverWait(browser, 30).until(lambda x: x.find_element("id", "saveDocterSeeTem")).click()#点击处理意见弹窗中的保存
        print ("填写病例成功")
    def inspection(self):#填写检验项目
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a')).click()#点击检验项目
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
    def check(self):#填写检查项目
        time.sleep(1)
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
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="saveCheckoutItems"]')).click()  # 点击保存
        time.sleep(1)
        WebDriverWait(browser, 30).until(lambda x: x.find_element_by_xpath('//*[@id="checkoutPresprint"]')).click()  #点击打印
        time.sleep(1)
        browser.back()#浏览器返回
        print ("填写检查项目成功")
