# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime

# p = Browser()
today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
print today.strftime('%Y-%m-%d')
print n_days.strftime('%Y-%m-%d')

class TestHis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
        global browser
        browser.maximize_window()
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址

        # browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址

        # browser.get("http://his.oasiscare.cn/uc/authentication/check?login=true&phone=&redirectUrl=http://his.oasiscare.cn:80/yunhis/security_check.action")
        # #正式地址
        time.sleep(2)
        print "setUp"
    @classmethod
    def tearDownClass(cls):
        browser.quit()
        time.sleep(2)
        print "TearDown"

    #登录
    def test001(self):
        browser.find_element_by_id("username").clear()  # 清空账号输入框
        browser.find_element_by_id("username").send_keys("17222222222")  # 输入用户名
        browser.find_element_by_id("password").clear()  # 清空密码输入框
        browser.find_element_by_id("password").send_keys("222222")  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        browser.find_element_by_xpath(".//*[@id='#clinics']/li[2]").click()  # 选择泓华金融街诊所测试
        # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
        # browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所准正式
        time.sleep(5)
        print "登录成功"

    #预约挂号
    def test002(self):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[3]/a/span[1]').click()  # 点击预约挂号
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"董焕焕")#输入姓名
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys("18611059298")#输入手机号
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()#点击空白处
        browser.find_element_by_xpath('//*[@id="sexWoman"]').click()#选择女
        browser.find_element_by_xpath('//*[@id="registAgeInput"]').send_keys(25)#输入年龄
        browser.find_element_by_xpath('//*[@id="select2-costTypeName-container"]').click()#点击费别处的请选择
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"VIP")#在费别处输入VIP
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择VIP
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="atureFlage"]').click()#勾选保险支付
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-InsureCompanyList-container"]').click()#点击保险信息处的请选择
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"兴业银行")#输入兴业银行
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  # 选择兴业银行
        browser.find_element_by_xpath('//*[@id="registInsureNum"]').send_keys(123456)#输入保险号
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()  # 点击空白处
        browser.find_element_by_xpath('//*[@id="register_deductible"]').send_keys(u"99.99")#输入自付款
        browser.find_element_by_xpath('//*[@id="register_CoInsurance"]').send_keys(u"0.87654321")#输入自付比例
        browser.find_element_by_xpath('//*[@id="register_copayment"]').send_keys(u'0.88')#输入定额手续费
        browser.find_element_by_xpath('//*[@id="register_insure_remark"]').send_keys(u"每年最高报销100万")#输入备注
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-zhenfee_select-container"]').click()#点击诊费处的请选择
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"常规诊费")#输入常规诊费
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择常规诊费
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()  # 点击空白处
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-Order_startTime-container"]').click()#点击就诊时间的开始时间
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"9:00")#就诊时间的开始时间输入9:00
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#就诊时间的开始时间选择9:00
        browser.find_element_by_xpath('//*[@id="select2-Order_endTime-container"]').click()#点击结束时间
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"10:00")#在结束时间输入10:00
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择10:00
        browser.find_element_by_xpath('//*[@id="1002"]').click()#就诊事项选择打针
        browser.find_element_by_xpath('//*[@id="1004"]').click()  # 就诊事项选择取药
        browser.find_element_by_xpath('//*[@id="1006"]').click()  # 就诊事项选择推拿
        browser.find_element_by_xpath('//*[@id="itemsNose"]').send_keys(u"青霉素过敏")#备注处输入青霉素过敏
        browser.find_element_by_xpath('//*[@id="pationtDtailBtn"]/small').click()#患者详细信息处点击展开
        target = browser.find_element_by_xpath('//*[@id="addressDetail"]')  # 滑动到地址处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到地址处
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="medicareCardNum"]').send_keys(123456)
        s1 = Select(browser.find_element_by_id("credentialType"))#下拉框的选择
        s1.select_by_index("1")#下拉框的选择军官证
        browser.find_element_by_xpath('//*[@id="credentialTypeNum"]').send_keys(1234567890)#输入军官证号
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-country-container"]').click()#点击民族处的国籍
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"中国")#在国籍处输入中国
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择中国
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-national-container"]').click()#点击民族
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"维吾尔族")#输入维吾尔族
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择维吾尔族
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="maritalStatus"]').click()#点击婚姻状态处的请选择
        t1 = Select(browser.find_element_by_id("maritalStatus"))  # 下拉框的选择
        t1.select_by_index("1")  # 下拉框的选择已婚
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="work"]').send_keys(u"测试工程师")#输入职业
        browser.find_element_by_xpath('//*[@id="companyName"]').send_keys(u"泓华国际医疗控股有限公司")#输入工作单位
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="select2-province-container"]').click()#选择住址处的省
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"北京")#
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#
        browser.find_element_by_xpath('//*[@id="select2-city-container"]').click()#选择住址处的市
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"北京市")#
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#
        browser.find_element_by_xpath('//*[@id="select2-district-container"]').click()#选择住址处的区
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"朝阳区")#
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#
        browser.find_element_by_xpath('//*[@id="addressDetail"]').send_keys(u"北辰东路北辰汇宾大厦B座19层")#填写详细地址
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="weight"]')  # 滑动到体重处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到体重处
        browser.find_element_by_xpath('//*[@id="temperature"]').send_keys(37)
        browser.find_element_by_xpath('//*[@id="heartRateNow"]').send_keys(70)
        browser.find_element_by_xpath('//*[@id="breatheNow"]').send_keys(80)
        browser.find_element_by_xpath('//*[@id="pulseRateNow"]').send_keys(90)
        browser.find_element_by_xpath('//*[@id="BP_hight"]').send_keys(120)
        browser.find_element_by_xpath('//*[@id="BP_low"]').send_keys(90)
        browser.find_element_by_xpath('//*[@id="height"]').send_keys(160)
        browser.find_element_by_xpath('//*[@id="weight"]').send_keys(60)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="historyShowBtn"]/small').click()#点击病史信息处的展开
        time.sleep(3)
        target = browser.find_element_by_xpath('//*[@id="allergiesHistory"]')  # 滑动到过敏史处
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到过敏史处
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="historyOfPresentIllness"]').send_keys(u"偏头痛")
        browser.find_element_by_xpath('//*[@id="personalHistory"]').send_keys(u"失眠、多梦")
        browser.find_element_by_xpath('//*[@id="allergiesHistory"]').send_keys(u"青霉素过敏")
        browser.find_element_by_xpath('//*[@id="pastHistory"]').send_keys(u"失眠、多梦")
        browser.find_element_by_xpath('//*[@id="familyHistory"]').send_keys(u"近视眼")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addRegister_save"]').click()#点击保存
        time.sleep(5)
        print "预约挂号成功"

    # 接诊
    def test003(self):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[4]/a/span[1]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]').click()  # 点击接诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="chielfComplaint"]').send_keys(u"感冒、发烧、咳嗽、嗓子疼")  # 输入主诉
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="saveForCommonMedicalRecord"]/a').click()#点击存为常用病例
        time.sleep(3)
        browser.current_window_handle # 此行代码用来定位当前页面
        time.sleep(3)
        browser.find_element_by_css_selector("li > input[type=\"text\"]").send_keys(u"感冒")
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="saveHisTem"]').click()#在病例名称弹窗处点击保存
        time.sleep(2)
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(u"感冒")  # 输入诊断信息
        time.sleep(2)
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.ENTER)  # 现在开始引入Keys在此处在进行引用键盘事件，用enter键选择诊断信息
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctorAdvice"]').send_keys(u"多喝水，好好休息")#填写处理意见
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_link_text(u"存为常用处理意见").click()#点击存为存为常用处理意见
        time.sleep(2)
        browser.find_element_by_css_selector("ul.templet_ziliao.case_names > li > input[type=\"text\"]").clear()#清除输入框
        time.sleep(2)
        browser.find_element_by_css_selector("ul.templet_ziliao.case_names > li > input[type=\"text\"]").send_keys(u"处理意见模板保存")#填写处理意见名称
        time.sleep(2)
        browser.find_element_by_id("saveDocterSeeTem").click()#点击处理意见弹窗中的保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="history_save"]').click()  # 点击病例右上角的保存
        time.sleep(2)
        print "填写病例成功"

    # 接诊界面填写检验项目
    def test004(self):
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()#点击检验项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  # 点击检验项目处的请选择
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"过敏原检测(食物组)")  #输入过敏原检测(食物组)
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择过敏原检测(食物组)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  # 点击检验项目处的请选择
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"ABO血型")  #输入ABO血型
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择ABO血型
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_save"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_presprint"]').click()#点击打印
        time.sleep(2)
        browser.back()#点击返回
        time.sleep(2)
        print "填写检验项目成功"

    # 接诊界面填写检查项目
    def test005(self):
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a').click()  # 点击检查项目
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="checkoutBox"]/div[1]/div/span[2]/span[1]/span').click()  # 点击检查项目处的请选择
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"多普勒听胎心")#输入多普勒听胎心
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择多普勒听胎心
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]').click()  # 点击检查项目处的请选择
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"泌尿系超声")#输入泌尿系超声
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)#选择泌尿系超声
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="saveCheckoutItems"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutPresprint"]').click()#点击打印
        time.sleep(2)
        browser.back()#浏览器返回
        time.sleep(2)
        print "填写检查项目成功"

    # 接诊界面填写治疗项目
    def test006(self):
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a').click()  # 点击治疗
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"隔物灸法")  # 输入治疗项目"隔物灸法"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  # 选择某项治疗"隔物灸法"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="selectedInspectListBox"]/form/div/div[3]/input').clear()  # 清除治疗项目"隔物灸法"的频次输入框
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="selectedInspectListBox"]/form/div/div[3]/input').send_keys(10)  # 输入治疗项目"隔物灸法"的频次为10次
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"颈椎正骨治疗")  # 输入治疗项目"颈椎正骨治疗"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  # 选择某项治疗"颈椎正骨治疗"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_save"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_presprint"]').click()#点击打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        print "填写治疗项目成功"

    # 接诊界面填写西药
    def test007(self):
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  # 点击西药处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"阿奇霉素注射液")  # 在处方药品处输入阿
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p').click()  # 选择阿奇霉素注射液
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"硫酸庆大霉素注射液")  # 在处方药品处输入硫酸庆大霉素注射液
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]').click()  # 硫酸庆大霉素注射液
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="saveForComenPres"]').click()#点击存为常用处方
        time.sleep(5)
        browser.current_window_handle#获取当前界面
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="saveConPresName"]').send_keys(u"感冒、发烧")#输入处方模板的名称
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="presSave"]').click()#保存处方模板
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input').send_keys(u"一次性换药包")#输入耗材一次性换药包
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]').click()#选择耗材一次性换药包
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div/div/div/span/input').clear()#清除耗材的数量
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div/div/div/span/input').send_keys(2)#填写好猜的数量为2
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input').send_keys(u"一次性纱布块")#输入耗材一次性纱布块
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]').click()#选择一次性纱布块
        time.sleep(2)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select').click()  # 点击诊费输入框
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select'))
        InputType.select_by_value("10001000012")#诊费由常规诊费   ￥500改成急诊诊费   ￥1000
        time.sleep(2)
        browser.find_element_by_css_selector("#addOtherFee").send_keys(u"护士出诊(平日)")  # 其他费用
        time.sleep(2)
        browser.find_element_by_css_selector("#addOtherRelateList > p > span.name.name-text").click()  # 选择护士出诊(平日)
        time.sleep(2)
        browser.find_element_by_css_selector("#prescription_save").click()  # 点击处方处的保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescription_print"]').click()#点击打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        print "填写西药处方成功"

    # 接诊界面填写中草药
    def test008(self):#填写草药处方
        time.sleep(2)
        browser.find_element_by_css_selector("#seeDoctoring_nav > ul > li.herbal-pres > a").click()  # 点击草药处方
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"荆芥")  # 在草药输入框中输入“荆芥”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择荆芥
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“荆芥”30g
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"防风")  # 在草药输入框中输入“防风”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择防风
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“防风”30g
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"羌活")  # 在草药输入框中输入“羌活”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择羌活
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“羌活”30g
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"独活")  # 在草药输入框中输入“独活”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择独活
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“独活”30g
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"川芎")  # 在草药输入框中输入“川芎”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择川芎
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“川芎”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"醋北柴胡")  # 在草药输入框中输入“醋北柴胡”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择醋北柴胡
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“醋北柴胡”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"前胡")  # 在草药输入框中输入“前胡”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择前胡
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“前胡”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"桔梗")  # 在草药输入框中输入“桔梗”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择桔梗
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“桔梗”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"麸炒枳壳")  # 在草药输入框中输入“麸炒枳壳”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择麸炒枳壳
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“麸炒枳壳”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"土茯苓")  # 在草药输入框中输入“土茯苓”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择土茯苓
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“土茯苓”30g
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"炙甘草")  # 在草药输入框中输入“炙甘草”
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择炙甘草
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(15)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  # 添加草药“炙甘草”15g
        time.sleep(2)



        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input').send_keys(6)#剂数填写6剂
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea')#滑动到处方输入框
        browser.execute_script("arguments[0].scrollIntoView();", target)#滑动到处方输入框
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea').send_keys(u"饭后服用，每天2次。")
        time.sleep(1)



        browser.find_element_by_css_selector("p.save-for-prescription-templat").click()#点击存为常用处方
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_css_selector("li > input[type=\"text\"]").clear()#清除处方模板输入框
        time.sleep(2)
        browser.find_element_by_css_selector("li > input[type=\"text\"]").send_keys(u"草药模板")#输入处方模板名称
        time.sleep(2)
        browser.find_element_by_css_selector("button").click()#在处方模板名称弹窗中点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalPres_save"]').click()#点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="contaleBtn"]/button[3]').click()#点击打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(3)
        browser.find_element_by_id("lookDetail").click()#点击查看收费明细
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer5"]/span[1]/a').click()#关闭收费明细
        time.sleep(2)

    # 结束就诊、完善病例
    def test009(self):
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div[1]/div[2]/p[2]/a').click()#点击结束就诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="offMadicalMess"]/div/a/button').click()#点击是
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="patient_state_tab"]/li[3]').click()  #点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/a[2]').click()  #点击完善病例
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="chielfComplaint"]').send_keys(u"完善病例")  #修改主诉
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="doctorAdvice"]').send_keys(u"完善病例")  #修改处理意见
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="history_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()#点击检验项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspece_reportList_content"]/div[2]/div[1]/div/div/img').click()  #删除检验项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  #点击添加检验项目
        time.sleep(3)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"24小时尿蛋白定量")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[2]').click()  #选择“24小时尿蛋白定量”
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_presprint"]').click()  #点击打印
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[3]/a').click()  #点击检查项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutReportBox"]/div[2]/div[1]/div/img').click()  #点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]').click()  #点击检查项目
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"经颅多普勒超声 ¥1500")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #选择经颅多普勒超声 ¥1500
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="saveCheckoutItems"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutPresprint"]').click()  #点击打印
        time.sleep(2)
        browser.back()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a').click()  #点击治疗
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspece_reportList_content"]/form[2]/div/div[7]/p/img').click()  #点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"宝宝VIPII型免疫套餐（1个月-3岁）")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择“宝宝VIPII型免疫套餐（1个月-3岁）”
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_presprint"]').click()  #点击打印
        time.sleep(2)
        browser.back()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  #点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  #点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="madicineList_content"]/form[2]/div/img').click()  #删除药品
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"达克宁")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p[2]/span[1]').click()  #选择硝酸咪康唑阴道软胶囊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[1]/div[2]/div/img').click()  #删除耗材
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input').send_keys(u"碘伏棉签")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]').click()  #选择碘伏棉签
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select').click()  #点击诊费
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select'))
        InputType.select_by_value("10001000011")  # 诊费由急诊诊费   ￥1000改成复诊诊费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/form/img').click()  #删除其他费用
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"医生出诊（夜间、休日）")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择"医生出诊（夜间、休日）"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescription_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescription_print"]').click()  #点击打印
        time.sleep(2)
        browser.back()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[6]/a').click()  #点击草药处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[1]/ul/li[11]').click()  #点击炙甘草
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[1]/ul/li[11]/span[4]').click()  #点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(u"黄芩")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  #选择黄芩
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(u"20")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  #点击新增
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input').clear()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input').send_keys(u"10")  #改成10剂
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalKind_01"]').click()  #选择外敷
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea').send_keys(u"修改备注")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalPres_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="contaleBtn"]/button[3]').click()  #点击打印
        time.sleep(2)
        browser.back()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="lookDetail"]').click()  # 点击查看收费明细
        time.sleep(2)
        browser.current_window_handle
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/span[1]/a')))  # 找到预约挂号的元素
        ys.click()  # 点击关闭
        time.sleep(2)






    # 检验工作台
    def test010(self):  # 检验工作台
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[5]/a/span[1]').click()  # 点击检验工作台
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_patient_content"]/div[1]/div[2]/a').click()  # 点击开始检验
        time.sleep(1)
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
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[7]/a').click()  # 点击治疗
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()#点击开始治疗
        time.sleep(2)

        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[8]')))  # 找登录按钮输入元素
        ys.click()  # #点击执行


        time.sleep(3)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_link_text(u"确认").click()#点击确定
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="startCheckout_nav"]/a').click()  # 点击返回

    # 检查工作台
    def test012(self):  # 检查工作台
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[6]/a/span[1]').click()# 点击检查工作台
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()  # 点击开始检查
        time.sleep(1)
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

    # 收费、已收费
    def test013(self):  # 点击收费/发药
        global browser
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a/span[1]').click()# 点击收费/发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()#点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li/div/div[2]').click()#点击待收费
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/form/div/div[2]/div[10]')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/form/div/div[2]/div[9]/p[1]/i').click()  # 点击收费

        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_xpath("(//input[@name='chioce_radio'])[2]").click()#点击刷卡
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="print_buying"]').click()#点击确定
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()  # 点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[1]/span[2]').click()  # 点击已收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li[1]/div/div[2]').click()  # 已收费界面，点击已收费
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[1]/div[2]/div[7]/span[1]')  # 滑动到打印账单处
        browser.execute_script("arguments[0].scrollIntoView();", target)  #  滑动到打印账单处
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[2]/div[1]/div[2]/div[7]/span[1]').click()  # 点击打印账单
        time.sleep(2)
        browser.back()
        time.sleep(2)


    # 退费、退费管理
    def test014(self):#点击结算管理
        global browser
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[4]/a').click()#点击结算管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()#点击详情
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/a/span')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/a/span').click()#点击退费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[3]/table/thead/tr/th[1]/label/input').click()#点击全选
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/span')  # 滑动到提交按钮
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到提交按钮
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[5]/div[2]/p').send_keys(u"不满意，不想要了")#填写退费原因
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/span').click()#点击提交
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()#点击退费弹窗中的确定
        time.sleep(3)
        browser.back()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[8]/a/span').click()  # 点击退费管理
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()