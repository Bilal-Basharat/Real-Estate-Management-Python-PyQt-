import csv
import re

  # reading file to show data
file = csv.reader(open('test.csv', 'r'))
rows = [row for row in file]
def convertStrToDigits(rows):
  for i in range(1,len(rows)):
    if 'Crore' in rows[i][2]:
      price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
      value =  float(price[0])
      value = value * 100
      rows[i][2] = value
    elif 'Lakh' in rows[i][2]:
      price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
      value =  float(price[0])
      rows[i][2] = value
    if 'Marla' in rows[i][4]:
      area = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][4])
      square =  float(area[0])
      rows[i][4] = square
    elif 'Kanal' in rows[i][4]:
      area = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][4])
      square =  float(area[0])
      square = square * 20
      rows[i][4] = square
    elif 'Sq. Yd.' in rows[i][4]:
      area = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][4])
      square =  float(area[0])
      square = square / 30
      rows[i][4] = square
  return rows
      

array = printArray(rows)
print(array)