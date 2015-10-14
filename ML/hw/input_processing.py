class Stock:
	def __init__(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_close;
'''	def set_all(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_closing;
'''

class files(list):
	def __init__(self,name,date):
		self.name = name
		self.date = date
	def set_all(self,name,date):
		self.name = name
		self.date = date

def find_file(list,target):
	for i in range(len(list)):
		print list[len(list)-i-1].name,target
		if(list[len(list)-i-1].name==target):
			return len(list)-i-1

def list_sort(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].date > list[j].date:
				list[i].date , list[j].date=list[j].date,list[i].date 
				list[i].name, list[j].name = list[j].name,list[i].name

def stock_sort(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].name > list[j].name:
				list[i].name,list[j].name=list[j].name,list[i].name
				list[i].date,list[j].date=list[j].date,list[i].date
				list[i].opening,list[j].opening=list[j].opening,list[i].opening
				list[i].closing,list[j].closing=list[j].closing,list[i].closing
				list[i].lowest,list[j].lowest=list[j].lowest,list[i].lowest
				list[i].volume,list[j].volume=list[j].volume,list[i].volume
				list[i].adj_close,list[j].adj_close=list[j].adj_close,list[i].adj_close
				#name,date, opening,closing,highest,lowest,volume,adj_close):

import json, os, sys

jsonIn = []
FileName =[]
file_list = []
Stock_temp = []
Stock_con = []
Stock_list = []
NULL = unicode('NULL')
ID = unicode('id')
folder = '../json/'
j=0
k=0


#user input #

target = sys.argv[1]
start =target[0:4:1]+'-'+target[4:6:1]+'-'+target[6:8:1]+'.json'
end = sys.argv[2]
end =end[0:4:1]+'-'+end[4:6:1]+'-'+end[6:8:1]+'.json'
days = int(sys.argv[3])
saved = sys.argv[4]

#filesNames is a list of all files in the direction of folder
for file_tuple in os.walk(folder):
	j+=1

#
for i in range(len(file_tuple[2])):
	FileName.append(file_tuple[2][i])
	file_list.append(files(FileName[i],int(FileName[i][0:4:1]+FileName[i][5:7:1]+FileName[i][8:10:1])))

#file list sort
list_sort(file_list)

flag=find_file(file_list,start)

for length in range(days+1):
	start = file_list[flag-length].name
	print "start",start
	fin = open(folder+start,"r")

	jsonIn.append(json.load(fin))

	for i in jsonIn[0].keys():
		Stock_list.append(i)
	j=0
	for i in Stock_list:
		if i == ID:
			print ID
		elif (jsonIn[0][i]['open'] == NULL) | (jsonIn[0][i]['close'] == NULL)| (jsonIn[0][i]['high'] == NULL) | (jsonIn[0][i]['low'] == NULL) | (jsonIn[0][i]['volume'] == NULL) | (jsonIn[0][i]['adj_close'] == NULL) :
			print ':NULL'
		else:
			Stock_temp.append(Stock(int(i),int(target[0:4]+target[5:7]+target[8:10]),float(jsonIn[0][i]['open']),float(jsonIn[0][i]['close']),float(jsonIn[0][i]['high']),float(jsonIn[0][i]['low']),float(jsonIn[0][i]['volume']),float(jsonIn[0][i]['adj_close'])))
		j+=1
	stock_sort(Stock_temp)
	Stock_con.append(Stock_temp)
	Stock_temp = []
	jsonIn = []
	Stock_list = []
	fin.close()
print len(Stock_temp)
print len(Stock_con)
print len(Stock_con[2])
for i in range(len(Stock_con)):
	for j in range(len(Stock_con[i])):
		print Stock_con[i][j].name,
	print '\n------------------------------------'


'''
Next step : start to process feeding data
'''




