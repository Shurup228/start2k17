"""Menus for game."""
# coding=utf-8

from gui.layout import GridLayout, Layout
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
        maps = Button('Choose map')
        options = Button('Options')
        exit = Button('Quit')

        start.clicked.connect(lambda: print('NotImplemented'))
        maps.clicked.connect(lambda:
                             self.changeScene(Maps, self._scene.SAVE))
        options.clicked.connect(lambda:
                                self.changeScene(Options, self._scene.SAVE))
        exit.clicked.connect(quit)

        self.addItem(self.DUMMY, 0, 0)
        self.addItem(self.DUMMY, 0, 2)
        self.addItem(start, 0, 1)
        self.addItem(maps, 1, 1)
        self.addItem(options, 2, 1)
        self.addItem(exit, 3, 1)


class Options(GridLayout):
    resLst = [[800, 600], [1024, 768], [1366, 768], [1920, 1080]]

    def __init__(self, scene):
        super().__init__(scene)
        self.view = self._scene.views()[0]
        self.view.escPressed.connect(self._scene.prevScene)

        self.currentRes = 0
        self.nativeW, self.nativeH = self._scene.sceneRect().size().width(), self._scene.sceneRect().size().height()

        self.makeLayout()

    def changeResol(self, resButton):
        if self.currentRes == 0:
            self.currentRes += 1
            self.view.scale(self.resLst[self.currentRes][0] / self.nativeW,
                            self.resLst[self.currentRes][1] / self.nativeH)
            resButton.changeText(str(self.resLst[self.currentRes][0]) + ' X ' + str(self.resLst[self.currentRes][1]))
            self.view.globalRes = [self.resLst[self.currentRes]]
            print('if')


        elif self.currentRes == len(self.resLst) - 1:
            self.view.scale(self.nativeW / self.resLst[self.currentRes][0],
                            self.nativeH / self.resLst[self.currentRes][1])
            resButton.changeText(str(int(self.nativeW)) + ' X ' + str(int(self.nativeH)))
            self.currentRes = 0
            self.view.globalRes = [self.nativeW, self.nativeH]
            print('elif', self.resLst[self.currentRes])

        else:
            self.view.scale(self.nativeW / self.resLst[self.currentRes][0],
                            self.nativeH / self.resLst[self.currentRes][1])
            self.currentRes += 1
            self.view.scale(self.resLst[self.currentRes][0] / self.nativeW,
                            self.resLst[self.currentRes][1] / self.nativeH)
            resButton.changeText(str(self.resLst[self.currentRes][0]) + ' X ' + str(self.resLst[self.currentRes][1]))
            self.view.globalRes = [self.resLst[self.currentRes]]
            print('else', self.resLst[self.currentRes])

    def makeLayout(self):
        if len(self.view.globalRes):
            buttonText = '{} X {}'.format(self.view.globalRes[0], self.view.globalRes[1])
        else:
            buttonText = '{} X {}'.format(self.nativeW, self.nativeH)
        back = Button('Back')
        res = Button(buttonText)
        back.clicked.connect(self._scene.prevScene)
        res.clicked.connect(lambda: self.changeResol(res))

        self.addItem(back, 0, 0)
        self.addItem(res, 0, 1)

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

        for row, map in enumerate(self.maps):
            button = Button(map)
            self.addItem(button, row, 1)

        back = Button('Back')
        back.clicked.connect(self._scene.prevScene)
        self.addItem(back, row + 1, 1)

    def hide(self):
        super().hide()
        self.view.escPressed.disconnect()
