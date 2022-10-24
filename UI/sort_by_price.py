import os
import csv
from ssl import Purpose
import pandas as pd

path = "E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv"
df = pd.read_csv(path )
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
    print("index: " + str(i))
    if ' ' in v:
        splited = v.split(' ')
    else:
        splited = v
    var=splited[0]
    if v[len(v)-1]=='e':
        for t in range (3,len(var),1): 
            s=s+var[t]
            #q=int(s)
        print(s)
        s = float(s)
        readable_price.append(s*100)
    else:
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)
        readable_price.append(float(s)) 
def SelectionSort(arr,start,end):
    l=1000000000000.0
    for i in range(start,end,1):
        if arr[i]<l:
            l=arr[i]
            x=i
    arr[x]=0
    return x
sorted_indeces=[]    
for i in range (0,len(readable_price)-1):
    w= SelectionSort(readable_price,0,len(readable_price))   
    sorted_indeces.append(w)
#for i in range (0,len(sorted_indeces)):    
 #   print(Agency_list[sorted_indeces[i]]+Price[sorted_indeces[i]]+City[sorted_indeces[i]])            

       
