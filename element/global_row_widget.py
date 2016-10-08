from ui.widgets.global_row import Ui_GlobalRow
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QDoubleSpinBox, QLineEdit, QCheckBox


class GlobalRow(QWidget):
    def __init__(self, name, value, delete_func):
        super().__init__()
        self.wid = Ui_GlobalRow()
        self.wid.setupUi(self)
        self.wid.pushButtonDelete.clicked.connect(delete_func)
        self.wid.comboBoxType.setCurrentIndex(-1)
        self.wid.comboBoxType.currentIndexChanged.connect(self.set_wid_type)
        self.wid.lineEditName.setText(name)
        self.init_combo_box(value)

    def init_combo_box(self, value):
        print(value, type(value))
        if isinstance(value, int):
            self.wid.comboBoxType.setCurrentIndex(0)
        elif isinstance(value, float):
            self.wid.comboBoxType.setCurrentIndex(1)
        elif isinstance(value, str):
            self.wid.comboBoxType.setCurrentIndex(2)
        elif isinstance(value, bool):
            self.wid.comboBoxType.setCurrentIndex(3)

    def set_wid_type(self, index):
        new_wid = [
            self._default_spin,
            self._default_double,
            QLineEdit,
            QCheckBox
        ][index]
        layout = self.wid.frameValue.layout()
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)
        layout.addWidget(new_wid())

    @staticmethod
    def _default_spin():
        widget = QSpinBox()
        widget.setMinimum(-999999999)
        widget.setMaximum(999999999)
        return widget

    @staticmethod
    def _default_double():
        widget = QDoubleSpinBox()
        widget.setMinimum(-999999999)
        widget.setMaximum(999999999)
        return widget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    test = GlobalRow('test', 1, lambda: print('X'))
    test.show()
    sys.exit(app.exec_())
