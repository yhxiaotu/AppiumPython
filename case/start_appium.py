#coding=utf-8
from appium import webdriver
import time
def get_driver():
	capabilities = {
	    "platformName": "Android",
	    "deviceName": "127.0.0.1:21503",
	    "app": "D:\\imoocapk\\mukewang.apk"
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
	return driver
#获取屏幕宽高
def get_size():
	size = driver.get_window_size()
	width = size['width']
	height = size['height']
	return width,height
#向左滑动
def swipe_left():
	x = get_size()[0]/10
	x1 = get_size()[0]/10*9
	y = get_size()[1]/2
	driver.swipe(x1,y,x,y)
#向右滑动
def swipe_right():
	x = get_size()[0]/10
	x1 = get_size()[0]/10*9
	y = get_size()[1]/2
	driver.swipe(x,y,x1,y,2000)
#向上滑动
def swipe_up():
	x = get_size()[0]/2
	y = get_size()[1]/10*9
	y1 = get_size()[1]/10
	driver.swipe(x,y,x,y1)
#向下滑动
def swipe_down():
	x = get_size()[0]/2
	y = get_size()[1]/10*9
	y1 = get_size()[1]/10
	driver.swipe(x,y1,x,y,2000)
#传入方向参数
def swipe_on(direction):
	if direction == 'left':
		swipe_left()
	elif direction == 'right':
		swipe_right()
	elif direction == 'up':
		swipe_up()
	else:
		swipe_down()

#向左向左向右向左向上，进入注册页
driver = get_driver()
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('right')
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('up')