#coding=utf-8
import sys
sys.path.append('D:/AppiumPython')
from keywords.get_keywords import GetKeyWords
from keywords.action_method import ActionMethod
from util.server import Server
import time

class RunMain:
	def __init__(self,i):
		server = Server()
		server.main()
		time.sleep(20)    #等待appium完全启动
		self.action_method = ActionMethod(i)

	def run_method(self):
		keywords = GetKeyWords()
		lines = keywords.get_case_lines()
		for i in range(1,lines):
			handle_step = keywords.get_handle_step(i)
			element_key = keywords.get_element_key(i)
			handle_value = keywords.get_handle_value(i)
			expect_element = keywords.get_expect_element(i)
			expect_handle = keywords.get_expect_handle(i)

			excute_handle = getattr(self.action_method,handle_step)
			if element_key != None:
				excute_handle(element_key,handle_value)
			else:
				excute_handle(handle_value)

			if expect_handle != None:
				expect_result = getattr(self.action_method,expect_handle)
				result = expect_result(expect_element)
				if result:
					keywords.write_actual_results(i,'pass')
				else:
					keywords.write_actual_results(i,'fail')
					self.action_method.driver.save_screenshot("../jpg/jpg0"+str(i)+".png")




if __name__ == '__main__':
	run = RunMain(0)
	run.run_method()
