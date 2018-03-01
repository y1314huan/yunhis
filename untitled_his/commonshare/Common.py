# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
global browser

def login(username,password):
    global browser
    # browser.find_element_by_id("username").clear()  # 清空账号输入框
    browser.find_element_by_id("username").send_keys(username)  # 输入用户名
    browser.find_element_by_id("password").clear()  # 清空密码输入框
    browser.find_element_by_id("password").send_keys(password)  # 输入密码
    browser.find_element_by_id("loginBtn").click()  # 点击登录
    time.sleep(2)
    # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
    browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所测试和准正式
    time.sleep(5)
    print("登录成功")

