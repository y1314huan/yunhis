# coding:utf-8
from selenium import webdriver
import unittest
import time
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
class TestHis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser.maximize_window()
        browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        # # ## 测试地址
        time.sleep(2)
        print ("setUp")
    @classmethod
    def tearDownClass(cls):
        # browser.quit()
        time.sleep(2)
        print ("TearDown")

    #登录
    def test001(self):
        global browser
        browser.find_element_by_id("username").send_keys("17444444444")  # 输入用户名
        browser.find_element_by_id("password").clear()  # 清空密码输入框
        browser.find_element_by_id("password").send_keys("444444")  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所测试和准正式
        time.sleep(5)
        print ("登录成功")
        expValue = u"董焕焕11"
        print(expValue)
        actValue = browser.find_element_by_xpath('//*[@id="personalName"]').text
        time.sleep(2)
        print(actValue)
        self.assertEqual(expValue,actValue)



if __name__ == '__main__':
    unittest.main()

