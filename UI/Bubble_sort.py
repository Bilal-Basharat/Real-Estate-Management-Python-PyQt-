import csv
from multiprocessing.reduction import duplicate
from os import read
import time
file = csv.reader(open('E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv', 'r'))
got = [row for row in file]
# for i in range(0,100):
#     for j in range(0,6):
#         print(rows[i][j])
    # print("\n")  
readable_price=[] 
splited=[]   
h=len(got) #how many rows    
for i in range (1,h-1):
    s=""
    v=got[i][2]
    splited = v.split(' ')
    var=splited[0]
    if v[len(v)-1]=='e':
        for t in range (3,len(var),1): 
            s=s+var[t]
            #q=int(s)
        s = float(s)*10000000.0
        readable_price.append(s)
    if v[len(v)-1]=='b':
        for t in range (3,len(var),1): 
            s=s+var[t]
            #q=int(s)
        s = float(s)*1000000000.0
        readable_price.append(s)
    if v[len(v)-1]=='h':
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)*100000.0
        readable_price.append(float(q)) 
    if v[len(v)-1]=='d':
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)
        readable_price.append(q) 
split=[]
area=[]
for j in range (1,h-1):
    s=""
    v=got[j][4]
    split = v.split(' ')
    a=split[0]
    var=split[1]
    if var[len(v)-1]=='l':
        s=float(a)*20    
        area.append(s)
    if var[len(v)-1]=='a':
        s=float(a)
        area.append(s)
    if var[len(v)-1]=='d':
        s=float(a)*0.03
        area.append(s) 
    if var[len(v)-1]=='.':
        s=float(a)*0.03
        area.append(s)       

# for i in range(10):
#     print(readable_price[i],"LAKH")            
duplicate=got
def bubble_sort(arr,c):
    if c==4:
      for i in range(0,h-2,1):
        arr[i][4]=area[i]       
    if c==3:
        for i in range(0,h-2,1):
            arr[i][3]=readable_price[i]       

    n = len(arr)-50000
    for i in range(n - 1):
        for j in range(0, n - i - 1,1):
            if arr[j][c] > arr[j + 1][c]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

    return arr
st=time.time()    
sorted_rows = bubble_sort(duplicate) #this is to sort on base of price
for i in range(0,1000):#if you wish to apply on string pass {bubble_sort(got)}
    for j in range(0,5):
        print(duplicate[i][j])
    print("\n") 
et=time.time()
t=et-st
# # with open('output.csv', 'w') as f:
# for i in range(0,10000-1):
#     for j in range(0,6):
#             f.writelines(sorted_rows[j][i])
#         f.writelines("\n")    
print(t)
# #sorted_rows = bubble_sort(rows)
# #print(sorted_rows)
