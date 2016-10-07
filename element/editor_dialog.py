from element.ignore_enter import IgnoreEnter
from element.confirm_dialog import ConfirmDialog


class EditorDialog(IgnoreEnter):
    def __init__(self, ui_cls, message):
        super().__init__()
        self.ui = ui_cls()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.save_and_exit())
        self.ui.buttonBox.rejected.connect(ConfirmDialog.confirm_exit(self, message))

    def save_data(self):
        pass

    def save_and_exit(self):
        self.save_data()
        self.done(1)
