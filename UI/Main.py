import time
import imp
import sys
import csv
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from muser import MUser
from mUserDL import MUserDL
import pandas as pd
import re

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
    
    def checkLogin(self):
        path = "users.csv"
        MUserDL.readDataFromFile(path)
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
                self.lblError.setText("Please fill in the fields")

    def userDashboard(self):
        # self.removeDockWidget(self.parentWidget)
        # sipbuildbilalbisharat@gmail.com
        dashBoard = userDashBoard()
        # widget = QStackedWidget()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)

        # widget.setFixedSize(800, 600)
        # widget.show()
        # sys.exit(app.exec_())

# signup class

class SignUpScreen(QMainWindow):
    def __init__(self):
        super(SignUpScreen,self).__init__()
        loadUi("SignUpPage.ui",self)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignUpBtn.clicked.connect(self.InitiateSignUp)
        # self.BtnBack.clicked.connect(self.WelcomePage)
        
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
        self.BtnExit.clicked.connect(self.gotoExit)
        self.BtnAddProperty.clicked.connect(self.gotoAddProperty)
    
    def gotoShowAllData(self):
        showTable = ShowTableData()
        widget.addWidget(showTable)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoAddProperty(self):
        addProperty = AddPropertyClass()
        widget.addWidget(addProperty)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoExit(self):
        sys.exit(app.exec_())

# Add Property Class
class AddPropertyClass(QMainWindow):
    def __init__(self):
        super(AddPropertyClass,self).__init__()
        loadUi("AddProperty.ui",self)
        self.purpose = ""
        self.PropertyType = ""
        # checking purpose check boxes
        if(self.chckPurposeRent.stateChanged.connect(self.purposeCheck) != None):
            self.purpose = self.chckPurposeRent.stateChanged.connect(self.purposeCheck)
        elif(self.chckPurposeSale.stateChanged.connect(self.purposeCheck) != None):
            self.purpose = self.chckPurposeSale.stateChanged.connect(self.purposeCheck)
        
        # checking Property Type check boxes
        if(self.ChckTypeHouse.stateChanged.connect(self.TypeCheck) != None):
            self.PropertyType = self.ChckTypeHouse.stateChanged.connect(self.TypeCheck)
        if(self.ChckTypeFlat.stateChanged.connect(self.TypeCheck) != None):
            self.PropertyType = self.ChckTypeFlat.stateChanged.connect(self.TypeCheck)
        if(self.ChckTypeFlat.stateChanged.connect(self.TypeCheck) != None):
            self.PropertyType = self.ChckTypeFlat.stateChanged.connect(self.TypeCheck)
        
        # submit add property Form button
        self.BtnSubmit.clicked.connect(self.addPropertyFunc)
    
    # logic function for purpose check boxex
    def purposeCheck(self, state):
        if state == Qt.Checked:
            if self.sender() == self.chckPurposeSale:
                self.chckPurposeRent.setChecked(False)
                return self.chckPurposeSale.text()
            else:
                self.chckPurposeSale.setChecked(False)
                return self.chckPurposeRent.text()
    
    # logic function for property type check boxex
    def TypeCheck(self, state):
        
        if state == Qt.Checked:
            if self.sender() == self.ChckTypeHouse:
                self.ChckTypeFlat.setChecked(False)
                self.ChckTypeFlat.setChecked(False)
                return self.ChckTypeHouse.text()

            elif self.sender() == self.ChckTypeFlat:
                self.ChckTypeHouse.setChecked(False)
                self.ChckTypeFlat.setChecked(False)
                return self.ChckTypeFlat.text()

            elif self.sender() == self.ChckTypeFlat:
                self.ChckTypeHouse.setChecked(False)
                self.ChckTypeFlat.setChecked(False)
                return self.ChckTypeFlat.text()
    # function for writing add property data to the file
    def addPropertyFunc(self):
        # retrieving data from input fields to store in file
        AgencyName  = self.lineAgencyName.text()
        CityName = self.cmbxCity.currentText()
        location = self.lineLocation.text()
        Area = self.cmbxArea.currentText()
        Price = self.linePrice.text()
        Contact = self.lineContactNo.text()

        with open("AllPakPropertyData.csv",'a', newline="") as csvWriter:
            writer = csv.writer(csvWriter)
            writer.writerow([AgencyName,self.PropertyType,Price,location,Area,self.purpose,CityName,Contact])
            csvWriter.close()
        msg = QMessageBox()
        msg.setText("Property Submitted Successfully!")
        msg.setWindowTitle("Added")
        msg.exec_()
        dashBoard = userDashBoard()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Show Table Data
class ShowTableData(QMainWindow):
    def __init__(self):
        super(ShowTableData,self).__init__()
        loadUi("ShowData.ui",self)
        
        # self.tableWidgetData = QtWidgets.QTableWidget()
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

    def loaddata(self):
        path = "AllPakPropertyData.csv"
        with open(path , 'r', newline="") as csvfile:
            # create the object of csv.reader()
            # df = pd.read_csv(csvfile,delimiter=',')
            csvReader = csv.reader(csvfile,delimiter=",")
            # self.tableWidgetData = QtWidgets.QTableWidget()
            self.TableWidgetData.setRowCount(734500)
            i = 0
            for row in csvReader:
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