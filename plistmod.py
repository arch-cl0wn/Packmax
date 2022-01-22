import csv
import numpy as np
plist=[]
plist_in=[]
tlist=[]
with open ('C:\\Users\\anush\\Desktop\\All_Projects\\PackMax\\Packmax\\tlist.csv',mode='r') as csvfile:
        myreader=csv.reader(csvfile,delimiter=';')
        for i in myreader:
            tlist.append(i)


with open ('plist.csv',mode='r')as csvfile:
        myreader=csv.reader(csvfile,delimiter=';')
        for i in myreader:
            plist_in.append(i)
            
n=[0,0,0,0,0,0,0]
for i in plist_in:
    vec_str=i[3]
    val=''
    vec_lis=[]
    for j in vec_str:
        if j=='<' or j==' 'or j=='[':
            pass
        elif j==',' or j=='>' or j==']':
            vec_lis.append(float(val))
            val=''
        else:
            val+=j
    n[0]=float(i[0])
    n[1]=float(i[1])
    n[2]=float(i[2])
    n[3]=vec_lis
    n[4]=int(i[4])
    n[5]=int(i[5])
    n[6]=int(i[6])
    lis=[n[0],n[1],n[2],n[3],n[4],n[5],n[6]]
    plist.append(lis)

for t in range (1,len(tlist)):
    tno=int(tlist[t][3])
    tw=int(tlist[t][1])
    ptw=int(tlist[t-1][1])
    for i in range (len(plist)):
        if plist[i][5]==tno:
            print('jdjsk')
            tnow=(tno-1)*(ptw+500)
            plist[i][3][0]+= tnow
            
            
            
'''for i in range (len(plist)):
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
    plist[i].append(0)'''
with open('plist1.csv','w',newline='') as f:
    writer=csv.writer(f,delimiter=';')
    writer.writerows(plist)
