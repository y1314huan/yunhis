# coding:utf-8
#为套餐收费的多种支付
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
from selenium.webdriver.support.ui import Select
import datetime

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径

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
        global browser
        browser.maximize_window()
        # browser.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址

        browser.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址

        # browser.get("http://his.oasiscare.cn/uc/authentication/check?login=true&phone=&redirectUrl=http://his.oasiscare.cn:80/yunhis/security_check.action")
        # #正式地址
        time.sleep(2)
        print ("setUp")
    @classmethod
    def tearDownClass(cls):
        browser.quit()
        time.sleep(2)
        print ("TearDown")

    #登录
    def test001(self):
        browser.find_element_by_id("username").clear()  # 清空账号输入框
        browser.find_element_by_id("username").send_keys("17444444444")  # 输入用户名
        browser.find_element_by_id("password").clear()  # 清空密码输入框
        browser.find_element_by_id("password").send_keys("444444")  # 输入密码
        browser.find_element_by_id("loginBtn").click()  # 点击登录
        time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="#clinics"]/li[1]').click()#正式环境云his测试诊所
        browser.find_element_by_xpath('//*[@id="#clinics"]/li[2]').click()  # 选择泓华金融街诊所测试和准正式
        time.sleep(5)
        print ("登录成功")


    # 收费、已收费
    def test002(self):  # 点击收费/发药
        global browser
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a/span[1]').click()# 点击收费/发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()#点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li/div/div[2]').click()#点击待收费
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[11]/ol')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[10]/p[1]/i').click()  # 点击收费
        time.sleep(2)

        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[2]/div[1]/i[1]')))  #
        ys.click()  #选择现金
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[2]/div[1]/input')))  #
        ys.clear()
        ys.send_keys(u"413.50") # 输入现金金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[2]/div[2]/i[1]')))  #
        ys.click()  # 选择刷卡
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[2]/div[2]/input')))  #
        ys.clear()
        ys.send_keys(u"100.00")  # 输入刷卡金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[4]/div[1]/i[1]')))  #个人汇款
        ys.click()  # 选择个人汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[4]/div[1]/input')))  # 输入个人汇款金额
        ys.clear()
        ys.send_keys(u"500")  # 输入个人汇款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[4]/div[2]/i[1]')))  # 公司汇款
        ys.click()  # 选择公司汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[4]/div[2]/input')))  # 公司汇款
        ys.clear()
        ys.send_keys(u"500")  # 输入公司汇款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[5]/div[2]/i[1]')))  # 选择其他
        ys.click()  # 选择其他
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer5"]/div[2]/div/ul/li[5]/div[2]/input')))  # 其他输入金额
        ys.clear()
        ys.send_keys(u"1000")  # 其他输入金额
        time.sleep(5)
        target = browser.find_element_by_xpath('//*[@id="print_buying"]')  #滑动到确定
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="print_buying"]')))  #
        ys.click()  #点击确定
        time.sleep(5)
        browser.back()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]').click()  #点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="constList"]/div[1]/div[1]/span[2]').click()  # 点击已收费状态
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="constList"]/div[2]/ul/li[1]/div/div[2]').click()  # 点击已收费按钮
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/div[7]/span')  # 滑动到打印账单详情页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到账单详情页面最底部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/div[7]/span').click()  # 点击打印账单
        time.sleep(2)
        browser.back()
        time.sleep(2)









if __name__ == '__main__':
    unittest.main()