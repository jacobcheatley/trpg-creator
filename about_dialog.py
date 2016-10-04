from PyQt5.QtWidgets import QDialog
from ui.dialogs.about_dialog import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
