from element.editor_dialog import EditorDialog
from ui.dialogs.stat import Ui_StatDialog
from misc import helper


class StatDialog(EditorDialog):
    def __init__(self, file_location):
        super().__init__(Ui_StatDialog, 'Are you sure you want to exit without saving this stat?')

        self.file_location = file_location
        data = helper.get_json_data(self.file_location)
        self.ui.lineEditName.setText(data['name'])
        self.ui.plainTextEditDescription.setPlainText(data['desc'])

    def get_data(self):
        return {
            'name': str(self.ui.lineEditName.text()),
            'desc': str(self.ui.plainTextEditDescription.toPlainText())
        }

    def save_data(self):
        helper.save_json_data(self.file_location, self.get_data())
