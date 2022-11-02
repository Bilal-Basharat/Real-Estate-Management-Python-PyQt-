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


def search (rows ,columnNo , search):
    n = len(rows)
    list = []    
    for i in range(n - 1):
            if(columnNo == 4):
                value = str(rows[i][columnNo])
                if (isfind(value,search)==True):
                    list.append(rows[i])
            else:
                if (isfind(rows[i][columnNo],search)==True):
                    list.append(rows[i])
                
    return list


# import csv
# file = csv.reader(open('AllPakPropertyData.csv', 'r'))
# rows = [row for row in file]  

    







