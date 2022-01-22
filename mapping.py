import collections
import csv

tnum=int(input("Enter the number of trucks: "))
tlist_dimensions=[]
with open ('/Users/shamoon/Projects/Packmax/t_dispatch.csv',mode='w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in range(tnum):
        tlist_dimensions.append(float(input("Enter the length: ")))
        tlist_dimensions.append(float(input("Enter the breadth: ")))
        tlist_dimensions.append(float(input("Enter the height: ")))
        csvwriter.writerow(tlist_dimensions)
        tlist_dimensions=[]

prod_num=int(input("Enter the number of products: "))
prod_dict={}
prod_details=[]

for i in range(prod_num):
    prod_details.append(float(input("Enter the length: ")))
    prod_details.append(float(input("Enter the breadth: ")))
    prod_details.append(float(input("Enter the height: ")))
    prod_details.append(float(input("Enter the weight: ")))
    prod_details.append(int(input("Enter number of units: ")))
    prod_dict[i]=prod_details
    prod_details=[]


ordered_prod_dict=collections.OrderedDict(sorted(prod_dict.items(), key=lambda kv: kv[1]))

trucks=tnum

for i in range(prod_num-1,0,-1):
    for j in range(prod_dict[prod_num][4]):
        if trucks==1:
            trucks=tnum
        prod_dict.append[trucks]
        trucks=trucks-1
    
with open ('/Users/shamoon/Projects/Packmax/p_dispatch.csv',mode='w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    for key in prod_dict:
        csvwriter.writerow(prod_dict[key])
