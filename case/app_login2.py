#coding=utf-8
import sys
sys.path.append('D:/AppiumPython')
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.read_init import ReadIni
from util.get_by_local import GetByLocal

def get_driver():
	capabilities = {
	  "platformName": "Android",
	  "automationName": "UiAutomator2",
	  "deviceName": "127.0.0.1:21513",
	  "app": "D:\\imoocapk\\mukewang.apk",
	  "noReset": "true"
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
	return driver

def go_login():
	#在注册页面，点击已有账号去登录
	driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

def login_by_id():
	get_by_local.get_element('username').send_keys('15811061916')
	get_by_local.get_element('password').send_keys('111111')
	get_by_local.get_element('login_button','login_button_element').click()

def login_by_class():
	#在注册页面，点击已有账号去登录
	elements = driver.find_elements_by_class_name('android.widget.TextView')
	print (len(elements))
	elements[4].click()

def login_by_node():
	#没有通过父级节点定位，不会
	#get_by_local = get_by_local.get_element('inputname')
	#获取页面输入框的所有classnames，通过索引定位
	elements = get_by_local.get_element('usernameclass')
	elements[0].send_keys('15811061916')
	elements[1].send_keys('111111')
	#获取登录按钮的classnames
	elements = get_by_local.get_element('login_button_class','login_button_element')
	elements[1].click()

def login_by_uiautomator():
	get_by_local.get_element('useruiautoclear').clear()
	get_by_local.get_element('usernameuiauto').send_keys('15811061916')
	get_by_local.get_element('userpassuiauto').send_keys(111111)
	get_by_local.get_element('login_button_uiauto','login_button_element').click()

def login_by_xpath():
	get_by_local.get_element('usernameclear').clear()
	get_by_local.get_element('usernamexpath').send_keys('15811061916')
	#driver.find_element_by_xpath('//android.widget.EditText[contains(@text,"手机号")]').send_keys('15811061916')
	get_by_local.get_element('passwordxpath').send_keys('111111')
	get_by_local.get_element('login_button_xpath','login_button_element').click()
	#driver.find_element_by_xpath('//android.widget.TextView[@text="登录"]').click()
	
def get_tost():
	tost_element = ("xpath","//*[contains(@text,'请输入密码')]")
	driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('15811061916')
	driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()
	tost = WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))
	print (tost)
	if tost:
		driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('llfs1056')
		driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()

		
driver = get_driver()
time.sleep(10)
get_by_local = GetByLocal(driver)
#login_by_id()
#login_by_node()
#login_by_xpath()
#login_by_uiautomator()
get_tost()