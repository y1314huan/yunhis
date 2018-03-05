# coding:utf-8
#套餐的退费、发药
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
from selenium.webdriver.support.ui import Select
import datetime

browser = webdriver.Chrome(
    r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径

today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
print(today.strftime('%Y-%m-%d'))
print(n_days.strftime('%Y-%m-%d'))


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
        print("setUp")

    @classmethod
    def tearDownClass(cls):
        browser.quit()
        time.sleep(2)
        print("TearDown")

    # 登录
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
        print("登录成功")



    # 发药、退药
    def test002(self):
        global browser
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a/span[1]').click()  # 点击收费/发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[1]').click()  # 点击发药
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li[1]/div/div[2]').click()  # 点击待发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="Allboxs"]/div[3]/div[3]/span').click()  # 西药发药点击确定
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'charge3_poup_btn')))  #
        ys.click()  # 弹窗中点击确定
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="Allboxs"]/div[3]/div[5]/span').click()  # 耗材发药点击确定
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "HC_charge3_poup_btn")))  #
        ys.click()  # 弹窗中点击确定
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="Vuelist"]/div/div[3]/span').click()  # 草药发药点击确定
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ZY_charge2_poup_btn')))  #
        ys.click()  # 弹窗中点击确定
        time.sleep(3)

        browser.find_element_by_xpath('//*[@id="taocanList"]/div/span').click()  # 套餐发药点击确定
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'charge3_poup_btn')))  #
        ys.click()  # 弹窗中点击确定
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[1]/div[1]/span[2]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/ul/li/div/div[2]').click()  # 点击已发药
        time.sleep(2)
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="DrugRuturn"]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到退药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="DrugRuturn"]').click()  # 点击退药
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'charge8_poup_btn')))  #
        ys.click()  # 弹窗中点击确定
        time.sleep(3)




    # 退费、退费管理
    def test003(self):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a/span[1]').click()  # 点击收费/发药
        time.sleep(3)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#content > div.charge.subhead > div > div > ul > li:nth-child(4) > a")))  #
        ys.click()  # 点击结算管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="table_excel"]/tbody/tr[1]/td[14]/a').click()  # 点击详情
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="printgroup"]/a/span')  # 滑动到代收付页面最底部
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到代收付页面最底部
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="printgroup"]/a/span').click()  # 点击退费
        time.sleep(2)
        browser.find_element_by_xpath(
            '//*[@id="ajax-content"]/div/div[1]/div[3]/div[3]/table/thead/tr/th[1]/label/input').click()  # 点击全选
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/span')  # 滑动到提交按钮
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到提交按钮

        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[5]/div[2]/p').send_keys(
            u"不满意，不想要了")  # 填写退费原因
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[3]/div[7]/span').click()  # 点击提交
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-btn0")))  #
        ys.click()  # 点击退费弹窗中的确定
        time.sleep(15)
        browser.back()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()