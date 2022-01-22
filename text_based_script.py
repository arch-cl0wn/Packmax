    # algorithm's module
import _3dbp
import csv
def print_script_info():
    print("Simple python script that simulates the packaging of rectangular boxes of any size.")
    print("Check out the readMe.md file for more info.")

def print_options():
    print("\"exit\" - ends the script.")
    print("\"options\" - shows what you need to type to execute a certain action")
    print("\"create bin\" - create a new bin")
    print("\"bin info\" - get bin's info")
    print("\"add item\" - add an item to unpacked items list")
    print("\"delete item\" - delete an unpacked item from a specific index")
    print("\"delete all unpacked items\" - remove all the items from unpacked items list")
    print("\"unpacked items info\" - get unpacked items info")
    print("\"pack items\" - pack items from items_list to bin")
    print("\"bin items info\" - get bin items info")
    print("\"export data\" - export the data as a csv file")
    print("\"remove bin items\" - remove all the items from current bin")

def vpython_preprocess(lis):
    lis.insert(5,1)
    type=lis[6]
    
    if type == 0: # normal position
        lis[3][0]+=lis[0]/2
        lis[3][1]+=lis[1]/2
        lis[3][2]+=lis[2]/2
        #return (self.width, self.height, self.depth)
    elif type == 1: # rotate Z
        lis[3][1]+=lis[0]/2
        lis[3][0]+=lis[1]/2
        lis[3][2]+=lis[2]/2
        #return (self.height, self.width, self.depth)
    elif type == 2: # rotate Y
        lis[3][0]+=lis[0]/2
        lis[3][2]+=lis[1]/2
        lis[3][1]+=lis[2]/2
        #return (self.width, self.depth, self.height)
    elif type == 3: # rotate X, rotate Y
        lis[3][2]+=lis[0]/2
        lis[3][0]+=lis[1]/2
        lis[3][1]+=lis[2]/2
        #return (self.depth, self.width, self.height)
    elif type == 4: # rotate X
        lis[3][2]+=lis[0]/2
        lis[3][1]+=lis[1]/2
        lis[3][0]+=lis[2]/2
        #return (self.depth, self.height, self.width)
    else: # rotate X, rotate Z
        lis[3][1]+=lis[0]/2
        lis[3][2]+=lis[1]/2
        lis[3][0]+=lis[2]/2
        #return (self.height, self.depth, self.width)
    for i in range(3):
        lis[i]=float(lis[i])
    return lis
def csvinput():
    pass
# Print script info right after script started
print_script_info()

# Show options
print_options()

# initialize bin
bin = None
pno = 1
# initialize unpacked items list
items_list = _3dbp.Items_List()
t=[]

# Script's main loop
while True:
    # get option
    option = input("Choose option...")

    if option == "exit":
        print("Script stopped.")
        break
    elif option == "options":
        print_options()
    elif option == "create bin":
        # get bin's info
        width =float( input("    Type bin's width: "))
        height = float(input("    Type bin's height: "))
        depth = float(input("    Type bin's depth: "))
        width= width*30.48
        height= height*30.48
        depth= depth*30.48
        weightlim=float(input("    Type bin's weightlimit: "))
        weightlim=weightlim*1000
        try:
            bin = _3dbp.Bin("Bin", int(width), int(height), int(depth), int(weightlim))
        except ValueError as e:
            print("Error:", e)
            bin = None
    elif option == "import bin":
        # get bin's info from csv file named 't_dispatch.csv'
        # # format for _dispatch is:
        ''' 
        width,height,depth
        ''' 
        with open("C:\\Users\\anush\\Desktop\\All_Projects\\PackMax\\Packmax\\t_dispatch.csv", "r",newline='') as f:
            reader=csv.reader(f,delimiter=',')
            for row in reader:
                width= float(row[0])*30.48
                height= float(row[1])*30.48
                depth= float(row[2])*30.48
                weightlim=float(row[3])*1000
        try:
            bin = _3dbp.Bin("Bin", int(width), int(height), int(depth), int(weightlim))
        except ValueError as e:
            print("Error:", e)
            bin = None
    elif option == "bin info":
        # display bin's properties
        if bin != None:
            bin.print_data()
        else:
            print("There is no existing bin!")
    elif option == "add item":
        # get item's info
        width = int(input("    Type item's width: "))
        height = int(input("    Type item's height: "))
        depth = int(input("    Type item's depth: "))
        weight= int(input("    Type item's weight:"))
        amount= int(input("    Type item's amount: "))
        width= width//10
        height= height//10
        depth= depth//10
        for i in range(amount):
            try:
                items_list.add_item(_3dbp.Item("Item", int(width), int(height), int(depth), int(pno), int(weight)))
            except ValueError as e:
                print("Error:", e)
        pno+=1
    elif option == "import items":
        # import items info from 'p_dispatch.csv'
        # format for p_dispatch is:
        ''' 
        width1,height1,depth1,amount1
        width2,height2,depth2,amount2
        width3,height3,depth3,amount3
        '''
        with open ('C:\\Users\\anush\\Desktop\\All_Projects\\PackMax\\Packmax\\p_dispatch.csv','r',newline='') as f:
            reader=csv.reader(f,delimiter=',')
            for row in reader:
                width= int(row[0])//10
                height= int(row[1])//10
                depth= int(row[2])//10
                amount= int(row[3])
                weight= int(row[4])
                for i in range(amount):
                    try:
                        items_list.add_item(_3dbp.Item("Item", int(width), int(height), int(depth), int(pno), int(weight)))
                    except ValueError as e:
                        print("Error:", e)
                pno+=1


    elif option == "delete item":
        # get index
        index = input("    Type item's index: ")
        try:
            items_list.delete_item(int(index))
        except ValueError as e:
            print("Error:", e)
    elif option == "delete all unpacked items":
        items_list = _3dbp.Items_List()
    elif option == "unpacked items info":
        # display unpacked items info
        items_list.print_data()
    elif option == "pack items":
        # apply the algorithm to input tuple (bin, unpacked items)
        if bin != None:
            _3dbp.bp3D(bin, items_list.items)
        else:
            print("There is no existing bin!")
    elif option == "bin items info":
        # display info about bin's items
        if bin != None:
            for index in range(len(bin.items)):
                print(str(index) + ")")
                bin.items[index].print_data()
        else:
            print("There is no existing bin!")
    elif option == "export data":
        # export info about bin's items
        if bin != None:
            lis=[]
            for index in range(len(bin.items)):
                plis= bin.items[index].list_data()
                plis= vpython_preprocess(plis)
                lis.append(plis)
            with open('plist.csv','w',newline='') as f:
                writer=csv.writer(f,delimiter=';')
                writer.writerows(lis)

        else:
            print("There is no existing bin!")
    elif option == "remove bin items":
        # remove all bin's items
        bin = _3dbp.Bin("Bin", bin.width, bin.height, bin.depth)
    else:
        print("Option not available. Type \"options\" to see the options")

    # blankline
    print("")

