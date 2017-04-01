"""Menus for game."""
# coding=utf-8

from logging import getLogger
from gui.layout import GridLayout, Map
from gui.buttons import Button

L = getLogger('gameLogger')


class MainMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        L.debug('\u001b[33mInitializing MainMenu\u001b[0m')
        self.makeLayout()

    def makeLayout(self):
        L.debug('\u001b[33mGenerating buttons and connecting them\u001b[0m')
        start = Button('Start')
        options = Button('Options')
        exit = Button('Quit')

        start.clicked.connect(lambda: self.scene.nextLayout(Maps, mode=self.scene.SAVE))
        options.clicked.connect(lambda: self.scene.nextLayout(Options, mode=self.scene.SAVE))
        exit.clicked.connect(quit)

        L.debug('\u001b[34mAdding buttons to layout\u001b[0m')
        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(options, 1, 1)
        self.addItem(exit, 2, 1)


class Options(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        L.debug('\u001b[33mInitializing Options menu\u001b[0m')

        L.debug('\u001b[34mmConnecting esc to prevLayout\u001b[0m')
        self.view.escPressed.connect(self.scene.prevLayout)
        self.makeLayout()

    def changeResolution(self, button):
        L.debug('\u001b[34mChanging resolution\u001b[0m')
        res = next(self.view.nextResolution)
        L.debug('\u001b[32mNew resolution: {} x {}\u001b[0m'.format(*res))
        self.view.resolution = res

        # Adapting layout to new geometry
        # Calls prepareGeomety under the hood
        L.debug('\u001b[34mResing layouts to new resolution\u001b[0m')
        self.scene.resizeLayouts()

        L.debug('\u001b[34mChanging button text\u001b[0m')
        button.changeText('Resolution:\n\n{} x {}'.format(*res))

    def makeLayout(self):
        try:
            text = 'Resolution:\n\n{} x {}'.format(*self.view.resolution)
        except TypeError:
            text = 'Resolution:\n\n{} x {}'.format(self.view.nativeW, self.view.nativeH)

        L.debug('\u001b[34mGenerating buttons and connecting them\u001b[0m')
        res = Button(text)
        back = Button('Back')

        res.clicked.connect(lambda: self.changeResolution(res))
        back.clicked.connect(self.scene.prevLayout)

        L.debug('\u001b[34mAdding buttons to layout\u001b[0m')
        self.addItem(res, 0, 0)
        self.addItem(back, 1, 0)

    def hide(self):
        super().hide()
        L.debug('\u001b[34mDisconnecting prevLayout from esc\u001b[0m')
        self.view.escPressed.disconnect(self.scene.prevLayout)


class Maps(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        L.debug('\u001b[33mInitializing Maps menu\u001b[0m')
        # List with maps
        self.maps = None

        L.debug('\u001b[34mConnecting esc to prevLayout\u001b[0m')
        self.view.escPressed.connect(self.scene.prevLayout)
        self.makeLayout()

    def getMaps(self):
        from os import listdir
        L.debug('\u001b[34mFilling self.maps from maps folder\u001b[0m')
        self.maps = [map for map in listdir('maps') if map.endswith('.map')]

    def makeLayout(self):
        self.getMaps()
        L.debug('\u001b[34mBuilding map\u001b[0m')

        row = col = 0
        for map in self.maps:
            if col == 3:
                col = 0
                row += 1

            button = Button(map)
            button.clicked.connect(lambda map=map:
                                   self.scene.nextLayout(Map, 'maps/' + map))
            self.addItem(button, row, col)

            col += 1

        back = Button('Back')
        back.clicked.connect(self.scene.prevLayout)
        self.addItem(back, row + 1, col - 1)
        L.debug('\u001b[32mMap built\u001b[0m')

    def hide(self):
        super().hide()
        L.debug('\u001b[34mDisconnecting prevLayout from esc\u001b[0m')
        self.view.escPressed.disconnect(self.scene.prevLayout)


class InGameMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        L.debug('\u001b[33mInitializing InGameMenu\u001b[0m')
        self.makeLayout()

    def makeLayout(self):
        L.debug('\u001b[34mCreating buttons and connecting them\u001b[0m')
        mainMenu = Button('Main Menu')
        resume = Button('Resume')
        exit = Button('Exit')

        mainMenu.clicked.connect(self.scene.recoverTimer)
        mainMenu.clicked.connect(lambda: self.scene.nextLayout(MainMenu))
        exit.clicked.connect(quit)

        L.debug('\u001b[34mConnecting esc to prevLayout\u001b[0m')
        self.view.escPressed.connect(self.scene.prevLayout)
        resume.clicked.connect(self.scene.prevLayout)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(resume, 0, 1)
        self.addItem(mainMenu, 1, 1)
        self.addItem(exit, 2, 1)

    def hide(self):
        super().hide()
        L.debug('\u001b[34mDisconnecting prevLayout from esc\u001b[0m')
        self.view.escPressed.disconnect(self.scene.prevLayout)
