import os
import csv
from ssl import Purpose
import pandas as pd
import time

def search (columnNo , search):
    import csv
    file = csv.reader(open('AllPakPropertyData.csv', 'r'))
    rows = [row for row in file]    
    n = len(rows)
    list = []    
    for i in range(n - 1):
            
            if (rows[i][columnNo]==search):
                
                list.append(rows[i])
                
    return list

path = "AllPakPropertyData.csv"
df = pd.read_csv(path)
a =search(1, "House")
print (a)
with open("search.csv" , 'a',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)







