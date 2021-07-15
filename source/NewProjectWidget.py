import logging
import sys
import os
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox
from ui.ui_new_project_window import Ui_NewProject

class NewProjectWidget(QWidget,Ui_NewProject):
    def __init__(self,workspacePath,type):
        super(NewProjectWidget, self).__init__()
        self.setupUi(self)

        self.fatherPath = workspacePath
        self.type = type
        self.name = "unname"
        self.projectPath_lineEdit.setText(os.path.abspath(self.fatherPath+"/"+self.name))
        self.select_pushButton.clicked.connect(self.select_workspace)
        #self.projectName_lineEdit.textChanged.connect()

    def select_workspace(self):
        pathNow = os.path.relpath(QFileDialog.getExistingDirectory(None, "Choose Dict Path", "../"))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = NewProjectWidget("D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\t_workspace","compile")
    mainWin.show()
    app.exec_()