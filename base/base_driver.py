#coding=utf-8
from appium import webdriver
import time
from util.write_device_command import WriteDeviceCommand

class BaseDriver:
	def android_driver(self,i):
		write_file = WriteDeviceCommand()
		device = write_file.get_value('device_info_'+str(i),'deviceName')
		port = write_file.get_value('device_info_'+str(i),'p')
		#print (port)
		capabilities = {
		  "platformName": "Android",
		  #"automationName": "UiAutomator2",
		  "deviceName": device,
		  "app": "D:\\imoocapk\\mukewang.apk",
		  "noReset": "true"
		}
		driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
		time.sleep(10)
		return driver

	def ios_driver(self):
		pass
	def get_driver(self):
		pass	