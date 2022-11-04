from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys
from user_interface.login import Login
from resource_path import resource_path


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon(resource_path('icon.jpg')))
    widget = Login()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
