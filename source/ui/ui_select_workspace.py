# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_select_workspace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectWorkspace(object):
    def setupUi(self, SelectWorkspace):
        if not SelectWorkspace.objectName():
            SelectWorkspace.setObjectName(u"SelectWorkspace")
        SelectWorkspace.resize(544, 218)
        self.label = QLabel(SelectWorkspace)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(20, 20, 691, 41))
        self.label.setMaximumSize(QSize(16777215, 16777214))
        self.label.setStyleSheet(u"font: 18pt \"Agency FB\";\n"
"")
        self.workspace_comboBox = QComboBox(SelectWorkspace)
        self.workspace_comboBox.setObjectName(u"workspace_comboBox")
        self.workspace_comboBox.setGeometry(QRect(149, 90, 271, 21))
        self.useAsDefault_checkBox = QCheckBox(SelectWorkspace)
        self.useAsDefault_checkBox.setObjectName(u"useAsDefault_checkBox")
        self.useAsDefault_checkBox.setGeometry(QRect(40, 130, 317, 23))
        self.useAsDefault_checkBox.setStyleSheet(u"font: 8pt \"Corbel\";\n"
"")
        self.select_pushButton = QPushButton(SelectWorkspace)
        self.select_pushButton.setObjectName(u"select_pushButton")
        self.select_pushButton.setGeometry(QRect(430, 90, 93, 28))
        self.label_2 = QLabel(SelectWorkspace)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 106, 21))
        self.label_2.setStyleSheet(u"font: 11pt \"Arial Rounded MT Bold\";")
        self.workspace_lineEdit = QLineEdit(SelectWorkspace)
        self.workspace_lineEdit.setObjectName(u"workspace_lineEdit")
        self.workspace_lineEdit.setGeometry(QRect(150, 90, 251, 21))
        self.layoutWidget = QWidget(SelectWorkspace)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 170, 195, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_pushButton = QPushButton(self.layoutWidget)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout.addWidget(self.ok_pushButton)

        self.cancel_pushButton = QPushButton(self.layoutWidget)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.horizontalLayout.addWidget(self.cancel_pushButton)


        self.retranslateUi(SelectWorkspace)

        QMetaObject.connectSlotsByName(SelectWorkspace)
    # setupUi

    def retranslateUi(self, SelectWorkspace):
        SelectWorkspace.setWindowTitle(QCoreApplication.translate("SelectWorkspace", u"SelectWorkspace", None))
        self.label.setText(QCoreApplication.translate("SelectWorkspace", u"EveIDE : Select a directory", None))
        self.useAsDefault_checkBox.setText(QCoreApplication.translate("SelectWorkspace", u"use this as the default and do not ask again", None))
        self.select_pushButton.setText(QCoreApplication.translate("SelectWorkspace", u"select", None))
        self.label_2.setText(QCoreApplication.translate("SelectWorkspace", u"Workspace:", None))
        self.ok_pushButton.setText(QCoreApplication.translate("SelectWorkspace", u"OK", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("SelectWorkspace", u"quit", None))
    # retranslateUi

