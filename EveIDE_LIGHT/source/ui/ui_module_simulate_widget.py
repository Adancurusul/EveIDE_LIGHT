# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_module_simulate_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_module_simulat_widget(object):
    def setupUi(self, module_simulat_widget):
        if not module_simulat_widget.objectName():
            module_simulat_widget.setObjectName(u"module_simulat_widget")
        module_simulat_widget.resize(437, 449)
        module_simulat_widget.setMaximumSize(QSize(17666, 16777215))
        self.verticalLayout_2 = QVBoxLayout(module_simulat_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(module_simulat_widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.project_comboBox = QComboBox(self.groupBox_2)
        self.project_comboBox.setObjectName(u"project_comboBox")

        self.horizontalLayout_2.addWidget(self.project_comboBox)

        self.selectProjectPath_pushButton = QPushButton(self.groupBox_2)
        self.selectProjectPath_pushButton.setObjectName(u"selectProjectPath_pushButton")
        self.selectProjectPath_pushButton.setMinimumSize(QSize(20, 20))
        self.selectProjectPath_pushButton.setMaximumSize(QSize(21, 21))
        icon = QIcon()
        icon.addFile(u":/pic/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectProjectPath_pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.selectProjectPath_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.iverlogPath_lineEdit = QLineEdit(self.groupBox_2)
        self.iverlogPath_lineEdit.setObjectName(u"iverlogPath_lineEdit")

        self.horizontalLayout.addWidget(self.iverlogPath_lineEdit)

        self.selectIverilogPath_pushButton = QPushButton(self.groupBox_2)
        self.selectIverilogPath_pushButton.setObjectName(u"selectIverilogPath_pushButton")
        self.selectIverilogPath_pushButton.setMinimumSize(QSize(20, 20))
        self.selectIverilogPath_pushButton.setMaximumSize(QSize(21, 21))
        self.selectIverilogPath_pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.selectIverilogPath_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.projectTree_groupBox = QGroupBox(module_simulat_widget)
        self.projectTree_groupBox.setObjectName(u"projectTree_groupBox")

        self.verticalLayout_2.addWidget(self.projectTree_groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.simulate_pushButton = QPushButton(module_simulat_widget)
        self.simulate_pushButton.setObjectName(u"simulate_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/pic/simulate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.simulate_pushButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.simulate_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(module_simulat_widget)

        QMetaObject.connectSlotsByName(module_simulat_widget)
    # setupUi

    def retranslateUi(self, module_simulat_widget):
        module_simulat_widget.setWindowTitle(QCoreApplication.translate("module_simulat_widget", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("module_simulat_widget", u"Settings ", None))
        self.label.setText(QCoreApplication.translate("module_simulat_widget", u"project:", None))
        self.selectProjectPath_pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("module_simulat_widget", u"iverilog:", None))
        self.selectIverilogPath_pushButton.setText("")
        self.projectTree_groupBox.setTitle(QCoreApplication.translate("module_simulat_widget", u"Project Tree", None))
        self.simulate_pushButton.setText(QCoreApplication.translate("module_simulat_widget", u"simulate", None))
    # retranslateUi

