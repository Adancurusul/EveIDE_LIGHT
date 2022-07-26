# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_arduino_compile_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_arduinoCompileWidget(object):
    def setupUi(self, arduinoCompileWidget):
        if not arduinoCompileWidget.objectName():
            arduinoCompileWidget.setObjectName(u"arduinoCompileWidget")
        arduinoCompileWidget.resize(336, 570)
        self.verticalLayout_3 = QVBoxLayout(arduinoCompileWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(arduinoCompileWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.groupBox_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.core_comboBox = QComboBox(self.layoutWidget)
        self.core_comboBox.setObjectName(u"core_comboBox")

        self.horizontalLayout.addWidget(self.core_comboBox)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.board_comboBox = QComboBox(self.layoutWidget)
        self.board_comboBox.setObjectName(u"board_comboBox")

        self.horizontalLayout.addWidget(self.board_comboBox)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.addZipLib_pushButton = QPushButton(self.layoutWidget1)
        self.addZipLib_pushButton.setObjectName(u"addZipLib_pushButton")

        self.horizontalLayout_2.addWidget(self.addZipLib_pushButton)

        self.searchLib_pushButton = QPushButton(self.layoutWidget1)
        self.searchLib_pushButton.setObjectName(u"searchLib_pushButton")

        self.horizontalLayout_2.addWidget(self.searchLib_pushButton)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.projectSelect_comboBox = QComboBox(self.layoutWidget2)
        self.projectSelect_comboBox.setObjectName(u"projectSelect_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projectSelect_comboBox.sizePolicy().hasHeightForWidth())
        self.projectSelect_comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.projectSelect_comboBox)

        self.arduinoProjectSelect_pushButton = QPushButton(self.layoutWidget2)
        self.arduinoProjectSelect_pushButton.setObjectName(u"arduinoProjectSelect_pushButton")
        self.arduinoProjectSelect_pushButton.setMinimumSize(QSize(20, 20))
        self.arduinoProjectSelect_pushButton.setMaximumSize(QSize(21, 21))
        icon = QIcon()
        icon.addFile(u":/pic/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arduinoProjectSelect_pushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.arduinoProjectSelect_pushButton)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.arduinoCliPath_lineEdit = QLineEdit(self.groupBox_2)
        self.arduinoCliPath_lineEdit.setObjectName(u"arduinoCliPath_lineEdit")

        self.horizontalLayout_4.addWidget(self.arduinoCliPath_lineEdit)

        self.arduinoCliSelect_pushButton = QPushButton(self.groupBox_2)
        self.arduinoCliSelect_pushButton.setObjectName(u"arduinoCliSelect_pushButton")
        self.arduinoCliSelect_pushButton.setMinimumSize(QSize(20, 20))
        self.arduinoCliSelect_pushButton.setMaximumSize(QSize(21, 21))
        self.arduinoCliSelect_pushButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.arduinoCliSelect_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.ArduinoProjectTree_groupBox = QGroupBox(arduinoCompileWidget)
        self.ArduinoProjectTree_groupBox.setObjectName(u"ArduinoProjectTree_groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ArduinoProjectTree_groupBox.sizePolicy().hasHeightForWidth())
        self.ArduinoProjectTree_groupBox.setSizePolicy(sizePolicy3)
        self.ArduinoProjectTree_groupBox.setMinimumSize(QSize(0, 270))

        self.verticalLayout_3.addWidget(self.ArduinoProjectTree_groupBox)

        self.groupBox = QGroupBox(arduinoCompileWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.serialSelect_comboBox = QComboBox(self.groupBox)
        self.serialSelect_comboBox.setObjectName(u"serialSelect_comboBox")

        self.gridLayout.addWidget(self.serialSelect_comboBox, 3, 2, 1, 1)

        self.checkCOM_pushButton = QPushButton(self.groupBox)
        self.checkCOM_pushButton.setObjectName(u"checkCOM_pushButton")

        self.gridLayout.addWidget(self.checkCOM_pushButton, 3, 3, 1, 1)

        self.upload_pushButton = QPushButton(self.groupBox)
        self.upload_pushButton.setObjectName(u"upload_pushButton")

        self.gridLayout.addWidget(self.upload_pushButton, 2, 3, 1, 1)

        self.compile_pushButton = QPushButton(self.groupBox)
        self.compile_pushButton.setObjectName(u"compile_pushButton")

        self.gridLayout.addWidget(self.compile_pushButton, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(arduinoCompileWidget)

        QMetaObject.connectSlotsByName(arduinoCompileWidget)
    # setupUi

    def retranslateUi(self, arduinoCompileWidget):
        arduinoCompileWidget.setWindowTitle(QCoreApplication.translate("arduinoCompileWidget", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("arduinoCompileWidget", u"Porject Settings", None))
        self.label.setText(QCoreApplication.translate("arduinoCompileWidget", u"Core:", None))
        self.label_2.setText(QCoreApplication.translate("arduinoCompileWidget", u"Board:", None))
        self.label_3.setText(QCoreApplication.translate("arduinoCompileWidget", u"Add Lib:", None))
        self.addZipLib_pushButton.setText(QCoreApplication.translate("arduinoCompileWidget", u"AddZipLib", None))
        self.searchLib_pushButton.setText(QCoreApplication.translate("arduinoCompileWidget", u"SearchLib", None))
        self.label_5.setText(QCoreApplication.translate("arduinoCompileWidget", u"Project:", None))
#if QT_CONFIG(tooltip)
        self.arduinoProjectSelect_pushButton.setToolTip(QCoreApplication.translate("arduinoCompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.arduinoProjectSelect_pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("arduinoCompileWidget", u"Arduino Cli Path:", None))
#if QT_CONFIG(tooltip)
        self.arduinoCliSelect_pushButton.setToolTip(QCoreApplication.translate("arduinoCompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.arduinoCliSelect_pushButton.setText("")
        self.ArduinoProjectTree_groupBox.setTitle(QCoreApplication.translate("arduinoCompileWidget", u"Project Tree", None))
        self.groupBox.setTitle(QCoreApplication.translate("arduinoCompileWidget", u"Compile Setting", None))
        self.label_4.setText(QCoreApplication.translate("arduinoCompileWidget", u"Upload COM:", None))
        self.checkCOM_pushButton.setText(QCoreApplication.translate("arduinoCompileWidget", u"check", None))
        self.upload_pushButton.setText(QCoreApplication.translate("arduinoCompileWidget", u"upload", None))
        self.compile_pushButton.setText(QCoreApplication.translate("arduinoCompileWidget", u"compile", None))
        self.label_7.setText(QCoreApplication.translate("arduinoCompileWidget", u"Compile:", None))
    # retranslateUi

