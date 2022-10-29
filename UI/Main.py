import imp
import sys
import re
import csv
import os
import time
from tracemalloc import start
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QTableWidget, QTableView, QMessageBox, QComboBox,QHBoxLayout
from PyQt5.QtGui import QPixmap
from muser import MUser
from mUserDL import MUserDL
import pandas as pd
import DynamicSearch
# import DynamicSearch
import SpecificSearch
import SpecifiedSearch
from sortingAlgo import SortingAlgo

# searchData = []    
index  = 0
newRows = []
# welcome screen
class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("WelcomePage.ui",self)
        self.LoginBtn.clicked.connect(self.gotoLogin)
        self.SignUpBtn.clicked.connect(self.gotoSignUp)

    def gotoLogin(self): 
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoSignUp(self):
        SignUp = SignUpScreen()
        widget.addWidget(SignUp)
        widget.setCurrentIndex(widget.currentIndex()+1)


# login Class
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("loginpage.ui",self)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbtn.clicked.connect(self.checkLogin)
        self.BtnBack.clicked.connect(self.WelcomePage)
        self.BtnClickHere.clicked.connect(self.signUpPage)
    def WelcomePage(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def signUpPage(self):
        signUp = SignUpScreen()
        widget.addWidget(signUp)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def checkLogin(self):        
        MUserDL.readDataFromFile()
        userEmail = self.txtEmail.text()
        UserPswd = self.txtPassword.text()

        if len(userEmail) == 0 or len(UserPswd) == 0:
            self.lblError.setText('Do not leave any field empty')
        else:
            user = MUser(userEmail, None, UserPswd, None)
            checkUser = MUserDL.SignIn(user)
            if(checkUser != None):
                self.lblError.setText("Login Successfully!")
                self.userDashboard()
            else:
                self.lblError.setText("Please enter a valid username and password")

    def userDashboard(self):
        dashBoard = userDashBoard()
        # widget = QStackedWidget()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)


# signup class

class SignUpScreen(QMainWindow):
    def __init__(self):
        super(SignUpScreen,self).__init__()
        loadUi("SignUpPage.ui",self)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignUpBtn.clicked.connect(self.InitiateSignUp)
        self.BtnBack.clicked.connect(self.WelcomePage)
    def WelcomePage(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def InitiateSignUp(self):
        userEmail = self.txtEmail.text()
        userName = self.txtUserName.text()
        UserPswd = self.txtPassword.text()
        UserRole = self.txtRole.text()
        
        if(len(userEmail) == 0 and len(userName) == 0 and len(UserPswd) == 0 and len(UserRole) == 0):
            self.lblError.setText('Do not leave any field empty')
        else:
            newUser = MUser(userEmail, userName, UserPswd, UserRole)
            userVerify = MUserDL.checkIfUserAlreadyExists(newUser)
            if(userVerify != None):
                MUserDL.addUserIntoList(userVerify)
                MUserDL.storedUserIntoFile(userVerify)
                self.lblError.setText("User Registered Successfully")
                self.resetValues()
            else:
                self.lblError.setText("This user already exists")
# QMessageBox().setText("User Registered Successfully")

        # x = msg.exec_()
    def resetValues(self):
        self.txtEmail.setText("")
        self.txtUserName.setText("")
        self.txtPassword.setText("")
        self.txtRole.setText("")


# user dashboard class
class userDashBoard(QMainWindow):
    def __init__(self):
        super(userDashBoard,self).__init__()
        loadUi("User_Dashboard.ui",self)
        
        self.BtnShowAll.clicked.connect(self.gotoShowAllData)
        self.BtnAdd.clicked.connect(self.gotoAddProperty)
        self.BtnExit.clicked.connect(self.gotoExit)
        self.BtnSearch.clicked.connect(self.multipleSearch)
        self.BtnScrap.clicked.connect(self.ScrapData)
        
        # reading data from file 
        file = csv.reader(open('AllPakPropertyData.csv', 'r'))
        self.rows = [row for row in file]

    def gotoShowAllData(self):
        showTable = ShowTableData()
        widget.addWidget(showTable)
        widget.setCurrentIndex(widget.currentIndex()+1)
   
    def ScrapData(self):
        Scrap = ScrapData()
        widget.addWidget(Scrap)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(800, 100)

    def gotoAddProperty(self):
        showAddProperty = AddProperty()
        widget.addWidget(showAddProperty)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoExit(self):
        sys.exit(app.exec_())
    
    def multipleSearch(self):
        global searchData
        propertyType = self.cmbxType.currentText()
        city = self.cmbxCity.currentText()
        purpose = self.cmbxPurpose.currentText()
        area = self.cmbxArea.currentText()
        PriceFrom = self.txtPriceFrom.text() 
        PriceTo = self.txtPriceTo.text()
        searchData = self.rows
        if(propertyType != 'Property Type'):
            searchData = DynamicSearch.search(searchData ,1, propertyType) 
        if (city !="City"):
            searchData = DynamicSearch.search(searchData ,6,city)
        if (purpose !="Purpose"):
            searchData = DynamicSearch.search(searchData ,5,purpose)
        if (area !="Area ( Unit: Marla )"):
            searchData = DynamicSearch.search(searchData ,4,area)
        showTable = ShowSpecificTableData()
        widget.addWidget(showTable)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


# defining add new property class
class AddProperty(QMainWindow):
    def __init__(self):
        super(AddProperty,self).__init__()
        loadUi("AddProperty.ui",self)
        self.BtnSubmit.clicked.connect(self.submitAddProperty)
    
    def submitAddProperty(self):
        Purpose = self.cmbxPurpose.currentText()
        PropertyType = self.cmbxPropertyType.currentText()
        City = self.cmbxCity.currentText()
        Location = self.lineLocation.text()
        Area = self.cmbxArea.currentText()
        Price = self.linePrice.text()
        AgencyName = self.lineAgencyName.text()
        Contact = self.lineContact.text()
        if(Purpose == "Purpose" and PropertyType == "Property Type" and City == "Select City" and Location == "" and Area == "Select Area" and Price == "" and AgencyName == "" and Contact == ""):
            msg = QMessageBox()
            msg.setText("Please fill in all the fields")
            msg.exec_()
        else:
            path = 'AllPakPropertyData.csv'
            with open(path,'a',encoding="utf-8",newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerow([AgencyName,PropertyType,Price,Location,Area,Purpose,City,Contact])
                fileInput.close()
            msg = QMessageBox()
            msg.setText("Property added successfully")
            msg.exec_()
            self.userDashboard()
        
    def userDashboard(self):
        dashBoard = userDashBoard()
        # widget = QStackedWidget()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Show Specific Table Data
class ShowSpecificTableData(QMainWindow):
    def __init__(self):
        super(ShowSpecificTableData,self).__init__()
        loadUi("ShowSpecificData.ui",self)        
        global searchData
        self.tableWidgetData = QtWidgets.QTableWidget()
        self.TableWidgetData.setColumnWidth(0, 200)
        self.TableWidgetData.setColumnWidth(1, 100)
        self.TableWidgetData.setColumnWidth(2, 150)
        self.TableWidgetData.setColumnWidth(3, 200)
        self.TableWidgetData.setColumnWidth(4, 100)
        self.TableWidgetData.setColumnWidth(5, 100)
        self.TableWidgetData.setColumnWidth(6, 150)
        self.TableWidgetData.setColumnWidth(7, 180)
        # tableWidget.setColumnWidth.setHorizontalHeaderLabels(["Name","Type","Price","Location","Area","Purpose","City","Contact"])
        self.loaddata(searchData)
        self.BtnSearch.clicked.connect(self.SearchedData)

                # back button implementation 
        self.BtnBack.clicked.connect(self.userDashboard)
        
        # exit button implementation 
        self.BtnExit.clicked.connect(self.Exit)

    def userDashboard(self):
        dashBoard = userDashBoard()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Exit(self):
        sys.exit(app.exec_())

    def SearchedData(self):
        global searchData
        searchedText = self.txtSearch.text()
        self.specifiedSearchArray = SpecifiedSearch.finalSearchFunction(searchData, searchedText)
        self.loaddata(self.specifiedSearchArray)

    def loaddata(self, searchData):
        # showTable = userDashBoard()
        # path = "AllPakPropertyData.csv"
        # with open(path , 'r', newline="") as csvfile:
        #     # create the object of csv.reader()
        #     # df = pd.read_csv(csvfile,delimiter=',')
        #     csvReader = csv.reader(csvfile,delimiter=",")
        #     # self.tableWidgetData = QtWidgets.QTableWidget()
        self.TableWidgetData.setRowCount(len(searchData))
        i = 0
        for row in searchData:
            self.TableWidgetData.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.TableWidgetData.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.TableWidgetData.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.TableWidgetData.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.TableWidgetData.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.TableWidgetData.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.TableWidgetData.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.TableWidgetData.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            i += 1
            
# Show Table Data
class ShowTableData(QMainWindow):
    def __init__(self):
        super(ShowTableData,self).__init__()
        loadUi("ShowData.ui",self)
        global newRows
        # reading file to show data
        file = csv.reader(open('AllPakPropertyData.csv', 'r'))
        self.rows = [row for row in file]
        
        self.newRows = self.convertStrToDigits(self.rows)
        
        # back button implementation 
        self.BtnBack.clicked.connect(self.userDashboard)
        
        # exit button implementation 
        self.BtnExit.clicked.connect(self.Exit)

        self.tableWidgetData = QtWidgets.QTableWidget()
        self.TableWidgetData.setColumnWidth(0, 150)
        self.TableWidgetData.setColumnWidth(1, 70)
        self.TableWidgetData.setColumnWidth(2, 100)
        self.TableWidgetData.setColumnWidth(3, 150)
        self.TableWidgetData.setColumnWidth(4, 100)
        self.TableWidgetData.setColumnWidth(5, 100)
        self.TableWidgetData.setColumnWidth(6, 100)
        self.TableWidgetData.setColumnWidth(7, 150)
        # tableWidget.setColumnWidth.setHorizontalHeaderLabels(["Name","Type","Price","Location","Area","Purpose","City","Contact"])
        self.loaddata(self.newRows)
        self.BtnSearch.clicked.connect(self.SearchedData)
        self.BtnSort.clicked.connect(self.SortData)
        
        self.BtnDetails.clicked.connect(self.viewDetails)
        # obtaining combobox from ui file
        self.MainCombo = self.findChild(QComboBox,"CmbxSortByType")
        self.SubCombo = self.findChild(QComboBox,"cmbxSortBySubType")
        
        # adding items into combobox
        # self.MainCombo.lineEdit().setPlaceHolderText("Select")
        self.MainCombo.addItem('Select Column')
        self.MainCombo.addItem('Agency Name')
        self.MainCombo.addItem('Property Type',['House','Flat','Residential Plot','Plot File','Commercial Plot','Agricultural Land'])
        self.MainCombo.addItem('Price',['Ascending','Descending'])
        self.MainCombo.addItem('Location')
        self.MainCombo.addItem('Area',['Ascending','Descending'])
        self.MainCombo.addItem('City',['Lahore','Islamabad','Rawalpindi','Karachi','Sialkot','Gujranwala'])
        self.MainCombo.addItem('Purpose',['For Sale','For Rent'])
        
        # updating combobox value at runtime
        # self.MainCombo.activated.connect(self.UpdateSortByType)

    def userDashboard(self):
        dashBoard = userDashBoard()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Exit(self):
        sys.exit(app.exec_())
   
    def viewDetails(self):
        global index
        # QTableWidget.selectionModel().selectionChanged.connect(self.)
        index = QtWidgets.QTableWidget.currentRow()
        viewPropertyDetails = viewPropertyDetail()
        widget.addWidget(viewPropertyDetails)
        widget.setCurrentIndex(widget.currentIndex()+1)

# function for converting unit price and marla unit
    def convertStrToDigits(self, rows):
        for i in range(len(rows)):
            if 'Arab' in rows[i][2]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
                value =  float(price[0])
                value = value * 10000
                rows[i][2] = value
            elif 'Crore' in rows[i][2]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
                value =  float(price[0])
                value = value * 100
                rows[i][2] = value
            elif 'Lakh' in rows[i][2]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
                value =  float(price[0])
                rows[i][2] = value
            elif 'Thousand' in rows[i][2]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
                value =  float(price[0])
                value = value /100
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

        # function for updating combobox value at runtime
    # def UpdateSortByType(self,index):
    #     self.SubCombo.clear()
    #     self.SubCombo.addItems(self.MainCombo.itemData(index))
       
    def SortData(self):
        import sortingAlgo
        sortedArray = []
        columnArray = ["Agency Name","Property Type","Price","Location","Area","Purpose","City"]
       
        if(self.CmbxSortAlgo.currentText() != "Select Sort Type" and self.MainCombo.currentText() != "Select Column" and self.CmbxSortByOrder.currentText() != "Select Order"):
       
            if(self.CmbxSortByOrder.currentText() == "Ascending"):
       
                #implementing selection sort    
                if(self.CmbxSortAlgo.currentText() == "Selection Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.SelectionSortForString(self.newRows, i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Selection Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)

            #implementing Merge sort    
                elif(self.CmbxSortAlgo.currentText() == "Merge Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.MergeSort(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Merge Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
                    
            #implementing Insertion sort    
                elif(self.CmbxSortAlgo.currentText() == "Insertion Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.InsertionSort(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Insertion Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
        
            #implementing bubble sort    
                elif(self.CmbxSortAlgo.currentText() == "Bubble Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.BubbleSort(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Bubble Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
            
            #implementing hybrid merge sort    
                elif(self.CmbxSortAlgo.currentText() == "HybridMerge Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.HybridMergeSort(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by HybridMerge Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
            
            #implementing Heap sort    
                elif(self.CmbxSortAlgo.currentText() == "Heap Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.heapSort(self.newRows, i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Heap Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
            
            #implementing Quick sort    
                elif(self.CmbxSortAlgo.currentText() == "Quick Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.quickSort(self.newRows,0,len(self.newRows)-1,i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Quick Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)


        #    desceding order algorithms
            elif(self.CmbxSortByOrder.currentText() == "Descending"):
                #implementing selection sort    
                if(self.CmbxSortAlgo.currentText() == "Selection Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.SelectionSortForStringDescending(self.newRows, i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Selection Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
        
            #implementing Merge sort    
                elif(self.CmbxSortAlgo.currentText() == "Merge Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.MergeSortDescending(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Merge Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)

            #implementing Insertion sort    
                elif(self.CmbxSortAlgo.currentText() == "Insertion Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.InsertionSortForDescending(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Insertion Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
        
            #implementing bubble sort    
                elif(self.CmbxSortAlgo.currentText() == "Bubble Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = SortingAlgo.BubbleSortForDescending(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Bubble Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
        
            
            #implementing hybrid merge sort    
                elif(self.CmbxSortAlgo.currentText() == "HybridMerge Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.HybridMergeSortForDescending(self.newRows,0,len(self.newRows), i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by HybridMerge Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)

            #implementing Heap sort    
                elif(self.CmbxSortAlgo.currentText() == "Heap Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.heapSortDescending(self.newRows, i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Heap Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
           
            #implementing Quick sort    
                elif(self.CmbxSortAlgo.currentText() == "Quick Sort"):
                    for i in range(len(columnArray)):
                        if(self.MainCombo.currentText() == columnArray[i]):
                            startTime = time.time()
                        # applying sorting algorithm
                            sortedArray = sortingAlgo.quickSortDescending(self.newRows,0,len(self.newRows)-1,i)
                        # calculating time taken by selection sorting algorithm
                            EndTime = time.time()  
                            totalTime = EndTime- startTime
                            msg = QMessageBox()
                            msg.setText("The time taken by Quick Sort is "+str(totalTime))
                            msg.exec_()
                        # loading data after sorting   
                            self.loaddata(sortedArray)
        else:
            msg = QMessageBox()
            msg.setText("Please select all values from dropdown lists")
            msg.exec_()                

    def SearchedData(self):
        searchedText = self.txtSearch.text()
        specifiedSearchArray = SpecifiedSearch.finalSearchFunction(self.rows, searchedText)
        self.loaddata(specifiedSearchArray)

    def loaddata(self, newRows):  
        self.TableWidgetData.setRowCount(len(newRows)) 
        i = 1
        for row in newRows:
            self.TableWidgetData.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.TableWidgetData.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.TableWidgetData.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TableWidgetData.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.TableWidgetData.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.TableWidgetData.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.TableWidgetData.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.TableWidgetData.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            i += 1
        

class ScrapData(QMainWindow):
    def __init__(self):
        super(ScrapData,self).__init__()
        loadUi("ScrapURL.ui",self)
        self.BtnScrap.clicked.connect(self.scrapDataFromWeb)
    
    def scrapDataFromWeb(self):
        import Property_Scrap
        scrapUrl = self.txtScrapURL.text()
        Property_Scrap.scrapData(scrapUrl)

class viewPropertyDetail(QMainWindow):
    def __init__(self):
        super(viewPropertyDetail,self).__init__()
        loadUi("SingleObjectData.ui",self)
        global index, newRows
         
         # back button implementation 
        self.BtnBack.clicked.connect(self.userDashboard)
        # exit button implementation 
        self.BtnExit.clicked.connect(self.Exit)
        self.lblTitle.setText('Property Details')
        self.lblName.setText(newRows[index][0])
        self.lblType.setText(newRows[index][1])
        self.lblPrice.setText(newRows[index][2])
        self.lblLocation.setText(newRows[index][3])
        self.lblArea.setText(newRows[index][4])
        self.lblPurpose.setText(newRows[index][5])
        self.lblCity.setText(newRows[index][6])
        self.lblContact.setText(newRows[index][7])

    def showTable(self):
        showTableData = showTableData()
        widget.addWidget(showTableData)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Exit(self):
        sys.exit(app.exec_())
      
       
            
#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome = userDashBoard()
# loginPage= LoginScreen()
# signUppage = SignUpScreen()
# user_Dashboard = userDashBoard()
widget.addWidget(welcome)
# widget.addWidget(loginPage)
# widget.addWidget(signUppage)
# widget.addWidget(user_Dashboard)
widget.setFixedSize(800, 600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')