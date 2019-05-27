# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pb
import sys
import requests
import webbrowser
# colums=["link","title","location","image","area","price"]


class Ui_Result(object):
    def setupUi(self, Result, n_product):
        ########################### LOAD DATA PROCESSED ###########################
        self.data = pb.read_csv("result.csv",sep="\t")
        ###########################################################################
        self.n_page = len(self.data)/5
        self.current_page = 1
        self.n_product = n_product
        Result.setObjectName("Result")
        Result.resize(981, 584)
        self.centralwidget = QtWidgets.QWidget(Result)
        self.centralwidget.setObjectName("centralwidget")

        self.myQListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myQListWidget.setGeometry(QtCore.QRect(0, 70, 981, 584))
        
        for i in range(self.n_product-5,self.n_product):
            ###### load Image ######
            image_url = self.data['image'][i]
            icon = QtGui.QPixmap()
            if str(image_url) == "nan":
                icon = QtGui.QPixmap('images/nophoto.jpg')
            else:
                r = requests.get(image_url)
                with open ('images/'+str(i)+'.jpg','wb') as f:
                    f.write(r.content)
                ### download #########
                icon = QtGui.QPixmap('images/'+str(i)+'.jpg')
            # icon.loadFromData(image)
            ###### Title ######
            title = self.data['title'][i]
            ###### other #####
            price = "Giá: " + self.data['price'][i]
            area = "Diện tích:" + self.data['area'][i]
            link = self.data['link'][i]
            other_infor = price + "\t\t" + area
            ##############################
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(title)
            myQCustomQWidget.setTextDown(other_infor)
            myQCustomQWidget.setIcon(icon.scaled(240, 150))

            # Create QListWidgetItem
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            myQListWidgetItem.setText(link)
            myQListWidgetItem.setForeground(QtGui.QColor(255,255,255))

            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.myQListWidget.clicked.connect(self.clicked)
        Result.setCentralWidget(self.centralwidget)
        ################## next  ######################
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(900, 5, 64, 64))
        pixmap = QtGui.QPixmap("images/icons8-forward-button-64.png")
        next_icon = QtGui.QIcon(pixmap)
        self.next_button.setIcon(next_icon)
        self.next_button.setIconSize(pixmap.rect().size())
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.click_next)
        Result.setCentralWidget(self.centralwidget)
        ################## image ######################
        self.image_search = QtWidgets.QLabel(self.centralwidget)
        self.image_search.setGeometry(QtCore.QRect(0, 0, 301, 70))
        self.image_search.setText("")
        pixmap = QtGui.QPixmap(("images/roogle.png"))
        image_search = pixmap.scaled(301, 70)
        self.image_search.setPixmap(image_search)
        self.image_search.setObjectName("image_search")
        self.icon_search = QtWidgets.QLabel(self.centralwidget)
        self.icon_search.setGeometry(QtCore.QRect(275, 50, 24, 24))
        self.icon_search.setText("")
        pixmap = QtGui.QPixmap(("images/icons8-search-48.png"))
        image_search = pixmap.scaled(24, 24)
        self.icon_search.setPixmap(image_search)
        self.icon_search.setObjectName("icon_search")
        Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def clicked(self, qmodelindex):
        text = self.myQListWidget.currentItem()
        webbrowser.open(text.text(), new=0, autoraise=True)
    
    def click_next(self,):
        self.n_product +=5
        self.current_page +=1
        if self.current_page > self.n_page:
            print("This is Final Page")
        else:
            self.myQListWidget.clear()
            for i in range(self.n_product-5,self.n_product):
                ###### load Image ######
                image_url = self.data['image'][i]
                icon = QtGui.QPixmap()
                if str(image_url) == "nan":
                    icon = QtGui.QPixmap('images/nophoto.jpg')
                else:
                    r = requests.get(image_url)
                    with open ('images/'+str(i)+'.jpg','wb') as f:
                        f.write(r.content)
                    ### download #########
                    icon = QtGui.QPixmap('images/'+str(i)+'.jpg')
                ###### Title ######
                title = self.data['title'][i]
                ###### other #####
                price = "Giá: " + self.data['price'][i]
                area = "Diện tích:" + self.data['area'][i]
                link = self.data['link'][i]
                other_infor = price + "\t\t" + area
                ##############################
                myQCustomQWidget = QCustomQWidget()
                myQCustomQWidget.setTextUp(title)
                myQCustomQWidget.setTextDown(other_infor)
                myQCustomQWidget.setIcon(icon.scaled(240, 150))

                # Create QListWidgetItem
                myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)
                # Set size hint
                myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                myQListWidgetItem.setText(link)
                myQListWidgetItem.setForeground(QtGui.QColor(255,255,255))

                # Add QListWidgetItem into QListWidget
                self.myQListWidget.addItem(myQListWidgetItem)
                self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.myQListWidget.clicked.connect(self.clicked)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "Result"))
    


class QCustomQWidget (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel    = QtWidgets.QLabel()
        self.textDownQLabel  = QtWidgets.QLabel()
        self.text_link = QtGui.QTextDocument()
        self.textUpQLabel.setFont(font)
        self.textDownQLabel.setFont(font)
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Result = QtWidgets.QMainWindow()
#     ui = Ui_Result()
#     ui.setupUi(Result,5)
#     Result.show()
#     sys.exit(app.exec_())
