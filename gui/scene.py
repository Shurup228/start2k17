"""Scene sets here."""
# coding=utf-8

from logging import getLogger
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QTimer

L = getLogger('gameLogger')


class _Wrapper:
    """Helper for scene combined mode."""

    def __init__(self, *layouts):
        L.debug('\u001b[33mCreating Wrapper for combo mode\u001b[0m')
        self.layouts = [*layouts]
        self.hided = True

        functions = ['pause', 'resume', 'resize', 'repaint', 'update',
                     'prepareGeometry']
        L.debug('\u001b[34mFilling Wrapper with functions\u001b[0m')

        # Creating functions for wrapper
        for func in functions:
            f = lambda func=func: self.forEach(func)
            setattr(self, func, f)

        self.__repr__ = self.__str__

    def __str__(self):
        return 'Wrapper[' + ', '.join([str(l) for l in self.layouts]) + ']'

    def __call__(self, *args):
        return self

    def addLayout(self, layout):
        L.debug('\u001b[34mAdding {} to Wrapper\u001b[0m'.format(layout))
        self.layouts.append(layout)

    def removeLayout(self, layout):
        L.debug('\u001b[34mRemoving {} from Wrapper\u001b[0m'.format(layout))
        self.layouts.remove(layout)
        L.debug('\u001b[34mHiding {}\u001b[0m'.format(layout))
        layout.hide()

    def forEach(self, funcName: str):
        if funcName not in 'prepareGeometryupdateresizerepaint':
            L.debug('\u001b[34mApplying {} in Wrapper\u001b[0m'.format(funcName))
        for layout in self.layouts:
            getattr(layout, funcName)()

    def hide(self):
        self.hided = True
        self.forEach('hide')

    def show(self):
        self.hided = False
        self.forEach('show')


class Scene(QGraphicsScene):
    __TIMER_DELAY = 20

    PAUSE = 'PAUSE'
    CLEAR = 'CLEAR'
    SAVE = 'SAVE'
    COMBINE = 'COMBINE'

    def __init__(self, *args):
        super().__init__(*args)
        L.debug('\u001b[33mInitializing scene\u001b[0m')
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
        L.debug('\u001b[33mInitializing timer\u001b[0m')
        self.__timer = QTimer(self)

        self.__timer.timeout.connect(self.__update)

        self.__timer.start(self.__TIMER_DELAY)

    def recoverTimer(self):
        self.__paused = False
        L.debug('\u001b[34mRecovering timer\u001b[0m')
        self.__timer.start()

        L.debug('\u001b[34mRecovering scene\u001b[0m')
        self.layout.resume()

    def __update(self):
        """Updates current scene."""
        try:
            currentScene = self.layout
        except IndexError:
            return

        currentScene.update()

    def resizeLayouts(self):
        """Resizes layouts in buffer.

        Primarily used when resolution changed =)
        """
        L.debug('\u001b[34mResizing {}\u001b[0m'.format(self.__sceneStack))
        for layout in self.__sceneStack:
            layout.prepareGeometry()

    def hide(self, layout):
        if not layout.hided:
            L.debug('\u001b[34mHiding {}\u001b[0m'.format(layout))
            layout.hide()
            return
        L.debug('\u001b[34mSkipping {}\u001b[0m'.format(layout))

    def show(self, layout):
        if layout.hided:
            L.debug('\u001b[34mShowing {}\u001b[0m'.format(layout))
            layout.show()
            return
        L.debug('\u001b[34mSkipping {}\u001b[0m'.format(layout))

    def clear(self):
        L.debug('\u001b[34mClearing {}\u001b[0m'.format(self.__sceneStack))
        for layout in self.__sceneStack:
            self.hide(layout)

        self.__sceneStack.clear()

    def wrap(self, toWrap):
        """Wraps scenes in wrapper and return it.

        toWrap is a dict, with key = layout and value = args, scene passed to
        layouts implicitly
        """
        L.debug('\u001b[34mWrapping {}\u001b[0m'.format(toWrap))
        wrapper = _Wrapper()
        for layout, args in toWrap.items():
            wrapper.addLayout(layout(self, *args))

        return wrapper

    def nextLayout(self, layout, *args, mode=None):
        mode = mode or self.CLEAR
        L.debug('\u001b[34mSetting next layout {} in {} mode\u001b[0m'.format(layout, mode))
        layout = layout(self, *args)

        if len(self.__sceneStack):
            if mode == self.PAUSE:
                L.debug('\u001b[34mPausing timer\u001b[0m')
                self.__timer.stop()

                self.__paused = True

                L.debug('\u001b[34mPausing {}\u001b[0m'.format(self.layout))
                self.layout.pause()
                self.layout.hide()
            elif mode == self.SAVE:
                self.hide(self.layout)
            elif mode == self.COMBINE:
                curScene = self.__sceneStack.pop()

                try:
                    curScene.addLayout(layout)
                except AttributeError:
                    layout = _Wrapper(curScene, layout)
            else:
                self.clear()

        self.__sceneStack.append(layout)
        L.debug('\u001b[32mCurrent scenes: {}\u001b[0m'.format(self.__sceneStack))
        self.show(layout)

    def prevLayout(self):
        L.debug('\u001b[34mFalling back to previsious scene\u001b[0m')
        currentScene = self.__sceneStack.pop()
        self.hide(currentScene)
        L.debug('\u001b[32mCurrent scenes: {}\u001b[0m'.format(self.__sceneStack))

        if self.__paused:
            self.recoverTimer()

        self.show(self.layout)
