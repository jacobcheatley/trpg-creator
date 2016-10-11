# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/inv_row.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InvRow(object):
    def setupUi(self, InvRow):
        InvRow.setObjectName("InvRow")
        InvRow.resize(229, 45)
        self.horizontalLayout = QtWidgets.QHBoxLayout(InvRow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditItemName = QtWidgets.QLineEdit(InvRow)
        self.lineEditItemName.setObjectName("lineEditItemName")
        self.horizontalLayout.addWidget(self.lineEditItemName)
        self.spinBoxItemCount = QtWidgets.QSpinBox(InvRow)
        self.spinBoxItemCount.setMinimum(1)
        self.spinBoxItemCount.setMaximum(999999999)
        self.spinBoxItemCount.setObjectName("spinBoxItemCount")
        self.horizontalLayout.addWidget(self.spinBoxItemCount)
        self.pushButtonDelete = QtWidgets.QPushButton(InvRow)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.retranslateUi(InvRow)
        QtCore.QMetaObject.connectSlotsByName(InvRow)

    def retranslateUi(self, InvRow):
        _translate = QtCore.QCoreApplication.translate
        InvRow.setWindowTitle(_translate("InvRow", "Form"))
        self.pushButtonDelete.setText(_translate("InvRow", "X"))

