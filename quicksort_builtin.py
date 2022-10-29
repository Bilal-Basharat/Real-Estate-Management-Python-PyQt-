import csv
from multiprocessing.reduction import duplicate
from os import read
import time
from operator import itemgetter
# from turtle import goto
file = csv.reader(open('AllPakPropertyData.csv', 'r'))
got = [row for row in file]

def extract_price(h, got):
    splited = []
    readable_price = []
    for i in range(1, h-1):
        s = ""
        v = got[i][2]
        splited = v.split(' ')
        var = splited[0]
        if v[len(v)-1] == 'e':
            for t in range(3, len(var), 1):
                s = s+var[t]
            # q=int(s)
            s = float(s)*10000000.0
            readable_price.append(s)
        if v[len(v)-1] == 'b':
            for t in range(3, len(var), 1):
                s = s+var[t]
            # q=int(s)
            q = float(s)*1000000000.0
            readable_price.append(q)
        if v[len(v)-1] == 'h':
            for t in range(3, len(var), 1):
                s = s+var[t]
            q = float(s)*100000.0
            readable_price.append(float(q))
        if v[len(v)-1] == 'd':
            for t in range(3, len(var), 1):
                s = s+var[t]
            q = float(s)*1000.0
            readable_price.append(q)
    return readable_price        
def extract_area(h, got):
    area = []
    for j in range(1, h-1):
        a = ""
        s = 0.0
        v = got[j][4]
        for w in range(0, 4):
            if v[w] == ' ':
                break
            if (v[w] != ' ') and (v[w] != ','):
                a = a+(v[w])
        if v[len(v)-1] == 'l':
            s = float(a)*20.0
            area.append(s)
        if v[len(v)-1] == 'a':
            s = float(a)
            area.append(s)
        if v[len(v)-1] == 'd':
            s = float(a)
            s = s*0.03
            area.append(s)
        if v[len(v)-1] == '.':
            s = float(a)
            s = s*0.03
            area.append(s)
    return area        

area=[]
price=[]
area=extract_area(len(got),got)
price=extract_price(len(got),got)
p=len(price)
for i in range(1, p-2, 1):
    got[i][4] = area[i]
    got[i][2] = price[i]
def partition(got,l,h,col):
    pivot = got[h][col]
    i = l - 1
    for j in range(l, h):
        if got[j][col] <= pivot:
            i = i + 1
            (got[i], got[j]) = (got[j], got[i])
    (got[i + 1], got[h]) = (got[h], got[i + 1])
    return i + 1
def quicksort(got,l,h,col):
    if l<h:
        pi=partition(got,l,h,col)
        quicksort(got, l, pi - 1,col)
        quicksort(got, pi + 1, h,col)
    # sorted(got, key=lambda x:x[2])
quicksort(got,0,len(got)-100,2) 
for i in range (0,100):
    for j in range(0,5):
        print(got[i][j])
    print("\n")             

# def sort(data):
#     if len(data)-50000 > 1:
#         Mid = len(data[0]) // 2
#         l = data[:Mid]
#         r = data[Mid:]
#         sort(l)
#         sort(r)

#         z = 0
#         x = 0
#         c = 0

#         while z < len(l) and x < len(r):
#             if l[z][2] < r[x][2]:
#                 data[c] = l[z]
#                 z += 1
#             else:
#                 data[c] = r[x]
#                 x += 1
#             c += 1

#         while z < len(l):
#             data[c] = l[z]
#             z += 1
#             c += 1

#         while x < len(r):
#             data[c] = r[x]
#             x += 1
#             c += 1
#         # print(data, 'done')
    
  
# # Driver code to test above
# arr = [4, 3, 5, 2, 1, 3, 2, 3]
# n = len(arr)
# quickSortIterative(arr, 0, n-1)
# print ("Sorted array is:")
# print (arr)
# for i in range(n):
# 	print (arr[i])

# This code is contributed by Mohit Kumra
