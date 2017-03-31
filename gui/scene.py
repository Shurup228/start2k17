"""Scene sets here."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QTimer


class Scene(QGraphicsScene):
    __TIMER_DELAY = 20

    PAUSE = 'pause'
    CLEAR = 'clear'
    COMBINE = 'combine'

    def __init__(self, *args):
        super().__init__(*args)
        self.__sceneStack = []
        self.initTimer()

    @property
    def layout(self):
        return self.__sceneStack[-1]

    def initTimer(self):
        self.__timer = QTimer(self)

        self.__timer.timeout.connect(self.__update)

        self.__timer.start(self.__TIMER_DELAY)

    def __update(self):
        """Updates current scene."""
        try:
            currentScene = self.__sceneStack[-1]
        except IndexError:
            return

        # If this is game layout, update all
        if isinstance(currentScene, tuple):
            for layout in currentScene:
                layout.update()

        currentScene.update()

    def resizeLayouts(self):
        """Resizes layouts in buffer.

        Primarily used when resolution changed =)
        """
        for layout in self.__sceneStack:
            if isinstance(layout, tuple):
                    for _layout in layout:
                        _layout.prepareGeometry()

            layout.prepareGeometry()

    def nextLayout(self, layout, *args, type_=None):
        type_ = type_ or self.CLEAR
        layout = layout(self, *args)

        if len(self.__sceneStack):
            if type_ == self.PAUSE:
                self.__timer.stop()

                self.__sceneStack[-1].pause()
            elif type_ == self.COMBINE:
                curScene = self.__sceneStack.pop()
                layout = (curScene, layout)
            else:
                self.__sceneStack.pop().hide()

        self.__sceneStack.append(layout)
        layout.show()

    def prevLayout(self):
        currentScene = self.__sceneStack.pop()
        currentScene.hide()

        self.__sceneStack[-1].show()
