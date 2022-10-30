from ast import Import
from tkinter.ttk import Progressbar
from attr import attrs
from select import select
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLResponse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
from csv import writer
from tqdm import tqdm
from Main import ScrapData
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QTableView, QMessageBox, QComboBox,QBoxLayout,QProgressBar

linksList = []
AgencyName = []
propertyType = []
propertyprice = []
propertyLocation = []
propertyArea = []
propertyPurpose = []
# QWidget.setMinimumWidth(800)
# layout = QBoxLayout()
# progressbar = QProgressBar()
# layout.addWidget(progressbar)
# QWidget.setLayout(layout)
def scrapData(scrapURL):
    
    filePath = 'AllPakPropertyData.csv'
    # instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument("--window-size=1920x1080")
    exec_Path = "C:\Program Files (x86)\chromedriver.exe"
    j = 1
    with open(filePath,'a', newline='') as outfile:
        writer = csv.writer(outfile)
        if(scrapURL == "https://www.zameen.com/"):
            urls = scrapURL+"Homes/Lahore-1-"
            for i in range(1,2):
                driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=exec_Path)
                driver.get(urls+str(i)+'.html')
                # driver.maximize_window()
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
                        button = driver.find_element(By.XPATH,('//button[@type="button"][@class="_5b77d672 da62f2ae _8a1d083b"]')).click()
                        # driver.execute_script("arguments[0].click();", button)
                        # href = soup.find('a',class_='_3bb2d41a').text
                        time.sleep(5)
                        pop_up = driver.find_element(By.XPATH,("//div[@class='_2ff591d9']"))
                        no = pop_up.find_element(By.TAG_NAME,'a').text
                        print(no)
                        cityArray = ['Lahore','Karachi','Sialkot','Gujranwala','Islamabad','rawalpindi']
                        for city in cityArray:
                            if city in location:
                                writer.writerow([Agency,type,Price,location,area,purpose,city,no])
                        # progressbar.setValue(j)
                        # j += 1
    # print(AgencyName)
    # print(propertyType)
    # print(propertyprice)
    # print(propertyLocation)
    # print(propertyArea)
    # print(propertyPurpose)
    outfile.close()
    driver.quit()
    driver.close()

