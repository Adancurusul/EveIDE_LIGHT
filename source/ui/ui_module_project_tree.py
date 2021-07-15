# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_module_project_tree.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_ProjectTree(object):
    def setupUi(self, ProjectTree):
        if not ProjectTree.objectName():
            ProjectTree.setObjectName(u"ProjectTree")
        ProjectTree.resize(294, 528)
        ProjectTree.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(ProjectTree)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(ProjectTree)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(87, 0))

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(48, 18, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.expand_pushButton = QPushButton(ProjectTree)
        self.expand_pushButton.setObjectName(u"expand_pushButton")
        self.expand_pushButton.setMinimumSize(QSize(20, 20))
        self.expand_pushButton.setMaximumSize(QSize(21, 21))
        self.expand_pushButton.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/pic/expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.expand_pushButton)

        self.collapse_pushButton = QPushButton(ProjectTree)
        self.collapse_pushButton.setObjectName(u"collapse_pushButton")
        self.collapse_pushButton.setMinimumSize(QSize(20, 20))
        self.collapse_pushButton.setMaximumSize(QSize(21, 21))
        icon1 = QIcon()
        icon1.addFile(u":/pic/collapse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.collapse_pushButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.collapse_pushButton)

        self.label = QLabel(ProjectTree)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(5, 21))

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(ProjectTree)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(21, 21))
        icon2 = QIcon()
        icon2.addFile(u":/pic/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.projectFile_treeWidget = QTreeWidget(ProjectTree)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.projectFile_treeWidget.setHeaderItem(__qtreewidgetitem)
        self.projectFile_treeWidget.setObjectName(u"projectFile_treeWidget")

        self.verticalLayout.addWidget(self.projectFile_treeWidget)


        self.retranslateUi(ProjectTree)

        QMetaObject.connectSlotsByName(ProjectTree)
    # setupUi

    def retranslateUi(self, ProjectTree):
        ProjectTree.setWindowTitle(QCoreApplication.translate("ProjectTree", u"Form", None))
#if QT_CONFIG(tooltip)
        self.expand_pushButton.setToolTip(QCoreApplication.translate("ProjectTree", u"<html><head/><body><p>Expand All</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.expand_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.collapse_pushButton.setToolTip(QCoreApplication.translate("ProjectTree", u"Collapse All", None))
#endif // QT_CONFIG(tooltip)
        self.collapse_pushButton.setText("")
        self.label.setText(QCoreApplication.translate("ProjectTree", u"|", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("ProjectTree", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
    # retranslateUi

