"""Layout like layouts in qt(QGridLayout)."""
# coding=utf-8

DUMMY = ''


class Layout:
    def __init__(self, scene):
        self.__scene = scene
        self.width, self.height = scene.width(), scene.height()
        self.rectWidth, self.rectHeight = self.width, self.height
        self.rows = 1
        self.colls = 1
        # items - matrix with elements
        self.items = [[]]

    def addItem(self, item, row, coll):
        self.rows = self.rows if row + 1 <= self.rows else row + 1
        self.colls = self.colls if coll + 1 <= self.colls else coll + 1
        self.resize()

        if item != DUMMY:
            self.__scene.addItem(item)

        self.items[row][coll] = item
        self.repaint()


    def resize(self):
        for x in range(self.rows + 1 - len(self.items)):
            self.items.append([])

        for row in range(len(self.items)):
            for y in range(self.colls - len(self.items[row])):
                self.items[row].append('')

        self.rectWidth = self.width / self.colls
        self.rectHeight = self.height / self.rows

    def repaint(self):
        for row in range(self.rows):
            for coll in range(self.colls):
                item = self.items[row][coll]

                if item == '':
                    continue

                rect = item.boundingRect()
                width, height = rect.width(), rect.height()

                sceneX = self.rectWidth * coll + self.rectWidth / 2
                x = sceneX - width / 2

                sceneY = self.rectHeight * row + self.rectHeight / 2
                y = sceneY - height / 2

                item.setPos(x, y)
