#coding=utf-8
import sys
sys.path.append('D:/AppiumPython')
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
from case.app_start_swipe import AppStartSwipe
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ActionMethod:
	def __init__(self,i):
		base_driver = BaseDriver()
		self.driver = base_driver.android_driver(i)
		self.get_by_local = GetByLocal(self.driver)
		self.app_start_swipe = AppStartSwipe(self.driver)

	def get_element(self,*args):
		element = self.get_by_local.get_element(args[0])
		if element == None:
			return None
		return element

	def input(self,*args):
		#输入值
		element = self.get_element(args[0])
		if element == None:
			return args[0], "元素没找到"
		element.send_keys(args[1])

	def on_click(self,*args):
		#元素点击
		element = self.get_element(args[0])
		if element == None:
			return args[0], "元素没找到"
		element.click()

	def sleep_time(self,*args):
		#等待时间
		time.sleep(int(args[0]))

	def page_swipe(self,*args):
		#页面滑动
		self.app_start_swipe.swipe_on(args[0])

	def get_tost(self,*args):
		#获取tost元素信息
		tost_element = ("xpath","//*[contains(@text,"+args[0]+")]")
		return WebDriverWati(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))