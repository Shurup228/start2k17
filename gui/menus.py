"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout
from gui.buttons import Button


class MainMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.makeLayout()

    def startGame(self):
        raise NotImplementedError

    def gotoOptions(self):
        layout = Options(self._scene)
        self._scene.nextScene(layout, self._scene.SAVE)

    def makeLayout(self):
        start = Button('Start')
        options = Button('Options')
        exit = Button('Quit')

        start.clicked.connect(self.startGame)
        options.clicked.connect(self.gotoOptions)
        exit.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(options, 1, 1)
        self.addItem(exit, 2, 1)


class Options(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.makeLayout()

    def makeLayout(self):
        back = Button('Back')

        back.clicked.connect(self._scene.prevScene)

        self.addItem(back, 0, 0)
