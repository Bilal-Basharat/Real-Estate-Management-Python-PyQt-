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
# import DynamicSearch
import SpecificSearch
# import Bubble_sort

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

# Show Table Data
class ShowTableData(QMainWindow):
    def __init__(self):
        super(ShowTableData,self).__init__()
        loadUi("ShowData.ui",self)
        
        # reading file to show data
        file = csv.reader(open('AllPakPropertyData.csv', 'r'))
        rows = [row for row in file]

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
        self.loaddata(rows)
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
    
    # def SortData(self, rows):
    #     if(self.MainCombo.currentText() == "Property Type"):
    #         sortedArray = Bubble_sort.bubble_sort(rows, 2)
    #         self.loaddata(sortedArray)

    #     elif(self.MainCombo.currentText() == "City"):
    #         sortedArray = Bubble_sort.bubble_sort(rows, 7)
    #         self.loaddata(sortedArray)

    #     elif(self.MainCombo.currentText() == "Purpose"):
    #         sortedArray = Bubble_sort.bubble_sort(rows, 6)
    #         self.loaddata(sortedArray)

    #     elif(self.MainCombo.currentText() == "Price"):
    #         sortedArray = Bubble_sort.bubble_sort(rows, 3)
    #         self.loaddata(sortedArray)
       
    #     elif(self.MainCombo.currentText() == "Area"):
    #         sortedArray = Bubble_sort.bubble_sort(rows, 5)
    #         self.loaddata(sortedArray)
    
    def SearchedData(self, rows):
        searchedText = self.txtSearch.text()
        specifiedSearchArray = SpecificSearch.finalSearchFunction(rows, searchedText)
        self.loaddata(specifiedSearchArray)

    def loaddata(self, rows):
        # path = "AllPakPropertyData.csv"
        # with open(path , 'r', newline="") as csvfile:
        #     # create the object of csv.reader()
        #     # df = pd.read_csv(csvfile,delimiter=',')
        #     csvReader = csv.reader(csvfile,delimiter=",")
        #     # self.tableWidgetData = QtWidgets.QTableWidget()
        self.TableWidgetData.setRowCount(len(rows))
        i = 0
        for row in rows:
            self.TableWidgetData.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.TableWidgetData.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.TableWidgetData.setItem(i, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.TableWidgetData.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.TableWidgetData.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.TableWidgetData.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.TableWidgetData.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.TableWidgetData.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            i += 1
            
#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome = WelcomeScreen()
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