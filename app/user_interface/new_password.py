import sys
from PyQt5.QtWidgets import QWidget, QApplication
from app.designer_files.new_password_ui import UiForm
from app.data_base.request import is_acc_exist, get_data, set_data, rename_table
from app.encryption.string_encryption import encode, decode
from app.encryption.hash_login import hash_login


class NewPassword(QWidget, UiForm):
    def __init__(self, back_widget):
        super().__init__()
        self.back_widget = back_widget
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.login_or_pass.hide()
        self.new_pass_label.hide()
        self.password_label.hide()
        self.login_label.hide()
        self.pass_changed.hide()
        self.connectButton(self.back, self.return_to_previous_window)
        self.connectButton(self.create_account, self.change_password)

    def change_password(self) -> None:
        """Смена пароля"""
        self.login_or_pass.hide()
        self.new_pass_label.hide()
        self.password_label.hide()
        self.login_label.hide()
        self.pass_changed.hide()

        login = self.login.text()
        password = self.password.text()
        new_password = self.new_password.text()

        if not login:
            self.login_label.show()
        if not password:
            self.password_label.show()
        if login and password:
            is_exist, user_hash = is_acc_exist(login, password)
            if is_exist:
                if not new_password:
                    self.new_pass_label.show()
                else:
                    for storage in get_data(user_hash, '', True):
                        data = get_data(user_hash=user_hash, storage_name=storage)
                        decode_data = decode(text=data[0], key=password) if data[0] else ''

                        encode_data = encode(text=decode_data, key=new_password)
                        set_data(storage, user_hash, encode_data)

                    new_user_hash = hash_login(login, new_password)
                    self.back_widget.user_hash = new_user_hash
                    self.back_widget.user_password = new_password
                    rename_table(old_name=user_hash, new_name=new_user_hash)
                    self.pass_changed.show()
            else:
                self.login_or_pass.show()

    def return_to_previous_window(self) -> None:
        """Возвращение к предыдущему окну"""
        self.close()
        self.back_widget.show()

    def connectButton(self, button, handler) -> None:
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = NewPassword()
    widget.show()
    sys.exit(app.exec())
