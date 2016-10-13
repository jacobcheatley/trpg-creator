# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/function.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FunctionDialog(object):
    def setupUi(self, FunctionDialog):
        FunctionDialog.setObjectName("FunctionDialog")
        FunctionDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEditFunc = QtWidgets.QPlainTextEdit(FunctionDialog)
        self.plainTextEditFunc.setAutoFillBackground(False)
        self.plainTextEditFunc.setStyleSheet("* {\n"
"    font-family: monospace;\n"
"}")
        self.plainTextEditFunc.setLineWidth(1)
        self.plainTextEditFunc.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEditFunc.setTabStopWidth(36)
        self.plainTextEditFunc.setObjectName("plainTextEditFunc")
        self.verticalLayout.addWidget(self.plainTextEditFunc)
        self.buttonBox = QtWidgets.QDialogButtonBox(FunctionDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FunctionDialog)
        QtCore.QMetaObject.connectSlotsByName(FunctionDialog)

    def retranslateUi(self, FunctionDialog):
        _translate = QtCore.QCoreApplication.translate
        FunctionDialog.setWindowTitle(_translate("FunctionDialog", "Edit Function"))

