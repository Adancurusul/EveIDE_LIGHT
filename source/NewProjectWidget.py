"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-16 14:39:17
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:06:20
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
import logging
import sys
import os
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox
from ui.ui_new_project_window import Ui_NewProject
from qtpy.QtCore import Signal
import logging


class NewProjectWidget(QWidget,Ui_NewProject):
    closeSignal = Signal(str,str)
    def __init__(self,workspacePath,type):
        super(NewProjectWidget, self).__init__()
        self.setupUi(self)

        self.fatherPath = workspacePath
        self.type = type
        self.name = "unname"
        self.projectPath_lineEdit.setText(os.path.abspath(self.fatherPath+"/"+self.name))
        self.projectPath_lineEdit.setToolTip(self.projectPath_lineEdit.text())
        self.select_pushButton.clicked.connect(self.select_workspace)
        self.projectName_label.setText(os.path.split(self.projectPath_lineEdit.text())[1])
        self.projectPath_lineEdit.textChanged.connect(self.line_changed)
        self.cancel_pushButton.clicked.connect(lambda : self.button_handler("cancel"))
        self.create_pushButton.clicked.connect(lambda : self.button_handler("create"))
        self.pathNow = ""

    def button_handler(self,which):
        if which == "cancel":
            self.pathNow = ""
            self.close()
        elif which == "create":
            self.pathNow = self.projectPath_lineEdit.text()
            if os.path.exists(self.pathNow):
                choose = QMessageBox.warning(self, "EveIDE_LIGHT -- CREATE warning",
                                    "{0} is already exists .still create? (files inside will not be changed)".format(self.pathNow),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                print(choose)
                if choose == QMessageBox.No:
                    pass
                else :
                    self.close()
            else :
                os.mkdir(self.pathNow)
                if self.type == "compile":
                    try:
                        os.mkdir(self.pathNow + "\\src")
                        os.mkdir(self.pathNow + "\\inc")
                    except Exception as e:
                        logging.debug(e)

                    #with open(self.pathNow+"/main.c","w+")as f:
                     #   f.write("//Created by EveIDE_LIGHT ")
                logging.debug("new projectCreated : path : "+self.pathNow+" . type : "+self.type)
                self.close()

    def closeEvent(self, event):
        self.closeSignal.emit(self.pathNow,self.type)
    def line_changed(self):
        self.projectName_label.setText(os.path.split(self.projectPath_lineEdit.text())[1])
        self.projectPath_lineEdit.setToolTip(self.projectPath_lineEdit.text())

    def select_workspace(self):
        pathNow = QFileDialog.getExistingDirectory(None, "Choose  Path", self.fatherPath)
        self.projectPath_lineEdit.clear()
        self.projectPath_lineEdit.setText(pathNow)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = NewProjectWidget("D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\t_workspace","compile")
    mainWin.show()
    app.exec_()