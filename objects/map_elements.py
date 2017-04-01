"""All walls, roads, etc goes here."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QImage


class Object(QGraphicsRectItem):
    def __init__(self, x=0, y=0, width=100, height=100):
        super().__init__(x, y, width, height)
        self.expandable = True
        self.resizable = False

    def setBoundingRect(self, x, y, width, height):
        self.setRect(x, y, width, height)


class BackgroundImage(Object):
    def __init__(self, image):
        super().__init__()
        self.image = image

    def paint(self, painter, style=None, widget=None):
        super().paint(painter, style, widget)

        source = QRectF(self.image.rect())
        target = self.scene().sceneRect()

        painter.drawImage(target, self.image, source)


class Wall(Object):

    def paint(self, painter, style=None, widget=None):
        super().paint(painter, style, widget)
        painter.eraseRect(self.boundingRect())

        source = QRectF(0, 0, 64, 64)
        target = self.boundingRect()
        image = QImage('sprites/wall.png')

        painter.drawImage(target, image, source)


class Air(Object):

    def paint(self, painter, style=None, widget=None):
        super().paint(painter, style, widget)
        painter.eraseRect(self.boundingRect())
