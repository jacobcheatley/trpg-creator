# Qt Standard Imports
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
# My files
from element.about_dialog import AboutDialog
from element.campaign_info_dialog import CampaignInfoDialog
from ui.main_window import Ui_MainWindow
from misc import helper
# Other imports
import json
import config


class MainWindow(QMainWindow):
    def __init__(self):
        # Boilerplate
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Specific stuff
        default_dir = config.get('default_dir')
        self._current_dir = QDir(default_dir) if default_dir else QDir()
        self.connect_actions()

    def connect_actions(self):
        # File
        self.ui.actionNew.triggered.connect(self.new_campaign)
        self.ui.actionOpen.triggered.connect(self.open_campaign)
        self.ui.actionQuit.triggered.connect(helper.exit_app)
        # Help
        self.ui.actionAbout.triggered.connect(self.show_simple_dialog(AboutDialog))

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
                campaign_info = self.show_campaign_info_dialog(qdir.dirName())
                if campaign_info:
                    self.current_dir = qdir
                    qdir.mkpath('./Items')
                    qdir.mkpath('./Scenarios')
                    qdir.mkpath('./Functions')
                    self.save_campaign_info(campaign_info)
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
        print(directory)

    @staticmethod
    def show_campaign_info_dialog(name):
        dialog = CampaignInfoDialog()
        dialog.ui.lineEditCampaign.setText(name)

        if dialog.exec_():
            return dialog.getData()
        else:
            return False

    @staticmethod
    def show_simple_dialog(cls):
        def inner():
            dialog = cls()
            dialog.exec_()

        return inner

    # Functions
    def save_campaign_info(self, campaign_info):
        with open(self.current_dir.path() + '/info.json', 'w') as out:
            json.dump(campaign_info, out)

    # Properties
    @property
    def current_dir(self):
        return self._current_dir

    @current_dir.setter
    def current_dir(self, value):
        self._current_dir = value
        config.set('default_dir', value.path())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
