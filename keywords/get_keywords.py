#coding=utf-8
from keywords.opera_excel import OperaExcel

class GetKeyWords:
	def __init__(self):
		self.opera_excel = OperaExcel()

	def get_case_lines(self):
		#获取case行数
		lines = self.opera_excel.get_lines()
		return lines

	def get_handle_step(self,row):
		#获取操作步骤里面操作方法的名字
		method_name = self.opera_excel.get_excel_value(row,3)
		return method_name

	def get_element_key(self,row):
		#获取操作元素的key
		element_key = self.opera_excel.get_excel_value(row,4)
		if element_key == '':
			return None
		return element_key

	def get_handle_value(self,row):
		#获取操作元素的值
		handle_value = self.opera_excel.get_excel_value(row,5)
		if handle_value == '':
			return None
		return handle_value

	def get_expect_element(self,row):
		#获取预期结果元素
		expect_element = self.opera_excel.get_excel_value(row,6)
		if expect_element == '':
			return None
		return expect_element

	def get_expect_handle(self,row):
		#获取预期操作步骤
		expect_handle = self.opera_excel.get_excel_value(row,7)
		if expect_handle == '':
			return None
		return expect_handle

	def write_actual_results(self,row,value):
		#获取实际结果
		self.opera_excel.write_value(row,8,value)

	def get_is_run(self,row):
		is_run = self.opera_excel.get_excel_value(row,9)
		if is_run == 'yes':
			return True
		else:
			return False



if __name__ == '__main__':
	get_keywords = GetKeyWord()
	print (get_keywords.get_element_key(7))
	get_keywords.write_actual_results(1,'b')

