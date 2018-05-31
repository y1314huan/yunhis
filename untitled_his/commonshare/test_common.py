# coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait



class His():
    def setUp(self):
        global browser
        browser = webdriver.Chrome()  # chromedriver.exe文件的路径
        browser.maximize_window()
        url = "http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action"
        browser.get(url)
        # # ## 测试地址
        browser.implicitly_wait(30)

    def tearDown(self):
        # browser.quit()
        print ("TearDown")
    #登录
    def login(self,username,psw):

        global browser
        u"""这里写了一个登陆的方法，账号和密码参数化"""
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", 'ipuut1')).send_keys(username)  # 输入用户名
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", 'ipuut2')).send_keys(psw)  # 输入密码
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", 'signin')).click()  # 点击登录
        WebDriverWait(browser, 30).until(lambda x: x.find_element("xpath", 'clinic')).click()  # 选择诊所