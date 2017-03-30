"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout, Layout, Map
from gui.buttons import Button


class MainMenu(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.makeLayout()

    def changeScene(self, scene: Layout, switchType):
        layout = scene(self._scene)
        self._scene.nextScene(layout, switchType)

    def makeLayout(self):
        start = Button('Start')
        options = Button('Options')
        exit = Button('Quit')

        start.clicked.connect(lambda:
                              self.changeScene(Maps, self._scene.SAVE))
        options.clicked.connect(lambda:
                                self.changeScene(Options, self._scene.SAVE))
        exit.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(options, 1, 1)
        self.addItem(exit, 2, 1)


class Options(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        self.view = self._scene.views()[0]
        self.view.escPressed.connect(self._scene.prevScene)

        self.makeLayout()

    def makeLayout(self):
        back = Button('Back')

        back.clicked.connect(self._scene.prevScene)

        self.addItem(back, 0, 0)

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect()


class Maps(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        # List with maps
        self.maps = None
        self.view = self._scene.views()[0]
        self.view.escPressed.connect(self._scene.prevScene)

        self.makeLayout()

    def getMaps(self):
        from os import listdir
        self.maps = [map for map in listdir('maps') if map.endswith('.map')]

    def makeLayout(self):
        self.getMaps()

        # Make our collon central
        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)

        row = col = 0
        for map in self.maps:
            if col == 3:
                col = 0
                row += 1

            button = Button(map)
            button.clicked.connect(lambda:
                                   self._scene.nextScene(Map(self._scene,
                                                             'maps/' + map)))
            self.addItem(button, row, col)

            col += 1

        back = Button('Back')
        back.clicked.connect(self._scene.prevScene)
        self.addItem(back, row + 1, 1)

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect()
