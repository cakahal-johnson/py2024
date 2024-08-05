import sys
# import PyQt5.QtWidgets as qtw
#
#
# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.show()
#
#
# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLayout, QLineEdit
from PyQt5.uic import loadUi


class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("cal2.ui", self)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("calculator")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())
