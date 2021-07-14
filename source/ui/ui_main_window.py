# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 631)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        icon = QIcon()
        icon.addFile(u":/pic/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionopen.setIcon(icon)
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        icon1 = QIcon()
        icon1.addFile(u":/pic/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionnew.setIcon(icon1)
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        icon2 = QIcon()
        icon2.addFile(u":/pic/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsave.setIcon(icon2)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        icon3 = QIcon()
        icon3.addFile(u":/pic/save_as.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionNewProject = QAction(MainWindow)
        self.actionNewProject.setObjectName(u"actionNewProject")
        self.actionOpenProject = QAction(MainWindow)
        self.actionOpenProject.setObjectName(u"actionOpenProject")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.actiontest_2 = QAction(MainWindow)
        self.actiontest_2.setObjectName(u"actiontest_2")
        self.actionModules = QAction(MainWindow)
        self.actionModules.setObjectName(u"actionModules")
        self.actionModules.setCheckable(True)
        self.actionModules.setChecked(True)
        self.actionOutputs = QAction(MainWindow)
        self.actionOutputs.setObjectName(u"actionOutputs")
        self.actionOutputs.setCheckable(True)
        self.actionOutputs.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpenRecentFile = QMenu(self.menuFile)
        self.menuOpenRecentFile.setObjectName(u"menuOpenRecentFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuProject = QMenu(self.menubar)
        self.menuProject.setObjectName(u"menuProject")
        self.menuOpenRecentProject = QMenu(self.menuProject)
        self.menuOpenRecentProject.setObjectName(u"menuOpenRecentProject")
        self.menuModules = QMenu(self.menubar)
        self.menuModules.setObjectName(u"menuModules")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuModules.menuAction())
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.menuOpenRecentFile.menuAction())
        self.menuOpenRecentFile.addAction(self.actiontest)
        self.menuView.addAction(self.actionModules)
        self.menuView.addAction(self.actionOutputs)
        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionOpenProject)
        self.menuProject.addAction(self.menuOpenRecentProject.menuAction())
        self.menuOpenRecentProject.addAction(self.actiontest_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"SaveAs", None))
        self.actionNewProject.setText(QCoreApplication.translate("MainWindow", u"NewProject", None))
        self.actionOpenProject.setText(QCoreApplication.translate("MainWindow", u"OpenProject", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actiontest_2.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actionModules.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.actionOutputs.setText(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpenRecentFile.setTitle(QCoreApplication.translate("MainWindow", u"OpenRecentFile", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuProject.setTitle(QCoreApplication.translate("MainWindow", u"Project", None))
        self.menuOpenRecentProject.setTitle(QCoreApplication.translate("MainWindow", u"OpenRecentProject", None))
        self.menuModules.setTitle(QCoreApplication.translate("MainWindow", u"Modules", None))
    # retranslateUi

