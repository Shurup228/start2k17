"""Buttons go here."""
# coding=utf-8

from logging import getLogger
from PyQt5.QtWidgets import QGraphicsObject
from PyQt5.QtCore import pyqtSignal, QRectF, Qt
from PyQt5.QtGui import QFont
from abc import abstractmethod, ABCMeta

L = getLogger('gameLogger')


class Widget(QGraphicsObject):
    """These methods should be reimplemented in subclasses."""

    def __init__(self, text, x=0, y=0, width=300, height=100,
                 resizable=True, expandable=False):
        super().__init__()
        self.text = text
        # Allow layout resize button
        self.resizable = resizable
        # Force button to occupy all available space
        self.expandable = expandable
        self._x, self._y = x, y
        self.width, self.height = width, height

    def setBoundingRect(self, x, y, width, height):
        self._x, self._y = x, y
        self.width, self.height = width, height
        self.prepareGeometryChange()

    def boundingRect(self):
        return QRectF(self._x, self._y, self.width, self.height)


class Button(Widget):
    clicked = pyqtSignal()

    def paint(self, painter, style=None, widget=None):
        rect = self.boundingRect()
        painter.eraseRect(rect)
        painter.drawText(rect, Qt.AlignCenter, self.text)
        painter.drawRect(rect)

    def mousePressEvent(self, event):
        L.debug('\u001b[34mButton clicked\u001b[0m')
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

    def changeText(self, text):
        self.__text = text
        self.prepareGeometryChange()


class Label(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = QFont()
        self.font.setPointSize(100)
        self.expandable = True

    def paint(self, painter, style=None, widget=None):
        rect = self.boundingRect()
        painter.eraseRect(rect)
        painter.setFont(self.font)
        painter.drawText(rect, Qt.AlignCenter, self.text)
