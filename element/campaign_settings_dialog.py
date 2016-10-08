from ui.dialogs.campaign_settings import Ui_CampaignSettingsDialog
from element.inv_row_widget import InvRow
from element.global_row_widget import GlobalRow
from PyQt5.QtWidgets import QListWidgetItem
from misc import helper
from element.editor_dialog import EditorDialog


class CampaignSettingsDialog(EditorDialog):
    def __init__(self, settings_dir):
        super().__init__(Ui_CampaignSettingsDialog, 'Are you sure you want to exit without saving the campaign settings?')

        # Connections
        self.ui.standardInventoryAdd.clicked.connect(
            lambda: self.add_inventory_item(self.ui.standardInventoryList, '', 1))
        self.ui.debugInventoryAdd.clicked.connect(
            lambda: self.add_inventory_item(self.ui.debugInventoryList, '', 1))
        self.ui.standardGlobalsAdd.clicked.connect(lambda: self.add_global_var(self.ui.standardGlobalsList, '', 0))
        self.ui.debugGlobalsAdd.clicked.connect(lambda: self.add_global_var(self.ui.debugGlobalsList, '', 0))
        
        # Setup
        self.settings_dir = settings_dir

        # Set up standard stuff
        standard_player_data = helper.get_json_data(settings_dir + '/std/player.json')
        standard_globals_data = helper.get_json_data(settings_dir + '/std/globals.json')

        for name, count in standard_player_data['inventory']['items'].items():
            self.add_inventory_item(self.ui.standardInventoryList, name, count)
        self.ui.standardCurrency.setValue(standard_player_data['inventory']['currency'])
        self.ui.standardStarting.setText(standard_player_data['scenario'])
        for name, value in standard_globals_data.items():
            self.add_global_var(self.ui.standardGlobalsList, name, value)
        # TODO: Stats

        # Set up debug stuff
        debug_player_data = helper.get_json_data(settings_dir + '/debug/player.json')
        debug_globals_data = helper.get_json_data(settings_dir + '/debug/globals.json')

        for name, count in debug_player_data['inventory']['items'].items():
            self.add_inventory_item(self.ui.debugInventoryList, name, count)
        self.ui.debugCurrency.setValue(debug_player_data['inventory']['currency'])
        self.ui.debugStarting.setText(debug_player_data['scenario'])
        for name, value in debug_globals_data.items():
            self.add_global_var(self.ui.debugGlobalsList, name, value)
        # TODO: Stats

        # Set up export stuff
        export_data = helper.get_json_data(settings_dir + '/export.json')

        self.ui.lineEditCampaignName.setText(export_data['name'])
        self.ui.lineEditCreator.setText(export_data['creator'])
        self.ui.plainTextEditAbout.setPlainText(export_data['about'])

    @staticmethod
    def add_inventory_item(inventory_list, name, count):
        list_item = QListWidgetItem(inventory_list)
        inv_row = InvRow(name, count, lambda: inventory_list.takeItem(inventory_list.row(list_item)))
        list_item.setSizeHint(inv_row.sizeHint())
        inventory_list.addItem(list_item)
        inventory_list.setItemWidget(list_item, inv_row)

    @staticmethod
    def add_global_var(globals_list, name, value):
        list_item = QListWidgetItem(globals_list)
        global_row = GlobalRow(name, value, lambda: globals_list.takeItem(globals_list.row(list_item)))
        list_item.setSizeHint(global_row.sizeHint())
        globals_list.addItem(list_item)
        globals_list.setItemWidget(list_item, global_row)

    def save_standard(self):
        # Init
        standard_start = str(self.ui.standardStarting.text())
        # Inventory
        standard_items = {}
        for index in range(self.ui.standardInventoryList.count()):
            item = self.ui.standardInventoryList.itemWidget(self.ui.standardInventoryList.item(index))
            standard_items[item.get_name()] = item.get_count()
        helper.save_json_data(self.settings_dir + '/std/player.json', {
            'scenario': standard_start,
            'inventory': {
                'currency': self.ui.standardCurrency.value(),
                'items': standard_items
            },
            'stats': {}
        })
        # Globals
        standard_globals = {}
        for index in range(self.ui.standardGlobalsList.count()):
            item = self.ui.standardGlobalsList.itemWidget(self.ui.standardGlobalsList.item(index))
            standard_globals[item.get_name()] = item.get_value()
        helper.save_json_data(self.settings_dir + '/std/globals.json', standard_globals)

    def save_debug(self):
        # Init
        debug_start = str(self.ui.debugStarting.text())
        # Inventory
        debug_items = {}
        for index in range(self.ui.debugInventoryList.count()):
            item = self.ui.debugInventoryList.itemWidget(self.ui.debugInventoryList.item(index))
            debug_items[item.get_name()] = item.get_count()
        helper.save_json_data(self.settings_dir + '/debug/player.json', {
            'scenario': debug_start,
            'inventory': {
                'currency': self.ui.debugCurrency.value(),
                'items': debug_items
            },
            'stats': {}
        })
        # Globals
        debug_globals = {}
        for index in range(self.ui.debugGlobalsList.count()):
            item = self.ui.debugGlobalsList.itemWidget(self.ui.debugGlobalsList.item(index))
            debug_globals[item.get_name()] = item.get_value()
        helper.save_json_data(self.settings_dir + '/debug/globals.json', debug_globals)

    def save_export(self):
        helper.save_json_data(self.settings_dir + '/export.json', {
            'name': self.ui.lineEditCampaignName.text(),
            'creator': self.ui.lineEditCreator.text(),
            'about': self.ui.plainTextEditAbout.toPlainText()
        })

    def save_data(self):
        self.save_standard()
        self.save_debug()
        self.save_export()
