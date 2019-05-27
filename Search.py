# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from results import Ui_Result
from query import *
class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(981, 584)
        self.lineEdit = QtWidgets.QLineEdit(Search)
        self.lineEdit.setGeometry(QtCore.QRect(210, 300, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(True)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("info_search")
        #######################################
        self.pushButton = QtWidgets.QPushButton(Search)
        self.pushButton.setGeometry(QtCore.QRect(410, 390, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("Button_Search")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        ########################################
        self.Search_image = QtWidgets.QLabel(Search)
        self.Search_image.setGeometry(QtCore.QRect(210, 120, 600, 120))
        self.Search_image.setText("")
        self.Search_image.setText("")
        self.Search_image.setObjectName("Search_image")
        pixmap = QtGui.QPixmap(("images/roogle.png"))
        image_search = pixmap.scaled(600, 120)
        self.Search_image.setPixmap(image_search)
        self.Search_image.setObjectName("Search_image")
        
        self.search_icon = QtWidgets.QLabel(Search)
        self.search_icon.setGeometry(QtCore.QRect(760, 300, 48, 48))
        self.search_icon.setText("")
        image_search = QtGui.QPixmap(("images/icons8-search-48.png"))
        self.search_icon.setPixmap(image_search)
        self.search_icon.setObjectName("search_icon")
        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)
        
    def on_pushButton_clicked(self):
###################### GET TEXT for processing in here ###########################
##################################################################################
        query = self.lineEdit.text()
############## open another window #####################
        result = Query(query)
        export_to_csv(result)
        self.Result = QtWidgets.QMainWindow()
        self.ui = Ui_Result()
        self.ui.setupUi(self.Result,5)
        self.Result.show()
    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Roogle"))
        self.pushButton.setText(_translate("Search", "Search"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QDialog()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())
