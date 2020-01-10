# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1247, 807)
        self.pushButton_TestSQL = QtWidgets.QPushButton(Form)
        self.pushButton_TestSQL.setGeometry(QtCore.QRect(70, 20, 75, 23))
        self.pushButton_TestSQL.setObjectName("pushButton_TestSQL")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(60, 700, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(210, 700, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.label_Hello = QtWidgets.QLabel(Form)
        self.label_Hello.setGeometry(QtCore.QRect(200, 30, 46, 13))
        self.label_Hello.setObjectName("label_Hello")
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setGeometry(QtCore.QRect(10, 90, 331, 601))
        self.treeView.setObjectName("treeView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 390, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_TestSQL.setText(_translate("Form", "SQL Запрос"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_Hello.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
