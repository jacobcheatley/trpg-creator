# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/other_stat_row.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherStatRow(object):
    def setupUi(self, OtherStatRow):
        OtherStatRow.setObjectName("OtherStatRow")
        OtherStatRow.resize(263, 65)
        self.horizontalLayout = QtWidgets.QHBoxLayout(OtherStatRow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelStatName = QtWidgets.QLabel(OtherStatRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatName.sizePolicy().hasHeightForWidth())
        self.labelStatName.setSizePolicy(sizePolicy)
        self.labelStatName.setObjectName("labelStatName")
        self.horizontalLayout.addWidget(self.labelStatName)
        self.frame = QtWidgets.QFrame(OtherStatRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxStart = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxStart.setObjectName("doubleSpinBoxStart")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxStart)
        self.horizontalLayout.addWidget(self.frame)
        self.pushButtonDelete = QtWidgets.QPushButton(OtherStatRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.retranslateUi(OtherStatRow)
        QtCore.QMetaObject.connectSlotsByName(OtherStatRow)

    def retranslateUi(self, OtherStatRow):
        _translate = QtCore.QCoreApplication.translate
        OtherStatRow.setWindowTitle(_translate("OtherStatRow", "Form"))
        self.labelStatName.setText(_translate("OtherStatRow", "Stat Name"))
        self.label_3.setText(_translate("OtherStatRow", "Start"))
        self.pushButtonDelete.setText(_translate("OtherStatRow", "X"))

