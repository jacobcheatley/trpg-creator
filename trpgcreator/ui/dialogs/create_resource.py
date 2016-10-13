# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/create_resource.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateResourceDialog(object):
    def setupUi(self, CreateResourceDialog):
        CreateResourceDialog.setObjectName("CreateResourceDialog")
        CreateResourceDialog.resize(323, 112)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateResourceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CreateResourceDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditId = QtWidgets.QLineEdit(CreateResourceDialog)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout.addWidget(self.lineEditId)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateResourceDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreateResourceDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateResourceDialog)

    def retranslateUi(self, CreateResourceDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateResourceDialog.setWindowTitle(_translate("CreateResourceDialog", "Create Resource"))
        self.label.setText(_translate("CreateResourceDialog", "Enter id for new {}"))

