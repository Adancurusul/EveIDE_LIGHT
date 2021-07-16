import re
import os
import sys
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox,QVBoxLayout
from ui.ui_module_simulate_widget import Ui_module_simulat_widget
from ui.ui_module_project_tree import Ui_ProjectTree
exSettingDict = {"projectPath":None,"testbenchFile":None,"toplevelFile":None,"iverilogPath":None,"gtkwavePath":None,"vvpPath":None,"simulatorPath":None}
def rmComments(text):
    singLineComments = re.compile(r'//(.*)', re.MULTILINE)
    multiLineComments = re.compile(r'/\*(.*)\*/', re.DOTALL)
    text = singLineComments.sub('', text)
    text = multiLineComments.sub('', text)
    return text

class moduleProjectTree(Ui_ProjectTree,QWidget):
    def __init__(self):
        super(moduleProjectTree,self).__init__()
        self.setupUi(self)
        self.name = "moduleProjectTree"
        self.expand_pushButton.clicked.connect(self.expand_tree)
        self.collapse_pushButton.clicked.connect(self.collapse_tree)
        self.comboBox.addItem("Project View")
        self.projectFile_treeWidget.setHeaderLabel("")
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





        pass
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
class SimFile():
    def __init__(self,projectPath,testBenchPath):
        self.projectPath = projectPath
        self.testBenchPath = testBenchPath
        self.fileList = []
        self.simFiles = []
        self.modules = []
        self.scan_files()
    def get_module_name(self,fileDict):
        fullPath = fileDict.get("fullPath",None)
        fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            lineList = []
            #print(fullPath)
            with open(fullPath,"r") as rFile:
                fileText = rmComments(rFile.read()).replace("\n"," ")
                #fileText = rmComments(rFile.read()).replace("\t", " ")
                fileList = re.split(";|endmodule|end",fileText)
                for each in fileList:
                    eachStr = each.lstrip()
                    #print(eachStr)
                    tp = r"(module)(\s+)(\w+)"
                    patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
                    pattern = re.compile(tp)
                    match = pattern.search(eachStr)
                    if match:
                        ms = match.group(3)
                        #print(ms)
                        fileDict["module"].append(ms)
                        self.modules.append(ms)

            #print(fileDict.get("submodule",""))
        return fileDict


    def get_module_in_tb(self):
        with open(self.testBenchPath,"r",encoding="utf-8") :
            pass
    def scan_files(self):
        import logging
        from ProjectManage import ProjectManage
        manager = ProjectManage(self.projectPath)
        self.fileList = manager.file_list
        verilogList  = []

        """
        这里
        没法给dict添加
        gkd
        先睡觉了
        
        """
        for eachFile in self.fileList:
            if eachFile.get("fileSuffix","") == "v" :
                eachFile["moduleName"] = eachFile.get("name","").split(".")[0]
                eachFile = self.get_module_name(eachFile)
                #eachFile = self.get_submodule(eachFile)
                #verilogList.append(eachFile)
                verilogList.append(eachFile)
        for eachFileDict in verilogList:
            eachFile = self.get_submodule(eachFileDict)
            logging.debug(eachFile.get("submodule",None))
            print(eachFile.get("submodule",None))
            #verilogList.append(eachFileDict)
        print(verilogList)
    def get_submodule(self,fileDict):
        fullPath = fileDict.get("fullPath", None)
        #print(fullPath)
        fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            with open(fullPath, "r") as rFile:
                fileText = rmComments(rFile.read())
                #print(self.modules)
                print(fullPath)
                for each in self.modules:

                    tp = r"(" + each + ")"
                    pattern = re.compile(tp)
                    match = pattern.search(fileText)
                    #print(match)
 
                    if match:
                        fileDict["submodule"].append(each)
        return fileDict
    def get_file_of_module(self,moduleName):
        moduleFileList = []
        for eachFile in self.fileList:
            if eachFile.get("moduleName","") == moduleName:
                moduleFileList.append(eachFile)
        for eachModule in moduleFileList :
            if eachModule not in self.simFiles:
                self.simFiles.append(eachModule)
        return moduleFileList
        #print(fileList)
if __name__ == '__main__':
    # initDark()

    c = SimFile("C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE","C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\SimRTL\\LPCE_PHY_tb.v")


    '''app = QApplication(sys.argv)
    mainWin = Simulator()
    mainWin.show()
    app.exec_()'''