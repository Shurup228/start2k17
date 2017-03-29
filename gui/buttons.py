
# coding=utf-8
from PyQt5.QtWidgets import (QGraphicsWidget, QStyleOptionButton, QStyle,
                            QApplication)


class ExitButton(QGraphicsWidget):
    def __init__(self):
        super().__init__()

    def paint(self, painter, option, widget=0):
        style = QStyleOptionButton()
        style.state = ((QStyle.State_Sunken if self.mouse_isPressed else
                        QStyle.State_Raised) | QStyle.State_Enabled)
        style.text = 'Text'
        style.palette = option.palette
        QApplication.style().drawControl(QStyle.CE_PushButton, style, painter)



    def mousePressEvent(self):
        self.mouse_isPressed = True
        self.update()

    def mouseReleaseEvent(self, event):
        self.mouse_isPressed = False
        self.update()
