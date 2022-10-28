import imp
import sys
import re
import csv
import os
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
import Bubble_sort
# from sortingAlgo import SortintAlgo
import test
# searchData = []    
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
        
        # reading data from file 
        file = csv.reader(open('AllPakPropertyData.csv', 'r'))
        rows = [row for row in file]

    def gotoShowAllData(self):
        showTable = ShowTableData()
        widget.addWidget(showTable)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        searchData = rows
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
        loadUi("ShowData.ui",self)        

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
        self.loaddata()
        self.BtnSearch.clicked.connect(self.SearchedData)
        # self.BtnSort.clicked.connect(self.SortData)

        # obtaining combobox from ui file
        self.MainCombo = self.findChild(QComboBox,"CmbxSortByType")
        self.SubCombo = self.findChild(QComboBox,"cmbxSortBySubType")
        
        # adding items into combobox
        # self.MainCombo.lineEdit().setPlaceHolderText("Select")
        self.MainCombo.addItem('Property Type',['House','Flat','Residential Plot','Plot File','Commercial Plot','Agricultural Land'])
        self.MainCombo.addItem('Price',['Ascending','Descending'])
        self.MainCombo.addItem('Area',['Ascending','Descending'])
        self.MainCombo.addItem('Purpose',['For Sale','For Rent'])
        self.MainCombo.addItem('City',['Lahore','Islamabad','Rawalpindi','Karachi','Sialkot','Gujranwala'])
        
        # updating combobox value at runtime
        self.MainCombo.activated.connect(self.UpdateSortByType)


        # function for updating combobox value at runtime
    def UpdateSortByType(self,index):
        self.SubCombo.clear()
        self.SubCombo.addItems(self.MainCombo.itemData(index))
           
    def SearchedData(self):
        searchedText = self.txtSearch.text()
        specifiedSearchArray = test.finalSearchFunction(rows, searchedText)
        self.loaddata(specifiedSearchArray)

    def loaddata(self):
        global searchData
        # showTable = userDashBoard()
        # path = "AllPakPropertyData.csv"
        # with open(path , 'r', newline="") as csvfile:
        #     # create the object of csv.reader()
        #     # df = pd.read_csv(csvfile,delimiter=',')
        #     csvReader = csv.reader(csvfile,delimiter=",")
        #     # self.tableWidgetData = QtWidgets.QTableWidget()
        print(len(searchData))
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
        
        # reading file to show data
        file = csv.reader(open('AllPakPropertyData.csv', 'r'))
        rows = [row for row in file]
        
        newRows = self.convertStrToDigits(rows)        
        print(newRows)
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
        self.loaddata(newRows)
        self.BtnSearch.clicked.connect(self.SearchedData)
        # self.BtnSort.clicked.connect(self.SortData)

        # obtaining combobox from ui file
        self.MainCombo = self.findChild(QComboBox,"CmbxSortByType")
        self.SubCombo = self.findChild(QComboBox,"cmbxSortBySubType")
        
        # adding items into combobox
        # self.MainCombo.lineEdit().setPlaceHolderText("Select")
        self.MainCombo.addItem('Property Type',['House','Flat','Residential Plot','Plot File','Commercial Plot','Agricultural Land'])
        self.MainCombo.addItem('Price',['Ascending','Descending'])
        self.MainCombo.addItem('Area',['Ascending','Descending'])
        self.MainCombo.addItem('Purpose',['For Sale','For Rent'])
        self.MainCombo.addItem('City',['Lahore','Islamabad','Rawalpindi','Karachi','Sialkot','Gujranwala'])
        
        # updating combobox value at runtime
        self.MainCombo.activated.connect(self.UpdateSortByType)

# function for converting unit price and marla unit
    def convertStrToDigits(self, rows):
        for i in range(len(rows)):
            if 'Arab' in rows[i][2]:
                price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)',rows[i][2])
                value =  float(price[0])
                value = value * 10000
                rows[i][2] = value
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

        # function for updating combobox value at runtime
    def UpdateSortByType(self,index):
        self.SubCombo.clear()
        self.SubCombo.addItems(self.MainCombo.itemData(index))
    
    # def SortData(self):
    #     if(self.CmbxSortAlgo.currentText() == "Bubble Sort"):
    #         if(self.MainCombo.currentText() == "Property Type"):
    #             sortedArray = Bubble_sort.bubble_sort(rows, 1,73336)
    #             self.loaddata(sortedArray)

    #         elif(self.MainCombo.currentText() == "City"):
    #             sortedArray = Bubble_sort.bubble_sort(rows, 6,100)
    #             self.loaddata(sortedArray)

    #         elif(self.MainCombo.currentText() == "Purpose"):
    #             sortedArray = Bubble_sort.bubble_sort(rows, 5,len(rows))
    #             self.loaddata(sortedArray)

    #         elif(self.MainCombo.currentText() == "Price"):
    #             sortedArray = Bubble_sort.bubble_sort(rows, 2,100)
    #             self.loaddata(sortedArray)
        
    #         elif(self.MainCombo.currentText() == "Area"):
    #             sortedArray = Bubble_sort.bubble_sort(rows, 4,100)
    #             self.loaddata(sortedArray)
       
        # if(self.CmbxSortAlgo.currentText() == "Selection Sort"):
        #     if(self.MainCombo.currentText() == "Property Type"):
        #         sortedArray = SortintAlgo.SelectionSortForString(rows, 1)
        #         self.loaddata(sortedArray)

        #     elif(self.MainCombo.currentText() == "City"):
        #         sortedArray = SortintAlgo.SelectionSortForString(rows, 6)
        #         self.loaddata(sortedArray)

        #     elif(self.MainCombo.currentText() == "Purpose"):
        #         sortedArray = SortintAlgo.SelectionSortForString(rows, 5)
        #         self.loaddata(sortedArray)

        #     elif(self.MainCombo.currentText() == "Price"):
        #         sortedArray = SortintAlgo.SelectionSort(rows, 2)
        #         self.loaddata(sortedArray)
        
        #     elif(self.MainCombo.currentText() == "Area"):
        #         sortedArray = SortintAlgo.SelectionSort(rows, 4)
        #         self.loaddata(sortedArray)
    
    def SearchedData(self):
        searchedText = self.txtSearch.text()
        specifiedSearchArray = test.finalSearchFunction(rows, searchedText)
        self.loaddata(specifiedSearchArray)

    def loaddata(self, newRows):
        # path = "AllPakPropertyData.csv"
        # with open(path , 'r', newline="") as csvfile:
        #     # create the object of csv.reader()
        #     # df = pd.read_csv(csvfile,delimiter=',')
        #     csvReader = csv.reader(csvfile,delimiter=",")
        #     # self.tableWidgetData = QtWidgets.QTableWidget()
        self.TableWidgetData.setRowCount(len(newRows))
        self.TableWidgetData.setItem(0, 0, QtWidgets.QTableWidgetItem('Agency Name'))
        self.TableWidgetData.setItem(0, 1, QtWidgets.QTableWidgetItem('Type'))
        self.TableWidgetData.setItem(0, 2, QtWidgets.QTableWidgetItem('Price'))
        self.TableWidgetData.setItem(0, 3, QtWidgets.QTableWidgetItem('Location'))
        self.TableWidgetData.setItem(0, 4, QtWidgets.QTableWidgetItem('Area'))
        self.TableWidgetData.setItem(0, 5, QtWidgets.QTableWidgetItem('City'))
        self.TableWidgetData.setItem(0, 6, QtWidgets.QTableWidgetItem("Purpose"))
        self.TableWidgetData.setItem(0, 7, QtWidgets.QTableWidgetItem('Contact'))
        i = 1
        for row in newRows:
            self.TableWidgetData.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.TableWidgetData.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.TableWidgetData.setItem(i, 2, QtWidgets.QTableWidgetItem(int(row[2])))
            self.TableWidgetData.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.TableWidgetData.setItem(i, 4, QtWidgets.QTableWidgetItem(int(row[4])))
            self.TableWidgetData.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.TableWidgetData.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.TableWidgetData.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            i += 1
            
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