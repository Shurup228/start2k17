"""Main project file."""
# coding=utf-8


from sys import argv, exit
from PyQt5.QtWidgets import (QWidget, QApplication, QBoxLayout, QDesktopWidget)
from PyQt5.QtCore import Qt

from gui.scene import Scene
from gui.view import GraphicsView
from gui.menus import MainMenu


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resMode = 0

        self.__size = QDesktopWidget().size()
        self.__scene = Scene(0, 0, self.__size.width(), self.__size.height())
        self.__view = GraphicsView(self.__scene, self)

        self.initUI()

    def initUI(self):
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        self.layout().addWidget(self.__view)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__layout = MainMenu(self.__scene)
        self.__scene.nextScene(self.__layout)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())
