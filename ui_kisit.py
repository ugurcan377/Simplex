# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisit.ui'
#
# Created: Mon Jun  4 20:17:22 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(471, 162)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Kısıt Ekle", None, QtGui.QApplication.UnicodeUTF8))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 450, 34))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.conNumber = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conNumber.sizePolicy().hasHeightForWidth())
        self.conNumber.setSizePolicy(sizePolicy)
        self.conNumber.setText(_fromUtf8(""))
        self.conNumber.setObjectName(_fromUtf8("conNumber"))
        self.horizontalLayout.addWidget(self.conNumber)
        self.conEq = QtGui.QLineEdit(self.layoutWidget)
        self.conEq.setMinimumSize(QtCore.QSize(251, 27))
        self.conEq.setText(_fromUtf8(""))
        self.conEq.setObjectName(_fromUtf8("conEq"))
        self.horizontalLayout.addWidget(self.conEq)
        self.k = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.k.setFont(font)
        self.k.setText(QtGui.QApplication.translate("Dialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.k.setObjectName(_fromUtf8("k"))
        self.horizontalLayout.addWidget(self.k)
        self.conRes = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conRes.sizePolicy().hasHeightForWidth())
        self.conRes.setSizePolicy(sizePolicy)
        self.conRes.setMaximumSize(QtCore.QSize(236, 16777215))
        self.conRes.setText(_fromUtf8(""))
        self.conRes.setObjectName(_fromUtf8("conRes"))
        self.horizontalLayout.addWidget(self.conRes)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 120, 431, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonAdd = QtGui.QPushButton(self.widget)
        self.buttonAdd.setText(QtGui.QApplication.translate("Dialog", "Ekle", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.horizontalLayout_2.addWidget(self.buttonAdd)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

