#coding=utf-8
import sys
sys.path.append('D:/AppiumPython')
from handle.login_handle import LoginHandle

class LoginBusiness:
	def __init__(self,i):
		self.login_handle = LoginHandle(i)

	def login_pass(self):
		self.login_handle.send_username('15811061916')
		self.login_handle.send_password('llfs1056')
		self.login_handle.click_login()

	def login_error(self):
		self.login_handle.send_username('15811061916')
		#self.login_handle.send_password('111111')
		self.login_handle.click_login()
		'''
		user_flag = self.login_handle.get_fail_tost('请输入密码')
		if user_flag:
			self.login_pass()
		else:
			print ('登录失败')
		'''

if __name__ == '__main__':
	login_business = LoginBusiness()
	login_business.login_error()