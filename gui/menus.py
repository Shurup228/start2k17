"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout
from gui.buttons import Button


class MainMenu(GridLayout):

    def changeResolution(self):
        if self.winWidget.resMode == 0:
            self.winWidget.resize(800, 600)
            self.winWidget.resMode = 1
        else:
            self.winWidget.showFullScreen()
            self.winWidget.resMode = 0

    def __init__(self, scene, widget):
        super().__init__(scene)
        self.winWidget = widget
        self.makeLayout()

    def startGame(self):
        pass

    def gotoOptions(self):
        newLayout = Options(self._scene)
        self._scene.nextScene(newLayout)

    def makeLayout(self):
        start = Button('Start')
        options = Button('Options')
        exit = Button('Quit')
        resolution = Button(str(self.winWidget.size.width()) +
                            ' X ' + str(self.winWidget.size.height()))

        start.clicked.connect(self.startGame)
        options.clicked.connect(self.gotoOptions)
        resolution.clicked.connect(self.changeResolution)
        exit.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(options, 1, 1)
        self.addItem(exit, 2, 1)
        self.addItem(resolution, 0, 0)


class Options(GridLayout):
    pass
