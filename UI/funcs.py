import random
def RandomArray(size):
    array = []
    min=0
    max=size
    for i in range (0,max):
        num=random.randint(min, max)
        array.append(num)
    return array
def InsertionSort(array,start,end):
    for x in range(start, end):
        key = array[x]
        j = x - 1
        while j >= start and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(0, len(array) - i - 1): 
            if (array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array 
def SelectionSort(array, start, end):
    for i in range(start,end):
        min_idx = i
        for j in range(i + 1, end):
            if array[j] < array[min_idx]:
                min_idx = j
        (array[i], array[min_idx]) = (array[min_idx], array[i])
    return array
def Merge(arr, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0, n1):
		L[i] = arr[p + i]
	for j in range(0, n2):
		R[j] = arr[q + 1 + j]
	i = 0	 
	j = 0	 
	k = p	 
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1    
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def MergeSort(arr, start, end):
    if start < end:
         m = start+(end-start)//2
         MergeSort(arr, start, m)
         MergeSort(arr, m+1, end)
         Merge(arr, start, m, end)
    return arr
def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2
# See if left child of root exists and is
# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l
# See if right child of root exists and is
# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
# Change root, if needed
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
# Heapify the root.
		heapify(arr, n, largest)
# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)
# Build a maxheap.
# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)
# One by one extract elements
	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)
arr = [12, 11, 13, 5, 88887,6, 7, ]
heapSort(arr)
print('Sorted array is')
for i in range(len(arr)):
	print(arr[i])
def bucketSort(array):
    bucket = []
    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])
    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))
# Quick sort in Python
# function to find the partition position
def partition(array, low, high):
  # choose the rightmost element as pivot
  pivot = array[high]
  # pointer for greater element
  i = low - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # return the position from where partition is done
  return i + 1
# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)
    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
# Counting sort in Python programming
def countingSort(array):
    size = len(array)
    output = [0] * size
    # Initialize count array
    count = [0] * 10
    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
# Radix sort in Python
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)
