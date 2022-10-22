import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from mUserDL import MUserDL
from muser import MUser

class userDashBoard(QMainWindow):
    def __init__(self):
        super(userDashBoard,self).__init__()
        loadUi("User_Dashboard.ui",self)        
        

                    