#-*- coding=UTF-8  -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class oasis(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "8"
        caps["deviceName"] = "vivo Y85A"
        caps["appPackage"] = "com.lcworld.hhylyh"
        caps["appActivity"] = ".splash.SplashActivity"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    def tearDown(self):
        pass
        # self.driver.quit()
    def testLogin001(self):
        global driver
        time.sleep(2)
#         swipe(self, start_x, start_y, end_x, end_y, duration=None)
#         - start_x - 开始滑动的x坐标
#     - start_y - 开始滑动的y坐标
#     - end_x - 结束点x坐标
#     - end_y - 结束点y坐标
#     - duration - 持续时间，单位毫秒



        # range(start, stop[, step])
        # 参数说明：
        # start: 计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
        # stop: 计数到stop结束，但不包括
        # stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        # step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        for i in range(0,4):
            i=i+1
            self.driver.swipe(649, 1039,23, 1039,  500)#滑屏3次
        time.sleep(1)
        self.driver.tap([(504, 1931), (586, 1931)], 500)  # 点击立即体验
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element("id", 'com.lcworld.hhylyh:id/longin_anniu')).click()  #点击登录
        self.driver.tap([(800, 894), (902, 904)], 500)  # 使用密码登录
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element("id", 'com.lcworld.hhylyh:id/et_id')).send_keys("16666666661")  # 输入手机号
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText')).send_keys("666661")  #输入密码
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element("id", 'com.lcworld.hhylyh:id/tv_login_btn')).click()  #点击登录
        time.sleep(3)
        self.driver.tap([(507, 1755), (576, 1760)], 500)  # 点击我知道了
        time.sleep(3)
        self.driver.tap([(863, 480), (870, 482)], 500)  # 点击×
        time.sleep(2)
        self.driver.tap([(306, 1174), (359, 1176)], 500)  # 点击暂不认证
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element("id", 'com.lcworld.hhylyh:id/iv_icon')).click()  #点击我的诊所

        # WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_css_selector('#screenshotContainer > div > div > div > div > div > div.Inspector__highlighter-box___Oi319.Inspector__inspected-element-box___3mBB4')).click()#点击我的诊所


        WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_css_selector('#screenshotContainer > div > div > div > div > div > div:nth-child(17)')).click()#选择云his测试诊所

        WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_css_selector('#screenshotContainer > div > div > div > div > div > div:nth-child(18)')).click()#点击移动接诊
        # WebDriverWait(self.driver, 30).until(lambda x: x.find_element("xpath", '//*[@id="screenshotContainer"]/div/div/div/div/div/div[18]')).click()  #点击移动接诊


if __name__ == '__main__':
    unittest.main()
