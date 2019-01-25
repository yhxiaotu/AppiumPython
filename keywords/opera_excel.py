#coding=utf-8
import xlrd
from xlutils.copy import copy

class OperaExcel:
	def __init__(self,file_path=None,i=None):
		if file_path == None:
			self.file_path = "D:/AppiumPython/config/keyword_case.xls"
		else:
			self.file_path = file_path
		if i == None:
			i = 0

		self.excel = self.opera_excel()
		self.data = self.get_sheets(i)
		self.write_new_excel = copy(self.excel)
		self.write_data = self.write_get_sheet(i)

	def opera_excel(self):
		#获取整个excel
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheets(self,i):
		#获取哪一个sheet
		tables = self.excel.sheets()[i]
		return tables

	def get_lines(self):
		#获取整个sheet行数
		lines = self.data.nrows
		return lines

	def get_excel_value(self,row,cell):
		#获取excel某行某列的值
		value = self.data.cell(row,cell).value
		return value

	def write_get_sheet(self,i):
		#excel写入操作（先copy原excel，再输入，最后保存）
		write_sheet = self.write_new_excel.get_sheet(i)
		return write_sheet

	def write_value(self,row,cell,value):
		self.write_data.write(row,cell,value)
		self.write_new_excel.save(self.file_path)



if __name__ == '__main__':
	opera_excel = OperaExcel()
	print (opera_excel.get_lines())
	print (opera_excel.get_excel_value(5,4))
	opera_excel.write_value(1,8,'a')