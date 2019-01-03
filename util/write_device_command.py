#conding=utf-8
import yaml

class WriteDeviceCommand:
	def get_data(self,i,device,port,bp):
		data = {
		"device_info_"+str(i):{
		"deviceName":device,
		"p":port,
		"bp":bp
		}
		}
		return data

	def write_data(self,i,device,port,bp):
		data = self.get_data(i,device,port,bp)
		with open("../config/deviceconfig.yaml","a") as fr:
			yaml.dump(data,fr)

	def clear_data(self):
		with open("../config/deviceconfig.yaml","w") as fr:
			fr.truncate()
		fr.close()

	def read_data(self):
		with open("../config/deviceconfig.yaml") as fr:
			data = yaml.load(fr)
		return data

	def get_value(self,key,port):
		data = self.read_data()
		value = data[key][port]
		return value

	def get_data_lines(self):
		data = self.read_data()
		return len(data)

if __name__ == '__main__':
	write_file = WriteDeviceCommand()
	print (write_file.get_value('device_info_1','deviceName'))
	#print (write_file.get_data_lines())