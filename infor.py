# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Smart\Desktop\Postulante_\infor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 472)
        MainWindow.setStyleSheet("background-color: rgb(10, 39, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info_pj = QtWidgets.QListWidget(self.centralwidget)
        self.info_pj.setGeometry(QtCore.QRect(10, 20, 301, 451))
        self.info_pj.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(236, 236, 236);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.info_pj.setObjectName("info_pj")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

