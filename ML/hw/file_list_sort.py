class Stock:
	def _init_(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_closing;
	def set_all(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_closing;

class files(list):
	def __init__(self,name,date):
		self.name = name
		self.date = date
	def set_all(self,name,date):
		self.name = name
		self.date = date

	
import csv
import os

Stock_list = []
FileName =[]
file_list = []

folder = '../raw'
#fin = open(file_name,'r')

j=0
k=0

for file_tuple in os.walk(folder):#filesNames is a list of all files in the direction of folder
	j+=1


for i in range(len(file_tuple[2])):
	FileName.append(file_tuple[2][i])
	if i == 0:
		file_list.append(files(FileName[i],int(FileName[i][4:12:1])))
	else:
		for j in range(len(file_list)):
			if file_list[j].date > int(FileName[i][4:12:1]):
				file_list.insert(j,files(FileName[i],int(FileName[i][4:12:1])))
				break
			elif j == len(file_list):
				file_list.append(files(FileName[i],int(FileName[i][4:12:1])))
				break
			j+=1
#			print j
i+=1
print i


'''
for i in range(len(file_tuple[2])):
#	file_list.append(files(FileName[i],FileName[i][4:12:1]))
	k+=1
#	print file_list[i].date
#	print file_list[i].name
#print k	
'''






