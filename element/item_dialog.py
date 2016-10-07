from element.editor_dialog import EditorDialog
from ui.dialogs.item import Ui_ItemDialog
from misc import helper


class ItemDialog(EditorDialog):
    def __init__(self, file_location):
        super().__init__(Ui_ItemDialog, 'Are you sure you want to exit without saving this item?')

        self.file_location = file_location
        data = helper.get_json_data(self.file_location)
        self.ui.lineEditName.setText(data['name'])
        self.ui.textEditDescription.setPlainText(data['desc'])
        self.ui.spinBoxValue.setValue(data['value'])
        self.ui.textEditUse.setPlainText(data['use'])

    def get_data(self):
        return {
            'name': str(self.ui.lineEditName.text()),
            'desc': str(self.ui.textEditDescription.toPlainText()),
            'value': self.ui.spinBoxValue.value(),
            'use': str(self.ui.textEditUse.toPlainText()),
            'equip': False  # TODO: Stats and equipment properly
        }

    def save_data(self):
        helper.save_json_data(self.file_location, self.get_data())
