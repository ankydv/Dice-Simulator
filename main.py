import sys,random
from PyQt5 import QtGui,uic
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic.uiparser import QtWidgets
from functions import visitRepo
from PyQt5 import QtWidgets
from PyQt5 import *
from About import Ui_MainWindow

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("dice.ui",self)
        self.roll()
        self.pushButton.clicked.connect(self.roll)
        self.actionVisit_Github_Repository.triggered.connect(visitRepo)
        self.actionAbout.triggered.connect(self.gotoScreen2)

    def gotoScreen2 (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def roll(self):
        arr=["1.png","2.png","3.png","4.png","5.png","6.png"]
        q=QtGui.QPixmap(random.choice(arr))
        self.label.setPixmap(q)
    
app=QApplication(sys.argv)
win=UI()
win.show()
app.exec_()