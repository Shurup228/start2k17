"""Main project file."""
# coding=utf-8


from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setLayout(QFormLayout())
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())
