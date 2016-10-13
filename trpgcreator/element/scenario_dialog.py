from PyQt5.QtWidgets import QListWidgetItem
from .editor_dialog import EditorDialog
from .option_row_widget import OptionRow
from trpgcreator.misc import helper
from trpgcreator.ui.dialogs.scenario import Ui_ScenarioDialog


class ScenarioDialog(EditorDialog):
    def __init__(self, file_location):
        super().__init__(Ui_ScenarioDialog, 'Are you sure you want to exit without saving this scenario?')

        # Connections
        self.ui.pushButtonAdd.clicked.connect(lambda: self.add_option('', ''))

        self.file_location = file_location
        # Populate data
        data = helper.get_json_data(self.file_location)
        self.ui.lineEditName.setText(data['name'])
        self.ui.textEditDescription.setPlainText(data['desc'])
        self.populate_options(data['options'])

    def add_option(self, desc, func):
        option_list = self.ui.optionList
        list_item = QListWidgetItem(option_list)
        option_row = OptionRow(desc, func, lambda: option_list.takeItem(option_list.row(list_item)))
        list_item.setSizeHint(option_row.sizeHint())
        option_list.addItem(list_item)
        option_list.setItemWidget(list_item, option_row)

    def populate_options(self, options_data):
        for option in options_data:
            desc = option['desc']
            func = option['func']
            self.add_option(desc, func)

    def save_data(self):
        name = self.ui.lineEditName.text()
        desc = self.ui.textEditDescription.toPlainText()
        options = []
        option_list = self.ui.optionList
        for index in range(option_list.count()):
            option = option_list.itemWidget(option_list.item(index))
            options.append(option.get_data())

        helper.save_json_data(self.file_location, {
            'name': name,
            'desc': desc,
            'options': options
        })
