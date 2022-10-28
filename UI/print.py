from ast import And, Or
import csv
from operator import and_
import re

  # reading file to show data
file = csv.reader(open('AllPakPropertyData.csv', 'r'))
rows = [row for row in file]
def printArray(rows):
  print(rows[1][2])
  # for row in rows:
  if ('Crore' in rows[2][2]):
    price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[2][2])
    print(price)
    

print(printArray(rows))