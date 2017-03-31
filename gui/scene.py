"""Scene sets here."""
# coding=utf-8

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QTimer


class Wrapper:
    """Helper for scene combined mode."""

    def __init__(self, *layouts):
        self.layouts = [*layouts]

        functions = ['pause', 'show', 'hide', 'resume', 'resize', 'repaint',
                     'update', 'prepareGeomety']
        for func in functions:
            f = lambda: self.forEach(func)
            setattr(self, func, f)

    def addLayout(self, layout):
        self.layouts.append(layout)

    def forEach(self, funcName: str):
        for layout in self.layouts:
            getattr(layout, funcName)()


class Scene(QGraphicsScene):
    __TIMER_DELAY = 20

    PAUSE = 'pause'
    CLEAR = 'clear'
    SAVE = 'save'
    COMBINE = 'combine'

    def __init__(self, *args):
        super().__init__(*args)
        # Layout buffer
        self.__sceneStack = []
        # Show when game on pause
        self.__paused = False
        self.__timer = None

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

        currentScene.update()

    def resizeLayouts(self):
        """Resizes layouts in buffer.

        Primarily used when resolution changed =)
        """
        for layout in self.__sceneStack:
            layout.prepareGeometry()

    def clear(self):
        for layout in self.__sceneStack:
            layout.hide()

        self.__sceneStack.clear()

    def nextLayout(self, layout, *args, type_=None):
        type_ = type_ or self.CLEAR
        layout = layout(self, *args)

        if len(self.__sceneStack):
            if type_ == self.PAUSE:
                self.__timer.stop()

                self.__paused = True

                self.__sceneStack[-1].pause()
            elif type_ == self.SAVE:
                self.__sceneStack[-1].hide()
            elif type_ == self.COMBINE:
                curScene = self.__sceneStack.pop()

                try:
                    curScene.addLayout(layout)
                except AttributeError:
                    layout = Wrapper(curScene, layout)
            else:
                self.clear()

        self.__sceneStack.append(layout)
        layout.show()

    def prevLayout(self):
        currentScene = self.__sceneStack.pop()
        currentScene.hide()

        if self.__paused:
            self.__paused = False
            self.__timer.start()

            self.__sceneStack[-1].resume()
        else:
            self.__sceneStack[-1].show()
