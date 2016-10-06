import os
import sys

from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QFileSystemModel
from ui.main_window import Ui_MainWindow


from element import context_menus
from element.about_dialog import AboutDialog
from element.campaign_info_dialog import CampaignInfoDialog
from element.item_dialog import ItemDialog
from element.create_resource_dialog import CreateResourceDialog

from misc import helper, resource
import config

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
        self.model = QFileSystemModel()
        self.init_tree_view()
        self.connect_actions()

    def connect_actions(self):
        # File
        self.ui.actionNew.triggered.connect(self.new_campaign)
        self.ui.actionOpen.triggered.connect(self.open_campaign)
        self.ui.actionQuit.triggered.connect(helper.exit_app)
        # Help
        self.ui.actionAbout.triggered.connect(helper.show_simple_dialog(AboutDialog))
        # Buttons
        self.ui.openFolderButton.clicked.connect(self.open_current_dir)

    # <editor-fold desc="Tree View">
    def init_tree_view(self):
        self.ui.filesTreeView.customContextMenuRequested.connect(self.custom_tree_menu)
        self.ui.filesTreeView.mouseDoubleClickEvent = self.custom_tree_double_click
        self.ui.filesTreeView.setHeaderHidden(True)
        self.ui.filesTreeView.setModel(self.model)
        self.refresh_tree_view()

    def refresh_tree_view(self):
        self.model.setRootPath(self.current_dir)
        root = self.model.index(self.current_dir)
        self.ui.filesTreeView.setRootIndex(root)
        for x in range(1, 4):
            self.ui.filesTreeView.hideColumn(x)  # TODO: Find a way to only have to do this once

    def file_edit_function(self, ext, file_location):
        if ext == resource.info.ext:
            return lambda: self.show_campaign_info_dialog(file_location)
        elif ext == resource.item.ext:
            return lambda: self.show_item_dialog(file_location)
        else:
            return lambda: helper.display_error('Operation not implemented yet.')

    def file_create_function(self, base_folder, file_location):
        resource_type = resource.folder_to_name[base_folder]

        def create_resource():
            new_id = CreateResourceDialog.get_new_id(resource_type)
            if new_id is not None and new_id.strip() != '':
                helper.save_json_data(file_location + '/' + new_id + resource.folder_to_ext[base_folder],
                                      resource.name_to_default[resource_type])
            else:
                print('Resource creation cancelled')

        # TODO: Additional/better checks here for duplicate files or empty name
        return create_resource

    def custom_tree_double_click(self, event):
        point = event.pos()
        index = self.ui.filesTreeView.indexAt(point)
        if index.isValid():
            item_name = self.model.itemData(index)[0]
            if '.' in item_name:
                # It's a file. Edit it.
                name, ext = os.path.splitext(item_name)
                self.file_edit_function(ext, self.model.filePath(index))()
            else:
                # It's a directory. Expand it.
                self.ui.filesTreeView.expand(index)

    def custom_tree_menu(self, point):
        index = self.ui.filesTreeView.indexAt(point)
        if index.isValid():
            item_name = self.model.itemData(index)[0]
            if '.' in item_name:
                # It's a file
                name, ext = os.path.splitext(item_name)
                menu = context_menus.build(
                    ('Edit ' + name, self.file_edit_function(ext, self.model.filePath(index))),
                    ('Delete ' + name, lambda: helper.display_error('Operation not implemented yet.'))
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
                    ('Create new ' + resource.folder_to_name[item_name], self.file_create_function(item_name, self.model.filePath(start_index))),
                    ('Create new folder', lambda: helper.display_error('Operation not implemented yet.'))
                )
                menu.exec_(self.ui.filesTreeView.mapToGlobal(point))
    # </editor-fold>

    # Actions
    def new_campaign(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(helper.one_up(self.current_dir))
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        dialog.setWindowTitle('Select folder name')
        if dialog.exec_():
            directory = dialog.selectedFiles()[0]
            qdir = QDir(directory)
            if not qdir.exists():
                name = qdir.dirName()
                creator = config.get('default_creator')
                confirm = self.init_campaign_info_dialog(name, creator, '')
                if confirm:
                    # If campaign info was OK'd, set up files
                    self.current_dir = qdir.path()
                    for folder_name in resource.folders:
                        qdir.mkpath('./' + folder_name)
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

    def open_current_dir(self):
        QDesktopServices.openUrl(QUrl(self.current_dir))

    # <editor-fold desc="Campaign Info Dialog">
    def init_campaign_info_dialog(self, name, creator, about):
        dialog = CampaignInfoDialog.setup(name, creator, about)
        exit_code = dialog.exec_()
        if exit_code:
            self.save_campaign_info(dialog.get_data())
        return exit_code

    def show_campaign_info_dialog(self, file_location):
        data = helper.get_json_data(file_location)
        dialog = CampaignInfoDialog.setup(data['name'], data['creator'], data['about'])
        if dialog.exec_():
            self.save_campaign_info(dialog.get_data())

    def save_campaign_info(self, campaign_info):
        config.set('default_creator', campaign_info['creator'])
        helper.save_json_data(self.current_dir + '/campaign.info', campaign_info)
    # </editor-fold>

    # <editor-fold desc="Item Dialog">
    def show_item_dialog(self, file_location):
        dialog = ItemDialog.setup(file_location)
        if dialog.exec_():
            helper.save_json_data(file_location, dialog.get_data())
    # </editor-fold>

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
