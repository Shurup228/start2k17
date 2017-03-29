"""View setup"""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsView



class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()

    def initView(self):
        self.show()