import csv
from multiprocessing.reduction import duplicate
from os import read
import time
file = csv.reader(open('E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv', 'r'))
got = [row for row in file]
h=len(got)
area=[]
readable_price=[] 
  
def extract_price():
    splited=[] 
    var=""  
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
def extract_area():
    for j in range (1,h-1):
        a=""
        s=0.0
        v=got[j][4]
        for w in range(0,4):
            if v[w]==' ':
                break
            if (v[w]!=' ')and(v[w]!=','):
                a=a+(v[w])    
    
        if v[len(v)-1]=='l':
            s=float(a)*20.0    
            area.append(s)
        if v[len(v)-1]=='a':
            s=float(a)
            area.append(s)
        if v[len(v)-1]=='d':
            s=float(a)
            s=s*0.03
            area.append(s) 
        if v[len(v)-1]=='.':
            s=float(a)
            s=s*0.03
            area.append(s)       
# for i in range(0,50):
    # print(area[i])
# for i in range(10):
#     print(readable_price[i],"LAKH")            
duplicate=got
def Selectionsort(arr,c):
    min_idx=0
    if c==4:#this 4 is for area
      extract_area()
      for i in range(1,h-2,1):
        arr[i][4]=area[i]       
    if c==2:    #this is for price 
        extract_price()
        for i in range(1,h-2,1):
            arr[i][2]=readable_price[i]       
    n = len(arr)-1000
    for i in range(1,n-1):
        min=10000000000.0
        for j in range(i + 1, n):
            if arr[j][c] < min:
                min=arr[j][c]
                min_idx = j
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
    return arr
st=time.time()    
sorted_rows = Selectionsort(duplicate,2) #this is to sort on base of price
for i in range(1,200):#if you wish to apply on string pass {bubble_sort(got)}
    for j in range(0,5):
        print(sorted_rows[i][j])
    print("\n") 
et=time.time()
t=et-st
print(t)
# # with open('output.csv', 'w') as f:
# for i in range(0,10000-1):
#     for j in range(0,6):
#             f.writelines(sorted_rows[j][i])
#         f.writelines("\n")    
# #sorted_rows = bubble_sort(rows)
# #print(sorted_rows)
