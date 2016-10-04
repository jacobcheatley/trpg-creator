# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/dialogs/about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 112)
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(6, 0, 391, 111))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.label.setText(_translate("AboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Created by Jacob Cheatley 2016</span></p><p align=\"center\"><span style=\" font-weight:600;\">GitHub:</span> &lt;soon&gt;</p><p align=\"center\"><span style=\" font-weight:600;\">TRPG GitHub:</span><a href=\"https://github.com/jacobcheatley/trpg\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/jacobcheatley/trpg</span></a></p></body></html>"))

