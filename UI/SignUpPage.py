import sys
from tkinter.messagebox import NO
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox ,QApplication, QWidget, QStackedWidget, QMainWindow, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from mUserDL import MUserDL
from muser import MUser
import csv
from csv import writer

class SignUpScreen(QMainWindow):
    def __init__(self):
        super(SignUpScreen,self).__init__()
        loadUi("SignUpPage.ui",self)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignUpBtn.clicked.connect(self.InitiateSignUp)
        
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
                self.show_popUp("User Registered Successfully!")
                self.resetValues()
            else:
                self.show_popUp("This user already exists")

    def show_popUp(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("User Registration")
        msg.setText(message)

        # x = msg.exec_()
    def resetValues(self):
        self.txtEmail.setText("Email")
        self.txtUserName.setText("User Name")
        self.txtPassword.setText("Password")
        self.txtRole.setText("Role")





        
