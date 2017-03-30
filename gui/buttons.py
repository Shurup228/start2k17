"""Buttons go here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsObject, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QRectF


class Button(QGraphicsObject):
    clicked = pyqtSignal()

    def __init__(self, text, winWidget=None, x=0, y=0, width=300, height=100):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.__text = text
        self.__widget = winWidget

    def boundingRect(self):
        return QRectF(self.x, self.y, self.width, self.height)

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.drawText(self.boundingRect().center(), self.__text)
        QPainter.drawRect(self.boundingRect())

    def mousePressEvent(self, *args, **kwargs):
        self.clicked.emit()

    def changeRes(self):
        size = self.__widget.size()
        resList = [[800, 600], [1024, 768]]
        for elem in resList:
            if size.width() is elem[0] and size.height is elem[1]:
                try:
                    newRes = resList[resList.index(elem) + 1]
                    self.__widget.resize(resList, 600)
                    self.__text = str(newRes[0]) + ' X ' + str(newRes[1])
                    self.__widget.update()
                except IndexError:
                    pass

