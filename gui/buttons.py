"""Buttons go here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsRectItem


class Button(QGraphicsRectItem):
    def __init__(self, text, x=0, y=0, width=300, height=100):
        super().__init__(x, y, width, height)
        self.__text = text

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.drawText(self.boundingRect().center(), self.__text)
        QPainter.drawRect(self.boundingRect())


class ExitButton(Button):

    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        return quit()


class StartGame(Button):

    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        return None
