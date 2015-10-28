#!/usr/bin/python

class Stock:
	def __init__(self,name,date, opening,closing,highest,lowest,volume,adj_close,up):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_close;
		self.up = up;
	def set_up(self,up):
		self.up = up

class DI:
	def __init__(self,DI):
		self.DI = DI;

class EMA12:
	def __init__(self,EMA12):
		self.EMA12 = EMA12;

class EMA26:
	def __init__(self,EMA26):
		self.EMA26 = EMA26;
		
class DIF:
	def __init__(self,DIF):
		self.DI = DI;
		
class MACD:
	def __init__(self,MACD):
		self.DI = DI;

class files(list):
	def __init__(self,name,date):
		self.name = name
		self.date = date
	def set_all(self,name,date):
		self.name = name
		self.date = date

def find_file(list,target):
	for i in range(len(list)):
		if(list[len(list)-i-1].name==target):
			return int(len(list)-i-1)
		elif(list[len(list)-i-1].name[5:7]==target[5:7]) & (list[len(list)-i-1].name[8:10]<target[8:10]) | (list[len(list)-i-1].name[5:7]<target[5:7]):
			return int(len(list)-i)
	return -1

def find_end_file(list,target):
	for i in range(len(list)):
		if(list[len(list)-i-1].name==target):
			return int(len(list)-i)
		elif(list[len(list)-i-1].name[5:7]==target[5:7]) & (list[len(list)-i-1].name[8:10]<target[8:10]) | (list[len(list)-i-1].name[5:7]<target[5:7]):
			return int(len(list)-i+1)
	return -1

def find_stock(list,target):
	for i in range(len(list)):
		if(list[len(list)-i-1].name==target):
			return len(list)-i-1
	return -1

def list_sort(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].date > list[j].date:
				list[i].date , list[j].date=list[j].date,list[i].date 
				list[i].name, list[j].name = list[j].name,list[i].name

def NameCmp(name,list):
	for i in range(len(list)):
		if name==list[i]:
			return 0
	else:
		return 1

def stock_sort(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if list[i].name > list[j].name:
				list[i].name,list[j].name=list[j].name,list[i].name
				list[i].date,list[j].date=list[j].date,list[i].date
				list[i].opening,list[j].opening=list[j].opening,list[i].opening
				list[i].closing,list[j].closing=list[j].closing,list[i].closing
				list[i].highest,list[j].highest=list[j].highest,list[i].highest
				list[i].lowest,list[j].lowest=list[j].lowest,list[i].lowest
				list[i].volume,list[j].volume=list[j].volume,list[i].volume
				list[i].adj_close,list[j].adj_close=list[j].adj_close,list[i].adj_close
				list[i].up,list[j].up=list[j].up,list[i].up

import json, os, sys

jsonIn = []
FileName =[]
file_list = []
Stock_temp = []
Stock_con = []
Stock_list = []
null_list = []
null = []
NULL = unicode('NULL')
ID = unicode('id')
taiex = unicode('taiex')
folder = '/home/banana/ML/json/'
j=0
k=0
#user input #
target = sys.argv[1]
start =target[0:4:1]+'-'+target[5:7:1]+'-'+target[8:10:1]+'.json'
end = sys.argv[2]
end =end[0:4:1]+'-'+end[5:7:1]+'-'+end[8:10:1]+'.json'
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

fexc = open("except","w")

flag=find_file(file_list,start)
flag_e=find_end_file(file_list,end)
if flag<5:
	print "No more previous day."
else:
	flag_s=flag - (days-1)
while (flag_s!=flag_e) & (flag_s!=-1) & (flag_e!=-1):
	start = file_list[flag_s].name
	print "start",start
	fin = open(folder+start,"r")

	jsonIn.append(json.load(fin))

	for i in jsonIn[0].keys():
		Stock_list.append(i)
	j=0
	for i in Stock_list:
		if (i == ID)|(i == taiex):
			print ID,
		else:
			try:
#				print int(i),int(start[0:4]+start[5:7]+start[8:10])
				Stock_temp.append(Stock(int(i),int(start[0:4]+start[5:7]+start[8:10]),float(jsonIn[0][i]['open']),float(jsonIn[0][i]['close']),float(jsonIn[0][i]['high']),float(jsonIn[0][i]['low']),float(jsonIn[0][i]['volume']),float(jsonIn[0][i]['adj_close']),99))
			except:
				fexc.write(str(start[0:4]+start[5:7]+start[8:10])+"\t"+str(i)+"\t"+str(jsonIn[0][i]['open'])+"\t"+str(jsonIn[0][i]['close'])+"\t"+str(jsonIn[0][i]['high'])+"\t"+str(jsonIn[0][i]['low'])+"\t"+str(jsonIn[0][i]['volume'])+"\t"+str(jsonIn[0][i]['adj_close'])+"\n")
				Stock_temp.append(Stock(0,0,0,0,0,0,0,0,99))
		j+=1
	stock_sort(Stock_temp)
	Stock_con.append(Stock_temp)
	Stock_temp = []
	jsonIn = []
	Stock_list = []
	fin.close()
	flag_s += 1
fexc.write("Check : \n")

for i in range(len(Stock_con)):
	for j in range(len(Stock_con[i])):#calculate up(1), down(-1) or NULL(99)
		bucket=find_stock(Stock_con[i-1],Stock_con[i][j].name)
		if Stock_con[i][j].name==0:
			Stock_con[i][j].set_up(99)
		elif i==0:
			Stock_con[i][j].set_up(0)
		elif bucket!=-1:
			up_down = Stock_con[i][j].opening - Stock_con[i-1][bucket].opening
			if  up_down>0:
				Stock_con[i][j].set_up(1)
			elif  up_down<0:
				Stock_con[i][j].set_up(-1)
			else:
				Stock_con[i][j].set_up(0)
#		elif bucket == -1:
#			Stock_con[i][j].set_up(0)
		else:
			Stock_con[i][j].set_up(99)

fexc.close()
count=1
label = []
fout = open(saved,"w")
flog = open("log","w")
fnull = open("null","w")
nine_min=0
nine_max=0
rsv=0
YK=50
TK=50
YD=50
TD=50
KD=0
KDY=0
KD_diff=0
MACD_cul=[]


for i in range(len(Stock_con)):
	for j in range(len(Stock_con[i])):
		fnull.write(str(Stock_con[i][j].date)+" "+str(Stock_con[i][j].name)+" "+str(count)+":"+str(Stock_con[i][j].opening)+" "+str(count+1)+":"+str(Stock_con[i][j].closing)+" "+str(count+2)+":"+str(Stock_con[i][j].highest)+" "+str(count+3)+":"+str(Stock_con[i][j].lowest)+" "+str(count+4)+":"+str(Stock_con[i][j].volume)+" "+str(count+5)+":"+str(Stock_con[i][j].adj_close)+str(Stock_con[i][j].up)+"\n")

for i in range(len(Stock_con)-(days-1)):
	for k in range(len(Stock_con[i+(days-1)])):
		if Stock_con[i+(days-1)][k].name != 0:
			temp = Stock_con[i+(days-1)][k].name
			buff =str(Stock_con[i+days-1][k].up)+" "
			for j in range(days):
				label.append(find_stock(Stock_con[i+j],temp))
			for j in range(days):
				if find_stock(Stock_con[i+j],temp)==-1:
					flog.write("-1:"+str(Stock_con[i+j][100].date)+" "+str(temp)+"\n")
					break
				elif Stock_con[i+j][label[j]].up==99:
					flog.write("99:"+str(Stock_con[i+j][label[j]].date)+" "+str(Stock_con[i+j][label[j]].name)+" "+str(1)+": "+str(Stock_con[i+j][label[j]].opening)+" "+str(2)+": "+str(Stock_con[i+j][label[j]].closing)+" "+str(3)+": "+str(Stock_con[i+j][label[j]].highest)+" "+str(4)+": "+str(Stock_con[i+j][label[j]].lowest)+" "+str(5)+": "+str(Stock_con[i+j][label[j]].volume)+" "+str(6)+": "+str(Stock_con[i+j][label[j]].adj_close)+"\n")
					break
				else:
					MACD_cul.append(tech((Stock_con[i+j][label[j]].highest+Stock_con[i+j][label[j]].lowest+2*Stock_con[i+j][label[j]].closing)/4,0))
					if j>=8:
						if j==8:
							for l in range(len(MACD_cul)):
								temp+=MACD_cul[l].DI
							MACD_cul[j].set_MACD(temp/9)
						else:
							MACD_cul[j].set_MACD(MACD_cul[j-1]*4/5+)
						if j==(days-9):
							nine_max=Stock_con[i+j][label[j]].highest
							nine_min=Stock_con[i+j][label[j]].lowest
						elif j>(days-9):
							if nine_min>Stock_con[i+j][label[j]].lowest:
								nine_min=Stock_con[i+j][label[j]].lowest
							if nine_max<Stock_con[i+j][label[j]].highest:
								nine_max=Stock_con[i+j][label[j]].highest
					#	buff+=str(count)+":"+str(Stock_con[i+j][label[j]].opening)+" "+str(count+1)+":"+str(Stock_con[i+j][label[j]].closing)+" "+str(count+2)+":"+str(Stock_con[i+j][label[j]].highest)+" "+str(count+3)+":"+str(Stock_con[i+j][label[j]].lowest)+" "+str(count+4)+":"+str(Stock_con[i+j][label[j]].volume)+" "+str(count+5)+":"+str(Stock_con[i+j][label[j]].adj_close)+" "
						if j ==days-1:
							rsv = ((Stock_con[i+j][label[j]].closing - nine_min )/(nine_max-nine_min))*100
							TK=(2*YK/3)+(rsv/3)
							TD=(2*YD/3)+(TK/3)
							KD=TK-TD
							KD_diff=KD-KDY
							KDY=KD
						#	fout.write(buff)
						#	fout.write(buff+"\n")#+str(count+6)+":"+str(rsv)+" "+str(count+7)+":"+str(TD)+" "+str(count+8)+":"+str(TK)+" "+str(count+9)+":"+str(KD)+" "+str(count+10)+":"+str(KD_diff)+" "+"\n")
							fout.write(buff+str(count)+":"+str(rsv)+" "+str(count+1)+":"+str(TD)+" "+str(count+2)+":"+str(TK)+" "+str(count+3)+":"+str(KD)+" "+str(count+4)+":"+str(KD_diff)+" "+"\n")
							buff = ""
							YD=TD
							TD=0
							YK=TK
							TK=0
							KD=0
							rsv=0
				#	count+=6
		else:
			flog.write("0:\n")
		buff = ""
		label = []
		count=1
fout.close()
flog.close()
fnull.close()