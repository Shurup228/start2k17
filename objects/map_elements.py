"""All walls, roads, etc goes here."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush


class Wall(QGraphicsRectItem):
    def __init__(self, x=0, y=0, width=100, height=100, expandable=True):
        super().__init__(x, y, width, height)
        self.expandable = expandable
        self.resizable = False

        self.setBrush(QBrush(Qt.black))

    def setBoundingRect(self, x, y, width, height):
        self.setRect(x, y, width, height)


class Air(QGraphicsRectItem):
    def __init__(self, x=0, y=0, width=100, height=100, expandable=True):
        super().__init__(x, y, width, height)
        self.expandable = expandable
        self.resizable = False

        self.setBrush(QBrush(Qt.white))

    def setBoundingRect(self, x, y, width, height):
        self.setRect(x, y, width, height)
