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

        self._view.escPressed.connect(self._scene.prevScene)
        self.makeLayout()

    def changeResolution(self, button):
        res = next(self._view.nextResolution)

        # Adapting layout to new geometry
        self.prepareGeometry(*res)

        button.changeText('Resolution:\n\n{} x {}'.format(*res))
        print('Button pressed, current res -> {} x {}'.format(*res))

    def makeLayout(self):
        try:
            text = 'Resolution:\n\n{} x {}'.format(*self._view.resolution)
        except TypeError:
            text = 'Resolution:\n\n{} x {}'.format(self._view.nativeW, self._view.nativeH)

        res = Button(text)
        back = Button('Back')

        res.clicked.connect(lambda: self.changeResolution(res))
        back.clicked.connect(self._scene.prevScene)

        self.addItem(res, 0, 0)
        self.addItem(back, 1, 0)

    def hide(self):
        super().hide()
        self._view.escPressed.disconnect()


class Maps(GridLayout):
    def __init__(self, scene):
        super().__init__(scene)
        # List with maps
        self.maps = None

        self._view.escPressed.connect(self._scene.prevScene)
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
            button.clicked.connect(lambda:
                                   self._scene.nextScene(Map(self._scene,
                                                             'maps/' + map)))
            self.addItem(button, row, col)

            col += 1

        back = Button('Back')
        back.clicked.connect(self._scene.prevScene)
        self.addItem(back, row + 1, col - 1)

    def hide(self):
        super().hide()
        self._view.escPressed.disconnect()
