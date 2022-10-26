import os
import csv
from ssl import Purpose
import pandas as pd
import time
# def searchWithAgencyName(df , key):
#     path = "AllPakPropertyData.csv"
#     df = pd.read_csv(path)
#     #print(df.dtypes)
#     Agency_list = df['Agency Name'].values.tolist()
#     Type = df['Type'].values.tolist()
#     Price=df['Price'].values.tolist()
#     location=df['Location'].values.tolist()
#     Area=df['Area'].values.tolist()
#     Purpose_list=df['Purpose'].values.tolist()
#     City=df['City'].values.tolist()
#     readable_price=[]
#     list=[]
   
#     for i in range(1,70):
#         print(i)
#         temp=""
#         if (Type[i]==key):
#             temp = Agency_list[i]+","+Type[i]+","+Price[i]+","+location[i]+","+Area[i]+","+Purpose_list[i]+","+City[i]+","+readable_price[i]+"\n"
            
#             list.append(temp)
#     return list
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







