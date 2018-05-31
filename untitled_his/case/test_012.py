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
from commonshare.his_common import His
from commonshare.his_common import browser
p = His()


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
        p.setUp()

    @classmethod
    def tearDownClass(cls):
        p.tearDown()

    # 登录
    def test001(self):
        p.login()


    # 发药、退药
    def test002(self):
        global browser
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[7]/a').click()  # 点击收费/发药
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
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[2]/ul/li[7]/a').click()  # 点击收费/发药
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