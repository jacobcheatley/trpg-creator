# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/stat.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatDialog(object):
    def setupUi(self, StatDialog):
        StatDialog.setObjectName("StatDialog")
        StatDialog.resize(400, 162)
        self.verticalLayout = QtWidgets.QVBoxLayout(StatDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(StatDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditName = QtWidgets.QLineEdit(self.frame)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.plainTextEditDescription = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEditDescription.setObjectName("plainTextEditDescription")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEditDescription)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(StatDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StatDialog)
        QtCore.QMetaObject.connectSlotsByName(StatDialog)

    def retranslateUi(self, StatDialog):
        _translate = QtCore.QCoreApplication.translate
        StatDialog.setWindowTitle(_translate("StatDialog", "Edit Stat"))
        self.label.setText(_translate("StatDialog", "Name"))
        self.label_2.setText(_translate("StatDialog", "Description"))

