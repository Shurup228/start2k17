"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout
from gui.buttons import Button


class MainMenu(GridLayout):
    def __init__(self, scene, widget):
        super().__init__(scene)
        self.winWidget = widget
        self.makeLayout()

    def startGame(self):
        pass

    def gotoOptions(self):
        pass

    def changeResolution(self):
        if self.winWidget.resMode == 0:
            self.winWidget.resize(800, 600)
            self.winWidget.resMode = 1
        else:
            self.winWidget.showFullScreen()
            self.winWidget.resMode = 0

    def makeLayout(self):
        startButton = Button('Start')
        optionsButton = Button('Options')
        exitButton = Button('Quit')
        resolutionButton = Button(str(self.winWidget.size.width()) +
                                  ' X ' + str(self.winWidget.size.height()))

        startButton.clicked.connect(self.startGame)
        optionsButton.clicked.connect(self.gotoOptions)
        resolutionButton.clicked.connect(self.changeResolution)
        exitButton.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(startButton, 0, 1)
        self.addItem(optionsButton, 1, 1)
        self.addItem(exitButton, 2, 1)
        self.addItem(resolutionButton, 0, 0)


class Options(GridLayout):
    pass
