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
        s = float(s)
        readable_price.append(s*100.0)
    else:
        for t in range (3,len(var),1): 
            s=s+var[t]
        q=float(s)
        readable_price.append(float(s)) 
st=time.time()
def partition(array, low, high):
  # choose the rightmost element as pivot
  pivot = array[high]
  # pointer for greater element
  i = low - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # return the position from where partition is done
  return i + 1
# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)
    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)
et =time.time()
t=et-st
quickSort(readable_price, 0, 68000)
print(readable_price) 
print("Total time in Sorting ",t)       
#for i in range (0,len(sorted_indeces)):    
 #   print(Agency_list[sorted_indeces[i]]+Price[sorted_indeces[i]]+City[sorted_indeces[i]])            

       
