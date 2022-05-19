"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-16 14:39:17
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-08-02 14:27:28
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """

import re
import os 
import sys
import logging
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox,QVBoxLayout
from ui.ui_module_simulate_widget import Ui_module_simulat_widget
from eve_module.ChangeEncoding import ChangeEncoding
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
        self.ChangeEncoding = ChangeEncoding()
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
        self.ChangeEncoding = ChangeEncoding()
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
    def search_supoort_files(self,fileDict):
        moduleList = fileDict.get("module", [])
        for eachModule in moduleList:
            #logging.debug("eachModule")
            #logging.debug(eachModule)
            submoduleList = eachModule.get("submoduleName", [])
            for eachSub in submoduleList:
                #logging.debug("eachSub")
                #logging.debug(eachSub)
                subModule = eachSub.get("submoduleFileDict")
                pathNow = subModule.get("fullPath", "")
                if not pathNow in self.supportList:
                    self.supportList.append(pathNow)
                    #logging.debug("addSub" + pathNow)
                    self.search_supoort_files(subModule)
        pass
    def simulate(self,simulateDict)->dict:
        #{"projectDict":self.leftWidget.simulateWidget.project_comboBox.currentText(),"topLevel":self.topLevelDict,"iverilogPath":iverilogPath,"dumpFile":dumpFile}
        simDict = {}
        projectPath = simulateDict.get("projectDict","")
        topLevelName = simulateDict.get("topLevel",{}).get("fullPath",None)
        iverilogPath = simulateDict.get("iverilogPath","")
        __includePath = projectPath
        __supportPath = projectPath
        __dumpFile = simulateDict.get("dumpFile", "")
        __iverilog = iverilogPath + r"\bin\iverilog "
        __vvp = iverilogPath + r"\bin\vvp "
        __gtkwave = iverilogPath + r"\bin\gtkwave "
        __gtkwave = __gtkwave.replace("/", "\\")
        __iverilog = __iverilog.replace("/", "\\")
        __vpp = __vvp.replace("/", "\\")
        return {}

    def do_simulate(self,simulateDict)->dict:

        '''#{"projectDict": dictToSim, "topLevel": self.topLevelDict, "iverilogPath": iverilogPath}
                compileStr = self.iverilogPath +" -o "+ self.outputFile+self.testbenchFile+self.toplevelFile+self.moduleStr
                vvpStr = ""
                gtlWaveStr = ""'''
        simDict = {}
        includeList = simulateDict.get("includeList",[])
        fileList = simulateDict.get("projectDict",[])
        topLevelName = (simulateDict.get("topLevel",{}).get("fullPath",None))
        iverilogPath = os.path.abspath(simulateDict.get("iverilogPath",""))
        __dumpFile = os.path.abspath(simulateDict.get("dumpFile",""))
        ipath=''
        for eachIncludePath in includeList :
            ipath+=" -I "+os.path.abspath(eachIncludePath)
        __includePath = ipath

        #t =
        #全部转换为绝对地址
        __outputName =  os.path.abspath(os.path.dirname(topLevelName)+"\\"+os.path.basename(topLevelName).split(".")[0]+ "_evesim")
        #__outputName = os.path.dirname(topLevelName)+"\\a.out"
        iverilogPath = (iverilogPath.replace("/","\\"))
        __iverilog =iverilogPath+r"\bin\iverilog "
        __vvp = iverilogPath+r"\bin\vvp "
        __gtkwave = iverilogPath+r"\gtkwave\bin\gtkwave "
        __gtkwave = __gtkwave.replace("/", "\\")
        __iverilog = __iverilog.replace("/", "\\")
        __vpp = __vvp.replace("/", "\\")

        simCompileStr = iverilogPath+" "
        self.supportList = []

        topFileDict = None
        #logging.debug(topLevelDict)
        if topLevelName :
            for eachFileDict in fileList :
                if topLevelName == eachFileDict.get("fullPath","") :
                    topFileDict = eachFileDict
                    #logging.debug(topFileDict)
                    break
        if topFileDict :
            moduleList = topFileDict.get("module",[])
            for eachModule in moduleList :
                #logging.debug("eachModule")
                #logging.debug(eachModule)
                submoduleList = eachModule.get("submoduleName",[])
                for eachSub in submoduleList:
                    #logging.debug("eachSub")
                    #logging.debug(eachSub)
                    subModule  = eachSub.get("submoduleFileDict")
                    pathNow = subModule.get("fullPath","")
                    if not pathNow in self.supportList :
                        self.supportList.append(pathNow)
                        #logging.debug("addSub"+pathNow)
                        self.search_supoort_files(subModule)

        #logging.debug(self.supportList)
        __supportStr = ""
        #print(self.supportList)
        for eachStr in self.supportList:
            __supportStr +=" "+os.path.abspath(eachStr)
        print(__supportStr)
        simDict["iverilog"] = __iverilog + __includePath+" -o "+__outputName+" "+os.path.abspath(topLevelName)+" "+__supportStr
        #simDict["iverilog"] = __iverilog + " -I " + __includePath  + " -y " + __includePath+ " -o  " + __outputName +" "+topLevelName
        simDict["vvp"] = __vvp + " -n " + os.path.abspath(__outputName) + " -lxt2"
        simDict["gtkwave"] = __gtkwave + __dumpFile
        logging.debug(simDict.get("gtkwave"))
        logging.debug(simDict.get("iverilog"))
        logging.debug(simDict.get("vvp"))
        return simDict

class DoBeforeSimulate():
    def __init__(self,projectPath,testBenchPath):
        self.projectPath = projectPath
        self.testBenchPath = testBenchPath
        self.fileList = []
        self.simFiles = []
        self.modules = []
        self.ChangeEncoding = ChangeEncoding()
        self.scan_files()
    def get_module_name(self,fileDict):
        fullPath = fileDict.get("fullPath",None)
        fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            lineList = []
            #logging.debug(fullPath)

            with open(fullPath,"r",self.ChangeEncoding.getEncoding(fullPath)) as rFile:
                fileText = rmComments(rFile.read()).replace("\n"," ")
                #fileText = rmComments(rFile.read()).replace("\t", " ")
                fileList = re.split(";|endmodule|end",fileText)
                for each in fileList:
                    eachStr = each.lstrip()
                    #logging.debug(eachStr)
                    tp = r"(module)(\s+)(\w+)"
                    #patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
                    pattern = re.compile(tp)
                    match = pattern.search(eachStr)
                    if match:
                        ms = match.group(3)
                        mdict = {"moduleName":ms,"submoduleName":[]}
                        #logging.debug(ms)
                        fileDict["module"].append(mdict)
                        self.modules.append(ms)

            #logging.debug(fileDict.get("submodule",""))
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
                #eachFile["moduleName"] = eachFile.get("name","").split(".")[0]
                eachFile = self.get_module_name(eachFile)
                #eachFile = self.get_submodule(eachFile)
                #verilogList.append(eachFile)
                verilogList.append(eachFile)
        for index in range(len(verilogList)):
            eachFileDict = verilogList[index]
            #for eachFileDict in verilogList:
            verilogList[index] = self.get_submodule(eachFileDict)
            logging.debug(eachFile.get("submodule",None))
            #logging.debug(eachFile.get("submodule",None))
            #verilogList.append(eachFileDict)
        logging.debug(verilogList)
    def get_submodule(self,fileDict):
        fullPath = fileDict.get("fullPath", None)
        #logging.debug(fullPath)
        #fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
        #if fullPath == "..\\..\\..\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\RTL\\LPCE_tx.v":
            with open(fullPath, "r") as rFile:
                fileText = rmComments(rFile.read())
                #splitStr = ""
                fileList = re.split(r"module\s+\w+",fileText)
                #logging.debug(fullPath)

                #logging.debug(fileList)
                for index in range(1,len(fileList)):#例化一定是在module里面
                    #logging.debug(index)
                    #logging.debug(len(fileList))
                    #logging.debug(fileList[index])
                    logging.debug(fullPath)
                    eachStr = fileList[index]
                    #logging.debug(eachStr)
                    for each in self.modules:
                        #tp = r"(" + each + ")([ \t\v\r\f]+|\()?"
                        tp = r"(" + each + ")(?!\w)"
                        #tt = r"(" + each + ")\s+\w+"
                        pattern = re.compile(tp)
                        match = pattern.search(eachStr)
                        # logging.debug(match)
                        if match:
                            logging.debug(match)
                            if not fileDict["module"][index-1]["moduleName"] == each :
                                fileDict["module"][index-1]["submoduleName"].append(each)
                                fileDict["submodule"].append(each)


                #logging.debug(self.modules)

        logging.debug(fileDict)
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
        #logging.debug(fileList)
if __name__ == '__main__':
    # initDark()

    c = DoBeforeSimulate("C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE","C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\SimRTL\\LPCE_PHY_tb.v")


    '''app = QApplication(sys.argv)
    mainWin = Simulator()
    mainWin.show()
    app.exec_()'''