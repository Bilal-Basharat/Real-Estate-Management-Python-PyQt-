import os
import csv
from ssl import Purpose
import pandas as pd
import time

path = "E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv"
df = pd.read_csv(path)
#print(df.dtypes)
Agency_list = df['Agency Name'].values.tolist()
Type = df['Type'].values.tolist()
Price=df['Price'].values.tolist()
location=df['Location'].values.tolist()
Area=df['Area'].values.tolist()
Purpose_list=df['Purpose'].values.tolist()
City=df['City'].values.tolist()
readable_price=[]

for i in range (0,len(Price)):
    s=""
    v=Price[i]
    if ' ' in v:
        splited = v.split(' ')
    else:
        splited = v
    var=splited[0]
    if v[len(v)-1]=='e':
        for t in range (3,len(var),1): 
            s=s+var[t]
            #q=int(s)
        s = float(s)*100000000
        readable_price.append(s)
    else:
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)*1000000
        readable_price.append(float(s)) 
#w=len(readable_price)
#print(w)        
for i in range(0,len(readable_price),1):
    print(readable_price[i])
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(0, end - i - 1): 
            if (array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                t1=Area[j]
                Area[j]=Area[j+1]
                Area[j+1]=t1
                t2=City[j]
                City[j]=City[j+1]
                City[j+1]=t2
    return array 
# st=time.time()
# for i in range (0,100):
#     print(Area[i]," ",City[i]," ",Price[i])
# BubbleSort(readable_price, 0, 100)
# print("After sorting")
# print("\n")
# print("\n")
# for i in range (0,100):
#     print(Area[i]," ",City[i]," ",Price[i])
# et =time.time()
# t=et-st
# print("Total time in Sorting ",t)       
#for i in range (0,len(sorted_indeces)):    
 #   print(Agency_list[sorted_indeces[i]]+Price[sorted_indeces[i]]+City[sorted_indeces[i]])            

       
