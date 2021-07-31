# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_left_module_widget_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(344, 756)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftModuleWidgetIn = QTabWidget(Form)
        self.leftModuleWidgetIn.setObjectName(u"leftModuleWidgetIn")
        self.leftModuleWidgetIn.setLayoutDirection(Qt.LeftToRight)
        self.leftModuleWidgetIn.setTabPosition(QTabWidget.West)
        self.project_tab = QWidget()
        self.project_tab.setObjectName(u"project_tab")
        icon = QIcon()
        icon.addFile(u":/pic/project.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftModuleWidgetIn.addTab(self.project_tab, icon, "")
        self.compile_tab = QWidget()
        self.compile_tab.setObjectName(u"compile_tab")
        icon1 = QIcon()
        icon1.addFile(u":/pic/compile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftModuleWidgetIn.addTab(self.compile_tab, icon1, "")
        self.simulate_tab = QWidget()
        self.simulate_tab.setObjectName(u"simulate_tab")
        icon2 = QIcon()
        icon2.addFile(u":/pic/simulate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftModuleWidgetIn.addTab(self.simulate_tab, icon2, "")

        self.horizontalLayout.addWidget(self.leftModuleWidgetIn)


        self.retranslateUi(Form)

        self.leftModuleWidgetIn.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.project_tab), QCoreApplication.translate("Form", u"project", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.compile_tab), QCoreApplication.translate("Form", u"compile", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.simulate_tab), QCoreApplication.translate("Form", u"simulate", None))
    # retranslateUi

