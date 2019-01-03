#coding=utf-8
import sys
sys.path.append("D:/AppiumPython")
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import time
from util.write_device_command import WriteDeviceCommand 

class Server:
	def __init__(self):
		self.dos = DosCmd()
		self.write_file = WriteDeviceCommand()
		self.devices_list = self.get_devices()
	def get_devices(self):
		#获取设备信息device
		devices_list = []
		result_list = self.dos.excute_cmd_result('adb devices')
		if len(result_list) >= 2:
			for i in result_list:
				if 'List' in i:
					continue
				devices_info = i.split('\t')
				if devices_info[1] == 'device':
					devices_list.append(devices_info[0])
			return devices_list
		else:
			print ('有没检测到设备')
			return None

	def get_ports(self,start_port):
		#获取端口port
		port = Port()
		port_list = port.create_port_list(start_port,self.devices_list)
		return port_list

	def create_command_list(self,i):
		#拼接启动命令：appium -p 4700 -bp 4900 -U 127.0.0.1:21503
		if self.devices_list != None:
			appium_port_list = self.get_ports(4700)
			bootstrap_port_list = self.get_ports(4900)
			
			command_list = []
			command = ("appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + self.devices_list[i] + " --no-reset --session-override")
			command_list.append(command)
			self.write_file.write_data(i,self.devices_list[i],str(appium_port_list[i]),str(bootstrap_port_list[i]))
			return command_list
		else:
			print ('创建启动命令失败')
			return None

	def start_server(self,i):
		self.start_list = self.create_command_list(i)
		print (self.start_list)
		self.dos.excute_cmd(self.start_list[0])

	def kill_server(self):
		server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list)>0:
			self.dos.excute_cmd('taskkill -F -PID node.exe')

	def main(self):
		self.kill_server()
		self.write_file.clear_data()
		if self.devices_list != None:
			for i in range(len(self.devices_list)):
				appium_start = threading.Thread(target=self.start_server,args=(i,))
				appium_start.start()
			time.sleep(20)
		else:
			return '启动失败'


if __name__ == '__main__':
	server = Server()
	print (server.main())
