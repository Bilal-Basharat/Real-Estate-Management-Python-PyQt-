import os
import csv
from ssl import Purpose
import pandas as pd
import time
def find(value , search):
    for i in range(len(search)):
       

        if (search[i] != value[i]):
            return False
    return True

def isfind(value , search):
    for i in range (len(value)):
        if (value[i] == search[0]):
          
            
            if( (find(value[i:len(value)+1], search))==True):
                return True
    return False


def search (columnNo , search):
    import csv
    file = csv.reader(open('D:/semester 2/Dsa/midterm-project/CS261F22PID42/UI/AllPakPropertyData.csv', 'r'))
    rows = [row for row in file]    
    n = len(rows)
    list = []    
    for i in range(n - 1):
            
            if (isfind(rows[i][columnNo],search)==True):
                
                list.append(rows[i])
                
    return list

a =search(1, "Portion")
print (a)
with open("search.csv" , 'w',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)
    







