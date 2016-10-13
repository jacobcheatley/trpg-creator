from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt


class IgnoreEnter(QDialog):
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() in (Qt.Key_Return, Qt.Key_Enter):
            pass  # TODO: Make this into a TAB hit instead
        else:
            super().keyPressEvent(QKeyEvent)
