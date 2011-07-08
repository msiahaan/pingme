# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pingme.ui'
#
# Created: Wed Dec 29 07:40:57 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PingMainWindow(object):
    def setupUi(self, PingMainWindow):
        PingMainWindow.setObjectName("PingMainWindow")
        PingMainWindow.resize(465, 170)
        self.centralWidget = QtGui.QWidget(PingMainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout.addWidget(self.urlLabel)
        self.urlLineEdit = QtGui.QLineEdit(self.centralWidget)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.horizontalLayout.addWidget(self.urlLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startPushButton = QtGui.QPushButton(self.centralWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startPushButton.setIcon(icon)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_2.addWidget(self.startPushButton)
        self.stopPushButton = QtGui.QPushButton(self.centralWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopPushButton.setIcon(icon1)
        self.stopPushButton.setObjectName("stopPushButton")
        self.horizontalLayout_2.addWidget(self.stopPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        PingMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(PingMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PingMainWindow)

    def retranslateUi(self, PingMainWindow):
        PingMainWindow.setWindowTitle(QtGui.QApplication.translate("PingMainWindow", "Ping Me!", None, QtGui.QApplication.UnicodeUTF8))
        self.urlLabel.setText(QtGui.QApplication.translate("PingMainWindow", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.startPushButton.setText(QtGui.QApplication.translate("PingMainWindow", "Start Ping!", None, QtGui.QApplication.UnicodeUTF8))
        self.stopPushButton.setText(QtGui.QApplication.translate("PingMainWindow", "Stop Ping ", None, QtGui.QApplication.UnicodeUTF8))

