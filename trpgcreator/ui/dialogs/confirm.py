# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/confirm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.resize(400, 142)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfirmDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ConfirmDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfirmDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConfirmDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfirmDialog.setWindowTitle(_translate("ConfirmDialog", "Confirm Action"))
        self.label.setText(_translate("ConfirmDialog", "TextLabel"))

