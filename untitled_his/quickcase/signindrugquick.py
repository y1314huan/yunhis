# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
today = datetime.datetime.now()
days = datetime.timedelta(days=1)
n_days = today + days
tom = n_days.strftime('%Y-%m-%d')
now = today.strftime('%Y-%m-%d')
class TestHis(unittest.TestCase):
    #打开浏览器
    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver.exe文件的路径
        global driver
        driver.maximize_window()
        driver.get("http://yun.oasisapp.cn:9080/uc/authentication/check?login=true&phone=&redirectUrl=http://yun.oasisapp.cn:8080/yunhis/security_check.action")
        ## 测试地址
        # driver.get("http://47.93.156.153:9090/uc/authentication/check?login=true&phone=&redirectUrl=http://47.93.156.153:8090/yunhis/security_check.action")
        # # 准正式地址
        # driver.get("http://his.oasisclinic.cn")
        # #正式地址
        print "setUp"

    #关闭浏览器
    @classmethod
    def tearDownClass(cls):#
        driver.quit()
        print "TearDown"

    #登录
    def test_LogIn(self):#
        global driver
        Username = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "username")))#找账号输入元素
        Username.clear()# 清空账号输入框
        Username.send_keys("17222222222")#输入账号
        Password = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "password")))#找密码输入元素
        Password.clear()#清空密码输入
        Password.send_keys("222222")#输入密码
        LoginBtn = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "loginBtn")))#找登录按钮输入元素
        LoginBtn.click()#点击登录
        Clinic = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='#clinics']/li[2]")))#找金融街诊所元素
        Clinic.click()#选择金融街诊所
        print "登录成功"

    #签到
    def test_SignIn(self):
        global driver
        Book = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/aside/section/ul/li[3]/a')))  #找到预约挂号的元素
        Book.click()#点击预约挂号
        Name = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registerName_input"]')))#找到姓名输入的元素
        Name.send_keys(u"董焕焕")#输入姓名
        time.sleep(1)
        Blank = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="addRegister_form"]/div/div[1]')))#找到空白的元素
        Blank.click()#点击空白
        TelephonNum = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="telephonNum"]')))#找到输入手机号的元素
        TelephonNum.send_keys("18611059298")#输入手机号
        Time = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="regis_data"]')))#找到输入时间的元素
        Time.clear()#清空时间
        Time.send_keys(tom)#输入时间
        time.sleep(3)
        Save = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="addRegister_save"]')))#找到保存按钮的元素
        Save.click()#点击保存
        time.sleep(2)
        PatientList = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appointment_nav"]/ul/li[2]/a')))#找到患者列表的元素
        PatientList.click()#点击患者列表
        time.sleep(2)
        NextDay = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appointRegis_nextDate_button"]')))#找到下一天的元素
        NextDay.click()#点击下一天
        Register = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appointRegister_patientCart_content"]/div[1]/div[2]/a')))#找到改约的元素
        Register.click()# 点击改约
        Date = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="regis_data"]')))  # 找到就诊日期的元素
        Date.clear()
        Date.send_keys(now)
        Print = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="presprint_1"]')))  # 找到保存并打印的元素
        Print.click()# 点击保存并打印
        time.sleep(2)
        driver.back()
        Patient = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appointment_nav"]/ul/li[2]/a')))  # 找到患者列表的元素
        Patient.click()# 点击患者列表
        SignIn = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appointRegister_patientCart_content"]/div/div[2]/p[1]')))  # 找到签到的元素
        SignIn.click()# 点击签到
        driver.refresh
        time.sleep(3)
        DoctorBench = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/aside/section/ul/li[4]/a')))  # 找到医生工作台的元素
        DoctorBench.click()# 点击医生工作台
        Reception = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="doctor_patient_cart_content"]/div[1]/div[2]/span[1]')))  # 找到接诊的元素
        Reception.click() # 点击接诊

    #药品（耗材）入库出库
    def test_Storage(self):
        # 入库
        time.sleep(2)
        pharmacy = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="medical"]')))  # 找到药房元素
        pharmacy.click()  # 点击药房
        driver.refresh()
        time.sleep(2)
        newstorage = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button')))  # 找到新增入库单元素
        newstorage.click()  # 点击新增入库单
        inputdrug  = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  # 找到药品输入框元素
        inputdrug.send_keys(u"阿奇霉素注射液")  #
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()
        time.sleep(1)
        durgnum  = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[6]/input')))  #
        durgnum.send_keys(u"1111")  #输入药品批号
        productdate = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[7]/input')))  #
        productdate.send_keys(now)  #输入生产日期
        indate = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[1]/td[8]/input')))  #
        indate.send_keys(u"2023-10-11")#输入有效期
        unitprice = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="stockIn_edit"]/tbody/tr/td[9]/input')))  #
        unitprice.send_keys(10)#输入单价
        num = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="stockIn_edit"]/tbody/tr/td[10]/input[2]')))  #
        num.clear()#清除数量
        num.send_keys(10)#输入数量
        inputdurg1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputdurg1.send_keys(u"硫酸庆大霉素注射液")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()
        time.sleep(1)
        durgnum1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[6]/input')))  #
        durgnum1.send_keys(u"1111")
        productdate1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[7]/input')))  #
        productdate1.send_keys(now)
        indate1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[8]/input')))  #
        indate1.send_keys(u"2023-10-11")
        unitprice1= WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[9]/input')))  #
        unitprice1.send_keys(10)
        num1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[10]/input[2]')))  #
        num1.clear()
        num1.send_keys(10)
        inputdurg3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputdurg3.send_keys(u"达克宁")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[2]').click()
        time.sleep(1)
        delete = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/span')))  #
        delete.click()
        supplier = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/input')))  #
        supplier.send_keys(u"同仁堂")#供应商输入同仁堂
        submit = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        submit.click()  # 点击提交审核
        details = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[1]')))  #
        details.click()  # 点击详情
        time.sleep(2)
        cancel = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[5]/span[4]')))  #
        cancel.click()  # 点击取消
        modification = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[2]')))  #
        modification.click()  # 点击修改
        time.sleep(2)
        inputdrug2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputdrug2.send_keys(u"三伏贴")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[2]').click()
        time.sleep(1)
        durgnum2= WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[6]/input')))  #
        durgnum2.send_keys(u"1111")
        productdate2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[7]/input')))  #
        productdate2.send_keys(now)
        indate2= WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[8]/input')))  #
        indate2.send_keys(u"2023-10-11")
        unitprice2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[9]/input')))  #
        unitprice2.send_keys(10)
        num2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[10]/input[4]')))  #
        num2.clear()
        num2.send_keys(10)
        inputdurg4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputdurg4.send_keys(u"达克宁")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()
        time.sleep(1)
        durgnum3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[6]/input')))  #
        durgnum3.send_keys(1111)
        productdate3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[7]/input')))  #
        productdate3.send_keys(now)
        indate3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[8]/input')))  #
        indate3.send_keys(u"2023-10-11")
        unitprice3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[9]/input')))  #
        unitprice3.send_keys(10)
        durgnum4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[10]/input[4]')))  #
        durgnum4.clear()
        durgnum4.send_keys(10)
        save = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        save.click()
        driver.refresh()
        check = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[4]')))  #
        check.click()  # 点击审核
        time.sleep(2)
        check1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_check"]')))  #
        check1.click()  # 在审核详情页点击审核
        # 出库
        time.sleep(2)
        output = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div/div/ul/li[2]/a/span')))  #
        output.click()
        driver.refresh()
        time.sleep(2)
        newoutput = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button')))  #
        newoutput.click()
        outputdurg = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        outputdurg.send_keys(u"达克宁")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[3]/td[3]').click()
        time.sleep(1)
        outputnum = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]')))  #
        outputnum.clear()
        outputnum.send_keys(8)
        outputdurg1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        outputdurg1.send_keys(u"三伏贴")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()
        time.sleep(1)
        outputdurg2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        outputdurg2.send_keys(u"701跌打镇痛膏")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[3]').click()  # 选择701跌打镇痛膏
        time.sleep(1)
        delete1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span')))  #
        delete1.click()  # 删除701跌打镇痛膏
        office = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]')))  #
        office.click() # 点击领用科室
        inputoffice = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        inputoffice.send_keys(u"心血管内科")  # 在科室处输入心血管内科
        inputoffice.send_keys(Keys.ENTER)  # 选择心血管内科
        recipient = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[4]/span/span[1]/span/span[2]')))  #
        recipient.click()#点击领用人
        inputrecipient = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        inputrecipient.send_keys(u"董焕焕")  # 在领用人处输入董焕焕
        inputrecipient.send_keys(Keys.ENTER)  # 选择董焕焕领用人
        check2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]/button')))  #
        check2.click()  # 提交审核
        delete2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[1]')))  #
        delete2.click()  # 点击详情
        time.sleep(2)
        cancel1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[3]/span[4]')))  #
        cancel1.click()  # 在详情页点击取消
        time.sleep(2)
        modification1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[2]')))  #
        modification1.click()  # 点击修改
        time.sleep(2)
        num3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[1]/td[12]/input[5]')))  #
        num3.clear()  #
        num3.send_keys(9)  #
        time.sleep(2)
        outputdurg3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        outputdurg3.send_keys(u"阿奇霉素注射")  #
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()  #
        time.sleep(2)
        save1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        save1.click()  # 点击保存
        driver.refresh()
        check3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[4]')))  #
        check3.click()  # 点击审核
        time.sleep(1)
        check4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_check"]')))  #
        check4.click()  # 在审核页点击审核
        # 耗材入库、审核
        driver.refresh()
        storage1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div/div/ul/li[1]/a/span')))  #
        storage1.click()#点击入库单管理
        time.sleep(2)
        driver.refresh()
        newstorage11 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button')))  #
        newstorage11.click()#点击新增入库单
        type1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select')))  #
        type1.click()  #点击类型
        time.sleep(1)
        InputType = Select(driver.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select'))
        InputType.select_by_value("2")
        time.sleep(1)
        inputconsumable = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable.send_keys(u"一次性换药包")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #
        time.sleep(1)
        consumablenum = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[6]/input')))  #
        consumablenum.send_keys("111")  #
        productdate4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[7]/input')))  #
        productdate4.send_keys(now)  #
        indate4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[8]/input')))  #
        indate4.send_keys(u"2023-10-11")  #
        price = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[9]/input')))  #
        price.send_keys(10)  #
        num4= WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[10]/input[2]')))  #
        num4.clear()  #
        num4.send_keys(10)
        inputconsumable1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable1.send_keys(u"一次性纱布块")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #
        time.sleep(2)
        consumablenum1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[6]/input')))  #
        consumablenum1.send_keys("111")  #
        productdate5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[7]/input')))  #
        productdate5.send_keys(now)  #
        indate5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[8]/input')))  #
        indate5.send_keys(u"2023-10-11")  #
        unitprice4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[9]/input')))  #
        unitprice4.send_keys(10)  #
        num5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[10]/input[2]')))  #
        num5.clear()
        num5.send_keys(10)  #
        inputconsumable2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable2.send_keys(u"一次性自粘敷贴")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[2]').click()  #
        time.sleep(1)
        delete3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[11]/span')))  #
        delete3.click()  #删除一次性自粘敷贴
        producter = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/input')))  #
        producter.send_keys(u"鲁抗制药")  #
        submit1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        submit1.click()  #点击提交审核
        details1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[1]')))  #
        details1.click()  #点击详情
        time.sleep(2)
        cancel2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[5]/span[4]')))  #
        cancel2.click()  #点击取消
        modification2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[2]')))  #
        modification2.click()  #点击修改
        time.sleep(2)
        inputconsumable3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable3.send_keys(u"碘伏棉签")  #
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr/td[2]').click()  #选择碘伏棉签
        time.sleep(1)
        consumablenum2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[6]/input')))  #
        consumablenum2.send_keys(222)#
        productdate6 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[7]/input')))  #
        productdate6.send_keys(now)  #
        indate6 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[8]/input')))  #
        indate6.send_keys(u"2023-10-11")  #
        unitprice5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[9]/input')))  #
        unitprice5.send_keys(10)  #
        num6 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[10]/input[4]')))  #
        num6.clear()  #
        num6.send_keys(10)  #
        inputconsumable4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable4.send_keys(u"碘伏消毒液")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[4]').click()
        time.sleep(1)
        delete4 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[4]/td[11]/span')))  #
        delete4.click()  #
        save2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        save2.click()  #点击保存
        driver.refresh()
        check5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[4]')))  #
        check5.click()  #点击审核
        time.sleep(1)
        check6 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_check"]')))  #
        check6.click()  #在详情页点击审核
        # 耗材出库、审核
        driver.refresh()
        output1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div/div/ul/li[2]/a/span')))  #
        output1.click()  #点击出库单管理
        newoutput1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[1]/div[1]/div[2]/a/button')))  #
        newoutput1.click()  #点击新增出库单
        type2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select')))  #
        type2.click()  #点击类型
        time.sleep(1)
        OutputType = Select(driver.find_element_by_xpath('//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[1]/select'))
        OutputType.select_by_value("2")
        time.sleep(1)
        inputconsumable5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable5.send_keys(u"一次性换药包")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()  #
        time.sleep(1)
        num7 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr/td[11]/input[4]')))  #
        num7.clear() #
        num7.send_keys(5)  #
        inputconsumable6 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable6.send_keys(u"一次性纱布块")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[4]').click()  #
        time.sleep(1)
        inputconsumable7 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable7.send_keys(u"碘伏棉签")  #
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[3]').click()  #
        time.sleep(2)
        delete5 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[3]/td[12]/span')))  #
        delete5.click()  # 点击删除
        inputoffice1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[3]/span/span[1]/span/span[2]')))  #
        inputoffice1.click()  #选择领用科室
        office1 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        office1.send_keys(u"中医全科")  #
        choose = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        choose.send_keys(Keys.ENTER)  #
        people = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div/form/div/ul/li/ul/li/div[4]/span/span[1]/span/span[2]')))  #
        people.click()  #点击领用人
        iuputpeople = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        iuputpeople.send_keys(u"沈志卫")  #
        selectpeople = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))  #
        selectpeople.send_keys(Keys.ENTER)
        check7 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]/button')))  #
        check7.click()#点击提交审核
        details2 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[1]')))  #
        details2.click()  #点击详情
        time.sleep(2)
        cancel3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ajax-content"]/div/div[2]/div[3]/span[4]')))  #
        cancel3.click()  #点击取消
        modification3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[2]')))  #
        modification3.click()  #点击修改
        time.sleep(2)
        num8 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit"]/tbody/tr[2]/td[12]/input[5]')))  #
        num8.clear()  #
        num8.send_keys(3)  #
        inputconsumable8 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choosekey"]')))  #
        inputconsumable8.send_keys(u"碘伏棉签") #
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choose"]/tbody/tr[1]/td[5]').click()  #
        time.sleep(1)
        save3 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_save"]')))  #
        save3.click()  #点击保存
        driver.refresh()
        check8 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="StockBills_menu0"]/span[4]')))  #
        check8.click()  #点击审核
        check9 = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stockIn_edit_check"]')))  #
        check9.click()#在审核页点击审核
if __name__ == '__main__':
    unittest.main()