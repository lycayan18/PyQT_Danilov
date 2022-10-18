import sys
from PyQt5.QtWidgets import QWidget, QApplication
from data_base.request import is_acc_exist
from designer_files.login_ui import UiForm
from user_interface.main_window import MainWindow
from user_interface.create_account import CreateAccount


class Login(QWidget, UiForm):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.label_3.hide()
        self.label_4.hide()
        self.label_6.hide()
        self.connectButton(self.enter, self.sign_in)
        self.connectButton(self.create_account, self.create_acc)

    def sign_in(self):
        self.label_3.hide()
        self.label_4.hide()
        self.label_6.hide()

        login = self.login.text()
        password = self.password.text()

        if not login:
            self.label_6.show()
        if not password:
            self.label_4.show()
        if login and password:
            if is_acc_exist(login, password)[0]:
                self.close()
                self.widget = MainWindow(is_acc_exist(login, password)[1])
                self.widget.show()
            else:
                self.label_3.show()
                self.login.clear()
                self.password.clear()

    def create_acc(self):
        self.hide()
        self.widget = CreateAccount(self)
        self.widget.show()

    def connectButton(self, button, handler):
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = Login()
    widget.show()
    sys.exit(app.exec())
