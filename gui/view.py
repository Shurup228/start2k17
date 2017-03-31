"""View setup."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal
from itertools import cycle


class GraphicsView(QGraphicsView):
    escPressed = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.resolution = None
        self.nativeW, self.nativeH = 0, 0
        self.nextResolution = self.resolutionChange()
        # Initializing generator
        next(self.nextResolution)

        # Disabling scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resolutionChange(self):
        resLst = [(800, 600), (1280, 720), (1366, 768), (1920, 1080)]

        # Scene size == native size
        rect = self.scene().sceneRect()
        self.nativeW, self.nativeH = int(rect.width()), int(rect.height())

        # Filter resolutions to not exceed native
        resolutions = [res for res in resLst if res[0] <= self.nativeW]
        # Set native resolution first
        resolutions = sorted(resolutions, key=lambda elem: -elem[0])

        # Infinity cycle with resolutions
        for res in cycle(resolutions):
            # Scale to native
            factor = self.nativeW / res[0], self.nativeH / res[1]
            self.scale(*factor)

            yield res
            self.resolution = res

            # Scale to next resolution
            factor = res[0] / self.nativeW, res[1] / self.nativeH
            self.scale(*factor)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        if event.key() == Qt.Key_Escape:
            self.escPressed.emit()
