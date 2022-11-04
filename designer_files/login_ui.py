# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_files\UI\login.ui'
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
        self.login = QtWidgets.QLineEdit(Form)
        self.login.setGeometry(QtCore.QRect(270, 240, 471, 61))
        self.login.setStyleSheet("color: rgb(163, 163, 163);\n"
                                 "font-size: 18px;\n"
                                 "border-radius: 10px;\n"
                                 "border: 2px solid rgb(100, 0, 0);\n"
                                 "background-color: rgb(79, 79, 79)")
        self.login.setText("")
        self.login.setObjectName("login")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 190, 67, 29))
        self.label.setStyleSheet("color: rgb(163, 163, 163);\n"
                                 "font-size: 18px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 340, 80, 29))
        self.label_2.setStyleSheet("color: rgb(163, 163, 163);\n"
                                   "font-size: 18px;")
        self.label_2.setObjectName("label_2")
        self.enter = QtWidgets.QPushButton(Form)
        self.enter.setGeometry(QtCore.QRect(270, 470, 181, 31))
        self.enter.setStyleSheet("font-size: 20px;\n"
                                 "color: rgb(163, 163, 163);\n"
                                 "border-radius: 10px;\n"
                                 "border: 1px solid rbg(0, 0, 0)")
        self.enter.setObjectName("enter")
        self.create_account = QtWidgets.QPushButton(Form)
        self.create_account.setGeometry(QtCore.QRect(20, 40, 211, 41))
        self.create_account.setStyleSheet("font-size: 20px;\n"
                                          "color: rgb(163, 163, 163);\n"
                                          "border-radius: 10px;\n"
                                          "border: 1px solid rbg(0, 0, 0)")
        self.create_account.setObjectName("create_account")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(270, 390, 471, 61))
        self.password.setStyleSheet("color: rgb(163, 163, 163);\n"
                                    "font-size: 18px;\n"
                                    "border-radius: 10px;\n"
                                    "border: 2px solid rgb(100, 0, 0);\n"
                                    "background-color: rgb(79, 79, 79)")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(350, 110, 328, 29))
        self.label_3.setStyleSheet("color: rgb(234, 0, 3)")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(380, 190, 150, 25))
        self.label_6.setStyleSheet("color: rgb(234, 0, 3)")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(380, 340, 163, 25))
        self.label_4.setStyleSheet("color: rgb(234, 0, 3)")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Secret Storage"))
        self.label.setText(_translate("Form",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Логин</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Пароль</span></p></body></html>"))
        self.enter.setText(_translate("Form", "Войти"))
        self.create_account.setText(_translate("Form", "Создать аккаунт"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Неверный логин или пароль!</span></p></body></html>"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:16pt;\">Введите логин!</span></p></body></html>"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:16pt;\">Введите пароль!</span></p></body></html>"))
