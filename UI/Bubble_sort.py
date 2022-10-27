import csv
import time
file = csv.reader(open('E:/mid_project/CS261F22PID42/UI/AllPakPropertyData.csv', 'r'))
rows = [row for row in file]
# for i in range(0,100):
#     for j in range(0,6):
#         print(rows[i][j])
    # print("\n")    
def bubble_sort(arr):
    n = len(arr)-60000
    for i in range(n - 1):
        for j in range(0, n - i - 1,1):
            if arr[j][6] > arr[j + 1][6]:
                print ( arr[j]+ arr[j + 1])
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print ( arr[j]+ arr[j + 1])
                

    return arr
st=time.time()    
sorted_rows = bubble_sort(rows)
# for i in range(0,100):
#      for j in range(0,6):
#          print(rows[i][j])
#      print("\n") 
et=time.time()
t=et-st
# with open('output.csv', 'w') as f:
#     for i in range(0,10000-1):
#         for j in range(0,6):
#             f.writelines(sorted_rows[j][i])
#         f.writelines("\n")    
print(t)
#sorted_rows = bubble_sort(rows)
#print(sorted_rows)
