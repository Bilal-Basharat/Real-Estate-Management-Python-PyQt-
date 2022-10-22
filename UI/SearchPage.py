import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from mUserDL import MUserDL
from muser import MUser

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("SearchPage.ui",self)
        if(user != None):
            self.loginbtn.clicked.connect(self.SeachPage())
    def SearchPage():
        

                    