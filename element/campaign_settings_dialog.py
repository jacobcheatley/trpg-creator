from element.ignore_enter import IgnoreEnter
from ui.dialogs.campaign_settings import Ui_CampaignSettingsDialog
from element.inv_row_widget import InvRow
from PyQt5.QtWidgets import QListWidgetItem
from misc import helper


class CampaignSettingsDialog(IgnoreEnter):
    def __init__(self, settings_dir):
        super().__init__()
        self.ui = Ui_CampaignSettingsDialog()
        self.ui.setupUi(self)

        # Connections
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(lambda: self.done(0))
        self.ui.standardInventoryAdd.clicked.connect(
            lambda: self.add_inventory_item(self.ui.standardInventoryList, '', 1)
        )
        self.ui.debugInventoryAdd.clicked.connect(
            lambda: self.add_inventory_item(self.ui.debugInventoryList, '', 1)
        )
        
        # Setup
        self.settings_dir = settings_dir

        # Set up standard stuff
        standard_player_data = helper.get_json_data(settings_dir + '/std/player.json')
        standard_globals_data = helper.get_json_data(settings_dir + '/std/globals.json')

        print(standard_player_data['inventory'])

        for name, count in standard_player_data['inventory']['items'].items():
            self.add_inventory_item(self.ui.standardInventoryList, name, count)
        self.ui.standardStarting.setText(standard_player_data['scenario'])
        # TODO: Stats
        # TODO: Globals

        # Set up debug stuff
        debug_player_data = helper.get_json_data(settings_dir + '/debug/player.json')
        debug_globals_data = helper.get_json_data(settings_dir + '/debug/globals.json')

        for name, count in debug_player_data['inventory']['items'].items():
            self.add_inventory_item(self.ui.debugInventoryList, name, count)
        self.ui.debugStarting.setText(debug_player_data['scenario'])
        # TODO: Stats
        # TODO: Globals
        

    @staticmethod
    def add_inventory_item(inventory_list, name, count):
        list_item = QListWidgetItem(inventory_list)
        inv_row = InvRow(name, count, lambda: inventory_list.removeItemWidget(list_item))
        list_item.setSizeHint(inv_row.sizeHint())
        inventory_list.addItem(list_item)
        inventory_list.setItemWidget(list_item, inv_row)

    def save_data(self):
        # Save standard stuff
        standard_start = str(self.ui.standardStarting.text())
        standard_items = {}
        for index in range(self.ui.standardInventoryList.count()):
            item = self.ui.standardInventoryList.itemWidget(self.ui.standardInventoryList.item(index))
            standard_items[item.get_name()] = item.get_count()
        helper.save_json_data(self.settings_dir + '/std/player.json', {
            'scenario': standard_start,
            'inventory': {
                'currency': 0,
                'items': standard_items
            },
            'stats': {}
        })
        
        # Save debug stuff
        debug_start = str(self.ui.debugStarting.text())
        debug_items = {}
        for index in range(self.ui.debugInventoryList.count()):
            item = self.ui.debugInventoryList.itemWidget(self.ui.debugInventoryList.item(index))
            debug_items[item.get_name()] = item.get_count()
        helper.save_json_data(self.settings_dir + '/debug/player.json', {
            'scenario': debug_start,
            'inventory': {
                'currency': 0,
                'items': debug_items
            },
            'stats': {}
        })
