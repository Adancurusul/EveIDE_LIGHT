import re
import os
import sys
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox,QVBoxLayout
from ui.ui_module_simulate_widget import Ui_module_simulat_widget
from ui.ui_module_project_tree import Ui_ProjectTree
exSettingDict = {"projectPath":None,"testbenchFile":None,"toplevelFile":None,"iverilogPath":None,"gtkwavePath":None,"vvpPath":None,"simulatorPath":None}
class moduleProjectTree(Ui_ProjectTree,QWidget):
    def __init__(self):
        super(moduleProjectTree,self).__init__()
        self.setupUi(self)
        self.name = "moduleProjectTree"
        self.expand_pushButton.clicked.connect(self.expand_tree)
        self.collapse_pushButton.clicked.connect(self.collapse_tree)
        #self.setMinimumSize(0,0)
        #self.resize(0,0)
        #self.setWindowFlags(Qt.FramelessWindowHint)

    def expand_tree(self):
        self.projectFile_treeWidget.expandAll()

    def collapse_tree(self):
        self.projectFile_treeWidget.collapseAll()


class Simulator(QWidget,Ui_module_simulat_widget):
    def __init__(self):
        super(Simulator, self).__init__()
        self.initUi()
        self.name = "simulator"
    def initUi(self):
        self.setupUi(self)
        self.ProjectTreeWidget = moduleProjectTree()
        #self.ProjectTree.setupUi(self.ProjectTree)
        #self.projectTree_groupBox
        groupLayout = QVBoxLayout()
        groupLayout.addWidget(self.ProjectTreeWidget)
        self.projectTree_groupBox.setLayout(groupLayout)


    def startSimulate(self,settingDict):
        self.projectPath = settingDict.get("projectPath","")
        self.testbenchFile = settingDict.get("testchFile","")
        self.toplevelFile = settingDict.get("toplevel","")
        self.iverilogPath = settingDict.get("iverilogPath","")
        self.gtkwavePath = settingDict.get("gtkwavePath","")
        self.vvpPath = settingDict.get("vvpPath","")
        self.simulatorPath = settingDict.get("simulatorPath","")
        self.outputFile = self.toplevelFile.split(".")[0]
        self.moduleList = []
        self.moduleStr = ""
    def get_module_list(self):
        mstr = ""
        for eachModule in self.moduleList:
            mstr+=eachModule
            mstr+=" "
        self.moduleStr = mstr


    #def start_simulate(self,settingDict):

    def do_simulate(self):
        compileStr = self.iverilogPath +" -o "+ self.outputFile+self.testbenchFile+self.toplevelFile+self.moduleStr
        vvpStr = ""
        gtlWaveStr = ""

if __name__ == '__main__':
    # initDark()
    app = QApplication(sys.argv)
    mainWin = Simulator()
    mainWin.show()
    app.exec_()