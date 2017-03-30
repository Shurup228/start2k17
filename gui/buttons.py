"""Buttons go here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtCore import pyqtSignal, QRectF


class Button(QGraphicsObject):
    clicked = pyqtSignal()

    def __init__(self, text, x=0, y=0, width=300, height=100, resizable=True):
        super().__init__()
        self._x, self._y = x, y
        self.width, self.height = width, height
        self.__text = text
        self.resizable = resizable

    def setBoundingRect(self, x, y, width, height):
        self._x, self._y = x, y
        self.width, self.height = width, height
        self.prepareGeometryChange()

    def boundingRect(self):
        return QRectF(self._x, self._y, self.width, self.height)

    def paint(self, painter, style=None, widget=None):
        painter.eraseRect(self.boundingRect())
        painter.drawText(self.boundingRect().center(), self.__text)
        painter.drawRect(self.boundingRect())

    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        self.clicked.emit()
