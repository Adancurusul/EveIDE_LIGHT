# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_module_compile_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_CompileWidget(object):
    def setupUi(self, CompileWidget):
        if not CompileWidget.objectName():
            CompileWidget.setObjectName(u"CompileWidget")
        CompileWidget.resize(377, 691)
        self.verticalLayout_7 = QVBoxLayout(CompileWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(CompileWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_4.addWidget(self.label)

        self.project_comboBox = QComboBox(CompileWidget)
        self.project_comboBox.setObjectName(u"project_comboBox")

        self.horizontalLayout_4.addWidget(self.project_comboBox)

        self.horizontalSpacer_6 = QSpacerItem(28, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.useDefault_pushButton = QPushButton(CompileWidget)
        self.useDefault_pushButton.setObjectName(u"useDefault_pushButton")

        self.horizontalLayout_4.addWidget(self.useDefault_pushButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.groupBox_2 = QGroupBox(CompileWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolchain_lineEdit = QLineEdit(self.groupBox_2)
        self.toolchain_lineEdit.setObjectName(u"toolchain_lineEdit")

        self.horizontalLayout_2.addWidget(self.toolchain_lineEdit)

        self.moreToolchain_pushButton = QPushButton(self.groupBox_2)
        self.moreToolchain_pushButton.setObjectName(u"moreToolchain_pushButton")
        self.moreToolchain_pushButton.setMinimumSize(QSize(20, 20))
        self.moreToolchain_pushButton.setMaximumSize(QSize(21, 21))
        icon = QIcon()
        icon.addFile(u":/pic/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moreToolchain_pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.moreToolchain_pushButton)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_3 = QGroupBox(CompileWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bit64_checkBox = QCheckBox(self.groupBox_3)
        self.bit64_checkBox.setObjectName(u"bit64_checkBox")
        self.bit64_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.bit64_checkBox)

        self.bit32_checkBox = QCheckBox(self.groupBox_3)
        self.bit32_checkBox.setObjectName(u"bit32_checkBox")
        self.bit32_checkBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.bit32_checkBox)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(17, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.i_checkBox = QCheckBox(self.groupBox_3)
        self.i_checkBox.setObjectName(u"i_checkBox")
        self.i_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.i_checkBox)

        self.a_checkBox = QCheckBox(self.groupBox_3)
        self.a_checkBox.setObjectName(u"a_checkBox")
        self.a_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.a_checkBox)

        self.m_checkBox = QCheckBox(self.groupBox_3)
        self.m_checkBox.setObjectName(u"m_checkBox")

        self.horizontalLayout_3.addWidget(self.m_checkBox)

        self.c_checkBox = QCheckBox(self.groupBox_3)
        self.c_checkBox.setObjectName(u"c_checkBox")

        self.horizontalLayout_3.addWidget(self.c_checkBox)

        self.f_checkBox = QCheckBox(self.groupBox_3)
        self.f_checkBox.setObjectName(u"f_checkBox")

        self.horizontalLayout_3.addWidget(self.f_checkBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(CompileWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.autoMakefile_checkBox = QCheckBox(self.groupBox_4)
        self.autoMakefile_checkBox.setObjectName(u"autoMakefile_checkBox")
        self.autoMakefile_checkBox.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.autoMakefile_checkBox)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.verticalSpacer_3 = QSpacerItem(38, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(CompileWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(141, 0))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.binaryOutput_checkBox = QCheckBox(self.groupBox)
        self.binaryOutput_checkBox.setObjectName(u"binaryOutput_checkBox")
        self.binaryOutput_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.binaryOutput_checkBox)

        self.mifOutput_checkBox = QCheckBox(self.groupBox)
        self.mifOutput_checkBox.setObjectName(u"mifOutput_checkBox")

        self.verticalLayout_5.addWidget(self.mifOutput_checkBox)

        self.coeOutput_checkBox = QCheckBox(self.groupBox)
        self.coeOutput_checkBox.setObjectName(u"coeOutput_checkBox")

        self.verticalLayout_5.addWidget(self.coeOutput_checkBox)

        self.normalOutput_checkBox = QCheckBox(self.groupBox)
        self.normalOutput_checkBox.setObjectName(u"normalOutput_checkBox")

        self.verticalLayout_5.addWidget(self.normalOutput_checkBox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.outputDir_lineEdit = QLineEdit(self.groupBox)
        self.outputDir_lineEdit.setObjectName(u"outputDir_lineEdit")
        self.outputDir_lineEdit.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.outputDir_lineEdit)

        self.moreOutputDir_pushButton = QPushButton(self.groupBox)
        self.moreOutputDir_pushButton.setObjectName(u"moreOutputDir_pushButton")
        self.moreOutputDir_pushButton.setMinimumSize(QSize(20, 20))
        self.moreOutputDir_pushButton.setMaximumSize(QSize(21, 21))
        self.moreOutputDir_pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.moreOutputDir_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(68, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.compile_pushButton = QPushButton(CompileWidget)
        self.compile_pushButton.setObjectName(u"compile_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/pic/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compile_pushButton.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.compile_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(48, 173, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.retranslateUi(CompileWidget)

        QMetaObject.connectSlotsByName(CompileWidget)
    # setupUi

    def retranslateUi(self, CompileWidget):
        CompileWidget.setWindowTitle(QCoreApplication.translate("CompileWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CompileWidget", u"Project:", None))
        self.useDefault_pushButton.setText(QCoreApplication.translate("CompileWidget", u"useDefaultSettings", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("CompileWidget", u"Toolchain", None))
#if QT_CONFIG(tooltip)
        self.moreToolchain_pushButton.setToolTip(QCoreApplication.translate("CompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.moreToolchain_pushButton.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("CompileWidget", u"CompileSettings", None))
        self.bit64_checkBox.setText(QCoreApplication.translate("CompileWidget", u"64bit", None))
        self.bit32_checkBox.setText(QCoreApplication.translate("CompileWidget", u"32bit", None))
        self.i_checkBox.setText(QCoreApplication.translate("CompileWidget", u"i", None))
        self.a_checkBox.setText(QCoreApplication.translate("CompileWidget", u"a", None))
        self.m_checkBox.setText(QCoreApplication.translate("CompileWidget", u"m", None))
        self.c_checkBox.setText(QCoreApplication.translate("CompileWidget", u"c", None))
        self.f_checkBox.setText(QCoreApplication.translate("CompileWidget", u"f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("CompileWidget", u"MakeFile", None))
        self.autoMakefile_checkBox.setText(QCoreApplication.translate("CompileWidget", u"Auto generate", None))
        self.groupBox.setTitle(QCoreApplication.translate("CompileWidget", u"OutputSettings", None))
        self.binaryOutput_checkBox.setText(QCoreApplication.translate("CompileWidget", u"BinOutput", None))
        self.mifOutput_checkBox.setText(QCoreApplication.translate("CompileWidget", u"MifOutput", None))
        self.coeOutput_checkBox.setText(QCoreApplication.translate("CompileWidget", u"CoeOutput", None))
        self.normalOutput_checkBox.setText(QCoreApplication.translate("CompileWidget", u"elfOutput", None))
        self.label_2.setText(QCoreApplication.translate("CompileWidget", u"output dir:", None))
#if QT_CONFIG(tooltip)
        self.outputDir_lineEdit.setToolTip(QCoreApplication.translate("CompileWidget", u"PathNow", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.moreOutputDir_pushButton.setToolTip(QCoreApplication.translate("CompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.moreOutputDir_pushButton.setText("")
        self.compile_pushButton.setText(QCoreApplication.translate("CompileWidget", u"compile", None))
    # retranslateUi

