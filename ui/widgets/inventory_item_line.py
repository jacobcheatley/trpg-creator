# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/inventory_item_line.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditItemName = QtWidgets.QLineEdit(Form)
        self.lineEditItemName.setObjectName("lineEditItemName")
        self.horizontalLayout.addWidget(self.lineEditItemName)
        self.spinBoxItemCount = QtWidgets.QSpinBox(Form)
        self.spinBoxItemCount.setMinimum(1)
        self.spinBoxItemCount.setMaximum(999999999)
        self.spinBoxItemCount.setObjectName("spinBoxItemCount")
        self.horizontalLayout.addWidget(self.spinBoxItemCount)
        self.pushButtonDelete = QtWidgets.QPushButton(Form)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonDelete.setText(_translate("Form", "Delete"))

