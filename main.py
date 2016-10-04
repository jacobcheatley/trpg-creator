import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.main_window import Ui_MainWindow
from about_dialog import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_actions()

    def connect_actions(self):
        self.ui.actionQuit.triggered.connect(self.exit_app)
        self.ui.actionAbout.triggered.connect(self.show_simple_dialog(AboutDialog))

    @staticmethod
    def exit_app():
        exit()

    @staticmethod
    def show_simple_dialog(cls):
        def inner():
            dialog = cls()
            dialog.exec_()
        return inner

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
