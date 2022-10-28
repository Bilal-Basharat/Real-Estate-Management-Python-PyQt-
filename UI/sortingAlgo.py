import csv
import pandas as pd

class SortintAlgo:
    def SelectionSort(array, start, end):
        for i in range(start,end):
            min_idx = i
            for j in range(i + 1, end):
                if array[j] < array[min_idx]:
                    min_idx = j
            (array[i], array[min_idx]) = (array[min_idx], array[i])
        return array