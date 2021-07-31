# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_project_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        if not NewProject.objectName():
            NewProject.setObjectName(u"NewProject")
        NewProject.resize(536, 183)
        self.verticalLayout_2 = QVBoxLayout(NewProject)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(NewProject)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.projectName_label = QLabel(self.groupBox_2)
        self.projectName_label.setObjectName(u"projectName_label")

        self.horizontalLayout.addWidget(self.projectName_label)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_pushButton = QPushButton(NewProject)
        self.create_pushButton.setObjectName(u"create_pushButton")

        self.verticalLayout.addWidget(self.create_pushButton)

        self.cancel_pushButton = QPushButton(NewProject)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.verticalLayout.addWidget(self.cancel_pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(NewProject)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.projectPath_lineEdit = QLineEdit(self.groupBox)
        self.projectPath_lineEdit.setObjectName(u"projectPath_lineEdit")

        self.horizontalLayout_2.addWidget(self.projectPath_lineEdit)

        self.select_pushButton = QPushButton(self.groupBox)
        self.select_pushButton.setObjectName(u"select_pushButton")
        self.select_pushButton.setMinimumSize(QSize(20, 20))
        self.select_pushButton.setMaximumSize(QSize(21, 21))
        icon = QIcon()
        icon.addFile(u":/pic/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.select_pushButton)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(NewProject)

        QMetaObject.connectSlotsByName(NewProject)
    # setupUi

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QCoreApplication.translate("NewProject", u"New Project", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewProject", u"ProjectName", None))
        self.projectName_label.setText("")
        self.create_pushButton.setText(QCoreApplication.translate("NewProject", u"Create", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("NewProject", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewProject", u"ProjectPath", None))
        self.select_pushButton.setText("")
    # retranslateUi