#coding=utf-8
import sys
sys.path.append("D:/AppiumPython")
from util.dos_cmd import DosCmd

class Port:
	def port_is_used(self,port_num):
		#判断端口是否被占用
		self.dos = DosCmd()
		flag = None
		command = 'netstat -ano | findstr '+str(port_num)
		result = self.dos.excute_cmd_result(command)
		if len(result)>0:
			flag = True
		else:
			flag = False
		return flag

	def create_port_list(self,start_port,devices_list):
		#生成可用端口
		port_list = []
		if devices_list != None:
			#直到端口数等于设备数之前，运行下面代码
			while len(port_list) != len(devices_list):
				#找到没被占用的端口
				if self.port_is_used(start_port) == False:
					#添加到端口列表
					port_list.append(start_port)
				#端口加1
				start_port = start_port + 1
			return port_list
		else:
			print ('生成可用端口失败')
			return None


if __name__ == '__main__':
	'''port = Port()
				li = [1,2,3,4,5]
				print (port.create_port_list(4699,li))'''

	