import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit
from PyQt5.uic import loadUi


class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("test.ui", self)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Chidera GUI")
        # self.buttons()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())