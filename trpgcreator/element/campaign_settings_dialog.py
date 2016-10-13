import os

from PyQt5.QtWidgets import QListWidgetItem
from .editor_dialog import EditorDialog
from .global_row_widget import GlobalRow
from .inv_row_widget import InvRow
from .other_stat_row_widget import OtherStatRow
from .resource_stat_row_widget import ResourceStatRow

from trpgcreator.misc import helper
from trpgcreator.ui.dialogs.campaign_settings import Ui_CampaignSettingsDialog


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
        standard_player_data = helper.get_json_data(self.settings_dir + '/std/player.json')
        standard_globals_data = helper.get_json_data(self.settings_dir + '/std/globals.json')

        self.init_player_data(standard_player_data,
                              self.ui.standardInventoryList,
                              self.ui.standardCurrency,
                              self.ui.standardStarting,
                              self.ui.standardResourceList,
                              self.ui.standardOtherList,
                              self.ui.standardHealthStart,
                              self.ui.standardHealthMax)
        self.init_globals_data(standard_globals_data, self.ui.standardGlobalsList)

        # Set up debug stuff
        debug_player_data = helper.get_json_data(self.settings_dir + '/debug/player.json')
        debug_globals_data = helper.get_json_data(self.settings_dir + '/debug/globals.json')

        self.init_player_data(debug_player_data,
                              self.ui.debugInventoryList,
                              self.ui.debugCurrency,
                              self.ui.debugStarting,
                              self.ui.debugResourceList,
                              self.ui.debugOtherList,
                              self.ui.debugHealthStart,
                              self.ui.debugHealthMax)
        self.init_globals_data(debug_globals_data, self.ui.debugGlobalsList)

        # Set up export stuff
        export_data = helper.get_json_data(self.settings_dir + '/export.json')

        self.ui.lineEditCampaignName.setText(export_data['name'])
        self.ui.lineEditCreator.setText(export_data['creator'])
        self.ui.plainTextEditAbout.setPlainText(export_data['about'])

    def init_player_data(self, player_data, inventory_list, currency, starting, resource_stat_list, other_stat_list, health_start, health_max):
        # Starting Scenario
        starting.setText(player_data['scenario'])

        # Items
        for name, count in player_data['inventory']['items'].items():
            self.add_inventory_item(inventory_list, name, count)

        # Currency
        currency.setValue(player_data['inventory']['currency'])

        # Stats
        stat_data = player_data['stats']
        base_dir = helper.one_up(self.settings_dir)

        # Health Stat
        if 'current' in stat_data['health']:
            health_start.setValue(stat_data['health']['current'])
        else:
            health_start.setValue(0)
        if 'max' in stat_data['health']:
            health_max.setValue(stat_data['health']['max'])
        else:
            health_max.setValue(0)

        # Other stat
        for filename in os.listdir(base_dir + '/Stats-Other'):
            stat_id = os.path.splitext(filename)[0]
            stat_name = helper.get_json_data(base_dir + '/Stats-Other/' + filename)['name']
            if stat_id in stat_data['other']:
                self.add_widget_to_list(other_stat_list, OtherStatRow(stat_name, stat_id, stat_data['other'][stat_id]['current']))
            else:
                self.add_widget_to_list(other_stat_list, OtherStatRow(stat_name, stat_id, 0))

        # Resource stat
        for filename in os.listdir(base_dir + '/Stats-Resource'):
            stat_id = os.path.splitext(filename)[0]
            stat_name = helper.get_json_data(base_dir + '/Stats-Resource/' + filename)['name']
            if stat_id in player_data['stats']['resource']:
                resource_data = stat_data['resource'][stat_id]
                self.add_widget_to_list(resource_stat_list, ResourceStatRow(stat_name, stat_id, resource_data['min'], resource_data['max'], resource_data['current']))
            else:
                self.add_widget_to_list(resource_stat_list, ResourceStatRow(stat_name, stat_id, 0, 0, 0))

    def init_globals_data(self, globals_data, globals_list):
        for name, value in globals_data.items():
            self.add_global_var(globals_list, name, value)

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

    @staticmethod
    def add_widget_to_list(widget_list, object):
        list_item = QListWidgetItem(widget_list)
        list_item.setSizeHint(object.sizeHint())
        widget_list.addItem(list_item)
        widget_list.setItemWidget(list_item, object)

    @staticmethod
    def save_player_data(file_location, starting, inventory_list, currency, other_list, resource_list, health_max, health_start):
        start = starting.text()
        # Inventory
        items = {}
        for index in range(inventory_list.count()):
            item = inventory_list.itemWidget(inventory_list.item(index))
            items[item.get_name()] = item.get_count()
        # Stats
        health_info = {'min': 0, 'max': health_max.value(), 'current': health_start.value()}

        other_stats = {}
        for index in range(other_list.count()):
            stat = other_list.itemWidget(other_list.item(index))
            other_stats[stat.stat_id] = stat.get_data()

        resource_stats = {}
        for index in range(resource_list.count()):
            stat = resource_list.itemWidget(resource_list.item(index))
            resource_stats[stat.stat_id] = stat.get_data()

        # Final player save
        helper.save_json_data(file_location, {
            'scenario': start,
            'inventory': {
                'currency': currency.value(),
                'items': items
            },
            'stats': {
                'health': health_info,
                'other': other_stats,
                'resource': resource_stats
            }
        })

    def save_standard(self):
        self.save_player_data(self.settings_dir + '/std/player.json',
                              self.ui.standardStarting,
                              self.ui.standardInventoryList,
                              self.ui.standardCurrency,
                              self.ui.standardOtherList,
                              self.ui.standardResourceList,
                              self.ui.standardHealthMax,
                              self.ui.standardHealthStart)
        # Globals
        standard_globals = {}
        for index in range(self.ui.standardGlobalsList.count()):
            item = self.ui.standardGlobalsList.itemWidget(self.ui.standardGlobalsList.item(index))
            standard_globals[item.get_name()] = item.get_value()
        helper.save_json_data(self.settings_dir + '/std/globals.json', standard_globals)

    def save_debug(self):
        self.save_player_data(self.settings_dir + '/debug/player.json',
                              self.ui.debugStarting,
                              self.ui.debugInventoryList,
                              self.ui.debugCurrency,
                              self.ui.debugOtherList,
                              self.ui.debugResourceList,
                              self.ui.debugHealthMax,
                              self.ui.debugHealthStart)
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
