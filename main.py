"""Main project file."""
# coding=utf-8


from sys import argv, exit
from PyQt5.QtWidgets import (QWidget, QApplication, QBoxLayout, QDesktopWidget)
from PyQt5.QtCore import Qt

from gui.scene import Scene
from gui.view import GraphicsView
from gui.layout import GridLayout
from gui.buttons import Button


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__size = QDesktopWidget().size()
        self.__scene = Scene(0, 0, self.__size.width(), self.__size.height())

        self.__view = GraphicsView(self.__scene, self)

        self.initUI()

    def initUI(self):
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        self.layout().addWidget(self.__view)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.showFullScreen()

        l = GridLayout(self.__scene)
        for i in range(3):
            for j in range(3):
                b = Button(str(i) + ' ' + str(j))
                l.addItem(b, i, j)

        self.__scene.nextScene(l)


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    exit(app.exec_())
