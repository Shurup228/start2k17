"""Buttons go here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtCore import pyqtSignal, QRectF


class Button(QGraphicsObject):
    clicked = pyqtSignal()

    def __init__(self, text, x=0, y=0, width=300, height=100):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.__text = text

    def boundingRect(self):
        return QRectF(self.x, self.y, self.width, self.height)

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.drawText(self.boundingRect().center(), self.__text)
        QPainter.drawRect(self.boundingRect())

    def mousePressEvent(self, *args, **kwargs):
        self.clicked.emit()
