#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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
	driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('15811061916')
	driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('llfs1055')
	driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()

def login_by_class():
	#在注册页面，点击已有账号去登录
	elements = driver.find_elements_by_class_name('android.widget.TextView')
	print (len(elements))
	elements[4].click()

def login_by_node():
	element = driver.find_element_by_class_name('android.widget.RelativeLayout')
	elements = element.find_elements_by_class_name('android.widget.EditText')
	elements[0].send_keys('15811061916')
	elements[1].send_keys('111111')
	#父节点用id
	#element = driver.find_element_by_id('cn.com.open.mooc:id/login')
	#element.find_element_by_class_name('android.widget.TextView').click()
	#父节点用class
	#elements = element.find_elements_by_class_name('android.widget.TextView')
	#elements[1].click()
	#通过driver.tap进行坐标定位(登录按钮坐标[201,408][518,468])
	driver.tap([(250,450)],2)
	#通过TouchAction进行坐标定位，需导入TouchAction包(短按:press;释放:release;执行:perform;点击:tap;等待:wait;长按:longPress;取消:cancel)
	#TouchAction(driver).press(x=250, y=450).release().perform()
	#TouchAction(driver).tap(x=250, y=450).perform()

def login_by_uiautomator():
	driver.find_element_by_android_uiautomator('new UiSelector().text("15811061916")').clear()
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys('15811061916')
	driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys(111111)
	driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()

def login_by_xpath():
	driver.find_element_by_xpath('//*[@text="15811061916"]').clear()
	driver.find_element_by_xpath('//*[contains(@text,"手机号")]').send_keys('15811061916')
	#driver.find_element_by_xpath('//android.widget.EditText[contains(@text,"手机号")]').send_keys('15811061916')
	driver.find_element_by_xpath('//*[@resource-id="cn.com.open.mooc:id/password_edit"]').send_keys('111111')
	driver.find_element_by_xpath('//*[@text="登录"]').click()
	#driver.find_element_by_xpath('//android.widget.TextView[@text="登录"]').click()

#原生app与h5切换
def get_web_view():
	#到猿问-有奖问答页面
	elements = driver.find_elements_by_id('cn.com.open.mooc:id/iv_icon')
	elements[2].click()
	#by_android_uiaotumator
	#elements = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/iv_icon")')
	#elements[2].click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[contains(@text,"有奖问答")]').click()
	#获取句柄(窗口webview)
	webview = driver.contexts
	print (webview)
	'''
	#切换到h5页面并点击超链接'AugularJS'
	for viw in webview:
		if viw == "WEBVIEW_cn.com.open.mooc":
			driver.switch_to.context(viw)
			break
	driver.find_element_by_link_text('AngularJS').click()
	#试着不切换窗口点击原生app的返回，不成功则切换原生app点击返回，并抛出不成功异常
	try:
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	except Exception as e:
		driver.switch_to.context(webview[0])
		time.sleep(2)
		driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
		raise e
	'''
	#切换到h5页面并点击超链接'AugularJS'
	driver.switch_to.context(webview[-1])
	driver.find_element_by_link_text('AngularJS').click()
	#切换原生app点击返回
	driver.switch_to.context(webview[0])
	time.sleep(2)
	driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	time.sleep(2)
	#再返回两次到首页
	driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	time.sleep(2)
	driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
	
def logout():
	#进入首页下栏我的
	element = driver.find_element_by_id('cn.com.open.mooc:id/sliding_tabs')
	elements = element.find_elements_by_class_name('android.support.v7.a.a$c')
	elements[3].click()
	time.sleep(2)
	#进入设置
	driver.find_element_by_id('cn.com.open.mooc:id/setting').click()
	time.sleep(2)
	#点击退出
	driver.find_element_by_id('cn.com.open.mooc:id/logout').click()
	driver.find_element_by_xpath('//android.widget.Button[@text="是"]').click()

def get_tost():
	tost_element = ("xpath","//*[contains(@text,'请输入密码')]")
	driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('15811061916')
	driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()
	tost = WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))
	print (tost)
	if tost:
		driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('llfs1055')
		driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()

		
driver = get_driver()
time.sleep(16)
#login_by_id()
#login_by_class()
#login_by_node()
#login_by_uiautomator()
#login_by_xpath()
#time.sleep(3)
#get_web_view()
#logout()
get_tost()