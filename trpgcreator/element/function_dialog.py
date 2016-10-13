from .editor_dialog import EditorDialog
from trpgcreator.ui.dialogs.function import Ui_FunctionDialog
from trpgcreator.misc import helper


class FunctionDialog(EditorDialog):
    def __init__(self, file_location):
        super().__init__(Ui_FunctionDialog, 'Are you sure you want to exit without saving this function?')

        self.file_location = file_location
        self.ui.plainTextEditFunc.setPlainText(helper.get_json_data(file_location))

    def save_data(self):
        helper.save_json_data(self.file_location, self.ui.plainTextEditFunc.toPlainText())