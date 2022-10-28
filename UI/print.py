import csv

  # reading file to show data
file = csv.reader(open('AllPakPropertyData.csv', 'r'))
rows = [row for row in file]
def printArray(rows):
    print(len(rows))

print(printArray(rows))