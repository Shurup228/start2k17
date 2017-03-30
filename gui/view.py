"""View setup."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal


class GraphicsView(QGraphicsView):
    escPressed = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        if event.key() == Qt.Key_Escape:
            self.escPressed.emit()
