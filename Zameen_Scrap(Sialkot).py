from attr import attrs
from select import select
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from csv import writer
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
linksList = []
AgencyName = []
propertyType = []
propertyprice = []
propertyLocation = []
propertyArea = []
propertyPurpose = []

filePath = 'E:\mid_project\CS261F22PID42/PropertyData(Sialkot).csv'
# file = open(filePath, 'r')
# if(file.read() == None):
#     file = open(filePath,'a')
#     writer = csv.writer(file)
#     writer.writerow['Agency Name','Property Type','Price','Location','Area','Purpose']
    
with open(filePath,'a', newline='') as outfile:
    writer = csv.writer(outfile)
    urls = "https://www.zameen.com/Homes/Sialkot-480-"
    for i in range(1,21):
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        driver.get(urls+str(i)+'.html')
        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')
        linksList = soup.findAll('div', class_="f74e80f3")
        for link in linksList:
            links = link.find('a',class_="_7ac32433")
            url = links['href']
            url = 'https://www.zameen.com' + url 
            driver.get(url)
            page_Content = driver.page_source
            soup = BeautifulSoup(page_Content, 'lxml')
            try:
                soup.find('div',class_="_5a588edf").text
            except AttributeError as error:
                print(error)
            else:
                Agency = soup.find('div',class_="_5a588edf").text
                AgencyName.append(Agency)
                column = soup.find('ul', class_="_033281ab")
                type = column.find('span', {"aria-label" : "Type"}).text
                propertyType.append(type)
                Price = column.find('span', {"aria-label" : "Price"}).text
                propertyprice.append(Price)
                location = column.find('span', {"aria-label" : "Location"}).text
                propertyLocation.append(location)
                area= column.find('span', {"aria-label" : "Area"}).text
                propertyArea.append(area)
                purpose = column.find('span', {"aria-label" : "Purpose"}).text
                propertyPurpose.append(purpose)
                writer.writerow([Agency,type,Price,location,area,purpose])
# print(AgencyName)
# print(propertyType)
# print(propertyprice)
# print(propertyLocation)
# print(propertyArea)
# print(propertyPurpose)
outfile.close()
driver.quit()
driver.close()

