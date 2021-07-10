from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QMessageBox
import qtpy
from qtpy import QtGui
from qtpy import QtCore
from ui.ui_select_workspace import Ui_SelectWorkspace
import sys
import os
import logging
from eve_module.cfgRead import cfgRead


cfgMainPath = "..\configure\cfgMainPath"


class SelectWorkspace(QWidget,Ui_SelectWorkspace):
    def __init__(self):
        super(SelectWorkspace,self).__init__()
        self.cfgDict = {}
        self.currentPath = None #path which the editor need to open
        self.cfgReader = cfgRead(cfgMainPath)
        if self.cfgReader.check_path():
            self.cfgDict = self.cfgReader.get_dict()
        self.init()

    def init(self):
        self.setupUi(self)
        self.logic_init()
        self.ui_init()

    def ui_init(self):
        self.workspace_comboBox.addItems(self.cfgDict["workspacePath"])
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(554, 218)

    def logic_init(self):
        if len(self.cfgDict["workspacePath"])>10:
            del self.cfgDict["workspacePath"][-1]
        self.workspace_comboBox.currentIndexChanged.connect(lambda : self.update_lineEdit("comboBox"))
        self.select_pushButton.clicked.connect(lambda : self.update_lineEdit("select"))
        self.ok_pushButton.clicked.connect(lambda : self.button_hander("ok"))
        self.cancel_pushButton.clicked.connect(lambda  : self.button_hander("cancel"))

    def button_hander(self,buttonName):
        if buttonName == "ok":
            self.cfgDict["useAsDefault"]  = int(self.useAsDefault_checkBox.isChecked())
            currentWorkspacePath = self.workspace_lineEdit.text()
            currentWorkspacePath = currentWorkspacePath.replace('\\','/')
            print(currentWorkspacePath)
            if os.path.exists(currentWorkspacePath) :

                self.cfgDict["workspaceNow"] = currentWorkspacePath

                self.currentPath = currentWorkspacePath
                self.close()
            else :
                QMessageBox.critical(self, "ERROR", "The path is not valid", QMessageBox.Ok)
        elif buttonName == "cancel":
            self.close()

    def update_lineEdit(self,which):
        if which == "comboBox":
            self.workspace_lineEdit.setText(self.workspace_comboBox.currentText())
        elif which == "select":
            pathNow = QFileDialog.getExistingDirectory(None, "Choose Dict Path", "../")
            self.cfgDict["workspacePath"].insert(0,pathNow)
            self.workspace_lineEdit.setText(pathNow)

    def select_from_file_system(self):
        pathNow = QFileDialog.getExistingDirectory(None, "Choose Dict Path", "../")
        #print(pathNow)

    def closeEvent(self, event ) :
        self.cfgReader.write_dict(self.cfgDict)
        logging.debug("close choosing workspace ui")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',)
    app = QApplication(sys.argv)
    mainWin = SelectWorkspace()
    from qt_material import apply_stylesheet


    apply_stylesheet(app, theme='light_blue.xml')
    #mainWin.ui_init()
    mainWin.show()
    sys.exit(app.exec_())


