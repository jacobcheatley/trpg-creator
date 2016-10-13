import os

from PyQt5.QtCore import QDir, QUrl, QFile
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QFileSystemModel

from .ui.main_window import Ui_MainWindow

from .element import context_menus
from .element.about_dialog import AboutDialog
from .element.item_dialog import ItemDialog
from .element.create_resource_dialog import CreateResourceDialog
from .element.campaign_settings_dialog import CampaignSettingsDialog
from .element.confirm_dialog import ConfirmDialog
from .element.scenario_dialog import ScenarioDialog
from .element.stat_dialog import StatDialog
from .element.function_dialog import FunctionDialog
from .element.console_dialog import ConsoleDialog

from .misc import helper, resource, export
from . import config


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
        self.ui.actionToFile.triggered.connect(self.export_to_file)
        # Run
        self.ui.actionStandard.triggered.connect(self.test_standard)
        # Help
        self.ui.actionAbout.triggered.connect(helper.show_simple_dialog(AboutDialog))
        # Tools
        self.ui.actionSettings.triggered.connect(self.show_campaign_settings)
        # Buttons
        self.ui.openFolderButton.clicked.connect(self.open_current_dir)

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
                self.current_dir = qdir.path()
                for folder_name in resource.folders:
                    qdir.mkpath('./' + folder_name)
                helper.save_json_data('{}/{}/health{}'.format(self.current_dir, resource.health_stat.folder,
                                                              resource.health_stat.ext),
                                      resource.health_stat.default)
                qdir.mkpath('./.settings/std')
                qdir.mkpath('./.settings/debug')
                resource.create_config_files(self.current_dir, qdir.dirName())
                self.refresh_tree_view()
            else:
                helper.display_error('Directory for campaign already exists.')  # This shouldn't happen

    def open_campaign(self):
        dialog = QFileDialog(self)
        directory = QFileDialog.getExistingDirectory(dialog,
                                                     caption='Select a campaign',
                                                     directory=helper.one_up(self.current_dir),
                                                     options=QFileDialog.ShowDirsOnly)
        if directory:
            self.current_dir = directory
            self.refresh_tree_view()

    def export_to_file(self):
        dialog = QFileDialog(self)
        file_location = QFileDialog.getSaveFileName(dialog,
                                                caption='Export campaign file',
                                                directory=self.current_dir,
                                                filter='*.trpg')[0]
        file_location = file_location.split('.')[0] + '.trpg'
        if file_location:
            export.export_to_file(self.current_dir, file_location)

    def test_standard(self):
        qdir = QDir(self.current_dir)
        qdir.mkpath('./.run')
        file_location = self.current_dir + '/.run/std.trpg'
        export.export_to_file(self.current_dir, file_location)
        dialog = ConsoleDialog(file_location).exec_()

    def open_current_dir(self):
        QDesktopServices.openUrl(QUrl(self.current_dir))

    def show_campaign_settings(self):
        try:
            CampaignSettingsDialog(self.current_dir + '/.settings').exec_()
        except FileNotFoundError as e:
            helper.display_error('You aren\'t in campaign. You cannot change campaign settings.')

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
        # TODO: Resource dict
        if ext == resource.item.ext:
            return ItemDialog(file_location).exec_
        elif ext == resource.scenario.ext:
            return ScenarioDialog(file_location).exec_
        elif ext in (resource.health_stat.ext, resource.res_stat.ext, resource.other_stat.ext):
            return StatDialog(file_location).exec_
        elif ext == resource.function.ext:
            return FunctionDialog(file_location).exec_
        else:
            return lambda: helper.display_error('Operation not implemented yet.')

    @staticmethod
    def file_create_function(base_folder, file_location):
        resource_type = resource.folder_to_name[base_folder]

        def create_resource():
            new_id = CreateResourceDialog.get_new_id(resource_type)
            if new_id is not None and new_id.strip() != '':
                helper.save_json_data(file_location + '/' + new_id + resource.folder_to_ext[base_folder],
                                      resource.name_to_default[resource_type])

        # TODO: Additional/better checks here for duplicate files
        return create_resource

    @staticmethod
    def file_delete_function(file_location):
        def delete_folder():
            if ConfirmDialog.yes_to('Are you sure you want to delete this file?'):
                QFile(file_location).remove()

        return delete_folder

    @staticmethod
    def folder_create_function(folder_location):
        def create_folder():
            new_id = CreateResourceDialog.get_new_id('folder')
            if new_id is not None and new_id.strip() != '':
                qdir = QDir(folder_location)
                qdir.mkpath('./' + new_id)

        # TODO: Additional/better checks here for duplicate folders
        return create_folder

    @staticmethod
    def folder_delete_function(folder_location):
        def delete_folder():
            qdir = QDir(folder_location)
            if ConfirmDialog.yes_to('Are you sure you want to delete this folder?'):
                qdir.removeRecursively()

        return delete_folder

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
                menu_actions = [
                    ('Edit ' + name, self.file_edit_function(ext, self.model.filePath(index)))
                ]
                try:
                    resource_object = resource.ext_to_object[ext]
                    if resource_object.delete:
                        menu_actions.append(
                            ('Delete ' + name, self.file_delete_function(self.model.filePath(index))))
                    menu = context_menus.build(menu_actions)
                    menu.exec_(self.ui.filesTreeView.mapToGlobal(point))
                except KeyError:
                    helper.display_error('Operation not supported.')
            else:
                # It's a folder
                start_index = index
                # Get the root
                if item_name not in resource.folder_to_name:
                    root = False
                    while item_name not in resource.folder_to_name:
                        index = index.parent()
                        item_name = self.model.itemData(index)[0]
                else:
                    root = True
                menu_actions = []
                resource_object = resource.folder_to_object[item_name]
                if resource_object.create:
                    menu_actions.append(('Create new ' + resource.folder_to_name[item_name],
                                         self.file_create_function(item_name, self.model.filePath(start_index))))
                if resource_object.subfolder:
                    menu_actions.append(('Create new folder',
                                         self.folder_create_function(self.model.filePath(start_index))))
                if not root:
                    menu_actions.append(('Delete folder',
                                         self.folder_delete_function(self.model.filePath(start_index))))
                if menu_actions:
                    menu = context_menus.build(menu_actions)
                    menu.exec_(self.ui.filesTreeView.mapToGlobal(point))
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
