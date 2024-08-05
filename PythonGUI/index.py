import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit
from PyQt5.uic import loadUi


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("sign.ui", self)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Sign in page")
        self.buttons()

        self.show()

    def buttons(self):
        self.submit_btn.clicked.connect(self.submit)
        self.clear_btn.clicked.connect(self.clear)

    def submit(self):
        text = self.input.text()
        print("hello world")

        self.label_btn_setText(f"Welcome {text} ")
        self.input.setText("")

    def clear(self):
        self.input.setText("")
        self.label_btn.setText("Welcome,")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())
