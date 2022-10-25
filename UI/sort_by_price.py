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
print (City)
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
        s = float(s)
        readable_price.append(s*100.0)
    else:
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)
        readable_price.append(float(s)) 
def Insertionsort(arr,start,ending):
    for i in range(start,ending,1):
        k=arr[i]
        j=i-1
        while k<arr[j] and j>=start:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k  
def merge(arr, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)
	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[p + i]
	for j in range(0, n2):
		R[j] = arr[q + j ]
	i = 0	 
	j = 0	 
	k = p	 
	while i < n1 and j<n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:# this is for to print the last indices of array
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
#sorted_indeces=[]    
#print(sorted_indeces)
st=time.time
def HybridmergeSort(arr, p, r):
    n=r-p
    if(n>43):
        if(p<r):
            q = p+(r-p)//2
            HybridmergeSort(arr, p, q)
            HybridmergeSort(arr, q+1, r)
            merge(arr, p, q, r)
    else:
        Insertionsort(arr,p,r)
HybridmergeSort(readable_price,0,len(readable_price))
et =time.time
t=et-st
print(readable_price) 
print("Total time in Sorting ",t)       
#for i in range (0,len(sorted_indeces)):    
 #   print(Agency_list[sorted_indeces[i]]+Price[sorted_indeces[i]]+City[sorted_indeces[i]])            

       
