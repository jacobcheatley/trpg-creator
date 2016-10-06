# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/test.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestDialog(object):
    def setupUi(self, TestDialog):
        TestDialog.setObjectName("TestDialog")
        TestDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(TestDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(TestDialog)
        self.buttonBox.accepted.connect(TestDialog.accept)
        self.buttonBox.rejected.connect(TestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TestDialog)

    def retranslateUi(self, TestDialog):
        _translate = QtCore.QCoreApplication.translate
        TestDialog.setWindowTitle(_translate("TestDialog", "Test Dialog"))

