"""Main project file."""
# coding=utf-8



from sys import argv, exit
from PyQt5.QtWidgets import (QWidget, QApplication, QFormLayout,
                            QDesktopWidget)
from PyQt5.QtCore import QRectF
from gui.scene import Scene
from gui.view import GraphicsView
from gui.menu_buttons import ExitButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__size = QDesktopWidget().size()
        self.__scene = Scene(0, 0, #self.__size.width(), self.__size.height())
                             100, 100)

        self.__view = GraphicsView()
        self.exitButton = ExitButton('quit', -400, -400)

        self.initUI()

    def initUI(self):

        self.setLayout(QFormLayout())
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.showFullScreen()

        self.__scene.addItem(self.exitButton)

        self.__view.setScene(self.__scene)
        self.__view.show()

if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())
