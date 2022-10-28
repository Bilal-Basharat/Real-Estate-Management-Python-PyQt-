import os
import csv
from ssl import Purpose
import pandas as pd
import time
rows = []
def find(value , search):
    for i in range(len(search)):
       
        
        if (search[i] != value[i]):
            return False
    return True

def isfind(value , search):
    for i in range (len(value)-1):
        if (value[i] == search[0]):
          
            
            if( (find(value[i:len(value)+1], search))==True):
                return True
    return False


def search (row ,columnNo , search):
    # global rows
    # rows = row 
    n = len(row)
    list = []    
    for i in range(n - 1):
            if (i<len(row)):

                if (isfind(row[i][columnNo],search)==True):
                    # 
                    list.append(row[i])
                    row.remove(row[i])
        
    return list
def finalSearchFunction(rows , key):
    a=[]
    for i in range(7):
        a = a + search(rows,i, key)
    return a
    




# import csv
# file = csv.reader(open('AllPakPropertyData.csv', 'r'))
# rows = [row for row in file] 
# a= finalSearchFunction(rows, "Karachi")
# # print (a)
# with open("search.csv" , 'w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(a)
    







