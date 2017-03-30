"""Layout like layouts in qt(QGridLayout)."""
# coding=utf-8
from gui.buttons import Button


class Layout:
    """Grid layout for managing simple menus."""

    # Dummy item
    DUMMY = ''

    def __init__(self, scene):
        self.__scene = scene
        self.width, self.height = scene.width(), scene.height()
        self.rectWidth, self.rectHeight = None, None
        self.rows, self.colls = 1, 1
        # items - matrix with elements
        self.items = [[]]

    def addItem(self, item, row, coll):
        self.rows = self.rows if row + 1 <= self.rows else row + 1
        self.colls = self.colls if coll + 1 <= self.colls else coll + 1
        self.resize()

        if item != self.DUMMY:
            self.__scene.addItem(item)

        self.items[row][coll] = item
        self.repaint()

    def resize(self):
        """Fill item matrix to fit in all colls and rows."""
        for x in range(self.rows + 1 - len(self.items)):
            self.items.append([])

        for row in range(len(self.items)):
            for y in range(self.colls - len(self.items[row])):
                self.items[row].append(self.DUMMY)

        self.rectWidth = self.width / self.colls
        self.rectHeight = self.height / self.rows

    def repaint(self):
        """Redraws all widgets after new added and matrix resized."""
        for row in range(self.rows):
            for coll in range(self.colls):
                item = self.items[row][coll]

                if item == self.DUMMY:
                    continue

                rect = item.boundingRect()
                width, height = rect.width(), rect.height()

                sceneX = self.rectWidth * coll + self.rectWidth / 2
                x = sceneX - width / 2

                sceneY = self.rectHeight * row + self.rectHeight / 2
                y = sceneY - height / 2

                item.setPos(x, y)


class MainMenu(Layout):
    def __init__(self, scene, widget):
        super().__init__(scene)
        self.winWidget = widget
        self.makeLayout()

    def makeLayout(self):
        startButton = Button('Start')
        optionsButton = Button('Options')
        exitButton = Button('Quit')
        resolutionButton = Button(str(self.winWidget.wWidth) + ' X ' + str(self.winWidget.wHeight),
                                  self.winWidget)

        #startButton.clicked.connect()
        #optionsButton.clicked.connect()
        resolutionButton.clicked.connect(resolutionButton.changeRes)
        exitButton.clicked.connect(quit)


        # self.addItem(Layout.DUMMY, 0, 0)
        # self.addItem(Layout.DUMMY, 0, 2)
        # self.addItem(startButton, 0, 1)
        # self.addItem(optionsButton, 1, 1)
        # self.addItem(exitButton, 2, 1)
        self.addItem(resolutionButton, 0, 0)

class Options(Layout):
    pass


