from ast import And, Or
import csv
from operator import and_
import re

  # reading file to show data
file = csv.reader(open('test.csv', 'r'))
rows = [row for row in file]
def printArray(rows):
  # price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[1][2])
  for i in range(len(rows)):
    if 'Crore' in rows[i][2]:
      price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
      price = price * 100
      # rows[i][2] = price
    elif 'Lakh' in rows[i][2]:
      price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
      # rows[i][2] = price
  return price
      

print(printArray(rows))