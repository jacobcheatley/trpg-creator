from trpgcreator.ui.dialogs.console import Ui_ConsoleDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QProcess


class ConsoleDialog(QDialog):
    def __init__(self, file_location):
        super().__init__()

        self.ui = Ui_ConsoleDialog()
        self.ui.setupUi(self)

        self.submitted = False

        self.ui.lineEditInput.returnPressed.connect(self.line_edit_keypress)
        self.ui.lineEditInput.setFocus()

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdout_ready)
        self.process.readyReadStandardError.connect(self.stderr_ready)
        self.process.started.connect(lambda: print('Started!'))
        self.process.finished.connect(lambda: print('Finished!'))

        self.process.start('trpg', [file_location])

    def stdout_ready(self):
        text = str(self.process.readAllStandardOutput(), 'utf-8')
        self.append(text)

    def stderr_ready(self):
        text = str(self.process.readAllStandardError())
        self.append(text)

    def append(self, text):
        old_text = self.ui.textEdit.toHtml()
        for line in text.splitlines():
            old_text += '{}<br>'.format(line)
        self.ui.textEdit.setHtml(old_text)
        self.ui.textEdit.verticalScrollBar().setSliderPosition(self.ui.textEdit.verticalScrollBar().maximum())

    def line_edit_keypress(self):
        text = self.ui.lineEditInput.text() + '\n'
        self.ui.lineEditInput.clear()
        self.append(text)
        self.process.write(text.encode())
