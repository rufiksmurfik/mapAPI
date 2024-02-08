# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_edit_coords = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_coords.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.line_edit_coords.setObjectName("line_edit_coords")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(380, 0, 75, 23))
        self.clear_btn.setObjectName("clear_btn")
        self.gibrid_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gibrid_btn.setGeometry(QtCore.QRect(565, 0, 91, 23))
        self.gibrid_btn.setObjectName("gibrid_btn")
        self.sputnik_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sputnik_btn.setGeometry(QtCore.QRect(565, 30, 91, 23))
        self.sputnik_btn.setObjectName("sputnik_btn")
        self.shema_btn = QtWidgets.QPushButton(self.centralwidget)
        self.shema_btn.setGeometry(QtCore.QRect(564, 60, 91, 23))
        self.shema_btn.setObjectName("shema_btn")
        self.map_QT = QtWidgets.QLabel(self.centralwidget)
        self.map_QT.setGeometry(QtCore.QRect(0, 110, 600, 450))
        self.map_QT.setText("")
        self.map_QT.setObjectName("map_QT")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(567, 90, 91, 17))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clear_btn.setText(_translate("MainWindow", "Сброс"))
        self.gibrid_btn.setText(_translate("MainWindow", "Гибрид"))
        self.sputnik_btn.setText(_translate("MainWindow", "Спутник"))
        self.shema_btn.setText(_translate("MainWindow", "Схема"))
        self.checkBox.setText(_translate("MainWindow", "Почт. индекс"))
