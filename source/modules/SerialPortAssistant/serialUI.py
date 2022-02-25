# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serialUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import serialUI_rc

class Ui_serialUI(object):
    def setupUi(self, serialUI):
        if not serialUI.objectName():
            serialUI.setObjectName(u"serialUI")
        serialUI.resize(728, 693)
        icon = QIcon()
        icon.addFile(u":/pic/serial.png", QSize(), QIcon.Normal, QIcon.Off)
        serialUI.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(serialUI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(serialUI)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(210, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formGroupBox = QGroupBox(self.widget)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formGroupBox.setMinimumSize(QSize(180, 250))
        self.verticalLayout_5 = QVBoxLayout(self.formGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.serialSelect_label = QLabel(self.formGroupBox)
        self.serialSelect_label.setObjectName(u"serialSelect_label")

        self.horizontalLayout_10.addWidget(self.serialSelect_label)

        self.serialSelect_comboBox = QComboBox(self.formGroupBox)
        self.serialSelect_comboBox.setObjectName(u"serialSelect_comboBox")

        self.horizontalLayout_10.addWidget(self.serialSelect_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.baudrate_label = QLabel(self.formGroupBox)
        self.baudrate_label.setObjectName(u"baudrate_label")

        self.horizontalLayout_9.addWidget(self.baudrate_label)

        self.baudRate_comboBox = QComboBox(self.formGroupBox)
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.addItem("")
        self.baudRate_comboBox.setObjectName(u"baudRate_comboBox")

        self.horizontalLayout_9.addWidget(self.baudRate_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.databit_label = QLabel(self.formGroupBox)
        self.databit_label.setObjectName(u"databit_label")

        self.horizontalLayout_8.addWidget(self.databit_label)

        self.dataBit_comboBox = QComboBox(self.formGroupBox)
        self.dataBit_comboBox.addItem("")
        self.dataBit_comboBox.addItem("")
        self.dataBit_comboBox.addItem("")
        self.dataBit_comboBox.addItem("")
        self.dataBit_comboBox.setObjectName(u"dataBit_comboBox")

        self.horizontalLayout_8.addWidget(self.dataBit_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.paritybit_label = QLabel(self.formGroupBox)
        self.paritybit_label.setObjectName(u"paritybit_label")

        self.horizontalLayout_7.addWidget(self.paritybit_label)

        self.checkBit_comboBox = QComboBox(self.formGroupBox)
        self.checkBit_comboBox.addItem("")
        self.checkBit_comboBox.addItem("")
        self.checkBit_comboBox.addItem("")
        self.checkBit_comboBox.addItem("")
        self.checkBit_comboBox.addItem("")
        self.checkBit_comboBox.setObjectName(u"checkBit_comboBox")

        self.horizontalLayout_7.addWidget(self.checkBit_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stopbit_label = QLabel(self.formGroupBox)
        self.stopbit_label.setObjectName(u"stopbit_label")

        self.horizontalLayout_6.addWidget(self.stopbit_label)

        self.stopBit_comboBox = QComboBox(self.formGroupBox)
        self.stopBit_comboBox.addItem("")
        self.stopBit_comboBox.addItem("")
        self.stopBit_comboBox.addItem("")
        self.stopBit_comboBox.setObjectName(u"stopBit_comboBox")

        self.horizontalLayout_6.addWidget(self.stopBit_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.state_label = QLabel(self.formGroupBox)
        self.state_label.setObjectName(u"state_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())
        self.state_label.setSizePolicy(sizePolicy1)
        self.state_label.setTextFormat(Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.state_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkSerial_pushButton = QPushButton(self.formGroupBox)
        self.checkSerial_pushButton.setObjectName(u"checkSerial_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkSerial_pushButton.sizePolicy().hasHeightForWidth())
        self.checkSerial_pushButton.setSizePolicy(sizePolicy2)
        self.checkSerial_pushButton.setMinimumSize(QSize(0, 23))
        self.checkSerial_pushButton.setAutoRepeatInterval(100)

        self.horizontalLayout_5.addWidget(self.checkSerial_pushButton)

        self.openSerial_pushButton = QPushButton(self.formGroupBox)
        self.openSerial_pushButton.setObjectName(u"openSerial_pushButton")
        sizePolicy2.setHeightForWidth(self.openSerial_pushButton.sizePolicy().hasHeightForWidth())
        self.openSerial_pushButton.setSizePolicy(sizePolicy2)
        self.openSerial_pushButton.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_5.addWidget(self.openSerial_pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.closeSerial_pushButton = QPushButton(self.formGroupBox)
        self.closeSerial_pushButton.setObjectName(u"closeSerial_pushButton")
        sizePolicy2.setHeightForWidth(self.closeSerial_pushButton.sizePolicy().hasHeightForWidth())
        self.closeSerial_pushButton.setSizePolicy(sizePolicy2)
        self.closeSerial_pushButton.setMinimumSize(QSize(0, 25))

        self.verticalLayout_5.addWidget(self.closeSerial_pushButton)


        self.verticalLayout_7.addWidget(self.formGroupBox)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(170, 0))
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hexReceive_checkBox = QCheckBox(self.groupBox_2)
        self.hexReceive_checkBox.setObjectName(u"hexReceive_checkBox")

        self.verticalLayout_3.addWidget(self.hexReceive_checkBox)

        self.showReceiveTime_checkBox = QCheckBox(self.groupBox_2)
        self.showReceiveTime_checkBox.setObjectName(u"showReceiveTime_checkBox")

        self.verticalLayout_3.addWidget(self.showReceiveTime_checkBox)


        self.horizontalLayout_18.addLayout(self.verticalLayout_3)

        self.clearReceive_pushButton = QPushButton(self.groupBox_2)
        self.clearReceive_pushButton.setObjectName(u"clearReceive_pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clearReceive_pushButton.sizePolicy().hasHeightForWidth())
        self.clearReceive_pushButton.setSizePolicy(sizePolicy3)
        self.clearReceive_pushButton.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_18.addWidget(self.clearReceive_pushButton)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(160, 120))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.timerSend_checkBox = QCheckBox(self.groupBox)
        self.timerSend_checkBox.setObjectName(u"timerSend_checkBox")

        self.horizontalLayout_17.addWidget(self.timerSend_checkBox)

        self.hexSend_checkBox = QCheckBox(self.groupBox)
        self.hexSend_checkBox.setObjectName(u"hexSend_checkBox")

        self.horizontalLayout_17.addWidget(self.hexSend_checkBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sendTimer_lineEdit = QLineEdit(self.groupBox)
        self.sendTimer_lineEdit.setObjectName(u"sendTimer_lineEdit")
        self.sendTimer_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.sendTimer_lineEdit)

        self.dw = QLabel(self.groupBox)
        self.dw.setObjectName(u"dw")

        self.horizontalLayout_4.addWidget(self.dw)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.clearSend_pushButton = QPushButton(self.groupBox)
        self.clearSend_pushButton.setObjectName(u"clearSend_pushButton")
        sizePolicy3.setHeightForWidth(self.clearSend_pushButton.sizePolicy().hasHeightForWidth())
        self.clearSend_pushButton.setSizePolicy(sizePolicy3)
        self.clearSend_pushButton.setMinimumSize(QSize(50, 25))

        self.verticalLayout_4.addWidget(self.clearSend_pushButton)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.verticalSpacer_3 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.chineseEncode_label = QLabel(self.widget)
        self.chineseEncode_label.setObjectName(u"chineseEncode_label")
        self.chineseEncode_label.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_21.addWidget(self.chineseEncode_label)

        self.chineseEncode_comboBox = QComboBox(self.widget)
        self.chineseEncode_comboBox.addItem("")
        self.chineseEncode_comboBox.addItem("")
        self.chineseEncode_comboBox.addItem("")
        self.chineseEncode_comboBox.setObjectName(u"chineseEncode_comboBox")
        self.chineseEncode_comboBox.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_21.addWidget(self.chineseEncode_comboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.formGroupBox_2 = QGroupBox(self.widget)
        self.formGroupBox_2.setObjectName(u"formGroupBox_2")
        self.formGroupBox_2.setMinimumSize(QSize(170, 120))
        self.verticalLayout_6 = QVBoxLayout(self.formGroupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.formGroupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.receiveCounter_label = QLabel(self.formGroupBox_2)
        self.receiveCounter_label.setObjectName(u"receiveCounter_label")

        self.horizontalLayout_11.addWidget(self.receiveCounter_label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.formGroupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.sendCounter_label = QLabel(self.formGroupBox_2)
        self.sendCounter_label.setObjectName(u"sendCounter_label")

        self.horizontalLayout_12.addWidget(self.sendCounter_label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.serialConnection_label = QLabel(self.formGroupBox_2)
        self.serialConnection_label.setObjectName(u"serialConnection_label")

        self.verticalLayout_6.addWidget(self.serialConnection_label)


        self.verticalLayout_7.addWidget(self.formGroupBox_2)


        self.horizontalLayout_16.addLayout(self.verticalLayout_7)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 2, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_4 = QGroupBox(serialUI)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(240, 55))
        self.groupBox_4.setMaximumSize(QSize(5555, 100))
        self.groupBox_4.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sendFile_lineEdit = QLineEdit(self.groupBox_4)
        self.sendFile_lineEdit.setObjectName(u"sendFile_lineEdit")
        self.sendFile_lineEdit.setMinimumSize(QSize(100, 25))
        self.sendFile_lineEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.sendFile_lineEdit)

        self.selectSendFile_pushButton = QPushButton(self.groupBox_4)
        self.selectSendFile_pushButton.setObjectName(u"selectSendFile_pushButton")
        self.selectSendFile_pushButton.setMinimumSize(QSize(20, 20))
        self.selectSendFile_pushButton.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.selectSendFile_pushButton)


        self.horizontalLayout_13.addLayout(self.horizontalLayout)

        self.sendFile_pushButton = QPushButton(self.groupBox_4)
        self.sendFile_pushButton.setObjectName(u"sendFile_pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sendFile_pushButton.sizePolicy().hasHeightForWidth())
        self.sendFile_pushButton.setSizePolicy(sizePolicy4)
        self.sendFile_pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.sendFile_pushButton)


        self.horizontalLayout_15.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(serialUI)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(240, 55))
        self.groupBox_3.setMaximumSize(QSize(5555, 100))
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.receiveFile_lineEdit = QLineEdit(self.groupBox_3)
        self.receiveFile_lineEdit.setObjectName(u"receiveFile_lineEdit")
        self.receiveFile_lineEdit.setMinimumSize(QSize(100, 25))
        self.receiveFile_lineEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.receiveFile_lineEdit)

        self.selectReceiveFile_pushButton = QPushButton(self.groupBox_3)
        self.selectReceiveFile_pushButton.setObjectName(u"selectReceiveFile_pushButton")
        self.selectReceiveFile_pushButton.setMinimumSize(QSize(20, 20))
        self.selectReceiveFile_pushButton.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.selectReceiveFile_pushButton)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_2)

        self.saveFile_pushButton = QPushButton(self.groupBox_3)
        self.saveFile_pushButton.setObjectName(u"saveFile_pushButton")
        self.saveFile_pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.saveFile_pushButton)


        self.horizontalLayout_15.addWidget(self.groupBox_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 1, 1, 1)

        self.widget_2 = QWidget(serialUI)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalGroupBox = QGroupBox(self.widget_2)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        sizePolicy1.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.receive_edit = QTextBrowser(self.verticalGroupBox)
        self.receive_edit.setObjectName(u"receive_edit")

        self.verticalLayout.addWidget(self.receive_edit)


        self.gridLayout.addWidget(self.verticalGroupBox, 0, 0, 1, 1)

        self.verticalGroupBox_2 = QGroupBox(self.widget_2)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy6)
        self.verticalGroupBox_2.setMinimumSize(QSize(340, 150))
        self.horizontalLayout_3 = QHBoxLayout(self.verticalGroupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.send_edit = QTextEdit(self.verticalGroupBox_2)
        self.send_edit.setObjectName(u"send_edit")
        self.send_edit.setMinimumSize(QSize(0, 50))
        self.send_edit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.send_edit)

        self.send_pushButton = QPushButton(self.verticalGroupBox_2)
        self.send_pushButton.setObjectName(u"send_pushButton")
        sizePolicy2.setHeightForWidth(self.send_pushButton.sizePolicy().hasHeightForWidth())
        self.send_pushButton.setSizePolicy(sizePolicy2)
        self.send_pushButton.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.send_pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.verticalGroupBox_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)


        self.retranslateUi(serialUI)

        self.checkSerial_pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(serialUI)
    # setupUi

    def retranslateUi(self, serialUI):
        serialUI.setWindowTitle(QCoreApplication.translate("serialUI", u"Form", None))
        self.formGroupBox.setTitle(QCoreApplication.translate("serialUI", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.serialSelect_label.setText(QCoreApplication.translate("serialUI", u"\u4e32\u53e3\u9009\u62e9\uff1a", None))
        self.baudrate_label.setText(QCoreApplication.translate("serialUI", u"\u6ce2\u7279\u7387\uff1a", None))
        self.baudRate_comboBox.setItemText(0, QCoreApplication.translate("serialUI", u"115200", None))
        self.baudRate_comboBox.setItemText(1, QCoreApplication.translate("serialUI", u"2400", None))
        self.baudRate_comboBox.setItemText(2, QCoreApplication.translate("serialUI", u"4800", None))
        self.baudRate_comboBox.setItemText(3, QCoreApplication.translate("serialUI", u"9600", None))
        self.baudRate_comboBox.setItemText(4, QCoreApplication.translate("serialUI", u"14400", None))
        self.baudRate_comboBox.setItemText(5, QCoreApplication.translate("serialUI", u"19200", None))
        self.baudRate_comboBox.setItemText(6, QCoreApplication.translate("serialUI", u"38400", None))
        self.baudRate_comboBox.setItemText(7, QCoreApplication.translate("serialUI", u"57600", None))
        self.baudRate_comboBox.setItemText(8, QCoreApplication.translate("serialUI", u"76800", None))
        self.baudRate_comboBox.setItemText(9, QCoreApplication.translate("serialUI", u"12800", None))
        self.baudRate_comboBox.setItemText(10, QCoreApplication.translate("serialUI", u"230400", None))
        self.baudRate_comboBox.setItemText(11, QCoreApplication.translate("serialUI", u"460800", None))

        self.databit_label.setText(QCoreApplication.translate("serialUI", u"\u6570\u636e\u4f4d\uff1a", None))
        self.dataBit_comboBox.setItemText(0, QCoreApplication.translate("serialUI", u"8", None))
        self.dataBit_comboBox.setItemText(1, QCoreApplication.translate("serialUI", u"7", None))
        self.dataBit_comboBox.setItemText(2, QCoreApplication.translate("serialUI", u"6", None))
        self.dataBit_comboBox.setItemText(3, QCoreApplication.translate("serialUI", u"5", None))

        self.paritybit_label.setText(QCoreApplication.translate("serialUI", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.checkBit_comboBox.setItemText(0, QCoreApplication.translate("serialUI", u"None", None))
        self.checkBit_comboBox.setItemText(1, QCoreApplication.translate("serialUI", u"Odd", None))
        self.checkBit_comboBox.setItemText(2, QCoreApplication.translate("serialUI", u"Even", None))
        self.checkBit_comboBox.setItemText(3, QCoreApplication.translate("serialUI", u"Mark", None))
        self.checkBit_comboBox.setItemText(4, QCoreApplication.translate("serialUI", u"Space", None))

        self.stopbit_label.setText(QCoreApplication.translate("serialUI", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.stopBit_comboBox.setItemText(0, QCoreApplication.translate("serialUI", u"1", None))
        self.stopBit_comboBox.setItemText(1, QCoreApplication.translate("serialUI", u"1.5", None))
        self.stopBit_comboBox.setItemText(2, QCoreApplication.translate("serialUI", u"2", None))

#if QT_CONFIG(tooltip)
        self.state_label.setToolTip(QCoreApplication.translate("serialUI", u"\u4e32\u53e3\u540d", None))
#endif // QT_CONFIG(tooltip)
        self.state_label.setText(QCoreApplication.translate("serialUI", u"\u65e0", None))
        self.checkSerial_pushButton.setText(QCoreApplication.translate("serialUI", u"\u68c0\u6d4b\u4e32\u53e3", None))
        self.openSerial_pushButton.setText(QCoreApplication.translate("serialUI", u"\u6253\u5f00\u4e32\u53e3", None))
        self.closeSerial_pushButton.setText(QCoreApplication.translate("serialUI", u"\u5173\u95ed\u4e32\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("serialUI", u"\u63a5\u6536\u8bbe\u7f6e", None))
        self.hexReceive_checkBox.setText(QCoreApplication.translate("serialUI", u"Hex\u63a5\u6536", None))
        self.showReceiveTime_checkBox.setText(QCoreApplication.translate("serialUI", u"\u663e\u793a\u65f6\u95f4", None))
        self.clearReceive_pushButton.setText(QCoreApplication.translate("serialUI", u"\u6e05\u9664", None))
        self.groupBox.setTitle(QCoreApplication.translate("serialUI", u"\u53d1\u9001\u8bbe\u7f6e", None))
        self.timerSend_checkBox.setText(QCoreApplication.translate("serialUI", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.hexSend_checkBox.setText(QCoreApplication.translate("serialUI", u"Hex\u53d1\u9001", None))
        self.sendTimer_lineEdit.setText(QCoreApplication.translate("serialUI", u"1000", None))
        self.dw.setText(QCoreApplication.translate("serialUI", u"ms/\u6b21", None))
        self.clearSend_pushButton.setText(QCoreApplication.translate("serialUI", u"\u6e05\u9664\u53d1\u9001", None))
        self.chineseEncode_label.setText(QCoreApplication.translate("serialUI", u"\u4e2d\u6587\u7f16\u7801\uff1a", None))
        self.chineseEncode_comboBox.setItemText(0, QCoreApplication.translate("serialUI", u"utf-8", None))
        self.chineseEncode_comboBox.setItemText(1, QCoreApplication.translate("serialUI", u"gb2312", None))
        self.chineseEncode_comboBox.setItemText(2, QCoreApplication.translate("serialUI", u"gbk", None))

        self.formGroupBox_2.setTitle(QCoreApplication.translate("serialUI", u"\u4e32\u53e3\u72b6\u6001", None))
        self.label.setText(QCoreApplication.translate("serialUI", u"\u5df2\u63a5\u6536\uff1a", None))
        self.receiveCounter_label.setText(QCoreApplication.translate("serialUI", u"0", None))
        self.label_2.setText(QCoreApplication.translate("serialUI", u"\u5df2\u53d1\u9001\uff1a", None))
        self.sendCounter_label.setText(QCoreApplication.translate("serialUI", u"0", None))
        self.serialConnection_label.setText(QCoreApplication.translate("serialUI", u"\u4e32\u53e3\u672a\u8fde\u63a5", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("serialUI", u"\u53d1\u9001\u6587\u4ef6", None))
        self.selectSendFile_pushButton.setText(QCoreApplication.translate("serialUI", u"*", None))
        self.sendFile_pushButton.setText(QCoreApplication.translate("serialUI", u"\u53d1\u9001\u6587\u4ef6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("serialUI", u"\u4fdd\u5b58\u5230\u6587\u4ef6", None))
        self.selectReceiveFile_pushButton.setText(QCoreApplication.translate("serialUI", u"*", None))
        self.saveFile_pushButton.setText(QCoreApplication.translate("serialUI", u"\u4fdd\u5b58\u5230\u6587\u4ef6", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("serialUI", u"\u63a5\u6536\u533a", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("serialUI", u"\u53d1\u9001\u533a", None))
        self.send_pushButton.setText(QCoreApplication.translate("serialUI", u"\u53d1\u9001", None))
    # retranslateUi

