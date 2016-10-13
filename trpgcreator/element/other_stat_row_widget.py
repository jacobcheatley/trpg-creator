from trpgcreator.ui.widgets.other_stat_row import Ui_OtherStatRow
from PyQt5.QtWidgets import QWidget


class OtherStatRow(QWidget):
    def __init__(self, stat_name, stat_id, current):
        super().__init__()
        self.wid = Ui_OtherStatRow()
        self.wid.setupUi(self)
        self.wid.doubleSpinBoxStart.setValue(current)
        self.wid.labelStatName.setText(stat_name)
        self.stat_id = stat_id

    def get_data(self):
        return {
            'current': self.wid.doubleSpinBoxStart.value()
        }
