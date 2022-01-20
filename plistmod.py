import csv
import numpy as np
plist=[]
plist_in=[]

with open ('plist.csv',mode='r')as csvfile:
        myreader=csv.reader(csvfile,delimiter=';')
        for i in myreader:
            plist_in.append(i)
for i in plist_in:
    vec_str=i[3]
    val=''
    vec_lis=[]
    for j in vec_str:
        if j=='<' or j==' ':
            pass
        elif j==',' or j=='>':
            vec_lis.append(float(val))
            val=''
        else:
            val+=j
    i[0]=float(i[0])
    i[1]=float(i[1])
    i[2]=float(i[2])
    i[3]=vec_lis
    i[4]=int(i[4])
    lis=[i[0],i[1],i[2],i[3],i[4]]
    plist.append(lis)
for i in range (len(plist)):
    if i in range(0,205):
        plist[i].append(1)
    elif i in range(206,411):
        plist[i].append(2)
    elif i in range(412,617):
        plist[i].append(3)
    elif i in range(618,823):
        plist[i].append(4)
    elif i in range(824,1000):
        plist[i].append(5)
    plist[i].append(0)
with open('plist1.csv','w',newline='') as f:
    writer=csv.writer(f,delimiter=';')
    writer.writerows(plist)
