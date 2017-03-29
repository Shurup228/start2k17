# coding=utf-8


from PyQt5.QtWidgets import (QGraphicsRectItem)


class Button(QGraphicsRectItem):
    def __init__(self, text, x, y, w=300, h=100):
        super().__init__(x, y, w, h)
        self.buttonText = text

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.drawText(self.boundingRect().center(), self.text)
        QPainter.drawRect(self.boundingRect())