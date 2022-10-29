import csv
from multiprocessing.dummy import Array
import pandas as pd
import re

class SortingAlgo:
# selection sort for ascending order
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
        return array

# selection sort for descending order
    def SelectionSortForStringDescending(array,colNo):
        end = len(array)
        for i in range(end):
            min_idx = i
            min_value = array[i][colNo]
            for j in range(i + 1, end):
                if array[j][colNo] > min_value:
                    min_value = array[j][colNo]
                    min_idx = j
                    
            if min_idx != i:
                temp = array[i]
                array[i] = array[min_idx]
                array[min_idx] = temp
        return array
    
    # insertion sort for ascending order implementation in project
    def InsertionSort(array,start,end,colNo):
        for x in range(start, end):
            temp = array[x]
            key = array[x][colNo]
            j = x - 1
            while j >= start and key < array[j][colNo]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp
        return array

    # insertion sort for descending order implementation in project
    def InsertionSortForDescending(array,start,end,colNo):
        for x in range(start, end):
            temp = array[x]
            key = array[x][colNo]
            j = x - 1
            while j <= start and key > array[j][colNo]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp
        return array
    
    # bubble sort for ascending order implementation in project
    def BubbleSort(array,start,end,colNo):
        for i in range(start,end):
            for j in range(0, len(array) - i - 1): 
                if (array[j][colNo] > array[j + 1][colNo]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array 

    # bubble sort for descending order implementation in project
    def BubbleSortForDescending(array,start,end,colNo):
        for i in range(start,end):
            for j in range(0, len(array) - i - 1): 
                if (array[j][colNo] < array[j + 1][colNo]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array 


# implementing Hybrid Merge Sort Algorithm for ascending order
def HybridMergeSort(array,start,end,colNo):
    
    minRun = end
    
    for i in range(start,end,minRun):
        SortingAlgo.InsertionSort(array, i, min((i+minRun),(end)),colNo)
        size = minRun
        while size < end:
            for j in range(start,end,size*2):
                mid = j + size - 1
                end = min((j + size * 2-1),(end-1))
                merged = hybMerge(colNo, left=array[j:mid+1][colNo], right=array[mid+1:end+1][colNo])
                
                array[j:j+len(merged)][colNo] = merged
        size *= 2
    return array
    
def hybMerge(colNo, left, right):
    i = 0
    j = 0
    l = []
    
    if(len(left) == 0):
        return right
    if(len(right) == 0):
        return left
    
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


# implementing Hybrid Merge Sort Algorithm for descending order
def HybridMergeSortForDescending(array,start,end,colNo):
    
    minRun = end
    
    for i in range(start,end,minRun):
        SortingAlgo.InsertionSortForDescending(array, i, min((i+minRun),(end)),colNo)
        size = minRun
        while size > end:
            for j in range(start,end,size*2):
                mid = j + size - 1
                end = min((j + size * 2-1),(end-1))
                merged = hybMerge(colNo, left=array[j:mid+1][colNo], right=array[mid+1:end+1][colNo])
                
                array[j:j+len(merged)][colNo] = merged
        size *= 2
    return array
    
def hybMerge(colNo, left, right):
    i = 0
    j = 0
    l = []
    
    if(len(left) == 0):
        return right
    if(len(right) == 0):
        return left
    
    while i < len(left) and j < len(right):
        if left[i][colNo] >= right[j][colNo]:
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


# implementing Heap Sort 
def heapify(arr, n, i,colNo):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i][colNo] < arr[l][colNo]:
        largest = l

    if r < n and arr[largest][colNo] < arr[r][colNo]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest,colNo)

def heapSort(arr,colNo):
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i,colNo)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0,colNo)
    return arr

# implementing Heap Sort in descending order 
def heapifyDescending(arr, n, i,colNo):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i][colNo] > arr[l][colNo]:
        largest = l

    if r < n and arr[largest][colNo] > arr[r][colNo]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapifyDescending(arr, n, largest,colNo)

def heapSortDescending(arr,colNo):
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapifyDescending(arr, n, i,colNo)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapifyDescending(arr, i, 0,colNo)
    return arr


# Quick sort implementation in Ascending order
# function to find the partition position
def partition(array, low, high,colNo):

  # choose the rightmost element as pivot
  pivot = array[high][colNo]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j][colNo] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function for performing Quicksort
def quickSort(array, low, high,colNo):
  if low < high:
    # find pivot element such that
    pi = partition(array, low, high,colNo)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1,colNo)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high,colNo)
  return array


# Quick sort implementation in Descending order
# function to find the partition position
def partitionDescending(array, low, high,colNo):

  # choose the rightmost element as pivot
  pivot = array[high][colNo]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j][colNo] > pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function for performing Quicksort
def quickSortDescending(array, low, high,colNo):
  if low < high:
    # find pivot element such that
    pi = partitionDescending(array, low, high,colNo)

    # recursive call on the left of pivot
    quickSortDescending(array, low, pi - 1,colNo)

    # recursive call on the right of pivot
    quickSortDescending(array, pi + 1, high,colNo)
  return array


# merge sort for project
def MergeSort(array,start,end, colNo):
    if len(array) <= 1:
        return array
    p = start
    r = end
    q = len(array) // 2
    left_half = array[:q]
    right_half = array[q:]
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



# data = [[8, 7, 2, 1, 0, 9, 6],[88, 77, 22, 11, 10, 19, 16],[58, 17, 22, 41, 60, 79, 86],[18, 57, 32, 21, 10, 39, 6],[38, 37, 32, 31, 30, 39, 36],[48, 47, 42, 41, 40, 49, 46],[98, 97, 92, 19, 90, 99, 96],[118, 117, 112, 111, 110, 119, 116]]
# data1 = MergeSort(data,0,len(data),5)
# print(data1)

# size = len(data)

# data1 = quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data1)

# arr = [1, 12, 9, 5, 6, 10]
# sortedArray = heapSortDescending(arr)
# # n = len(sortedArray)
# print("Sorted array is",sortedArray)


# file = csv.reader(open('test.csv', 'r'))
# rows = [row for row in file]
# print(SortintAlgo.SelectionSort(rows, 2))

# def main():
# array1 = ['Lahore','Karachi','Abbotabad','RawalPindi','Islamabad']
# # # array1 = [2,3,4,6,1,7,8,10]
# print(SortingAlgo.BubbleSort(array1, 0,len(array1)))
# main()
# for i in range(len(rows)):
#     print(SortintAlgo.SelectionSort(rows, 2))
