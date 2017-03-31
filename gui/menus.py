"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout, Map
from gui.buttons import Button


class MainMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.makeLayout()

    def makeLayout(self):
        start = Button('Start')
        options = Button('Options')
        exit = Button('Quit')

        start.clicked.connect(lambda: self.scene.nextLayout(Maps, type_=self.scene.SAVE))
        options.clicked.connect(lambda: self.scene.nextLayout(Options, type_=self.scene.SAVE))
        exit.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(options, 1, 1)
        self.addItem(exit, 2, 1)


class Options(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)

        self.view.escPressed.connect(self.scene.prevLayout)
        self.makeLayout()

    def changeResolution(self, button):
        res = next(self.view.nextResolution)
        self.view.resolution = res

        # Adapting layout to new geometry
        # Calls prepareGeomety under the hood
        self.scene.resizeLayouts()

        button.changeText('Resolution:\n\n{} x {}'.format(*res))

    def makeLayout(self):
        try:
            text = 'Resolution:\n\n{} x {}'.format(*self.view.resolution)
        except TypeError:
            text = 'Resolution:\n\n{} x {}'.format(self.view.nativeW, self.view.nativeH)

        res = Button(text)
        back = Button('Back')

        res.clicked.connect(lambda: self.changeResolution(res))
        back.clicked.connect(self.scene.prevLayout)

        self.addItem(res, 0, 0)
        self.addItem(back, 1, 0)

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect(self.scene.prevLayout)


class Maps(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        # List with maps
        self.maps = None

        self.view.escPressed.connect(self.scene.prevLayout)
        self.makeLayout()

    def getMaps(self):
        from os import listdir
        self.maps = [map for map in listdir('maps') if map.endswith('.map')]

    def makeLayout(self):
        self.getMaps()

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

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect(self.scene.prevLayout)


class InGameMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.makeLayout()

    def makeLayout(self):
        mainMenu = Button('Main Menu')
        resume = Button('Resume')
        exit = Button('Exit')

        mainMenu.clicked.connect(lambda: self.scene.nextLayout(MainMenu))
        exit.clicked.connect(quit)

        self.view.escPressed.connect(self.scene.prevLayout)
        resume.clicked.connect(self.scene.prevLayout)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(resume, 0, 1)
        self.addItem(mainMenu, 1, 1)
        self.addItem(exit, 2, 1)

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect(self.scene.prevLayout)
