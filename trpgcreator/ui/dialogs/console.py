# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/console.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConsoleDialog(object):
    def setupUi(self, ConsoleDialog):
        ConsoleDialog.setObjectName("ConsoleDialog")
        ConsoleDialog.resize(887, 549)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConsoleDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(ConsoleDialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.lineEditInput = QtWidgets.QLineEdit(ConsoleDialog)
        self.lineEditInput.setObjectName("lineEditInput")
        self.verticalLayout.addWidget(self.lineEditInput)

        self.retranslateUi(ConsoleDialog)
        QtCore.QMetaObject.connectSlotsByName(ConsoleDialog)

    def retranslateUi(self, ConsoleDialog):
        _translate = QtCore.QCoreApplication.translate
        ConsoleDialog.setWindowTitle(_translate("ConsoleDialog", "Run Campaign Console"))

