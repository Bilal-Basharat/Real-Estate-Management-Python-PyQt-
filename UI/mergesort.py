import os
import csv
from ssl import Purpose
import pandas as pd
import time
def searchWithAgencyName(df , key):
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
    list=[]
    for i in range(len(Agency_list)):
        sublist=[]
        if (Agency_list[i]==key):
            sublist.append(Agency_list[i])

path = "E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv"
df = pd.read_csv(path)
print (df)








