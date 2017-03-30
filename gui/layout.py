"""Layout like layouts in qt(QGridLayout)."""
# coding=utf-8

from abc import ABCMeta, abstractmethod


class Layout(metaclass=ABCMeta):
    """Base layout class(For inheritance only)."""

    def __init__(self, scene):
        self.__scene = scene

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass


class GridLayout(Layout):
    """Grid layout for managing simple menus."""

    # Dummy item
    DUMMY = ''

    def __init__(self, scene):
        super().__init__(scene)
        self.__scene = scene
        self.__width, self.__height = scene.width(), scene.height()
        self.__rectWidth, self.__rectHeight = None, None
        self.rows, self.colls = 1, 1
        # items - matrix with elements
        self.items = [[]]

    def addItem(self, item, row, coll):
        self.rows = self.rows if row + 1 <= self.rows else row + 1
        self.colls = self.colls if coll + 1 <= self.colls else coll + 1
        self.resize()

        self.items[row][coll] = item
        self.repaint()

    def resize(self):
        """Fill item matrix to fit in all colls and rows."""
        for x in range(self.rows + 1 - len(self.items)):
            self.items.append([])

        for row in range(len(self.items)):
            for y in range(self.colls - len(self.items[row])):
                self.items[row].append(self.DUMMY)

        self.__rectWidth = self.__width / self.colls
        self.__rectHeight = self.__height / self.rows

    def repaint(self):
        """Redraws all widgets after new added and matrix resized."""
        for row in range(self.rows):
            for coll in range(self.colls):
                item = self.items[row][coll]

                if item == self.DUMMY:
                    continue

                rect = item.boundingRect()
                width, height = rect.width(), rect.height()

                sceneX = self.__rectWidth * coll + self.__rectWidth / 2
                x = sceneX - width / 2

                sceneY = self.__rectHeight * row + self.__rectHeight / 2
                y = sceneY - height / 2

                item.setPos(x, y)

    def show(self):
        pass

    def hide(self):
        pass
