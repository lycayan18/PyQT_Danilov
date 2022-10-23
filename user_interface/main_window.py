import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QInputDialog, QErrorMessage
from PyQt5.QtCore import Qt
from designer_files.main_window_ui import UiForm
from data_base.request import create_storage, get_data
from user_interface.input_data import InputData
from user_interface.new_password import NewPassword


class MainWindow(QWidget, UiForm):
    def __init__(self, user_hash: str, user_password: str):
        super().__init__()
        self.user_hash = user_hash
        self.user_password = user_password
        self.initUI()

    def initUI(self):
        self.setupUi(self)

        self.storage.hide()
        self.scroll_layout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setLayout(self.scroll_layout)

        self.storage.setFixedSize(721, 51)
        self.connectButton(self.add_category, self.new_storage)
        self.connectButton(self.change_password, self.open_password_window)

        self.displaying_buttons()

    def create_button(self, name: str) -> QPushButton:
        """Создание кнопки хранилища"""
        btn = QPushButton(name, self)
        btn.setStyleSheet("color: rgb(198, 0, 3);\n"
                          "font-size: 25px;\n"
                          "text-align: left;\n"
                          "padding-left: 15px;\n"
                          "background-color: rgb(113, 113, 113);\n"
                          "border-radius: 10px;\n"
                          "border: 1px solid rgb(168, 0, 2);")
        return btn

    def new_storage(self) -> None:
        """Новое хранилище"""
        self.scrollArea.setStyleSheet("""QScrollBar{
                                        background : black;
                                      }
                                      
                                      QScrollBar::handle{
                                        background : gray;
                                      }
                                      
                                      QScrollBar::handle::pressed{
                                        background : red;
                                        }""")

        dialog = QInputDialog()
        name, ok_pressed = dialog.getText(self, "Название хранилища",
                                          "Введите название хранилища")

        if ok_pressed and name:
            if name not in get_data(self.user_hash, '', True):
                create_storage(storage_name=name, user_hash=self.user_hash, data='')
                self.displaying_buttons()
            else:
                error = QErrorMessage(self)
                error.setStyleSheet("""color: white;
                                        """)
                error.showMessage('Хранилище с таким названием уже существует, пожалуйста выберете другое')

    def open_input_window(self) -> None:
        """Открытие окна ввода"""
        self.hide()
        self.widget = InputData(back_widget=self, storage_name=self.sender().text(), user_hash=self.user_hash,
                                user_password=self.user_password)
        self.widget.show()

    def open_password_window(self):
        """Открытие окна для изменения пароля"""
        self.hide()
        self.widget = NewPassword(self)
        self.widget.show()

    def displaying_buttons(self) -> None:
        """Отображение всех кнопок"""
        for row in range(self.scroll_layout.rowCount()):  # Очищение лэйаута
            for col in range(self.scroll_layout.columnCount()):
                w = self.scroll_layout.itemAtPosition(row, col)
                if w:
                    w.widget().deleteLater()

        for item in get_data(self.user_hash, '', True):
            count = self.scroll_layout.count()
            btn = self.create_button(item)
            btn.setFixedSize(721, 51)
            self.connectButton(btn, self.open_input_window)
            self.scroll_layout.addWidget(btn, count, 0, alignment=Qt.AlignTop)

    def connectButton(self, button, handler):
        button.clicked.connect(lambda: handler())


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow('')
    widget.show()
    sys.exit(app.exec())
