class Stock:
	def __init__(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self.lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_close;

class files(list):
	def __init__(self,name,date):
		self.name = name
		self.date = date

def list_sort(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].date > list[j].date:
				temp = list[i].date 
				list[i].date = list[j].date
				list[j].date = temp
				temp = list[i].name
				list[i].name = list[j].name
				list[j].name = temp
				
def stock_sort(list):#name,date, opening,closing,highest,lowest,volume,adj_close
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].name > list[j].name:
				temp = list[i].date #date
				list[i].date = list[j].date
				list[j].date = temp
				temp = list[i].name#name
				list[i].name = list[j].name
				list[j].name = temp
				temp = list[i].opening #open
				list[i].opening = list[j].opening
				list[j].opening = temp
				temp = list[i].closing#close
				list[i].closing = list[j].closing
				list[j].closing = temp
				temp = list[i].highest #high
				list[i].highest = list[j].highest
				list[j].highest = temp
				temp = list[i].lowest#low
				list[i].lowest = list[j].lowest
				list[j].lowest = temp
				temp = list[i].volume #vol
				list[i].volume = list[j].volume
				list[j].volume = temp
				temp = list[i].adj_close#adj
				list[i].adj_close = list[j].adj_close
				list[j].adj_close = temp

def find_date(date,days,list)
	


import json
import os

jsonIn = []
FileName =[]
file_list = []
Stock_con = []
Stock_list = []
NULL = unicode('NULL')
ID = unicode('id')
folder = '../json/'
j=0
k=0

target = raw_input(">>>Start:")
target =target[0:4:1]+'-'+target[4:6:1]+'-'+target[6:8:1]+'.json'
end = raw_input(">>>End:")
end =end[0:4:1]+'-'+end[4:6:1]+'-'+end[6:8:1]+'.json'
days = raw_input(">>>Days:")
saved = raw_input(">>>Output path:")


for file_tuple in os.walk(folder):#filesNames is a list of all files in the direction of folder
	j+=1

for i in range(len(file_tuple[2])):
	FileName.append(file_tuple[2][i])
	file_list.append(files(FileName[i],int(FileName[i][0:4:1]+FileName[i][5:7:1]+FileName[i][8:10:1])))
	
list_sort(file_list)
flag=0
while(1)
	find_date(target,days,file_list)
	fin = open(folder+target,"r")
	jsonIn[flag].append(json.load(fin))
	for i in jsonIn[flag][0].keys():
		Stock_list.append(i)

	for i in Stock_list:	#name,date, opening,closing,highest,lowest,volume,adj_close
		if i == ID:
			print ID
		elif (jsonIn[flag][0][i]['open'] == NULL) | (jsonIn[flag][0][i]['close'] == NULL)| (jsonIn[flag][0][i]['high'] == NULL) | (jsonIn[flag][0][i]['low'] == NULL) | (jsonIn[flag][0][i]['volume'] == NULL) | (jsonIn[flag][0][i]['adj_close'] == NULL) :
			print ':NULL'
		else:
			Stock_con.append(Stock(int(i),int(target[0:4]+target[5:7]+target[8:10]),float(jsonIn[flag][0][i]['open']),float(jsonIn[flag][0][i]['close']),float(jsonIn[flag][0][i]['high']),float(jsonIn[flag][0][i]['low']),float(jsonIn[flag][0][i]['volume']),float(jsonIn[flag][0][i]['adj_close'])))
	
	stock_sort(Stock_con)
	flag+=1
