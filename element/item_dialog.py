from ui.dialogs.item import Ui_ItemDialog
from misc import helper
from element.ignore_enter import IgnoreEnter
from element.confirm_dialog import ConfirmDialog


class ItemDialog(IgnoreEnter):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ItemDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(ConfirmDialog.confirm_exit(self, 'Are you sure you want to exit without saving this item?'))

    def get_data(self):
        return {
            'name': str(self.ui.lineEditName.text()),
            'desc': str(self.ui.textEditDescription.toPlainText()),
            'value': self.ui.spinBoxValue.value(),
            'use': str(self.ui.textEditUse.toPlainText()),
            'equip': False  # TODO: Stats and equipment properly
        }

    @classmethod
    def setup(cls, file_location):
        data = helper.get_json_data(file_location)
        dialog = ItemDialog()
        dialog.ui.lineEditName.setText(data['name'])
        dialog.ui.textEditDescription.setPlainText(data['desc'])
        dialog.ui.spinBoxValue.setValue(data['value'])
        dialog.ui.textEditUse.setPlainText(data['use'])
        # TODO: Equip
        return dialog
