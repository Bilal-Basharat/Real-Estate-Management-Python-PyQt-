import csv
from multiprocessing.dummy import Array
import pandas as pd
import re

class SortintAlgo:
    def SelectionSort(array, columnNo):
        lengthOfArray = len(array)
        for i in range(lengthOfArray):
            if 'Crore' in array[i][columnNo]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',array[i][columnNo])
                price = price * 100
            elif 'Lakh' in array[i][columnNo]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',array[i][columnNo])
                return price
        # for i in range(lengthOfArray):
        #     min_idx = i
        #     for j in range(i + 1, lengthOfArray):
        #         if array[j][columnNo] < array[min_idx][columnNo]:
        #             min_idx = j
        #     (array[i], array[min_idx]) = (array[min_idx], array[i])
        # return array

    def SelectionSortForString(array, start, end):
        for i in range(end):
            min_idx = i
            min_value = array[i]
            for j in range(i + 1, end):
                if array[j] < min_value:
                    min_value = array[j]
                    min_idx = j
                    
            if min_idx != i:
                temp = array[i]
                array[i] = array[min_idx]
                array[min_idx] = temp
                # array[i], array[min_idx] = array[min_idx], array[i]
        return array

file = csv.reader(open('test.csv', 'r'))
rows = [row for row in file]
array = ['Lahore','Karachi','Abbotabad','RawalPindi','Islamabad']
print(SortintAlgo.SelectionSort(rows, 2))

array1 = [2,3,4,6,1,7,8,10]
print(SortintAlgo.SelectionSortForString(array1, 0,len(array1)))
# for i in range(len(rows)):
#     print(SortintAlgo.SelectionSort(rows, 2))


