"""Scene sets here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):
    def __init__(self, *args):
        super().__init__(*args)
