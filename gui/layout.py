"""Layout like layouts in qt(QGridLayout)."""
# coding=utf-8

from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItem


class Layout(metaclass=ABCMeta):
    """Base layout class(For inheritance only)."""

    def __init__(self, scene: QGraphicsScene):
        self.__scene = scene
        # Keeps all items in layout
        self.__items = []
        # State of layout
        self.__pause = False
        # Parent item for group
        self.__rootItem = None

    @abstractmethod
    def addItem(self):
        pass

    @abstractmethod
    def show(self):
        """Show all item's in layout."""
        pass

    @abstractmethod
    def hide(self):
        """The same as show but hide."""
        pass

    def pause(self):
        pass

    def update(self):
        """Updates all items in layout."""
        pass


class GridLayout(Layout):
    """Grid layout for managing simple menus."""

    # Dummy item
    DUMMY = ''

    def __init__(self, scene: QGraphicsScene):
        super().__init__(scene)
        self.__scene = scene
        self.__width, self.__height = scene.width(), scene.height()
        self.__rectWidth, self.__rectHeight = None, None
        self.rows, self.colls = 1, 1
        self.items = [[]]

    def hasItem(self):
        for row in self.items:
            for item in row:
                if item != self.DUMMY:
                    return True

        return False

    def addItem(self, item: QGraphicsItem, row: int, coll: int):
        if item != self.DUMMY:
            if not self.hasItem():
                self.__rootItem = item
                self.__rootItem.setParentItem(None)
            else:
                item.setParentItem(self.__rootItem)

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

                # Center of scene rect in which we will place widget
                sceneX = self.__rectWidth * coll + self.__rectWidth / 2
                sceneY = self.__rectHeight * row + self.__rectHeight / 2

                # Center of widget bounding rect
                x = sceneX - width / 2
                y = sceneY - height / 2

                # We need to shift item coords because of itemGroup
                # Fucking itemGroup in qt shifts all coords by parent coords
                # FUCK!!
                x = x - self.__rootItem.x() if item != self.__rootItem else x
                y = y - self.__rootItem.y() if item != self.__rootItem else y

                item.setPos(x, y)

    def show(self):
        # Here, at last, we can use the benefits of item group
        self.__scene.addItem(self.__rootItem)

    def hide(self):
        # Here too
        self.__scene.removeItem(self.__rootItem)
