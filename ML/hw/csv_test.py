import csv  
f = open('twse20150922.csv', 'r')  
for row in csv.reader(f):  
    print row  
f.close()  
