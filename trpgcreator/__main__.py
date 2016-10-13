from trpgcreator.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
