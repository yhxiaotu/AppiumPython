#coding=utf-8
from appium import webdriver

class AppStartSwipe:
	def __init__(self,driver):
		self.driver = driver

	def get_size(self):
		#获取屏幕宽高
		size = self.driver.get_window_size()
		width = size['width']
		height = size['height']
		return width,height
	
	def swipe_left(self):
		#向左滑动
		x = self.get_size()[0]/10
		x1 = self.get_size()[0]/10*9
		y = self.get_size()[1]/2
		self.driver.swipe(x1,y,x,y)
	
	def swipe_right(self):
		#向右滑动
		x = self.get_size()[0]/10
		x1 = self.get_size()[0]/10*9
		y = self.get_size()[1]/2
		self.driver.swipe(x,y,x1,y,2000)
	
	def swipe_up(self):
		#向上滑动
		x = self.get_size()[0]/2
		y = self.get_size()[1]/10*8
		y1 = self.get_size()[1]/10
		self.driver.swipe(x,y,x,y1)
	
	def swipe_down(self):
		#向下滑动
		x = self.get_size()[0]/2
		y = self.get_size()[1]/10*9
		y1 = self.get_size()[1]/10
		self.driver.swipe(x,y1,x,y,2000)
	
	def swipe_on(self,direction):
		#传入方向参数
		if direction == 'left':
			self.swipe_left()
		elif direction == 'right':
			self.swipe_right()
		elif direction == 'up':
			self.swipe_up()
		else:
			self.swipe_down()