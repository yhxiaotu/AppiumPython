#coding=utf-8
from util.read_init import ReadIni

class GetByLocal:

	def __init__(self,driver):
		self.driver = driver

	def get_element(self,key,section=None):
		read_ini = ReadIni()
		local = read_ini.get_value(key,section)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'classname':
					return self.driver.find_element_by_class_name(local_by)
				elif by == 'classnames':
					return self.driver.find_elements_by_class_name(local_by)
				elif by == 'uiauto':
					return self.driver.find_element_by_android_uiautomator(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				#self.driver.save_screenshot("../jpg/jpg0"+str(i)+".png")
				return None
		else:
			return None