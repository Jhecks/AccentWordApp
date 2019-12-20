# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inserter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 144)
        Dialog.setMinimumSize(QtCore.QSize(382, 144))
        Dialog.setMaximumSize(QtCore.QSize(382, 144))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Inserter/Без названия.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 181, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(44, 30, 321, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление слов"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Введите недостающее слово"))
        self.label_2.setText(_translate("Dialog", "Ударную гласную укажите в верхнем регистре"))
