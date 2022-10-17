import sys
from PyQt5.QtWidgets import QWidget, QApplication
from designer_files.input_data_ui import UiForm
from data_base.request import set_data, get_data, delete_storage


class InputData(QWidget, UiForm):
    def __init__(self, back_widget, storage_name: str, user_hash: str):
        super().__init__()
        self.back_widget = back_widget
        self.storage_name = storage_name
        self.user_hash = user_hash
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.connectButton(self.back, self.return_to_previous_window)
        self.connectButton(self.save, self.save_data)
        self.connectButton(self.delete_2, self.delete)
        self.open_data()

    def return_to_previous_window(self) -> None:
        self.close()
        self.back_widget.show()
        self.back_widget.displaying_buttons()

    def save_data(self) -> None:
        data = self.plainTextEdit.toPlainText()
        set_data(self.storage_name, self.user_hash, data)
        # TODO: сделать шифрование

    def open_data(self) -> None:
        data = get_data(self.user_hash, self.storage_name)
        self.plainTextEdit.setPlainText(data[0])

    def delete(self):
        delete_storage(self.storage_name, self.user_hash)
        self.return_to_previous_window()

    def connectButton(self, button, handler):
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = InputData()
    widget.show()
    sys.exit(app.exec())
