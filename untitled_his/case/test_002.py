# coding:utf-8
#1、追加。2、多种支付

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
from commonshare.his_common import His
from commonshare.his_common import browser
p = His()


# p = Browser()
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
        p.setUp()

    @classmethod
    def tearDownClass(cls):
        p.tearDown()

    # 登录
    def test001(self):
        p.login()
    # 收费、已收费
    def test002(self):  # 点击收费/发药
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[9]/a/span[1]').click()# 点击收费/发药
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/ul/li[2]/a').click()  # 点击收费
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="constList"]/div[2]/ul/li[1]/div/div[3]').click()  #点击追加
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="addSave"]')  #滑动到收费并保存
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"一次性纱布块")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择一次性纱布块
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"专家异地出诊交通费1")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #选择专家异地出诊交通费1
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"专家异地出诊交通费2")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  # 选择专家异地出诊交通费2
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addSave"]').click()  #点击保存并收费
        time.sleep(5)
        target = browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[10]/p[1]/i')  #滑动到收费
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/form/div/div[2]/div[10]/p[1]/i').click()  #点击收费
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[2]/div[1]/i[1]')))  #
        ys.click()  #选择现金
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[2]/div[1]/input')))  #
        ys.clear()
        ys.send_keys(u"721.59") # 输入现金金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[2]/div[2]/i[1]')))  #
        ys.click()  # 选择刷卡
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[2]/div[2]/input')))  #
        ys.clear()
        ys.send_keys(u"1000.00")  # 输入刷卡金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[4]/div[1]/i[1]')))  #个人汇款
        ys.click()  # 选择个人汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[4]/div[1]/input')))  # 输入个人汇款金额
        ys.clear()
        ys.send_keys(u"1000")  # 输入个人汇款金额
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[4]/div[2]/i[1]')))  # 公司汇款
        ys.click()  # 选择公司汇款
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[4]/div[2]/input')))  # 公司汇款
        ys.clear()
        ys.send_keys(u"1000")  # 输入公司汇款金额
        time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer25"]/div[2]/div/ul/li[5]/div[1]/i[1]')))  # 选择储值卡
        # ys.click()  # 选择储值卡
        # time.sleep(5)
        # ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer25"]/div[2]/div/ul/li[5]/div[1]/input')))  # 储值卡输入金额
        # ys.clear()
        # ys.send_keys(u"1000")   # 储值卡输入金额
        # time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[5]/div[2]/i[1]')))  # 选择其他
        ys.click()  # 选择其他
        time.sleep(5)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layui-layer7"]/div[2]/div/ul/li[5]/div[2]/input')))  # 其他输入金额
        ys.clear()
        ys.send_keys(u"2000")  # 其他输入金额
        time.sleep(5)
        target = browser.find_element_by_xpath('//*[@id="print_buying"]')  #滑动到确定
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="print_buying"]')))  #
        ys.click()  #点击确定
        time.sleep(3)
        browser.back()
        time.sleep(3)

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