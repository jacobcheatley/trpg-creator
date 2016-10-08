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
        self.set_value(value)

    def get_data(self):
        return self.wid.lineEditName.text(), self.get_value()

    def get_value(self):
        value_widget = self.wid.frameValue.layout().itemAt(0).widget()
        index = self.wid.comboBoxType.currentIndex()
        if index in (0, 1):
            return value_widget.value()
        elif index == 2:
            return value_widget.text()
        elif index == 3:
            return value_widget.isChecked()
        else:
            return None  # This shouldn't happen

    def set_value(self, value):
        value_widget = self.wid.frameValue.layout().itemAt(0).widget()
        index = self.wid.comboBoxType.currentIndex()
        if index in (0, 1):
            value_widget.setValue(value)
        elif index == 2:
            return value_widget.setText(value)
        elif index == 3:
            return value_widget.setChecked(value)
        else:
            return None  # This shouldn't happen

    def init_combo_box(self, value):
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
    test = GlobalRow('test', 1, lambda: print(test.get_data()))
    test.show()
    sys.exit(app.exec_())
