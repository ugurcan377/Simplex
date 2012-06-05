# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yoneylem.ui'
#
# Created: Mon Jun  4 11:44:34 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(786, 219)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simplex ", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 22, 751, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_profit = QtGui.QLabel(self.layoutWidget)
        self.label_profit.setText(QtGui.QApplication.translate("MainWindow", "Kar Fonksyonu =", None, QtGui.QApplication.UnicodeUTF8))
        self.label_profit.setObjectName(_fromUtf8("label_profit"))
        self.horizontalLayout.addWidget(self.label_profit)
        self.profit = QtGui.QLineEdit(self.layoutWidget)
        self.profit.setText(QtGui.QApplication.translate("MainWindow", "8P+6T", None, QtGui.QApplication.UnicodeUTF8))
        self.profit.setObjectName(_fromUtf8("profit"))
        self.horizontalLayout.addWidget(self.profit)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 170, 751, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonCon = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCon.sizePolicy().hasHeightForWidth())
        self.buttonCon.setSizePolicy(sizePolicy)
        self.buttonCon.setText(QtGui.QApplication.translate("MainWindow", "Kısıt Ekle", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCon.setObjectName(_fromUtf8("buttonCon"))
        self.horizontalLayout_2.addWidget(self.buttonCon)
        self.button_enter = QtGui.QPushButton(self.layoutWidget1)
        self.button_enter.setText(QtGui.QApplication.translate("MainWindow", "Tabloyu Oluştur", None, QtGui.QApplication.UnicodeUTF8))
        self.button_enter.setObjectName(_fromUtf8("button_enter"))
        self.horizontalLayout_2.addWidget(self.button_enter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

