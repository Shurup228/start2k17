
# coding=utf-8

from gui.button import Button


class ExitButton(Button):

    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        return quit()


class StartGame(Button):
    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        return None