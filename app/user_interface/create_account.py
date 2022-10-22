import sys
from PyQt5.QtWidgets import QWidget, QApplication
from app.designer_files.create_account_ui import UiForm
from app.data_base.request import add_account, UserInDataBase


class CreateAccount(QWidget, UiForm):
    def __init__(self, back_widget):
        super().__init__()
        self.back_widget = back_widget
        self.initUI()

    def initUI(self) -> None:
        self.setupUi(self)
        self.label_3.hide()
        self.label_4.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.connectButton(self.back, self.return_to_previous_window)
        self.connectButton(self.create_account, self.create_acc)

    def return_to_previous_window(self) -> None:
        """Возвращение к предыдущему окну"""
        self.close()
        self.back_widget.show()

    def create_acc(self) -> None:
        """Создание аккаунта"""
        self.label_4.hide()
        self.label_6.hide()
        self.label_7.hide()

        login = self.login.text()
        password = self.password.text()

        if not login:
            self.label_6.show()
        if not password:
            self.label_4.show()
        if login and password:
            try:
                add_account(login, password)
                self.label_3.show()
            except UserInDataBase:
                self.label_7.show()

    def connectButton(self, button, handler):
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = CreateAccount()
    widget.show()
    sys.exit(app.exec())
