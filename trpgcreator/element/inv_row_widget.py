from trpgcreator.ui.widgets.inv_row import Ui_InvRow
from PyQt5.QtWidgets import QWidget, QApplication


class InvRow(QWidget):
    def __init__(self, name, count, delete_func):
        super().__init__()
        self.wid = Ui_InvRow()
        self.wid.setupUi(self)
        self.wid.lineEditItemName.setText(name)
        self.wid.spinBoxItemCount.setValue(count)
        self.wid.pushButtonDelete.clicked.connect(delete_func)

    def get_name(self):
        return str(self.wid.lineEditItemName.text())

    def get_count(self):
        return self.wid.spinBoxItemCount.value()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    test = InvRow()
    test.show()
    sys.exit(app.exec_())
