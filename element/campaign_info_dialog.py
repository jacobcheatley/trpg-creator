from element.ignore_enter import IgnoreEnter
from ui.dialogs.campaign_info import Ui_CampaignInfoDialog
from element.confirm_dialog import ConfirmDialog


class CampaignInfoDialog(IgnoreEnter):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CampaignInfoDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.done(1))
        self.ui.buttonBox.rejected.connect(ConfirmDialog.confirm_exit(self, 'Are you sure you want to exit without saving campaign info?'))

    def get_data(self):
        return {
            'name': str(self.ui.lineEditCampaign.text()),
            'creator': str(self.ui.lineEditCreator.text()),
            'about': str(self.ui.textEditAbout.toPlainText())
        }

    @classmethod
    def setup(cls, name, creator, about):  # Method signature different from other setups because of first time popup
        dialog = CampaignInfoDialog()
        dialog.ui.lineEditCampaign.setText(name)
        dialog.ui.lineEditCreator.setText(creator)
        dialog.ui.textEditAbout.setPlainText(about)
        return dialog
