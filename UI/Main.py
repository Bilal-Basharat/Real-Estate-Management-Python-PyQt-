import imp
import sys
import csv
from tkinter.filedialog import Open
import sipbuild
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QTableWidget, QTableView
from PyQt5.QtGui import QPixmap
import sqlite3
from muser import MUser
from mUserDL import MUserDL
import pandas as pd

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
    
    def gotoShowAllData(self):
        showTable = ShowTableData()
        widget.addWidget(showTable)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoExit(self):
        sys.exit(app.exec_())



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
            self.TableWidgetData.setRowCount(73409)
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