import collections

tnum=int(input("Enter the number of trucks: "))
tlist_dimensions=[]
truck_dict={}
for i in range(tnum):
    tlist_dimensions.append(float(input("Enter the length: ")))
    tlist_dimensions.append(float(input("Enter the breadth: ")))
    tlist_dimensions.append(float(input("Enter the height: ")))
    truck_dict[i]=tlist_dimensions
    tlist_dimensions=[]

prod_dict={}
prod_dimensions=[]
prod_num=int(input("Enter the number of products: "))
for i in range(prod_num):
    prod_dimensions.append(float(input("Enter the length: ")))
    prod_dimensions.append(float(input("Enter the breadth: ")))
    prod_dimensions.append(float(input("Enter the height: ")))
    prod_dimensions.append(float(input("Enter the weight: ")))
    prod_dict[i]=prod_dimensions
    prod_dimensions=[]

ordered_prod_dict=collections.OrderedDict(sorted(prod_dict.items(), key=lambda kv: kv[1]))

trucks=tnum

for i in range(prod_num-1,0,-1):
    if trucks==1:
        trucks=tnum
    truck_dict[trucks].append(i)
    trucks=trucks-1
    

