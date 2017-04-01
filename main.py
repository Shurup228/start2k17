"""Main project file."""
# coding=utf-8


import logging
from sys import argv, exit
from PyQt5.QtWidgets import (QWidget, QApplication, QBoxLayout, QDesktopWidget)
from PyQt5.QtCore import Qt

from gui.scene import Scene
from gui.view import GraphicsView
from gui.menus import MainMenu
from gui.layout import Background

L = logging.getLogger('gameLogger')
L.setLevel(logging.DEBUG)
f = logging.Formatter('[%(levelname)s] : %(filename)s|line %(lineno)d|func %(funcName)s -> %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
L.addHandler(ch)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resMode = 0

        self.__size = QDesktopWidget().size()
        self.__scene = Scene(0, 0, self.__size.width(), self.__size.height())
        self.__view = GraphicsView(self.__scene, self)

        L.debug('\u001b[33mInitialized MainWindow\u001b[0m')
        self.initUI()

    def initUI(self):
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        self.layout().addWidget(self.__view)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__scene.nextLayout(Background, 'mainBackground.jpg')
        self.__scene.nextLayout(MainMenu, mode=self.__scene.COMBINE)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        L.debug('\u001b[33mInitialized layout, showing...\u001b[0m')
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())
