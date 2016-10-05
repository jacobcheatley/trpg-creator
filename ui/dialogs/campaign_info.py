# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/campaign_info.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CampaignInfoDialog(object):
    def setupUi(self, CampaignInfoDialog):
        CampaignInfoDialog.setObjectName("CampaignInfoDialog")
        CampaignInfoDialog.resize(400, 258)
        self.verticalLayoutWidget = QtWidgets.QWidget(CampaignInfoDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditCampaign = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditCampaign.setObjectName("lineEditCampaign")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCampaign)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditCreator = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditCreator.setObjectName("lineEditCreator")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCreator)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEditAbout = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditAbout.setObjectName("textEditAbout")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEditAbout)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.verticalLayoutWidget.raise_()
        self.lineEditCampaign.raise_()

        self.retranslateUi(CampaignInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(CampaignInfoDialog)

    def retranslateUi(self, CampaignInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        CampaignInfoDialog.setWindowTitle(_translate("CampaignInfoDialog", "Campaign Info"))
        self.label.setText(_translate("CampaignInfoDialog", "Campaign Name"))
        self.label_2.setText(_translate("CampaignInfoDialog", "Creator Name"))
        self.label_3.setText(_translate("CampaignInfoDialog", "About Text"))

