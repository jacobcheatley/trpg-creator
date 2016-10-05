from PyQt5.QtWidgets import QDialog
from ui.dialogs.campaign_info import Ui_CampaignInfoDialog


class CampaignInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CampaignInfoDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(lambda: self.done(0))

    def getData(self):
        return {
            'name': str(self.ui.lineEditCampaign.text()),
            'creator': str(self.ui.lineEditCreator.text()),
            'about': str(self.ui.textEditAbout.toPlainText())
        }