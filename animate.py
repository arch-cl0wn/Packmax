import vpython as vp
import time 
import csv
global plist,tlist,prod_list,truck_list,textures
'''Format of prod_list: [[name,length,width,height]]'''
truck_list=[['407 TEMPO',9.8,6.4,7],['32 Feet Container',32,8.3,8.2]]
prod_list=[['Home Locker',250,350,320],['Fire Resistant Safe',545,415,435],['Direct Cool refrigerator',1180,576,623],['Slimline',1835,485,50],['Wardrobe',1980,1018,537]]
plist_in=[]
tlist=[]
ptw=1
#tlist format [length,width,height,truck_no]
plist=[]
#plist format [width,height,depth,[position vector],prod_id,truck_no,orientation(0 or 1)]
textures = ['https://i.imgur.com/oas0l7s.png',
                    'https://i.imgur.com/gjCFnwc.png',
                    'https://i.imgur.com/B78s1fr.png',
                    'https://i.imgur.com/2tOUDap.png',
                    'https://i.imgur.com/15kGeQy.png',
                    'https://i.imgur.com/Wc3VQRD.png',
                    'https://i.imgur.com/FFoEnr7.png',
                    'https://i.imgur.com/rlF6dfx.png',
                    'https://i.imgur.com/xllai4t.png',
                    'https://i.imgur.com/grcVF5q.png',
                    'https://i.imgur.com/OvPQfs5.png']

with open ('C:\\Users\\anush\\Desktop\\All_Projects\\PackMax\\Packmax\\plist1.csv',mode='r')as csvfile:
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




with open ('C:\\Users\\anush\\Desktop\\All_Projects\\PackMax\\Packmax\\tlist.csv',mode='r') as csvfile:
        myreader=csv.reader(csvfile,delimiter=';')
        for i in myreader:
            tlist.append(i)
global Speed, SA
Speed=1
SA=False
def PC_SetScene(prod_list):
    global textures
    tx=0   
    vp.scene.width = 1440
    vp.scene.height = 620

    '''Product index'''
    tnol,tnow,tnoh=0,-2550,9000
    bl,bh,mpw=200,200,0
    for produ in prod_list:
        pw=produ[2]
        if pw>mpw:
            mpw=pw
    bl+= 5*mpw
    for produ in prod_list:
        pl=produ[1]
        pw=produ[2]
        ph=produ[3]
        pn=produ[0]
        bh+=ph
        vp.box(pos=vp.vector(tnow,tnoh-0.5,tnol+(pl/2)),length=pl,width=pw,height=ph,texture=textures[tx], opacity=0.6)
        vp.label(pos=vp.vector(tnow+(pw)+(mpw),tnoh-0.5,tnol+(pl/2)+pl),text=pn,color=vp.color.blue,opacity=0.5,box=0,height=15)
        if tx<=10:
            tx+=1
        else:
            tx=0
        tnoh+=ph+50
    bh+=prod_list[0][3]
    
    '''box for Product index'''
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-bh-100),tnol),length=bh,radius=5,axis=vp.vector(0,10,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-bh-100),tnol),length=bl,radius=5,axis=vp.vector(10,0,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100+bl),(tnoh-bh-100),tnol),length=bh,radius=5,axis=vp.vector(0,10,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-100),tnol),length=bl,radius=5,axis=vp.vector(10,0,0))
    vp.label(pos=vp.vector((tnow-(mpw)+100+(bl/2)),(tnoh-100),tnol),text='Index')
    
    '''Axis'''
    vp.arrow(color=vp.color.red, pos=vp.vector(-2550,6000,0), axis=vp.vector(10,0,0), radius=5,length=2000,opacity=0.5)    # X axis
    vp.label(pos=vp.vector(-489,6000,0), text="length", color=vp.color.red, height=15, box=0,opacity=0.5)        # X Label
    vp.arrow(color=vp.color.green, pos=vp.vector(-2550,6000,0), axis=vp.vector(0,10,0), radius=5,length=2000,opacity=0.5)  # Y axis
    vp.label(pos=vp.vector(-2550,8011,0), text="height", color=vp.color.green, height=15, box=0,opacity=0.5)     # Y Label
    vp.arrow(color=vp.color.blue, pos=vp.vector(-2550,6000,0), axis=vp.vector(0,0,10), radius=5,length=2000,opacity=0.5)   # Z axis
    vp.label(pos=vp.vector(-2550,6000,2011), text="width", color=vp.color.blue, height=15, box=0,opacity=0.5)    # Z Label
    '''menu'''
    vp.button(text='Next',bind=NextProd)
    vp.slider(text='Speed',bind=Speedconc,min=0,max=400,value=10)
    vp.checkbox(text='Show All',bind=ShowAll)
    vp.radio(text='Pause/Play',bind=pauseplay)
    vp.scene.append_to_caption('    ')
    vp.button(text='Prev',bind=PrevProd)
def smart_SetScene(prod_list):
    global textures, SA
    tx=0   
    vp.scene.width = 1080
    vp.scene.height = 1500
    tnol,tnow,tnoh=0,-2550,9000
    
    bl,bh,mpw=200,200,0
    for produ in prod_list:
        pw=produ[2]
        if pw>mpw:
            mpw=pw
    bl+= 5*mpw
    
    for produ in prod_list:
        pl=produ[1]
        pw=produ[2]
        ph=produ[3]
        pn=produ[0]

        bh+=ph
        vp.box(pos=vp.vector(tnow,tnoh-0.5,tnol+(pl/2)),length=pl,width=pw,height=ph,texture=textures[tx], opacity=0.6)
        vp.label(pos=vp.vector(tnow+(pw)+(mpw),tnoh-0.5,tnol+(pl/2)+pl),text=pn,color=vp.color.blue,opacity=0.5,box=0,height=15)
        if tx<=10:
            tx+=1
        else:
            tx=0
        tnoh+=ph+50

    bh+=prod_list[0][3]
    
    '''Product index'''
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-bh-100),tnol),length=bh,radius=5,axis=vp.vector(0,10,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-bh-100),tnol),length=bl,radius=5,axis=vp.vector(10,0,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100+bl),(tnoh-bh-100),tnol),length=bh,radius=5,axis=vp.vector(0,10,0))
    vp.cylinder(pos=vp.vector((tnow-(mpw)+100),(tnoh-100),tnol),length=bl,radius=5,axis=vp.vector(10,0,0))
    vp.label(pos=vp.vector((tnow-(mpw)+100+(bl/2)),(tnoh-100),tnol),text='Index')
    
    '''Axis'''
    vp.arrow(color=vp.color.red, pos=vp.vector(-2550,6000,0), axis=vp.vector(10,0,0), radius=5,length=2000,opacity=0.5)    # X axis
    vp.label(pos=vp.vector(-489,6000,0), text="length", color=vp.color.red, height=15, box=0,opacity=0.5)        # X Label
    vp.arrow(color=vp.color.green, pos=vp.vector(-2550,6000,0), axis=vp.vector(0,10,0), radius=5,length=2000,opacity=0.5)  # Y axis
    vp.label(pos=vp.vector(-2550,8011,0), text="height", color=vp.color.green, height=15, box=0,opacity=0.5)     # Y Label
    vp.arrow(color=vp.color.blue, pos=vp.vector(-2550,6000,0), axis=vp.vector(0,0,10), radius=5,length=2000,opacity=0.5)   # Z axis
    vp.label(pos=vp.vector(-2550,6000,2011), text="width", color=vp.color.blue, height=15, box=0,opacity=0.5)    # Z Label
    '''menu'''
    vp.scene.append_to_caption('\n\n')
    vp.button(text='Prev',bind=PrevProd, width=80,align='right')
    vp.scene.append_to_caption('                    ')
    vp.wtext(text='Speed of Animation: ')
    vp.slider(text='Speed',bind=Speedconc,min=0,max=400,step=10, width=15)
    vp.scene.append_to_caption('                    ')
    vp.checkbox(text='Show All',bind=ShowAll)
    vp.scene.append_to_caption('                    ')
    vp.radio(text='Pause/Play',bind=pauseplay)
    vp.scene.append_to_caption('                    ')
    vp.button(text='Next',bind=NextProd, width=80,align='left')

def truck3d(tl,tw,th,tno=1):
    global ptw
    tnol, tnow, tnoh = 0,0,0
    if tno != 1:
        tnow=(tno - 1)*(ptw+500)
        
    tex='truck'+str(tno)
    vp.box(pos=vp.vector(   tnow-0.5,     tnoh+(th/2),    tnol+(tl/2)), length=1, width=tl,height=th,opacity=0.4) # Truck Right 3D
    vp.box(pos=vp.vector(tnow+tw-0.5,     tnoh+(th/2),    tnol+(tl/2)), length=1, width=tl,height=th,opacity=0.4) # Truck Left 3D
    vp.box(pos=vp.vector(tnow+(tw/2),     tnoh+th-0.5,    tnol+(tl/2)), length=tw,width=tl,height=1, opacity=0.4) # Truck Top 3D
    vp.label(pos=vp.vector(tnow+(tw/2),     tnoh+th-0.5,    tnol+(tl/2)),text=tex) # Truck Label
    vp.box(pos=vp.vector(tnow+(tw/2),        tnoh-0.5,    tnol+(tl/2)), length=tw,width=tl,height=1, opacity=0.4) # Truck Base 3D
    vp.box(pos=vp.vector(tnow+(tw/2), tnoh+(th/2)-0.5,           tnol), length=tw,width=1, height=th,opacity=0.4) # Truck Back 3D
    ptw=tw
def product3d(pl,pw,ph,poi,pid,ori):
    global textures,nx,px,Speed
    pid-=1
    if pid>10:
        pid-=10
    posi=list(poi)
    posi[2]+=500
    prod=vp.box(pos=vp.vector(posi[0],posi[1],posi[2]),length=pl,width=pw,height=ph,texture=textures[pid], opacity=0.6) #Product 3D
    if ori==1:
        if Speed!=0:
            time.sleep(0.25/Speed)
            prod.rotate(angle=45,axis=vp.vector(0,1,0))
            time.sleep(0.25/Speed)
            prod.rotate(angle=90,axis=vp.vector(0,1,0))
        else:
            while Speed==0:
                pass
        
    for o in range(25):
        prod.pos-=vp.vector(0,0,20)
        if Speed!=0:
            time.sleep(0.125/Speed)
        else:
            while Speed==0:
                pass
    posi=list(poi)



def NextProd(b) :
    global currentprod,nx
    currentprod+=1
    nx=True
def PrevProd(b):
    global currentprod,px
    currentprod-=1
    px=True
def Speedconc(x):
    global Speed
    Speed=x.value
def pauseplay(c):
    global Speed
    if c.checked==True:
        Speed=0
    elif c.checked==False:
        Speed=1
def ShowAll(c):
    global SA
    if c.checked==True:
        SA=1
    if c.checked==False:
        SA=0

PC_SetScene(prod_list)

#main animation
currentprod,nx,px=0,False,False

for i in tlist:
    currentprod=0
    tno=int(float(i[3]))

    truck3d(float(i[2]),float(i[1]),float(i[0]),tno)
    while currentprod<=(len(plist)-1):
        p=plist[currentprod]
        if p[5]==tno:
            product3d(p[0],p[2],p[1],p[3],p[4],p[6])
        if SA==1:
            currentprod+=1


