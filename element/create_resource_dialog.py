from PyQt5.QtWidgets import QDialog
from ui.dialogs.create_resource import Ui_CreateResourceDialog


class CreateResourceDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateResourceDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(lambda: self.done(0))

    @classmethod
    def get_new_id(cls, resource_type):
        dialog = CreateResourceDialog()
        dialog.setWindowTitle('Create new ' + resource_type)
        dialog.ui.label.setText('Enter ID for ' + resource_type)
        if dialog.exec_():
            return str(dialog.ui.lineEditId.text())
        else:
            return None
