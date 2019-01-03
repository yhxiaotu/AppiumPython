#coding=utf-8
import configparser

class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = 'D:/AppiumPython/config/LocalElement.ini'
		else:
			self.file_path = file_path
		self.date = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path,encoding="utf-8-sig")
		return read_ini

	def get_value(self,key,section=None):
		if section == None:
			section = 'login_element'
		try:
			value = self.date.get(section,key)
		except:
			value = None
		return value
		

if __name__ == '__main__':
	read_ini = ReadIni()
	print (read_ini.get_value('username','login_element'))