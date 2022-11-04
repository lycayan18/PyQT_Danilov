# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_files\UI\input_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 550)
        Form.setStyleSheet("background: rgb(43, 43, 43)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 10, 152, 42))
        self.label.setStyleSheet("color: rgb(206, 206, 206)")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 60, 811, 431))
        self.plainTextEdit.setStyleSheet("color: rgb(163, 163, 163);\n"
                                         "font-size: 14px;\n"
                                         "background-color: rgb(22, 22, 22);")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(30, 500, 101, 31))
        self.save.setStyleSheet("font-size: 16px;\n"
                                "color: rgb(163, 163, 163);\n"
                                "border-radius: 10px;\n"
                                "border: 1px solid rbg(0, 0, 0)")
        self.save.setObjectName("save")
        self.input_file = QtWidgets.QPushButton(Form)
        self.input_file.setGeometry(QtCore.QRect(160, 500, 121, 31))
        self.input_file.setStyleSheet("font-size: 16px;\n"
                                      "color: rgb(163, 163, 163);\n"
                                      "border-radius: 10px;\n"
                                      "border: 1px solid rbg(0, 0, 0)")
        self.input_file.setObjectName("input_file")
        self.delete_2 = QtWidgets.QPushButton(Form)
        self.delete_2.setGeometry(QtCore.QRect(670, 500, 161, 31))
        self.delete_2.setStyleSheet("font-size: 16px;\n"
                                    "color: rgb(163, 163, 163);\n"
                                    "border-radius: 10px;\n"
                                    "border: 1px solid rbg(0, 0, 0)")
        self.delete_2.setObjectName("delete_2")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.back.setStyleSheet("font-size: 16px;\n"
                                "color: rgb(163, 163, 163);\n"
                                "border-radius: 10px;\n"
                                "border: 1px solid rbg(0, 0, 0)")
        self.back.setObjectName("back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Secret Storage"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:26pt;\">Название</span></p></body></html>"))
        self.save.setText(_translate("Form", "Сохранить"))
        self.input_file.setText(_translate("Form", "Вставить файл"))
        self.delete_2.setText(_translate("Form", "Удалить хранилище"))
        self.back.setText(_translate("Form", "<- Назад"))
