# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yoneylem2.ui'
#
# Created: Thu May 31 17:00:29 2012
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
        MainWindow.resize(760, 471)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.labelUp = QtGui.QLabel(self.centralwidget)
        self.labelUp.setGeometry(QtCore.QRect(160, 40, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelUp.setFont(font)
        self.labelUp.setStyleSheet(_fromUtf8(""))
        self.labelUp.setText(_fromUtf8(""))
        self.labelUp.setObjectName(_fromUtf8("labelUp"))
        self.labelLeft = QtGui.QLabel(self.centralwidget)
        self.labelLeft.setGeometry(QtCore.QRect(30, 90, 121, 321))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelLeft.setFont(font)
        self.labelLeft.setStyleSheet(_fromUtf8(""))
        self.labelLeft.setText(_fromUtf8(""))
        self.labelLeft.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.labelLeft.setObjectName(_fromUtf8("labelLeft"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 90, 560, 321))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 438, 741, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelResult = QtGui.QLabel(self.widget)
        self.labelResult.setText(_fromUtf8(""))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.horizontalLayout_2.addWidget(self.labelResult)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonPrev = QtGui.QPushButton(self.widget)
        self.buttonPrev.setText(QtGui.QApplication.translate("MainWindow", "Onceki Tablo", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPrev.setObjectName(_fromUtf8("buttonPrev"))
        self.horizontalLayout.addWidget(self.buttonPrev)
        self.buttonNext = QtGui.QPushButton(self.widget)
        self.buttonNext.setText(QtGui.QApplication.translate("MainWindow", "Sonraki Tablo", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.horizontalLayout.addWidget(self.buttonNext)
        self.buttonFinish = QtGui.QPushButton(self.widget)
        self.buttonFinish.setText(QtGui.QApplication.translate("MainWindow", "Sonuc", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonFinish.setObjectName(_fromUtf8("buttonFinish"))
        self.horizontalLayout.addWidget(self.buttonFinish)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

