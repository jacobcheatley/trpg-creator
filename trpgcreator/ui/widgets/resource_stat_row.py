# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/widgets/resource_stat_row.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResourceStatRow(object):
    def setupUi(self, ResourceStatRow):
        ResourceStatRow.setObjectName("ResourceStatRow")
        ResourceStatRow.resize(205, 111)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ResourceStatRow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelStatName = QtWidgets.QLabel(ResourceStatRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatName.sizePolicy().hasHeightForWidth())
        self.labelStatName.setSizePolicy(sizePolicy)
        self.labelStatName.setObjectName("labelStatName")
        self.horizontalLayout.addWidget(self.labelStatName)
        self.frame = QtWidgets.QFrame(ResourceStatRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBoxMin = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMin.setMaximum(999999999.0)
        self.doubleSpinBoxMin.setObjectName("doubleSpinBoxMin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxMin)
        self.doubleSpinBoxStart = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxStart.setMaximum(999999999.0)
        self.doubleSpinBoxStart.setObjectName("doubleSpinBoxStart")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxStart)
        self.doubleSpinBoxMax = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxMax.setMaximum(999999999.0)
        self.doubleSpinBoxMax.setObjectName("doubleSpinBoxMax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxMax)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(ResourceStatRow)
        QtCore.QMetaObject.connectSlotsByName(ResourceStatRow)

    def retranslateUi(self, ResourceStatRow):
        _translate = QtCore.QCoreApplication.translate
        ResourceStatRow.setWindowTitle(_translate("ResourceStatRow", "Form"))
        self.labelStatName.setText(_translate("ResourceStatRow", "Stat Name"))
        self.label_2.setText(_translate("ResourceStatRow", "Min"))
        self.label_3.setText(_translate("ResourceStatRow", "Start"))
        self.label_4.setText(_translate("ResourceStatRow", "Max"))

