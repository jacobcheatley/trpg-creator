from PyQt5.QtWidgets import QDialog
from ui.dialogs.test import Ui_TestDialog


class TestDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestDialog()
        self.ui.setupUi(self)
