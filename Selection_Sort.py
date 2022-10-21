def SelectionSort(arr,start,end):
    l=100
    for i in range(start,end,1):
        if arr[i]<l:
            l=arr[i]
            x=i
    temp=arr[start]
    arr[start]=arr[x] 
    arr[x]=temp 
for k in range (0,15,1):   
    SelectionSort(arr,k,15)      