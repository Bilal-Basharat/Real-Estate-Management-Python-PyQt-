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
from csv import writer
from tqdm import tqdm

linksList = []
AgencyName = []
propertyType = []
propertyprice = []
propertyLocation = []
propertyArea = []
propertyPurpose = []

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
    with open(filePath,'a', newline='') as outfile:
        writer = csv.writer(outfile)
        if(scrapURL == "https://www.zameen.com/"):
            urls = scrapURL+"Homes/Lahore-1-"
            for i in range(1,100):
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

