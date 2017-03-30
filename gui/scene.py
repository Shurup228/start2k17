"""Scene sets here."""
# coding=utf-8


from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QTimer
from gui.layout import Layout


class Scene(QGraphicsScene):
    __TIMER_DELAY = 20

    PAUSE = 'pause'
    CLEAR = 'clear'

    def __init__(self, *args):
        super().__init__(*args)
        self.__sceneStack = []
        self.initTimer()

    def initTimer(self):
        self.__timer = QTimer(self)

        self.__timer.timeout.connect(self.update)

        self.__timer.start(self.__TIMER_DELAY)

    def update(self):
        try:
            currentScene = self.__sceneStack[0]
        except IndexError:
            return

        currentScene.update()

    def nextScene(self, layout: Layout, switchType=None):
        switchType = switchType or self.CLEAR

        if len(self.__sceneStack):
            if switchType == self.PAUSE:
                self.__timer.stop()

                self.__sceneStack[0].pause()
            else:
                self.__sceneStack[0].hide()
                self.__sceneStack.pop()

        self.__sceneStack.append(layout)
        layout.show()

    def prevScene(self):
        pass
