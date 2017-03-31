"""View setup."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal
from itertools import cycle


class GraphicsView(QGraphicsView):
    escPressed = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.nativeW, self.nativeH = 0, 0
        self.resolution = self.resolution()

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resolution(self):
        resLst = [(800, 600), (1280, 720), (1366, 768), (1920, 1080)]

        rect = self.scene().sceneRect()
        self.nativeW, self.nativeH = rect.width(), rect.height()

        resolutions = [res for res in resLst if res[0] <= self.nativeW]
        resolutions = sorted(resolutions, key=lambda elem: -elem[0])

        for res in cycle(resolutions):
            factor = self.nativeW / res[0], self.nativeH / res[1]
            self.scale(*factor)

            yield res

            factor = res[0] / self.nativeW, res[1] / self.nativeH
            self.scale(*factor)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        if event.key() == Qt.Key_Escape:
            self.escPressed.emit()
