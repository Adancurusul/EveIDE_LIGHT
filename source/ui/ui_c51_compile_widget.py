# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_c51_compile_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_C51CompileWidget(object):
    def setupUi(self, C51CompileWidget):
        if not C51CompileWidget.objectName():
            C51CompileWidget.setObjectName(u"C51CompileWidget")
        C51CompileWidget.resize(391, 445)
        self.verticalLayout = QVBoxLayout(C51CompileWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(C51CompileWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(65, 60))

        self.horizontalLayout_2.addWidget(self.label)

        self.c51project_comboBox = QComboBox(C51CompileWidget)
        self.c51project_comboBox.setObjectName(u"c51project_comboBox")

        self.horizontalLayout_2.addWidget(self.c51project_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(17, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_3 = QLabel(C51CompileWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.xramSize_lineEdit = QLineEdit(C51CompileWidget)
        self.xramSize_lineEdit.setObjectName(u"xramSize_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.xramSize_lineEdit)

        self.label_4 = QLabel(C51CompileWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.iramSize_lineEdit = QLineEdit(C51CompileWidget)
        self.iramSize_lineEdit.setObjectName(u"iramSize_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.iramSize_lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.groupBox_2 = QGroupBox(C51CompileWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QSize(16777215, 60))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.c51toolchain_lineEdict = QLineEdit(self.groupBox_2)
        self.c51toolchain_lineEdict.setObjectName(u"c51toolchain_lineEdict")
        self.c51toolchain_lineEdict.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.c51toolchain_lineEdict, 0, 0, 1, 1)

        self.c51moreToolchain_pushButton = QPushButton(self.groupBox_2)
        self.c51moreToolchain_pushButton.setObjectName(u"c51moreToolchain_pushButton")
        self.c51moreToolchain_pushButton.setMinimumSize(QSize(20, 20))
        self.c51moreToolchain_pushButton.setMaximumSize(QSize(21, 21))
        icon = QIcon()
        icon.addFile(u":/pic/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.c51moreToolchain_pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.c51moreToolchain_pushButton, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_3 = QSpacerItem(17, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.groupBox = QGroupBox(C51CompileWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c51outputDir_lineEdit = QLineEdit(self.groupBox)
        self.c51outputDir_lineEdit.setObjectName(u"c51outputDir_lineEdit")
        self.c51outputDir_lineEdit.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.c51outputDir_lineEdit)

        self.c51moreOutputDir_pushButton = QPushButton(self.groupBox)
        self.c51moreOutputDir_pushButton.setObjectName(u"c51moreOutputDir_pushButton")
        self.c51moreOutputDir_pushButton.setMinimumSize(QSize(20, 20))
        self.c51moreOutputDir_pushButton.setMaximumSize(QSize(21, 21))
        self.c51moreOutputDir_pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.c51moreOutputDir_pushButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer_4 = QSpacerItem(17, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.c51compile_pushButton = QPushButton(C51CompileWidget)
        self.c51compile_pushButton.setObjectName(u"c51compile_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/pic/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.c51compile_pushButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.c51compile_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(C51CompileWidget)

        QMetaObject.connectSlotsByName(C51CompileWidget)
    # setupUi

    def retranslateUi(self, C51CompileWidget):
        C51CompileWidget.setWindowTitle(QCoreApplication.translate("C51CompileWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("C51CompileWidget", u"Project:", None))
        self.label_3.setText(QCoreApplication.translate("C51CompileWidget", u"xram size:", None))
        self.label_4.setText(QCoreApplication.translate("C51CompileWidget", u"iram size:", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("C51CompileWidget", u"Toolchain", None))
#if QT_CONFIG(tooltip)
        self.c51moreToolchain_pushButton.setToolTip(QCoreApplication.translate("C51CompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.c51moreToolchain_pushButton.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("C51CompileWidget", u"OutputDir", None))
#if QT_CONFIG(tooltip)
        self.c51outputDir_lineEdit.setToolTip(QCoreApplication.translate("C51CompileWidget", u"PathNow", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.c51moreOutputDir_pushButton.setToolTip(QCoreApplication.translate("C51CompileWidget", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.c51moreOutputDir_pushButton.setText("")
        self.c51compile_pushButton.setText(QCoreApplication.translate("C51CompileWidget", u"compile", None))
    # retranslateUi

