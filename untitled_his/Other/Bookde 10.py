# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from commonshare.His import Browser
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径

class TestHis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global browser
        browser.maximize_window()
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址

        # browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址

        # browser.get("http://his.oasisclinic.cn")
        # #正式地址
        time.sleep(2)
        print ("setUp")
    @classmethod
    def tearDownClass(cls):
        browser.quit()
        time.sleep(2)
        print ("TearDown")


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
        print ("登录成功")


    def test002(self):
        s = 0
        while s < 10:
            s = s + 1
            #预约挂号
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div[3]/aside/section/ul/li[2]/a").click()  # 点击预约挂号
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(s)#
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul').click()  # 点击空白处
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys("18611059298")#输入手机号
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="addRegister_save"]').click()#点击保存
            time.sleep(1)
            print ("预约挂号成功")
            #取消
            browser.find_element_by_xpath('//*[@id="appointment_nav"]/ul/li[2]/a').click()#点击患者列表
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="appointRegis_cart_tab"]/li[2]').click()#点击候诊中
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="appointRegister_patientCart_content"]/div[1]/div[2]/p[2]').click()#点击取消
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="cancel_rigister"]/div/button[1]').click()
            time.sleep(1)
        print (s)
if __name__ == '__main__':
    unittest.main()