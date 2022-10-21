def Insertionsort(arr,start,ending):
    for i in range(start,ending,1):
          k=arr[i]
          j=i-1
          while k<arr[j] and j>=start:
            arr[j+1]=arr[j]
            j=j-1
          arr[j+1]=k  
def merge(arr, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)
	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[p + i]
	for j in range(0, n2):
		R[j] = arr[q + j + 1]
	i = 0	 
	j = 0	 
	k = p	 
	while i < n1 and j<n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:# this is for to print the last indices of array
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def HybridmergeSort(arr, p, r):
    n=r-p
    if(n>43):
        if(p<r):
            q = p+(r-p)//2
            HybridmergeSort(arr, p, q)
            HybridmergeSort(arr, q+1, r)
            merge(arr, p, q, r)
    else:
        Insertionsort(arr,p,r)
