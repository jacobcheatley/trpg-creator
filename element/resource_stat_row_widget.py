from ui.widgets.resource_stat_row import Ui_ResourceStatRow
from PyQt5.QtWidgets import QWidget


class ResourceStatRow(QWidget):
    def __init__(self, stat_id, min, max, current):
        super().__init__()
        self.wid = Ui_ResourceStatRow()
        self.wid.setupUi(self)
        self.wid.doubleSpinBoxMin.setValue(min)
        self.wid.doubleSpinBoxMax.setValue(max)
        self.wid.doubleSpinBoxStart.setValue(current)
        self.stat_id = stat_id

    def get_data(self):
        return {
            'min': self.wid.doubleSpinBoxMin.value(),
            'max': self.wid.doubleSpinBoxMax.value(),
            'current': self.wid.doubleSpinBoxStart.value()
        }
