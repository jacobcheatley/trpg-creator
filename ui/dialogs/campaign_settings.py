# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/campaign_settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CampaignSettingsDialog(object):
    def setupUi(self, CampaignSettingsDialog):
        CampaignSettingsDialog.setObjectName("CampaignSettingsDialog")
        CampaignSettingsDialog.resize(885, 630)
        self.verticalLayout = QtWidgets.QVBoxLayout(CampaignSettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(CampaignSettingsDialog)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tabStandard = QtWidgets.QWidget()
        self.tabStandard.setObjectName("tabStandard")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabStandard)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tabStandard)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabInit = QtWidgets.QWidget()
        self.tabInit.setObjectName("tabInit")
        self.formLayout = QtWidgets.QFormLayout(self.tabInit)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.tabInit)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.standardStarting = QtWidgets.QLineEdit(self.tabInit)
        self.standardStarting.setObjectName("standardStarting")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.standardStarting)
        self.tabWidget_2.addTab(self.tabInit, "")
        self.tabInventory = QtWidgets.QWidget()
        self.tabInventory.setObjectName("tabInventory")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabInventory)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.tabInventory)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.standardCurrency = QtWidgets.QSpinBox(self.frame)
        self.standardCurrency.setMaximum(999999999)
        self.standardCurrency.setObjectName("standardCurrency")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.standardCurrency)
        self.verticalLayout_4.addWidget(self.frame)
        self.label_4 = QtWidgets.QLabel(self.tabInventory)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.standardInventoryList = QtWidgets.QListWidget(self.tabInventory)
        self.standardInventoryList.setObjectName("standardInventoryList")
        self.verticalLayout_4.addWidget(self.standardInventoryList)
        self.standardInventoryAdd = QtWidgets.QPushButton(self.tabInventory)
        self.standardInventoryAdd.setObjectName("standardInventoryAdd")
        self.verticalLayout_4.addWidget(self.standardInventoryAdd)
        self.tabWidget_2.addTab(self.tabInventory, "")
        self.tabStats = QtWidgets.QWidget()
        self.tabStats.setObjectName("tabStats")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabStats)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.tabStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.standardHealthFrame = QtWidgets.QFrame(self.tabStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standardHealthFrame.sizePolicy().hasHeightForWidth())
        self.standardHealthFrame.setSizePolicy(sizePolicy)
        self.standardHealthFrame.setObjectName("standardHealthFrame")
        self.verticalLayout_6.addWidget(self.standardHealthFrame)
        self.label_9 = QtWidgets.QLabel(self.tabStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.standardResourceList = QtWidgets.QListWidget(self.tabStats)
        self.standardResourceList.setObjectName("standardResourceList")
        self.verticalLayout_6.addWidget(self.standardResourceList)
        self.label_10 = QtWidgets.QLabel(self.tabStats)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.standardOtherList = QtWidgets.QListWidget(self.tabStats)
        self.standardOtherList.setObjectName("standardOtherList")
        self.verticalLayout_6.addWidget(self.standardOtherList)
        self.tabWidget_2.addTab(self.tabStats, "")
        self.tabGlobals = QtWidgets.QWidget()
        self.tabGlobals.setObjectName("tabGlobals")
        self.tabWidget_2.addTab(self.tabGlobals, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tabStandard, "")
        self.tabDebug = QtWidgets.QWidget()
        self.tabDebug.setObjectName("tabDebug")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabDebug)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tabDebug)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tabInit1 = QtWidgets.QWidget()
        self.tabInit1.setObjectName("tabInit1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tabInit1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tabInit1)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.debugStarting = QtWidgets.QLineEdit(self.tabInit1)
        self.debugStarting.setObjectName("debugStarting")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.debugStarting)
        self.tabWidget_3.addTab(self.tabInit1, "")
        self.tabInventory1 = QtWidgets.QWidget()
        self.tabInventory1.setObjectName("tabInventory1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabInventory1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.tabInventory1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.debugCurrency = QtWidgets.QSpinBox(self.frame_2)
        self.debugCurrency.setObjectName("debugCurrency")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.debugCurrency)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.label_6 = QtWidgets.QLabel(self.tabInventory1)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.debugInventoryList = QtWidgets.QListWidget(self.tabInventory1)
        self.debugInventoryList.setObjectName("debugInventoryList")
        self.verticalLayout_5.addWidget(self.debugInventoryList)
        self.debugInventoryAdd = QtWidgets.QPushButton(self.tabInventory1)
        self.debugInventoryAdd.setObjectName("debugInventoryAdd")
        self.verticalLayout_5.addWidget(self.debugInventoryAdd)
        self.tabWidget_3.addTab(self.tabInventory1, "")
        self.tabStats1 = QtWidgets.QWidget()
        self.tabStats1.setObjectName("tabStats1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabStats1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.tabStats1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.debugHealthFrame = QtWidgets.QFrame(self.tabStats1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugHealthFrame.sizePolicy().hasHeightForWidth())
        self.debugHealthFrame.setSizePolicy(sizePolicy)
        self.debugHealthFrame.setObjectName("debugHealthFrame")
        self.verticalLayout_7.addWidget(self.debugHealthFrame)
        self.label_12 = QtWidgets.QLabel(self.tabStats1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.debugResourceList = QtWidgets.QListWidget(self.tabStats1)
        self.debugResourceList.setObjectName("debugResourceList")
        self.verticalLayout_7.addWidget(self.debugResourceList)
        self.label_13 = QtWidgets.QLabel(self.tabStats1)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.debugOtherList = QtWidgets.QListWidget(self.tabStats1)
        self.debugOtherList.setObjectName("debugOtherList")
        self.verticalLayout_7.addWidget(self.debugOtherList)
        self.tabWidget_3.addTab(self.tabStats1, "")
        self.tabGlobals1 = QtWidgets.QWidget()
        self.tabGlobals1.setObjectName("tabGlobals1")
        self.tabWidget_3.addTab(self.tabGlobals1, "")
        self.verticalLayout_3.addWidget(self.tabWidget_3)
        self.tabWidget.addTab(self.tabDebug, "")
        self.tabDescriptions = QtWidgets.QWidget()
        self.tabDescriptions.setObjectName("tabDescriptions")
        self.label = QtWidgets.QLabel(self.tabDescriptions)
        self.label.setGeometry(QtCore.QRect(380, 250, 67, 17))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tabDescriptions, "")
        self.tabExport = QtWidgets.QWidget()
        self.tabExport.setObjectName("tabExport")
        self.formLayout_5 = QtWidgets.QFormLayout(self.tabExport)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_14 = QtWidgets.QLabel(self.tabExport)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEditCampaignName = QtWidgets.QLineEdit(self.tabExport)
        self.lineEditCampaignName.setObjectName("lineEditCampaignName")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCampaignName)
        self.label_15 = QtWidgets.QLabel(self.tabExport)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tabExport)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEditCreator = QtWidgets.QLineEdit(self.tabExport)
        self.lineEditCreator.setObjectName("lineEditCreator")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditCreator)
        self.plainTextEditAbout = QtWidgets.QPlainTextEdit(self.tabExport)
        self.plainTextEditAbout.setObjectName("plainTextEditAbout")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEditAbout)
        self.tabWidget.addTab(self.tabExport, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(CampaignSettingsDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CampaignSettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CampaignSettingsDialog)

    def retranslateUi(self, CampaignSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        CampaignSettingsDialog.setWindowTitle(_translate("CampaignSettingsDialog", "Campaign Settings"))
        self.label_2.setText(_translate("CampaignSettingsDialog", "Starting Scenario"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabInit), _translate("CampaignSettingsDialog", "Initialisation"))
        self.label_5.setText(_translate("CampaignSettingsDialog", "Starting Currency"))
        self.label_4.setText(_translate("CampaignSettingsDialog", "Items"))
        self.standardInventoryAdd.setText(_translate("CampaignSettingsDialog", "Add"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabInventory), _translate("CampaignSettingsDialog", "Player Inventory"))
        self.label_8.setText(_translate("CampaignSettingsDialog", "Health"))
        self.label_9.setText(_translate("CampaignSettingsDialog", "Resource Stats"))
        self.label_10.setText(_translate("CampaignSettingsDialog", "Other Stats"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabStats), _translate("CampaignSettingsDialog", "Player Stats"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabGlobals), _translate("CampaignSettingsDialog", "Globals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStandard), _translate("CampaignSettingsDialog", "Standard Variables"))
        self.label_3.setText(_translate("CampaignSettingsDialog", "Starting Scenario"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabInit1), _translate("CampaignSettingsDialog", "Initialisation"))
        self.label_7.setText(_translate("CampaignSettingsDialog", "Starting Currency"))
        self.label_6.setText(_translate("CampaignSettingsDialog", "Items"))
        self.debugInventoryAdd.setText(_translate("CampaignSettingsDialog", "Add"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabInventory1), _translate("CampaignSettingsDialog", "Player Inventory"))
        self.label_11.setText(_translate("CampaignSettingsDialog", "Health"))
        self.label_12.setText(_translate("CampaignSettingsDialog", "Resource Stats"))
        self.label_13.setText(_translate("CampaignSettingsDialog", "Other Stats"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabStats1), _translate("CampaignSettingsDialog", "Player Stats"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabGlobals1), _translate("CampaignSettingsDialog", "Globals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDebug), _translate("CampaignSettingsDialog", "Debug Variables"))
        self.label.setText(_translate("CampaignSettingsDialog", "WIP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDescriptions), _translate("CampaignSettingsDialog", "Descriptions"))
        self.label_14.setText(_translate("CampaignSettingsDialog", "Campaign Name"))
        self.label_15.setText(_translate("CampaignSettingsDialog", "Creator"))
        self.label_16.setText(_translate("CampaignSettingsDialog", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExport), _translate("CampaignSettingsDialog", "Export"))

