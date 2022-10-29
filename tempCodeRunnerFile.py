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
