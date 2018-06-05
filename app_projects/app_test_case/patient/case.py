#-*- coding=UTF-8  -*-
__author__ = 'poptest'
import unittest
import time
from appium import webdriver
class oasis(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android",
        desired_caps["platformVersion"] = "5.1.1",
        desired_caps["deviceName"] =  "DUK_AL20",
        desired_caps["appPackage"] = "com.lcworld.oasismedical",
        desired_caps["appActivity"] = ".splash.SplashActivity"
        self.driver = webdriver.Remote("http://172.20.0.174:4723/wd/hub", desired_caps)
        # desired_caps={}
        # desired_caps['device'] = 'DUK_AL20'#生成厂商
        # desired_caps['deviceName'] = 'DUK_AL20'#model  设备名
        # desired_caps['platformName'] = 'Android'#操作平台
        # desired_caps['version'] = '5.1.1'#版本
        # self.driver=webdriver.Remote("http://172.20.0.174:4723/wd/hub",desired_caps)
        # hub连接手机的服务，http://172.20.0.174:4723表示本地IP
    def tearDown(self):
        pass
    def testLogin001(self):
        time.sleep(2)
        self.driver.swipe(649, 1039,23, 1039,  500)
        time.sleep(1)
        self.driver.swipe(649, 1039,23, 1039,  500)
        time.sleep(1)
        self.driver.swipe(649, 1039,23, 1039,  500)
        time.sleep(1)
        self.driver.tap([(301, 1232), (417, 1229)], 100)  # 点击立即体验
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()




















