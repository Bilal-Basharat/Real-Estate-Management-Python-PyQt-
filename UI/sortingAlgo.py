import csv
from multiprocessing.dummy import Array
import pandas as pd
import re

class SortingAlgo:

    def SelectionSortForString(array,colNo):
        end = len(array)
        for i in range(end):
            min_idx = i
            min_value = array[i][colNo]
            for j in range(i + 1, end):
                if array[j][colNo] < min_value:
                    min_value = array[j][colNo]
                    min_idx = j
                    
            if min_idx != i:
                temp = array[i]
                array[i] = array[min_idx]
                array[min_idx] = temp
                # array[i], array[min_idx] = array[min_idx], array[i]
        return array
    
    def InsertionSort(array,start,end,colNo):
        for x in range(start, end):
            key = array[x][colNo]
            j = x - 1
            while j >= start and key < array[j][colNo]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        return array

# merge sort for project
def MergeSort(array,start,end, colNo):
    if end <= 1:
        return array
    p = start
    r = end
    q = len(array) // 2
    left_half = array[:q][colNo]
    right_half = array[q:][colNo]
    left = MergeSort(left_half,p,q,colNo)
    right = MergeSort(right_half,q+1,r,colNo)
    return Merge(left, right,colNo)

def Merge(left, right,colNo):    
    i = 0
    j = 0
    l = []
    while i < len(left) and j < len(right):
        if left[i][colNo] <= right[j][colNo]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l
# file = csv.reader(open('test.csv', 'r'))
# rows = [row for row in file]
# print(SortintAlgo.SelectionSort(rows, 2))

# def main():
# array1 = ['Lahore','Karachi','Abbotabad','RawalPindi','Islamabad']
# # array1 = [2,3,4,6,1,7,8,10]
# print(SortintAlgo.InsertionSort(array1, 0,len(array1)))
# main()
# for i in range(len(rows)):
#     print(SortintAlgo.SelectionSort(rows, 2))
