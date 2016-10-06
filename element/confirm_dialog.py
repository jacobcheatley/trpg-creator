from element.ignore_enter import IgnoreEnter
from ui.dialogs.confirm import Ui_ConfirmDialog


class ConfirmDialog(IgnoreEnter):
    def __init__(self, question):
        super().__init__()
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(lambda: self.done(0))
        self.ui.label.setText(question)

    @classmethod
    def yes_to(cls, question):
        return ConfirmDialog(question).exec_()

    @classmethod
    def confirm_exit(cls, dialog, question):
        def func():
            if ConfirmDialog(question).exec_():
                dialog.done(0)
            else:
                pass

        return func
