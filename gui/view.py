"""View setup."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt


class GraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
