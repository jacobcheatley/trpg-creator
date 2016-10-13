# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/item.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ItemDialog(object):
    def setupUi(self, ItemDialog):
        ItemDialog.setObjectName("ItemDialog")
        ItemDialog.resize(400, 374)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ItemDialog.sizePolicy().hasHeightForWidth())
        ItemDialog.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(ItemDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 356))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBoxValue = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxValue.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBoxValue.setMinimum(0)
        self.spinBoxValue.setMaximum(999999999)
        self.spinBoxValue.setProperty("value", 0)
        self.spinBoxValue.setObjectName("spinBoxValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxValue)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEditDescription = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.textEditDescription.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEditDescription.setObjectName("textEditDescription")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEditDescription)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEditUse = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.textEditUse.setStyleSheet("* {\n"
"    font-family: monospace;\n"
"}")
        self.textEditUse.setTabStopWidth(36)
        self.textEditUse.setObjectName("textEditUse")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEditUse)
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ItemDialog)
        QtCore.QMetaObject.connectSlotsByName(ItemDialog)
        ItemDialog.setTabOrder(self.lineEditName, self.spinBoxValue)
        ItemDialog.setTabOrder(self.spinBoxValue, self.textEditDescription)
        ItemDialog.setTabOrder(self.textEditDescription, self.textEditUse)

    def retranslateUi(self, ItemDialog):
        _translate = QtCore.QCoreApplication.translate
        ItemDialog.setWindowTitle(_translate("ItemDialog", "Edit Item"))
        self.label.setText(_translate("ItemDialog", "Name"))
        self.label_2.setText(_translate("ItemDialog", "Value"))
        self.label_3.setText(_translate("ItemDialog", "Description"))
        self.label_4.setText(_translate("ItemDialog", "Use Function"))

