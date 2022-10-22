import sys
from PyQt5.QtWidgets import QWidget, QApplication
from app.designer_files.input_data_ui import UiForm
from app.data_base.request import set_data, get_data, delete_storage
from app.encryption.string_encryption import encode, decode


class InputData(QWidget, UiForm):
    def __init__(self, back_widget, storage_name: str, user_hash: str, user_password: str):
        super().__init__()
        self.back_widget = back_widget
        self.storage_name = storage_name
        self.user_hash = user_hash
        self.user_password = user_password
        self.initUI()

    def initUI(self) -> None:
        self.setupUi(self)
        self.connectButton(self.back, self.return_to_previous_window)
        self.connectButton(self.save, self.save_data)
        self.connectButton(self.delete_2, self.delete)
        self.open_data()

    def return_to_previous_window(self) -> None:
        """Возвращение к предыдущему окну"""
        self.close()
        self.back_widget.show()
        self.back_widget.displaying_buttons()

    def save_data(self) -> None:
        """Сохранение данных в БД"""
        data = self.plainTextEdit.toPlainText()
        encode_data = encode(text=data, key=self.user_password)
        set_data(self.storage_name, self.user_hash, encode_data)

    def open_data(self) -> None:
        """Открытие данных из БД"""
        data = get_data(self.user_hash, self.storage_name)
        if data[0]:
            decode_data = decode(text=data[0], key=self.user_password)
            self.plainTextEdit.setPlainText(decode_data)

    def delete(self) -> None:
        """Удаление хранилища"""
        delete_storage(self.storage_name, self.user_hash)
        self.return_to_previous_window()

    def connectButton(self, button, handler):
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = InputData()
    widget.show()
    sys.exit(app.exec())
