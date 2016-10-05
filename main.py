# Qt Standard Imports
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QFileSystemModel, QAction
# My UI files
from element.about_dialog import AboutDialog
from element.campaign_info_dialog import CampaignInfoDialog
from ui.main_window import Ui_MainWindow
from element import context_menus
# My Other Imports
from misc import helper, resource
import config
# Other Imports
import json
import os


class MainWindow(QMainWindow):
    def __init__(self):
        # Boilerplate
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Specific stuff
        default_dir = config.get('default_dir')
        self._current_dir = default_dir if default_dir else '.'
        self.setWindowTitle('TRPG Creator - [{}]'.format(self.current_dir))
        self.connect_actions()
        self.model = QFileSystemModel()
        self.init_tree_view()

    def connect_actions(self):
        # File
        self.ui.actionNew.triggered.connect(self.new_campaign)
        self.ui.actionOpen.triggered.connect(self.open_campaign)
        self.ui.actionQuit.triggered.connect(helper.exit_app)
        # Help
        self.ui.actionAbout.triggered.connect(self.show_simple_dialog(AboutDialog))

    def init_tree_view(self):
        self.ui.filesTreeView.customContextMenuRequested.connect(self.custom_tree_menu)
        self.ui.filesTreeView.setHeaderHidden(True)
        self.ui.filesTreeView.setModel(self.model)
        self.refresh_tree_view()

    def refresh_tree_view(self):
        self.model.setRootPath(self.current_dir)
        self.ui.filesTreeView.setRootIndex(self.model.index(self.current_dir))
        for x in range(1, 4):
            self.ui.filesTreeView.hideColumn(x)  # TODO: Find a way to only have to do this once

    def custom_tree_menu(self, point):
        index = self.ui.filesTreeView.indexAt(point)
        if index.isValid():
            item_name = self.model.itemData(index)[0]
            if '.' in item_name:
                # It's a file
                name, ext = os.path.splitext(item_name)
                menu = context_menus.build(
                    ('Edit ' + name, lambda: print('EDIT RESOURCE')),
                    ('Delete ' + name, lambda: print('DELETE RESOURCE'))
                )
                menu.exec_(self.ui.filesTreeView.mapToGlobal(point))
            else:
                # It's a folder
                start_index = index
                # Get the root
                while item_name not in resource.folder_to_name:
                    index = index.parent()
                    item_name = self.model.itemData(index)[0]
                menu = context_menus.build(
                    ('Create new ' + resource.folder_to_name[item_name], lambda: print('CREATE RESOURCE')),
                    ('Create new folder', lambda: print('CREATE FOLDER'))
                )
                menu.exec_(self.ui.filesTreeView.mapToGlobal(point))
        else:
            print('Invalid')

    # Dialog Functions
    def new_campaign(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(helper.one_up(self.current_dir))
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        if dialog.exec_():
            directory = dialog.selectedFiles()[0]
            qdir = QDir(directory)
            if not qdir.exists():
                name = qdir.dirName()
                creator = config.get('default_creator')
                campaign_info = self.show_campaign_info_dialog(name, creator, '')
                if campaign_info is not None:
                    self.current_dir = qdir.path()
                    for folder_name in resource.folders:
                        qdir.mkpath('./' + folder_name)
                    self.save_campaign_info(campaign_info)
                    self.refresh_tree_view()
                else:
                    print('Cancelled creating campaign.')
            else:
                helper.display_error('Directory for campaign already exists.')  # This shouldn't happen
        else:
            print('Not saved.')

    def open_campaign(self):
        dialog = QFileDialog(self)
        directory = QFileDialog.getExistingDirectory(dialog,
                                                     caption='Select a campaign',
                                                     directory=helper.one_up(self.current_dir),
                                                     options=QFileDialog.ShowDirsOnly)
        if directory:
            self.current_dir = directory
            self.refresh_tree_view()
        else:
            print('Nothing selected.')

    @staticmethod
    def show_campaign_info_dialog(name, creator, about):
        dialog = CampaignInfoDialog()
        dialog.ui.lineEditCampaign.setText(name)
        dialog.ui.lineEditCreator.setText(creator)
        dialog.ui.textEditAbout.setPlainText(about)

        if dialog.exec_():
            return dialog.getData()
        else:
            return None

    @staticmethod
    def show_simple_dialog(cls):
        def inner():
            dialog = cls()
            dialog.exec_()

        return inner

    # Functions
    def save_campaign_info(self, campaign_info):
        config.set('default_creator', campaign_info['creator'])
        with open(self.current_dir + '/campaign.info', 'w') as out:
            json.dump(campaign_info, out)

    def debug_action(self, text):
        def inner():
            print(text)
        return inner

    # Properties
    @property
    def current_dir(self):
        return self._current_dir

    @current_dir.setter
    def current_dir(self, value):
        self._current_dir = value
        self.setWindowTitle('TRPG Creator - [{}]'.format(value))
        config.set('default_dir', value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showMaximized()
    sys.exit(app.exec_())
