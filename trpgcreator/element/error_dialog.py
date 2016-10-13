from PyQt5.QtWidgets import QDialog
from trpgcreator.ui.dialogs.error import Ui_ErrorDialog


class ErrorDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.ui = Ui_ErrorDialog()
        self.ui.setupUi(self)
        self.ui.label.setText(message)
