# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "DUK_AL20"
caps["appPackage"] = "com.taobao.taobao"
caps["appActivity"] = "com.taobao.tao.welcome.Welcome"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("法律声明及隐私权政策核心条款弹窗")
el1.click()
el2 = driver.find_element_by_accessibility_id("法律声明及隐私权政策核心条款弹窗")
el2.click()
el3 = driver.find_element_by_id("com.taobao.taobao:id/yes")
el3.click()
el5 = driver.find_element_by_id("com.taobao.taobao:id/uik_mdButtonDefaultPositive")
el5.click()
el6 = driver.find_element_by_id("android:id/icon")
el6.click()
el7 = driver.find_element_by_accessibility_id("¥151.00")
el7.click()

driver.quit()