import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from mUserDL import MUserDL
from muser import MUser
from User_DashBoard import userDashBoard
import pandas as pd

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
                self.userDashBoard()
            else:
                self.lblError.setText("Please enter a valid username and password")
    
    def show_popUp(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login")
        msg.setText(message)
        msg.setIcon(QMessageBox.warning)
    def userDashBoard(self):
        app = QApplication(sys.argv)
        dashBoard = userDashBoard()
        widget = QStackedWidget()
        widget.addWidget(dashBoard)
        widget.setFixedSize(800, 600)
        widget.show()
        
if name == "__main__":