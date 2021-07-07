# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_left_module_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_leftModuleWidget(object):
    def setupUi(self, leftModuleWidget):
        if not leftModuleWidget.objectName():
            leftModuleWidget.setObjectName(u"leftModuleWidget")
        leftModuleWidget.resize(364, 682)
        self.horizontalLayout_3 = QHBoxLayout(leftModuleWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dockWidget = QDockWidget(leftModuleWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftModuleWidgetIn = QTabWidget(self.dockWidgetContents)
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

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout_3.addWidget(self.dockWidget)


        self.retranslateUi(leftModuleWidget)

        self.leftModuleWidgetIn.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(leftModuleWidget)
    # setupUi

    def retranslateUi(self, leftModuleWidget):
        leftModuleWidget.setWindowTitle(QCoreApplication.translate("leftModuleWidget", u"Form", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.project_tab), QCoreApplication.translate("leftModuleWidget", u"project", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.compile_tab), QCoreApplication.translate("leftModuleWidget", u"compile", None))
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.simulate_tab), QCoreApplication.translate("leftModuleWidget", u"simulate", None))
    # retranslateUi

