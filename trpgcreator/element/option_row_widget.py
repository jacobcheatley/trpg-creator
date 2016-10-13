from trpgcreator.ui.widgets.option import Ui_OptionRow
from PyQt5.QtWidgets import QWidget


class OptionRow(QWidget):
    def __init__(self, desc, func, delete_func):
        super().__init__()
        self.wid = Ui_OptionRow()
        self.wid.setupUi(self)
        self.wid.lineEditDescription.setText(desc)
        self.wid.plainTextEditFunction.setPlainText(func)
        self.wid.pushButtonDelete.clicked.connect(delete_func)

    def get_data(self):
        return {
            'desc': str(self.wid.lineEditDescription.text()),
            'func': self.wid.plainTextEditFunction.toPlainText()
        }
