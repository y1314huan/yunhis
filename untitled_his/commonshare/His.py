# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
global browser
class Browser():
    def Browserinit(self,myurl):#登录
        browser.maximize_window()
        time.sleep(2)
        browser.get(myurl)#请求网址
    def TestLogin(self,username,passwd):#登录并选择诊所
        browser.find_element_by_id("username").clear()#清空账号输入框
        browser.find_element_by_id("username").send_keys(username)  # 输入用户名
        browser.find_element_by_id("password").clear()#清空密码输入框
        browser.find_element_by_id("password").send_keys(passwd)  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()#选择泓华金融街诊所准正式
        time.sleep(5)
        print "登录成功"
    def Browserclose(self):#关闭网页
        browser.quit()
    def BookingRegister(self,name,telephone):#预约挂号
        browser.find_element_by_xpath("/html/body/div[2]/aside/section/ul/li[2]/a/i").click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(name)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()
        browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys(telephone)
        browser.find_element_by_xpath('//*[@id="addRegister_save"]').click()
        time.sleep(5)
        print "预约挂号成功"
    def DoctorBench(self):# 点击医生工作台
        browser.find_element_by_xpath('/html/body/div[2]/aside/section/ul/li[3]/a').click()  # 点击医生工作台
        time.sleep(2)
    def ClickJz(self):#点击接诊
        browser.find_element_by_xpath('//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]').click()  # 点击接诊
        time.sleep(2)
    def Case(self,description,diagnose):
        browser.find_element_by_xpath('//*[@id="chielfComplaint"]').send_keys(description)  # 输入主诉
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(diagnose)  # 输入诊断信息
        time.sleep(2)
        browser.find_element_by_css_selector("input.select2-search__field").send_keys(
            Keys.ENTER)  # 现在开始引入Keys在此处在进行引用键盘事件，用enter键选择诊断信息
        time.sleep(2)
        print "填写病例成功"
    def SaveButton(self,value):#医生工作台的保存按钮
        browser.find_element_by_xpath(value).click()  # 点击保存
        time.sleep(2)
    def ClickCheckout(self):# 点击检验项目
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()  # 点击检验项目
        time.sleep(2)
    def WriteCheckout(self,AddCheckout):#填写检验项目
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  # 点击检验项目处的请选择
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(AddCheckout)  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
    def ClickInspect(self):# 点击检查项目
        browser.find_element_by_css_selector("#seeDoctoring_nav > ul > li.checkout.active > a").click()  # 点击检查项目
        time.sleep(2)
    def WriteInspect(self,AddInspect):# 填写检查项目
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(AddInspect)
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        time.sleep(2)
    def ClickTherapy(self):# 点击治疗
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a').click()  # 点击治疗
        time.sleep(2)
    def WriteTherapy(self,Therapy):#填写治疗
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(Therapy)  # 输入治疗项目"隔物灸法"
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  # 选择某项治疗"隔物灸法"
        time.sleep(2)
    def ClearImport(self,xpath,num):
        browser.find_element_by_xpath(xpath).clear()  # 清除治疗项目"隔物灸法"的频次输入框
        time.sleep(2)
        browser.find_element_by_xpath(xpath).send_keys(num)  # 输入治疗项目"隔物灸法"的频次为10次
        time.sleep(2)
    def Click(self,value):#点击
        browser.find_element_by_xpath(value).click()
        time.sleep(2)
    def Back(self):
        browser.back()
        time.sleep(5)
    def ClickLong(self,value):#点击
        browser.find_element_by_xpath(value).click()
        time.sleep(5)
    def Prescription(self,value):
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(value)  # 在处方药品处输入硫酸庆大霉素注射液
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]').click()  # 硫酸庆大霉素注射液
        time.sleep(2)
    def Select(self,value):#选择
        browser.find_element_by_css_selector(value).click()
        time.sleep(2)
    def Import(self,value1,value2):
        browser.find_element_by_css_selector(value1).send_keys(value2)
        time.sleep(2)
    def ChinesePrescription(self,value1,value2):#填写草药
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(value1)#在草药输入框中输入“荆芥”
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()#选择荆芥
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()#清除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(value2)#
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()#添加草药“荆芥”30g
        time.sleep(2)
    def Down(self,value):#将滚动条拖动到指定位置
        target = browser.find_element_by_xpath(value)
        browser.execute_script("arguments[0].scrollIntoView();", target)


