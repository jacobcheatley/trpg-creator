# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/option.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionRow(object):
    def setupUi(self, OptionRow):
        OptionRow.setObjectName("OptionRow")
        OptionRow.resize(219, 91)
        self.horizontalLayout = QtWidgets.QHBoxLayout(OptionRow)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(OptionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditDescription = QtWidgets.QLineEdit(self.frame)
        self.lineEditDescription.setObjectName("lineEditDescription")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditDescription)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEditFunction = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditFunction.sizePolicy().hasHeightForWidth())
        self.plainTextEditFunction.setSizePolicy(sizePolicy)
        self.plainTextEditFunction.setMaximumSize(QtCore.QSize(16777215, 40))
        self.plainTextEditFunction.setObjectName("plainTextEditFunction")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEditFunction)
        self.horizontalLayout.addWidget(self.frame)
        self.pushButtonDelete = QtWidgets.QPushButton(OptionRow)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.retranslateUi(OptionRow)
        QtCore.QMetaObject.connectSlotsByName(OptionRow)

    def retranslateUi(self, OptionRow):
        _translate = QtCore.QCoreApplication.translate
        OptionRow.setWindowTitle(_translate("OptionRow", "Form"))
        self.label.setText(_translate("OptionRow", "Description"))
        self.label_2.setText(_translate("OptionRow", "Function"))
        self.pushButtonDelete.setText(_translate("OptionRow", "X"))

