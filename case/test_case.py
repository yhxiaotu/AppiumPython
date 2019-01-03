#coding=utf-8
import sys
sys.path.append('D:/AppiumPython')
import unittest
import HTMLTestRunner
import threading
import multiprocessing
import time
from business.login_business import LoginBusiness
from util.server import Server
from appium import webdriver
from util.write_device_command import WriteDeviceCommand

class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		global parames
		parames = parame 

class CaseTest(ParameTestCase):
	@classmethod
	def setUpClass(cls):
		print ('setUpClass------->',parames)
		cls.login_business = LoginBusiness(parames)

	def setUp(self):
		print ("setUp\n")

	def test_case01(self):
		print ("test_case01里面的参数",parames)
		self.login_business.login_error()
		#self.assertEqual(1,2,'数据应相等')
		#self.assertNotEqual(1,2,'数据应不等')
	#跳过单条case
	#@unittest.skip("CaseTest")
	def test_case02(self):
		print ("test_case02里面的参数",parames)
		self.login_business.login_pass()
		#flag = True
		#self.assertTrue(flag)
		#self.assertFalse(flag)

	def tearDown(self):
		print ("tearDown")

	@classmethod
	def tearDownClass(cls):
		print ("tearDownClass")

def appium_init():
	server = Server()
	server.main()

def get_suite(i):
	print ("get_suite里面的",i)
	suite = unittest.TestSuite()	
	suite.addTest(CaseTest("test_case01",parame=i))
	suite.addTest(CaseTest("test_case02",parame=i))
	#unittest.TextTestRunner().run(suite)
	html_file = "D:/AppiumPython/report/report"+str(i)+".html"
	fp = open(html_file,mode='wb')
	HTMLTestRunner.HTMLTestRunner(fp).run(suite)

def get_count():
	write_file = WriteDeviceCommand()
	count = write_file.get_data_lines()
	return count

if __name__ == '__main__':
	appium_init()
	#process = []
	for i in range(get_count()):
		#print (i)
		t = multiprocessing.Process(target=get_suite,args=(i,))
		t.start()
		#threads.append(t)
	# for j in threads:
	# 	j.start()