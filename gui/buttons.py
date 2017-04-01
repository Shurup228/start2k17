"""Buttons go here."""
# coding=utf-8

from logging import getLogger
from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtCore import pyqtSignal, QRectF, Qt

L = getLogger('gameLogger')


class Button(QGraphicsObject):
    clicked = pyqtSignal()

    def __init__(self, text, x=0, y=0, width=300, height=100, resizable=True,
                 expandable=False):
        super().__init__()
        self._x, self._y = x, y
        self.width, self.height = width, height
        self.__text = text
        # Allow layout resize button
        self.resizable = resizable
        # Force button to occupy all available space
        self.expandable = expandable

        L.debug('\u001b[33mCreated button<{}>, resizable: {},'.format(
                text.replace('\n', ''), resizable) +
                ' expandable: {}\u001b[0m'.format(expandable))

    def setBoundingRect(self, x, y, width, height):
        self._x, self._y = x, y
        self.width, self.height = width, height
        self.prepareGeometryChange()

    def boundingRect(self):
        return QRectF(self._x, self._y, self.width, self.height)

    def paint(self, painter, style=None, widget=None):
        painter.eraseRect(self.boundingRect())
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.__text)
        painter.drawRect(self.boundingRect())

    def mousePressEvent(self, event):
        L.debug('\u001b[34mButton clicked\u001b[0m')
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

    def changeText(self, text):
        self.__text = text
        self.prepareGeometryChange()
