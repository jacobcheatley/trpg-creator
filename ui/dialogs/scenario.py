# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/scenario.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScenarioDialog(object):
    def setupUi(self, ScenarioDialog):
        ScenarioDialog.setObjectName("ScenarioDialog")
        ScenarioDialog.resize(460, 524)
        self.verticalLayout = QtWidgets.QVBoxLayout(ScenarioDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(ScenarioDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditName = QtWidgets.QLineEdit(self.frame)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEditDescription = QtWidgets.QTextEdit(self.frame)
        self.textEditDescription.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEditDescription.setObjectName("textEditDescription")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditDescription)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(ScenarioDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.optionList = QtWidgets.QListWidget(ScenarioDialog)
        self.optionList.setObjectName("optionList")
        self.verticalLayout.addWidget(self.optionList)
        self.pushButtonAdd = QtWidgets.QPushButton(ScenarioDialog)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayout.addWidget(self.pushButtonAdd)
        self.buttonBox = QtWidgets.QDialogButtonBox(ScenarioDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ScenarioDialog)
        QtCore.QMetaObject.connectSlotsByName(ScenarioDialog)

    def retranslateUi(self, ScenarioDialog):
        _translate = QtCore.QCoreApplication.translate
        ScenarioDialog.setWindowTitle(_translate("ScenarioDialog", "Edit Scenario"))
        self.label_2.setText(_translate("ScenarioDialog", "Name"))
        self.label_3.setText(_translate("ScenarioDialog", "Description"))
        self.label.setText(_translate("ScenarioDialog", "Options"))
        self.pushButtonAdd.setText(_translate("ScenarioDialog", "Add"))

