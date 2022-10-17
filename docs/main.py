from PyQt5.QtWidgets import QApplication
import sys
from user_interface.login import Login


def main():
    app = QApplication([])
    widget = Login()
    widget.show()
    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()
