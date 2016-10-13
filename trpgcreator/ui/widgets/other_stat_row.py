# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/other_stat_row.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherStatRow(object):
    def setupUi(self, OtherStatRow):
        OtherStatRow.setObjectName("OtherStatRow")
        OtherStatRow.resize(264, 45)
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
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxStart = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxStart.setMaximum(999999999.0)
        self.doubleSpinBoxStart.setObjectName("doubleSpinBoxStart")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxStart)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(OtherStatRow)
        QtCore.QMetaObject.connectSlotsByName(OtherStatRow)

    def retranslateUi(self, OtherStatRow):
        _translate = QtCore.QCoreApplication.translate
        OtherStatRow.setWindowTitle(_translate("OtherStatRow", "Form"))
        self.labelStatName.setText(_translate("OtherStatRow", "Stat Name"))
        self.label_3.setText(_translate("OtherStatRow", "Start"))

