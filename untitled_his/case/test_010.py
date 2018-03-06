# coding:utf-8
#套餐（收费项目设置医生工作台）
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


    #套餐
    def test002(self):
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]/a/span[1]').click()  #点击系统管理
        time.sleep(2)
        target = browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]/ul/li[5]/a')  #滑动到字典
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[14]/ul/li[4]/a').click()  #点击收费项目设置
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="collect_fees"]/ul/li[4]/a').click()  #点及其他项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="treatment_btn"]').click()  #点击添加其他项目
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="item_name"]').send_keys(u"新增套餐")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-ZL_item-container"]').click()  #点击项目类型
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"套餐")  #
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="unit_ids"]').send_keys(u"人次")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="nowprice_ids"]').send_keys(u"1000.99")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="charging_item_btn"]').click()  #点击保存
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="tr_z0"]/td[7]/span[2]/a').click()  #点击关联项目
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"三伏贴")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]').click()  #选择三伏贴
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"达克宁")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]').click()  #选择达克宁
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))#选择耗材
        InputType.select_by_value("2")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"一次性换药包") #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[2]/div[2]/p/span[1]').click()  #选择一次性换药包
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"一次性纱布块")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[2]/div[2]/p/span[1]').click()  #选择一次性纱布块
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))  # 选择检验
        InputType.select_by_value("3")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"脂蛋白")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[3]/div/p[1]').click()  #选择脂蛋白
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"17-羟维生素D3")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[3]/div/p').click()  #选择17-羟维生素D3
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))  # 选择检查
        InputType.select_by_value("4")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"多普勒听胎心")  #
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[3]/div/p[1]').click()  #选择多普勒听胎心
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"腹部彩超")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[3]/div/p[2]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))  # 选择治疗
        InputType.select_by_value("5")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"关节矫正复位")  #
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[2]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"颈椎正骨治疗")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))  # 选择诊费
        InputType.select_by_value("7")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"诊费及体检费")  #
        time.sleep(2)
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="additem"]/div/div[4]/div/p[4]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="additem"]/div/div[4]/div/p[4]').click()  #
        time.sleep(2)
        InputType = Select(browser.find_element_by_xpath('//*[@id="projectType"]'))  # 选择其他
        InputType.select_by_value("6")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"无菌敷贴")  #
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="addOtherRelateList1"]/p[1]/span[1]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList1"]/p[1]/span[1]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="orherRelation_save"]').click()  #点击保存
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="ajax-content"]/div/div[1]/div[2]/table/tbody/tr[1]/td[5]').click()  #点击删除
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="orherRelation_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="orherRelation"]').click()  #点击返回
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[4]/a/span[1]').click()  #点击医生工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="fasterLookDoctorBtn"]').click()  #点击快速接诊
        time.sleep(2)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="registerName_input"]').send_keys(u"套餐")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="fasterRigis_form"]/div[8]/div[1]/label').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="telephonNum"]').send_keys(u"18611059298") #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="fasterDo"]').click()  #点击接诊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[2]/a').click()  #点击检验工作台
        time.sleep(2)
        browser.refresh()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-inspectSearchInput-container"]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"抗核抗体ANA")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seeDoctoring_nav"]/ul/li[3]/a')))  #
        ys.click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="select2-checkoutSearchLis-container"]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u"甲状腺超声")  #
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[4]/a').click()  #点击治疗
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"隔物灸法")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="seeDoctoring_nav"]/ul/li[5]/a').click()  #点击处方
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadicine"]').send_keys(u"达克宁")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addMadiclRelateList"]/p/span[1]').click()  # 选择硝酸咪康唑阴道软胶囊
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/input').send_keys(u"碘伏棉签")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="consumable_box"]/div/div[2]/div/div/div[2]/p/span[1]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select').click()  #
        time.sleep(1)
        InputType = Select(browser.find_element_by_xpath('//*[@id="prescriptionContentBox"]/div[4]/div/div/select'))
        InputType.select_by_value("10001000016")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="addOtherFee"]').send_keys(u"新增套餐")  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="addOtherRelateList"]/p/span[1]').click()  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="otherFeeContent"]/p/span').click()  #点击套餐详情
        time.sleep(2)
        target = browser.find_element_by_xpath('//*[@id="addOtherFee"]')  #
        browser.execute_script("arguments[0].scrollIntoView();", target)  #
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="prescription_save"]').click()  #点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="setmeal"]/div[2]/div/span').click()  #点击打印
        time.sleep(3)
        browser.back()
        time.sleep(2)
        browser.find_element_by_css_selector("#seeDoctoring_nav > ul > li.herbal-pres > a").click()  # 点击草药处方
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/input').send_keys(
            u"荆芥")  # 在草药输入框中输入“荆芥”
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/div[1]/div/div/div[2]/p[1]/span[1]').click()  # 选择荆芥
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').clear()  # 清除
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[1]/span/input').send_keys(30)  #
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[2]/div/div[2]/div/ul/li/div/div[2]/span[1]/img').click()  #


        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[3]/div/div/input').send_keys(6)  # 剂数填写6剂
        time.sleep(1)
        target = browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea')  # 滑动到处方输入框
        browser.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到处方输入框
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalsPresBox"]/div/div[4]/div/div[2]/textarea').send_keys(
            u"饭后服用，每天2次。")
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="herbalPres_save"]').click()  # 点击保存
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="contaleBtn"]/button[4]/a').click()  #点击结束就诊
        time.sleep(5)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="offMadicalMess"]/div/a/button').click()  #
        time.sleep(2)

        # 检验工作台
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[5]/a/span[1]').click()  # 点击检验工作台
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inspect_patient_content"]/div[1]/div[2]/a').click()  # 点击开始检验
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspectSavePrint"]').click()  # 点击保存与打印
        time.sleep(3)
        browser.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="inSaveYes"]').click()  #点击继续
        # time.sleep(3)
        browser.back()  # 点击浏览器的返回
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="inspectSystm_patientCart_tab"]/li[3]/span[2]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="inspect_patient_content"]/div[1]/div[2]/a').click()  # 点击查看
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="againPrint"]').click()  # 点击打印报告
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)

        # 治疗工作台
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[7]/a').click()  # 点击治疗
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()#点击开始治疗
        time.sleep(2)
        ys = WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/span')))  #
        ys.click()  # #点击执行
        time.sleep(3)
        browser.current_window_handle
        time.sleep(2)
        browser.find_element_by_link_text(u"确认").click()#点击确定
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="treatPrint"]').click()  # 点击查看并打印
        time.sleep(2)
        browser.back()
        time.sleep(2)

        # 检查工作台
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/aside/section/ul/li[6]/a/span[1]').click()# 点击检查工作台
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div[1]/div[2]/a').click()  # 点击开始检查
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="chDes"]').send_keys(u"头疼、发烧、咳嗽、眩晕")  # 输入描述信息
        browser.find_element_by_xpath('//*[@id="chResult"]').send_keys(u"感冒")  # 输入结论
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkoutSavePrint"]').click()  # 点击保存与打印
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="inSaveYes"]').click()  # 点击继续
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patientCart_tab"]/li[3]/span[2]').click()  # 点击已完成
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkout_patient_cart_content"]/div/div[2]/a').click()  # 点击查看
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="checkAgainPrint"]').click()  # 点击打印报告
        time.sleep(2)
        browser.back()  # 点击浏览器的返回
        time.sleep(2)












if __name__ == '__main__':
    unittest.main()