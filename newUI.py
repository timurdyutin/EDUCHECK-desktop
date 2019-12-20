# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QApplication, QFileDialog, QInputDialog,
                             QMainWindow, QSizePolicy, QTableWidgetItem,
                             QTextEdit, QWidget, QScrollArea, QTableWidget, QCalendarWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate


class MainWindow(object):
    def setupUi(self, Form):
        Form.setWindowTitle('EDUCHECK')
        Form.setWindowIcon(QIcon('educheck.png')) 
        Form.setObjectName("EDUCHECK")
        Form.resize(640, 348)
        Form.setFixedSize(640, 348)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 50, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 50, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 10, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 50, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 621, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(QtCore.QRect(10, 90, 621, 251))
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "День"))
        self.pushButton_2.setText(_translate("Form", "Неделя"))
        self.pushButton_3.setText(_translate("Form", "Табель успеваемости"))
        self.pushButton_4.setText(_translate("Form", "Выйти"))
        self.label.setText(_translate("Form", "Привет,"))
        self.pushButton_5.setText(_translate("Form", "Месяц"))
        

class AuthWindow(object):
    def setupUi(self, Form):
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(400, 278)        
        Form.setFixedSize(400, 278)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 381, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 150, 381, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 381, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 261, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.textEdit.setTabChangesFocus(True)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)                
        self.textEdit_2.setEnabled
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите свой логин и пароль"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Войти"))


if __name__ == '__main__':        
    app = QApplication(sys.argv)        
    wid = MainWindow()
    wid.show()
    sys.exit(app.exec())