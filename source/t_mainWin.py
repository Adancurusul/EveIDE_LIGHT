'''
加 ：
检查文件是否改动


'''
__version__ = "V0.0.1"
import datetime

import logging
import time
from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFormLayout, QLineEdit, QTabWidget, \
    QMdiArea, QTextEdit, QDockWidget, QSplitter, QMdiSubWindow, QTreeWidgetItem, QMessageBox,QMenu,QAction
from qtpy.QtCore import Qt, Signal, QTimer,QSize,QFile
from qtpy.QtGui import QPalette, QBrush, QColor,QIcon,QCursor
import qtpy
from qtpy import QtGui
from qtpy import QtCore
import sys
import functools
import os,shutil,subprocess
from ui.ui_main_window import Ui_MainWindow
from LeftModuleWidget import LeftModuleWidget
from OutputWidget import OutputWidget
from EditorWidget import EditorWidget
from eve_module.cfgRead import cfgRead
from eve_module.CreateInstance import CreateInsance
from eve_module.GetSimDumpFile import GetSimDumpFile
from eve_module.ChangeEncoding import ChangeEncoding
from eve_module.GetFunctionInC import GetFunctionInC
from eve_module.SimulateThread import SimulateThread
from eve_module.EmittingStr import EmittingStr
from ProjectManage import ProjectManage
from SelectWorkspace import SelectWorkspace
from NewProjectWidget import NewProjectWidget
from SimulatorFileManager import SimulatorFileManager
ex_cfgMainDict = {"workspaceSetting":{}}
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)

def read_cfg(cfgPath) -> dict:
    cfgReader = cfgRead(cfgPath)
    return cfgReader.get_dict()


def write_cfg(cfgPath, writeDict):
    cfgReader = cfgRead(cfgPath)
    cfgReader.write_dict(writeDict)
    # return cfgReader.get_dict()


class MainWinUi(QMainWindow, Ui_MainWindow):
    __main_cfg_path = cfgMainPath = "..\configure\cfgMainPath"
    #__project_cfg_path = "../configure/cfgPorjectList.evecfg"

    __workspace_cfg_path = "../configure/cfgWorkspace.evecfg"

    __simulator_cfg_path = "../configure/cfgSimulater.evecfg"

    projectTreeDictList = []
    #_surpprot_file_suffix_list[]

    def __init__(self):
        super(MainWinUi, self).__init__()
        # self.testUi()
        #sys.stdout = EmittingStr()
        #sys.stderr = EmittingStr()
        #sys.stdout.textWritten.connect(self.outputWritten)
        #sys.stderr.textWritten.connect(self.outputWritten)

        self.firstInit = 0  # 第一次启动selectworkspace
        self.initWorkspace()


    def initWorkspace(self):
        self.showMinimized()
        self.workspaceSelector = SelectWorkspace()
        if self.workspaceSelector.cfgDict.get("useAsDefault",0) == 1:
            self.initAll()
            #self.showMaximized()
        else:

            self.workspaceSelector.show()
            self.workspaceSelector.closeSignal.connect(self.initAll)

    def initAll(self):
        if self.firstInit:
            self.updateWorkspace()
        else:
            logging.debug("initAll")
            self.showNormal()
            self.initUi()
            self.initLogic()
            self.init_simulator()
            self.init_timer()
            self.untitledNum = 1
    def init_timer(self):
        self.timerCheckFile = QTimer()
        self.timerCheckFile.timeout.connect(self.check_file)
        self.timerCheckFile.start(10000)

    def initLogic(self):
        self.ChangeEncoding = ChangeEncoding()

        self.firstInit = 1

        self.treeWidget = self.leftWidget.projectWidget.projectFile_treeWidget
        self.simulateTreeWidget = self.leftWidget.simulateWidget.ProjectTreeWidget.projectFile_treeWidget
        logging.debug("nowSim"+str(self.simulateTreeWidget ))
        self.treeWidget.setHeaderLabel("")
        cfgDict = read_cfg(self.__workspace_cfg_path)
        self.workspacePath = cfgDict.get("workspaceNow","../")
        write_cfg(self.__workspace_cfg_path,cfgDict)
        self.projectList = self.check_compile_projects
        self.simulateList = self.check_simulate_projcet
        self.__project_cfg_path = self.workspacePath+"/cfgPorjectList.evecfg"
        cfgDictProject = read_cfg(self.__project_cfg_path)
        compileSettingList = self.clear_unused_compile_project(cfgDictProject.get("comlipeSetting",[]),self.projectList)

        cfgDictProject["comlipeSetting"] = compileSettingList
        write_cfg(self.__project_cfg_path,cfgDictProject)

        self.leftWidget.compileWidget.addSettingsDictList(compileSettingList)

        logging.debug("workspace Now :" + self.workspacePath)
        if ( self.workspacePath == "") or (self.workspacePath is  None):
            self.workspacePath = "./"
        logging.debug("workspace now is:" + self.workspacePath)
        self.setWindowTitle("EveIDE-LIGHT  "+ os.path.abspath(self.workspacePath))
        self.set_workspace_tree()
        # 刷新树状列表
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 打开右键菜单的策略
        self.treeWidget.customContextMenuRequested.connect(self.project_tree_right_click)  # 绑定事件
        self.init_sub_thread()
        self.view_dock_closeEvent()
        self.connect_signal()

    def clear_unused_compile_project(self,projectSettingList,projectList):
        realSettingList = []
        for eachProject in projectList:
            findSetting = 0
            ex_projectPath = eachProject
            compileSettingDefaultEx = {"projectName":os.path.basename(ex_projectPath),"projectPath":ex_projectPath,"gccPath":"modules/bin","outputPath":ex_projectPath+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
                                       "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-addr2line","if64bit":1}

            for eachSetting in projectSettingList:
                fullPath = eachSetting.get("projectPath",None)
                if fullPath :
                    if fullPath == eachProject :
                        realSettingList.append(eachSetting)
                        findSetting = 1
            if not findSetting:
                realSettingList.append(compileSettingDefaultEx)
        return realSettingList
    def init_sub_thread(self):
        self.simulateThread = SimulateThread()

    def outputWritten(self, text):

        # self.textEdit.clear()
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.TextOutput.setTextCursor(cursor)
        self.TextOutput.ensureCursorVisible()


    def check_file(self):
        subWindowList = self.mdi.subWindowList()
        #logging.debug(subWindowList)
        for eachWindow in subWindowList:
            widgetNow = eachWindow.widget()
            dictNow = widgetNow.dictNow
            if not dictNow.get("newFile",None):
                #logging.debug(dictNow)
                fullPath = dictNow.get("fullPath",None)
                if not fullPath is None:
                    if os.path.exists(fullPath):
                        lastSaveTime = int(os.stat(fullPath).st_mtime)
                        openTime = dictNow.get("openTime",None)
                        if openTime is not None:
                            if  openTime < lastSaveTime:
                                self.timerCheckFile.stop()
                                self.ask_if_reload(os.path.relpath(fullPath),eachWindow,dictNow)
                    else:
                        eachWindow.close()

    def ask_if_reload(self,fileName,windowNow,fileDict):
        choose = QMessageBox.warning(self, "EveIDE_LIGHT -- FILE warning",
                                     "{0} has been changed outside ,reload?".format(fileName),QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if choose == QMessageBox.Yes:
            windowNow.close()
            self.addEditorWidget(fileDict)
    def updateTextOutput(self,color,outStr):
        self.TextOutput.append(color%outStr)
    def do_compile_for_project(self,settingList,currentPorjectName):
        '''
        TODO:
        目前只支持单文件自动编译，后期会增加多文件

        :param settingList:
        :param currentPorjectName:
        :return:
        '''
        #compileSettingDefaultEx = {"projectName":os.path.basename(ex_projectPath),"projectPath":ex_projectPath,"gccPath":"modules/bin","outputPath":ex_projectPath+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
        #                           "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-addr2line","if64bit":1}
        self.save_compile_settings(settingList)
        for eachDict in settingList:
            if currentPorjectName == eachDict.get("projectName",""):
                dictNow = eachDict
                pathNow = dictNow.get("projectPath","")
                if dictNow.get("autoMakefile",1)==1:
                    gccPath = eachDict.get("gccPath","")
                    gccPrefix = self.get_gcc_prefix(gccPath)
                    eachDict["gccPrefix"] = gccPrefix
                    outputPath = eachDict.get("outputPath","")
                    if dictNow.get("if64bit",1):
                        marchStr = " -march=rv64"
                        if dictNow.get("i",0):
                            marchStr+="i"
                        if dictNow.get("m",0):
                            marchStr+="m"
                        if dictNow.get("a",0):
                            marchStr+="a"
                        if dictNow.get("c",0):
                            marchStr+="c"
                        if dictNow.get("f",0):
                            marchStr+="f"
                        mabiStr = " -mabi=lp64 "
                    else:
                        marchStr = "-march=rv32"
                        if dictNow.get("i",0):
                            marchStr+="i"
                        if dictNow.get("m",0):
                            marchStr+="m"
                        if dictNow.get("a",0):
                            marchStr+="a"
                        if dictNow.get("c",0):
                            marchStr+="c"
                        if dictNow.get("f",0):
                            marchStr+="f"
                        mabiStr = " -mabi=ilp32 "
                    compilePrefixStr = gccPath+gccPrefix+marchStr+mabiStr
                    if os.path.exists(pathNow+"\\main.S") :
                        fileStr = pathNow+"\\main.S"
                    elif os.path.exists(pathNow+"\\main.c"):
                        fileStr = pathNow+"\\main.c"
                    elif os.path.exists(pathNow+"\\main.s"):
                        fileStr = pathNow+"\\main.s"
                    else :
                        fileStr = pathNow+"\\main.c"
                    compileStrList = []
                    compileStrList.append(compilePrefixStr+" -c "+fileStr+" -o "+outputPath+"\main.bin")
                    

                    #-march=rv32i -mabi=ilp32
                    #-march=rv64ia -mabi=lp64
                else :
                    self.do_make(pathNow)



    def do_make(self,path):
        pass

    def get_gcc_prefix(self,gccPath):
        #commandDict = [""]
        usefulFileList = []
        preFixNow = None
        for files in os.listdir(gccPath) :

            #print("get Prefix",files)
            if "objcopy.exe" in files:
                #print("get Prefix",files.replace("objcopy.exe",""))
                preFixNow = files.replace("objcopy.exe","")
                break
        return preFixNow


    def save_compile_settings(self,settingList):
        cfgDict = read_cfg(self.__project_cfg_path)
        cfgDict["comlipeSetting"] = settingList
        write_cfg(self.__project_cfg_path,cfgDict)
        logging.debug("workspace_cfg saved")

    def connect_signal(self):
        self.leftWidget.compileWidget.compileSignal.connect(self.do_compile_for_project)
        self.leftWidget.projectWidget.pushButton.clicked.connect(self.set_workspace_tree)
        self.actionnew.triggered.connect(lambda: self.addEditorWidget(fileDict=None))
        self.actionopen.triggered.connect(self.openFile)
        self.actionSaveAs.triggered.connect(lambda : self.saveAsFile(self.mdi.activeSubWindow()))
        self.actionsave.triggered.connect(self.saveFile)
        self.actionSelectWorkspace.triggered.connect(self.selectNewWorkspace)
        self.actionModules.toggled.connect(functools.partial(self.view_handler, "Modules"))
        self.actionOutputs.toggled.connect(functools.partial(self.view_handler, "Outputs"))
        self.actionNewCompile.triggered.connect(lambda : self.new_project_widget("compile"))
        self.actionNewSimulate.triggered.connect(lambda : self.new_project_widget("simulate"))
        self.treeWidget.itemDoubleClicked.connect(self.open_project_file)
        self.mdi.subWindowActivated.connect(self.current_editor_changed)
        self.simulateThread.updateTextOutput.connect(self.updateTextOutput)
        # .parent
        # setItem
    def update_workspace(self):
        #self.showNormal()
        logging.debug("updateLogic")
        self.initLogic()
        self.init_simulator()
        self.init_timer()
        self.untitledNum = 1
    def selectNewWorkspace(self):


        #workspaceSelector = SelectWorkspace()

        self.workspaceSelector.show()
        self.workspaceSelector.closeSignal.connect(self.initAll)
    def init_simulator(self):
        cfgDict = read_cfg(self.workspacePath + "./cfgPorjectList.evecfg")
        #cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
        #cfgDict = cfg.get_dict()
        self.simulateProjectList= cfgDict.get("simulate_projectPathList",[])
        self.iverilogPathDict = read_cfg(self.__simulator_cfg_path)
        self.iverilogPath = self.iverilogPathDict.get("iverilogPath","")
        self.simulateProjectList.reverse()
        simList = []
        self.topLevelDict = {}
        for each in self.simulateProjectList:
            simList.append(os.path.abspath(each))
        self.simulateTreeWidget.clear()
        self.leftWidget.simulateWidget.project_comboBox.clear()
        self.leftWidget.simulateWidget.project_comboBox.addItems(simList)
        #self.leftWidget.simulateWidget.project_comboBox.setItemText(0,"")
        self.leftWidget.simulateWidget.project_comboBox.setToolTip(self.leftWidget.simulateWidget.project_comboBox.currentText())
        self.leftWidget.simulateWidget.iverlogPath_lineEdit.setText(self.iverilogPath)
        #self.leftWidget.projectWidget.projectFile_treeWidget
        self.leftWidget.simulateWidget.selectProjectPath_pushButton.clicked.connect(lambda : self.simulator_project_path("project"))
        self.leftWidget.simulateWidget.selectIverilogPath_pushButton.clicked.connect(lambda : self.simulator_project_path("iverilog"))

        self.simulateTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 打开右键菜单的策略
        self.simulateTreeWidget.customContextMenuRequested.connect(self.sim_tree_right_click)  # 绑定事件

        self.leftWidget.simulateWidget.project_comboBox.currentIndexChanged.connect(self.update_sim_tree)
        self.leftWidget.simulateWidget.simulate_pushButton.clicked.connect(self.do_simulate)
        self.simulateTreeWidget.itemDoubleClicked.connect(self.open_project_file)
        self.leftWidget.simulateWidget.ProjectTreeWidget.pushButton.clicked.connect(self.update_sim_tree)
        self.currentProjectPath = self.leftWidget.simulateWidget.project_comboBox.currentText()
        if not self.currentProjectPath == "":
            projectManager = ProjectManage(self.currentProjectPath)
            projectTreeDict = projectManager.porject_dict
            #print(projectTreeDict)
            simulatorFileManager = SimulatorFileManager(self.currentProjectPath)
            simulatorFileDict = simulatorFileManager.simulateFileDict
            self.projectTreeDictList.append(projectTreeDict)
            # 创建工程树
            self.set_sim_project_tree(projectTreeDict,self.simulateTreeWidget,simulatorFileDict)
            self.simFileDict = simulatorFileDict
            simulatorInculdeDict = simulatorFileManager.includeFileList
            self.simIncludeDict = simulatorInculdeDict
    def project_tree_right_click(self,pos):
        nodeNow = self.treeWidget.itemAt(pos)
        #nodeNow = self.simulateTreeWidget.itemAt(pos)
        currentDict = nodeNow.dictNow
        if not (currentDict.get("ifSubmodule", 0)):
            if (currentDict.get("fileSuffix", "") == "v") or (currentDict.get("fileSuffix", "") == "sv"):
                popMenu = QMenu()
                #popMenu.addAction(QAction(u'set ' + currentDict.get("name", "") + ' as the top level ', self))
                #popMenu.addAction(QAction(u'create instance file : inst_' + currentDict.get("name", ""), self))
                popMenu.addAction(QAction(u'open file : ' + currentDict.get("name", ""), self))
                popMenu.addAction(QAction(u'delete file : ' + currentDict.get("name", ""), self))
                popMenu.triggered[QAction].connect(self.project_right_click_handler)
                popMenu.exec_(QCursor.pos())
            else:
                nameNow = currentDict.get("name",None)
                if nameNow:
                    popMenu = QMenu()
                    popMenu.addAction(QAction(u'delete current item: ' + nameNow, self))
                    popMenu.triggered[QAction].connect(self.project_right_click_handler)
                    popMenu.exec_(QCursor.pos())

            logging.debug(nodeNow.dictNow)
    def sim_tree_right_click(self,pos):
        #item = self.simulateTreeWidget.currentItem()

        nodeNow = self.simulateTreeWidget.itemAt(pos)
        currentDict = nodeNow.dictNow
        if not (currentDict.get("ifSubmodule",0)):
            if (currentDict.get("fileSuffix","") == "v")or (currentDict.get("fileSuffix","") == "sv"):
                popMenu = QMenu()
                popMenu.addAction(QAction(u'set '+currentDict.get("name","")+' as the top level ', self))
                popMenu.addAction(QAction(u'create instance file : inst_'+currentDict.get("name",""), self))
                popMenu.addAction(QAction(u'open file : ' + currentDict.get("name", ""), self))
                popMenu.addAction(QAction(u'delete file : ' + currentDict.get("name", ""), self))
                popMenu.triggered[QAction].connect(self.simulate_right_click_handler)
                popMenu.exec_(QCursor.pos())
            else :
                popMenu = QMenu()
                popMenu.addAction(QAction(u'delete current item: ' + currentDict.get("name", ""), self))
                popMenu.triggered[QAction].connect(self.simulate_right_click_handler)
                popMenu.exec_(QCursor.pos())


            logging.debug(nodeNow.dictNow)
    def project_right_click_handler(self,q):
        treeNode = self.treeWidget.currentItem()
        currentDict = treeNode.dictNow

        textNow = q.text()
        if "create instance file" in textNow:
            pre = os.path.dirname(currentDict.get("fullPath", ""))
            nameNow = currentDict.get("name", "")
            newPath = pre + "/inst_" + nameNow
            c = CreateInsance()
            c.CreateInsance(currentDict.get("fullPath", ""), newPath)
            if os.path.exists(newPath):
                projectManager = ProjectManage(self.currentProjectPath)
                projectTreeDict = projectManager.porject_dict
                simulatorFileManager = SimulatorFileManager(self.currentProjectPath)
                simulatorFileDict = simulatorFileManager.simulateFileDict

                self.projectTreeDictList.append(projectTreeDict)
                # 创建工程树
                self.set_sim_project_tree(projectTreeDict, self.simulateTreeWidget, simulatorFileDict)
                self.simFileDict = simulatorFileDict
                simulatorInculdeDict = simulatorFileManager.includeFileList
                self.simIncludeDict = simulatorInculdeDict
                # self.addEditorWidget()
            pass  # logging.debug("a")
        elif "as the top level" in textNow:
            topNode = currentDict.get("currentNode", None)
            if topNode:
                if not self.topLevelDict == {}:
                    lastTop = self.topLevelDict.get("currentNode", None)
                    try:
                        lastTop.setBackgroundColor(0, QtGui.QColor('white'))
                    except:
                        pass
                topNode.setBackgroundColor(0, QtGui.QColor('blue'))
                self.topLevelDict = currentDict
            else:
                QMessageBox.warning(self, "EveIDE_LIGHT -- SIMULATE Error",
                                    "UNKNOWN")
            # logging.debug("b")
        elif "open file" in textNow:
            self.addEditorWidget(currentDict)
        elif "delete " in textNow:
            fullPath = os.path.abspath(currentDict.get("fullPath", ""))
            choose = QMessageBox.warning(self, "EveIDE_LIGHT -- FILE warning",
                                         "Sure to delete {0} ? ".format(fullPath),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose == QMessageBox.Yes:
                try:
                    os.remove(fullPath)
                except:
                    os.removedirs(fullPath)
                self.check_file()
                self.update_sim_tree()

    def simulate_right_click_handler(self,q):
        treeNode = self.simulateTreeWidget.currentItem()
        currentDict = treeNode.dictNow

        textNow = q.text()
        if "create instance file" in textNow :
            pre = os.path.dirname(currentDict.get("fullPath",""))
            nameNow = currentDict.get("name","")
            newPath = pre+"/inst_"+nameNow
            c = CreateInsance()
            c.CreateInsance(currentDict.get("fullPath",""),newPath)
            if os.path.exists(newPath) :

                projectManager = ProjectManage(self.currentProjectPath)
                projectTreeDict = projectManager.porject_dict
                simulatorFileManager = SimulatorFileManager(self.currentProjectPath)
                simulatorFileDict = simulatorFileManager.simulateFileDict

                self.projectTreeDictList.append(projectTreeDict)
                # 创建工程树
                self.set_sim_project_tree(projectTreeDict, self.simulateTreeWidget, simulatorFileDict)
                self.simFileDict = simulatorFileDict
                simulatorInculdeDict = simulatorFileManager.includeFileList
                self.simIncludeDict = simulatorInculdeDict
                #self.addEditorWidget()
            pass #logging.debug("a")
        elif "as the top level" in textNow:
            topNode = currentDict.get("currentNode",None)
            if topNode:
                if not self.topLevelDict == {}:
                    lastTop = self.topLevelDict.get("currentNode",None)
                    try:
                        lastTop.setBackgroundColor(0, QtGui.QColor('white'))
                    except:
                        pass
                topNode.setBackgroundColor(0, QtGui.QColor('blue'))
                self.topLevelDict = currentDict
            else :
                QMessageBox.warning(self, "EveIDE_LIGHT -- SIMULATE Error",
                                    "UNKNOWN")
            #logging.debug("b")
        elif "open file" in textNow:
            self.addEditorWidget(currentDict)
        elif "delete " in textNow:
            fullPath = os.path.abspath(currentDict.get("fullPath",""))
            choose = QMessageBox.warning(self, "EveIDE_LIGHT -- FILE warning",
                                         "Sure to delete {0} ? ".format(fullPath),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose == QMessageBox.Yes:
                try:
                    os.remove(fullPath)
                except:
                    os.removedirs(fullPath)
                self.check_file()
                self.update_sim_tree()

    def open_simulate_file(self,currentTree):
        logging.debug(currentTree)
    def update_sim_tree(self):

        self.leftWidget.simulateWidget.project_comboBox.setToolTip(self.leftWidget.simulateWidget.project_comboBox.currentText())
        self.currentProjectPath = self.leftWidget.simulateWidget.project_comboBox.currentText()
        projectManager = ProjectManage(self.currentProjectPath)
        projectTreeDict = projectManager.porject_dict
        simulatorFileManager = SimulatorFileManager(self.currentProjectPath)
        simulatorFileDict = simulatorFileManager.simulateFileDict

        self.projectTreeDictList.append(projectTreeDict)
        #logging.debug(str(projectTreeDict).replace("\'", "\""))
        # 创建工程树
        self.simulateTreeWidget.clear()
        self.set_sim_project_tree(projectTreeDict,self.simulateTreeWidget,simulatorFileDict)
        self.simFileDict = simulatorFileDict
        simulatorInculdeDict = simulatorFileManager.includeFileList
        self.simIncludeDict = simulatorInculdeDict
    def simulator_project_path(self,which):
        if which == "project":
            pathNow = os.path.relpath(QFileDialog.getExistingDirectory(None, "Choose Simulate Path", self.workspacePath))
            if not pathNow is None:
                self.simulateProjectList.insert(0,os.path.relpath(pathNow))
                #self.leftWidget.simulateWidget.project_comboBox.addItems(self.simulateProjectList)
                cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
                cfgDict = cfg.get_dict()
                self.simulateProjectList.reverse()
                cfgDict["simulate_projectPathList"] =self.simulateProjectList
                cfg.write_dict(cfgDict)
                self.leftWidget.simulateWidget.project_comboBox.clear()
                self.simulateProjectList.reverse()
                simList = []
                self.topLevelDict = {}
                for each in self.simulateProjectList:
                    simList.append(os.path.abspath(each))
                self.leftWidget.simulateWidget.project_comboBox.addItems(simList)

        elif which == "iverilog":
            pathNow = os.path.relpath(QFileDialog.getExistingDirectory(None, "Choose iverilog Path", self.workspacePath))
            if not pathNow is None:
                self.leftWidget.simulateWidget.iverlogPath_lineEdit.setText(pathNow)

    def do_simulate(self):
        pathNow = self.leftWidget.simulateWidget.iverlogPath_lineEdit.text()
        self.iverilogPathDict["iverilogPath"] = pathNow
        write_cfg(self.__simulator_cfg_path,self.iverilogPathDict)
        dictToSim = self.simFileDict

        if  self.topLevelDict =={}:
            QMessageBox.warning(self, "EveIDE_LIGHT -- SIMULATE Error",
                                "Please Set the Top Level First(Right Click on the file)")
        else:
            logging.debug("simulate")
            iverilogPath = self.leftWidget.simulateWidget.iverlogPath_lineEdit.text()

            if os.path.exists(iverilogPath+"/gtkwave"):
                g = GetSimDumpFile()
                #logging.debug(self.topLevelDict.get("fullPath"))
                dumpFile = g.getDumpFile(self.topLevelDict.get("fullPath"))
                dumpFileInitPath = os.path.basename(dumpFile)
                dumpFilePath = dumpFile
                if not dumpFile == "":
                    '''第一种方式自动找依赖'''

                    simulateSettingDict = {"includeList":self.simIncludeDict,"projectDict":dictToSim,"topLevel":self.topLevelDict,"iverilogPath":iverilogPath,"dumpFile":dumpFile,"projectPath":self.leftWidget.simulateWidget.project_comboBox.currentText()}
                    simulateStrDict = self.leftWidget.simulateWidget.do_simulate(simulateSettingDict)#得到iverilog的三个命令
                    #print(simulateStrDict)
                    iverilogList = [simulateStrDict.get("iverilog"),simulateStrDict.get("vvp"),simulateStrDict.get("gtkwave")]#
                    self.simulateThread.init_thread(iverilogList,dumpFileInitPath,dumpFilePath)
                    self.TextOutput.clear()
                    self.simulateThread.start()




                else :
                    QMessageBox.warning(self, "EveIDE_LIGHT -- SIMULATE Error",
                                        "top level file error , make sure you have add \ninitial\nbegin\n$dumpfile(\"xx.vcd\");\n$dumpvars(0,{0});\nend".format((self.topLevelDict.get("name","").split(".")[0])))

            else :
                QMessageBox.warning(self, "EveIDE_LIGHT -- SIMULATE Error",
                                    "Incorrect iverilog path!\n (gtkwave should be in the path)")
    def add_new_project(self,pathNow,type):
        if not pathNow == "":
            cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
            cfgDict = cfg.get_dict()
            if type == "compile":
                cfgDict["compile_projectPathList"].append(os.path.relpath(pathNow))
                settingList = self.clear_unused_compile_project(cfgDict.get("compileSetting",[]),cfgDict.get("compile_projectPathList",[]))
                cfgDict["compileSetting"] = settingList
                cfg.write_dict(cfgDict)
                if not os.path.exists(pathNow + "\\main.S"):
                    with open(pathNow + "\\main.S", "w+", newline='')as r:
                        strToWrite = "/***Generate by EveIDE_LIGHT at " + datetime.datetime.now().strftime(
                            '%Y-%m-%d %H:%M:%S'+"***/")
                        strToWrite += "\n/****************" + __version__ + "******************/"
                        r.write(strToWrite)
                self.leftWidget.compileWidget.addSettingsDictList(settingList)
                self.set_workspace_tree()


            elif type == "simulate":
                cfgDict["simulate_projectPathList"].append(os.path.relpath(pathNow))
                cfg.write_dict(cfgDict)
                self.init_simulator()

            self.set_workspace_tree()

    def new_project_widget(self,type):
        newProjectWidget = NewProjectWidget(self.workspacePath,type)
        newProjectWidget.show()
        newProjectWidget.closeSignal.connect(self.add_new_project)
        #newProjectWidget.setWindowFlags(Qt.FramelessWindowHint)


    def view_handler(self, which, state):
        # logging.debug(state)
        if which == "Modules":
            if state:
                self.LeftDockWidget.show()
            else:
                self.LeftDockWidget.close()

        if which == "Outputs":
            if state:
                self.OutputDock.show()
            else:
                self.OutputDock.close()

        # self.timerUpdateUi = QTimer()
        # self.timerUpdateUi.timeout.connect(self.updateUI)
        # self.timerUpdateUi.start(100)

    def open_project_file(self, currentTree):
        #logging.debug("currentTree :"+str(currentTree))
        currentTreeDict = currentTree.dictNow
        #logging.debug("currentTree :"+str(currentTreeDict))
        if currentTreeDict.get("type", "") == "file":
            self.addEditorWidget(currentTreeDict)

    def openFile(self):
        #editorNow = self.mdi.currentSubWindow().widget()
        try:
            filename, _buff = QFileDialog.getOpenFileName(self, 'SaveAs',self.workspacePath, 'All (*.*)')
        except Exception as e:
            logging.debug(e)
            filename, _buff = QFileDialog.getOpenFileName(self, 'SaveAs', './', 'All (*.*)')
        if filename:
            fileDict = {
                "fullPath":os.path.relpath(filename),
                "name":os.path.basename(filename),
                "type":"file",
                "fileSuffix":filename.split(".")[-1],
                "currentNode":None,
            }
            self.addEditorWidget(fileDict)
        valueNow = ""
        # editorNow.get_value(valueNow)
        #logging.debug(valueNow)
    @property
    def check_simulate_projcet(self):
        cfgPath = self.workspacePath + "./cfgPorjectList.evecfg"
        if os.path.exists(cfgPath):
            cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
            cfgDict = cfg.get_dict()
            #cfgDict = read_cfg(self.__project_cfg_path)
            projectList = cfgDict.get("simulate_projectPathList","")
            formatList = []
            for pro in projectList:
                if pro not in formatList:
                    formatList.append(pro)
            projectList = formatList
            cfgDict["simulate_projectPathList"] = projectList
            for eachProject in projectList:
                if not os.path.exists(eachProject):
                    logging.debug("project :" + eachProject + " is not exist")
                    cfgDict["simulate_projectPathList"].remove(eachProject)
                else:
                    logging.debug("find project :" + eachProject)
            # cfg.write_dict(cfgDict)
            write_cfg(cfgPath, cfgDict)
            return projectList
        else:
            logging.debug("without workspacecfg , create new one")
            with open(cfgPath, "w+"):
                pass
            d = {"compile_projectPathList": [], "simulate_projectPathList": []}

            workspacecfg = cfgRead(self.workspacePath)
            workspacecfg.write_dict(d)
            return []
    @property
    def check_compile_projects(self):
        cfgPath = self.workspacePath + "./cfgPorjectList.evecfg"
        if os.path.exists(cfgPath):
            try :
                cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
                cfgDict = cfg.get_dict()
                #cfgDict = read_cfg(self.__project_cfg_path)
                projectList = cfgDict.get("compile_projectPathList","")
                formatList = []
                for pro in projectList:
                    if pro not in formatList:
                        formatList.append(pro)
                projectList = formatList
                cfgDict["compile_projectPathList"] = projectList
                for eachProject in projectList:
                    if not os.path.exists(eachProject):
                        logging.debug("project :" + eachProject + " is not exist")
                        cfgDict["compile_projectPathList"].remove(eachProject)
                    else:
                        logging.debug("find project :" + eachProject)
                # cfg.write_dict(cfgDict)
                write_cfg(cfgPath, cfgDict)
                return projectList
            except Exception as e:
                logging.debug(e)
                cfg = cfgRead(self.workspacePath + "./cfgPorjectList.evecfg")
                ifCreate = QMessageBox.warning(self, "EveIDE_LIGHT -- OPEN Error",
                                    "Failed to read workspace config {0}\ncreate a new one for this workspace ? ".format(
                                        os.path.abspath(cfgPath)))

                d = {"compile_projectPathList": [], "simulate_projectPathList": []}
                cfg.write_dict(d)
                return []



        else:
            logging.debug("without workspacecfg , create new one")
            ifCreate = QMessageBox.warning(self, "EveIDE_LIGHT -- OPEN Error",
                                           "Failed to read workspace config {0}\ncreate a new one for this workspace ? ".format(
                                               os.path.abspath(cfgPath)))
            with open(cfgPath, "w+"):
                pass
            d = {"compile_projectPathList":[],"simulate_projectPathList":[]}

            workspacecfg = cfgRead(self.workspacePath)
            workspacecfg.write_dict(d)

            return []

    def saveFile(self):
        print("intoSaveFile")
        activeWindow = self.mdi.activeSubWindow()
        editor = activeWindow.widget()
        editorDict = editor.dictNow
        print(editorDict)
        if activeWindow:
            editor = activeWindow.widget()
            editorDict = editor.dictNow
            savePath = editorDict.get("fullPath", None)
            print("savePath",savePath)
            editor.dictNow["openTime"] = int(time.time())
            #logging.debug(editorDict)fileDict["openTime"] = int(time.time())
            print("save")
            if savePath :
                strToSave = editor.bridge.value
                try:
                    print("intosave")
                    '''#print(strToSave)
                    fh = QFile(savePath)
                    if not fh.open(QtCore.QIODevice.WriteOnly):
                        raise IOError(str(fh.errorString()))
                    stream = QtCore.QTextStream(fh)
                    stream.setCodec("UTF-8")
                    stream << strToSave'''

                    with open(savePath, "w+",encoding="utf-8",newline='') as saveFile:
                        saveFile.write(strToSave)
                        #print(strToSave)
                        editor.setWindowTitle(activeWindow.windowTitle().replace("*", ""))
                        editor.finishInit = 1


                except Exception as e:
                    logging.debug(e)
                    QMessageBox.warning(self, "EveIDE_LIGHT -- SAVE Error",
                                        "Failed to save {0}".format(savePath))
                '''finally:
                    if fh is not None:
                        fh.close()'''
            else:
                self.saveAsFile(activeWindow)

        #logging.debug("saveFile")

    def saveAsFile(self,windowNow):
        try:
            filename, _buff = QFileDialog.getSaveFileName(self, 'SaveAs',self.workspacePath, 'All (*.*)')
        except Exception as e:
            logging.debug(e)
            filename, _buff = QFileDialog.getSaveFileName(self, 'SaveAs', './', 'All (*.*)')
        if filename:
            fileDict = {
                "fullPath":os.path.relpath(filename),
                "name":os.path.basename(filename),
                "type":"file",
                "fileSuffix":filename.split(".")[-1],
                "currentNode":None,
            }
            editor = windowNow.widget()
            editor.dictNow = fileDict

            if editor.dictNow.get("newFile",None) is not None:
                editor.dictNow["newFile"] = 0
            editor.setWindowTitle(fileDict.get("name",""))
            with open(filename,"w+"):
                pass
            self.mdi.setActiveSubWindow(windowNow)
            self.saveFile()
            #self.saveFile()
            #我也不知道为什么没法调用savefile，睡觉了小命要紧
            #bug？？？

    def updateUI(self):
        pass

    def testUi(self):
        self.setupUi(self)
        editorNow = EditorWidget()
        self.LeftDockWidget = QDockWidget("Modules", self)
        self.LeftDockWidget.setWidget(editorNow)
        self.addDockWidget(Qt.RightDockWidgetArea, self.LeftDockWidget)

    def get_workspace_path(self):
        pass

    def set_workspace_tree(self):
        self.treeWidget.clear()
        self.projectList = self.check_compile_projects
        for eachProject in self.projectList:
            print("creatingTree for "+str(eachProject))
            projectManager = ProjectManage(eachProject)
            projectTreeDict = projectManager.porject_dict
            self.projectTreeDictList.append(projectTreeDict)
            logging.debug(str(projectTreeDict).replace("\'", "\""))
            # 创建工程树
            self.set_project_tree(projectTreeDict,self.treeWidget)


    def set_sim_project_tree(self,projectTreeDict,treeNow,moduleDict):
        self.simTreeNodeFileList = []
        treeNow.clear()
        treeNow.setHeaderLabel("Workspace now :" + os.path.basename(self.workspacePath))
        treeNow.setColumnCount(1)
        # logging.debug("now tree:"+str(projectTreeDict))
        #
        #print(projectTreeDict)
        nodeName = projectTreeDict.get("node", "")
        nodeDirs = projectTreeDict.get("dirs", "")
        filesNow = projectTreeDict.get("files", "")
        rootNode = QTreeWidgetItem(treeNow)
        rootNode.setText(0, nodeName)
        rootNode.dictNow = projectTreeDict
        print("project tree dict"+str(projectTreeDict))
        rootNode.setIcon(0, self.dirIcon)
        # rootNode.setIcon()
        for eachFile in filesNow:
            currentName =eachFile.get("name", None)
            if currentName:
                # logging.debug("rootFiles:"+str(eachFile))
                childNode = QTreeWidgetItem()
                childNode.dictNow = eachFile
                childNode.setText(0, currentName)
                childNode.dictNow["currentNode"] = childNode
                childNode.dictNow["simulate"] = 1
                self.simTreeNodeFileList.append(eachFile)
                rootNode.addChild(childNode)
                #logging.debug("childNode:" + str(childNode))
                self.set_file_icon(childNode, childNode.dictNow)
                for eachDict in moduleDict :
                    if eachDict.get("name","") == currentName :
                        if not eachDict.get("module",[]) == [] :
                            for eachModuleDict in eachDict.get("module",[]) :
                                childModuleNode = QTreeWidgetItem()
                                di = eachFile
                                #di["ifSubmodule"] = 1
                                childModuleNode.dictNow = di
                                childModuleNode.setText(0,eachModuleDict.get("moduleName",""))
                                childNode.addChild(childModuleNode)
                                childModuleNode.setIcon(0,self.moduleIcon)
                                if not eachModuleDict.get("submoduleName",[]) == [] :
                                    for eachSubmoduleName in eachModuleDict.get("submoduleName", []):
                                        nameN = eachSubmoduleName.get("name","")
                                        di = eachSubmoduleName.get("submoduleFileDict", {})
                                        if di == {}:
                                            di = eachFile
                                        childSubmoduelNode = QTreeWidgetItem()
                                        di["ifSubmodule"] = 1
                                        childSubmoduelNode.dictNow = di
                                        childSubmoduelNode.setText(0,nameN)
                                        childModuleNode.addChild(childSubmoduelNode)
                                        childSubmoduelNode.setIcon(0,self.submoduleIcon)


            # childNode.setIcon()
        for eachDir in nodeDirs:
            #print(eachDir)
            childNode = QTreeWidgetItem()
            dirDict = eachDir.get("child", None)
            if dirDict:
                # logging.debug("dirDict"+str(dirDict).replace("\'","\""))
                childNode.setText(0, eachDir.get("name", None))
                if childNode:
                    rootNode.addChild(childNode)
                    childNode.dictNow = eachDir
                    childNode.dictNow["currentNode"] = childNode
                    #print(childNode)
                    #print(dirDict)
                    #(moduleDict)
                    self.set_sim_child_tree(childNode, dirDict,moduleDict)
                    childNode.setIcon(0, self.dirIcon)
        checkPathList = []
        subWindowList = self.mdi.subWindowList()
        for eachWindow in subWindowList:
            widgetNow = eachWindow.widget()
            dictNow = widgetNow.dictNow
            # logging.debug(dictNow)
            fullPath = dictNow.get("fullPath", None)
            if not fullPath is None:
                for eachFile in self.simTreeNodeFileList :
                    if eachFile.get("fullPath","") == fullPath :
                        #logging.debug("::::...getSame",fullPath)
                        widgetNow.dictNow["currentNode"] = eachFile.get("currentNode")
                        treeNow.setCurrentItem(eachFile.get("currentNode"))



    def set_sim_child_tree(self, rootNode, childDict,moduleDict):
        nodeName = childDict.get("node", "")
        dirsDict = childDict.get("dirs", "")
        filesNow = childDict.get("files", "")
        for eachFile in filesNow:
            currentName = eachFile.get("name", "")
            # logging.debug("rootFiles:"+str(eachFile))
            childNode = QTreeWidgetItem()
            childNode.dictNow = eachFile
            childNode.dictNow["currentNode"] = childNode
            childNode.dictNow["simulate"] = 1
            childNode.setText(0, currentName)
            rootNode.addChild(childNode)
            self.simTreeNodeFileList.append(eachFile)
            self.set_file_icon(childNode,childNode.dictNow)
            for eachDict in moduleDict :
                if eachDict.get("name","") == currentName :
                    if not eachDict.get("module",[]) == [] :
                        for eachModuleDict in eachDict.get("module",[]) :
                            childModuleNode = QTreeWidgetItem()
                            di = eachFile
                            #di["ifSubmodule"] = 1
                            childModuleNode.dictNow = di
                            childModuleNode.setText(0,eachModuleDict.get("moduleName",""))
                            childNode.addChild(childModuleNode)
                            childModuleNode.setIcon(0, self.moduleIcon)
                            if not eachModuleDict.get("submoduleName", []) == []:
                                for eachSubmoduleName in eachModuleDict.get("submoduleName", []):
                                    nameN = eachSubmoduleName.get("name", "")
                                    di = eachSubmoduleName.get("submoduleFileDict", {})
                                    if di == {}:
                                        di = eachFile
                                    di["ifSubmodule"] = 1
                                    childSubmoduelNode = QTreeWidgetItem()
                                    childSubmoduelNode.dictNow = di
                                    childSubmoduelNode.setText(0, nameN)
                                    childModuleNode.addChild(childSubmoduelNode)
                                    childSubmoduelNode.setIcon(0, self.submoduleIcon)

        for eachDir in dirsDict:
            childNode = QTreeWidgetItem()
            dirDict = eachDir.get("child", "")
            # logging.debug("dirDict"+str(dirDict).replace("\'","\""))
            childNode.setText(0, eachDir.get("name", ""))
            rootNode.addChild(childNode)
            childNode.dictNow = eachDir
            childNode.dictNow["currentNode"] = childNode
            self.set_sim_child_tree(childNode, dirDict,moduleDict)
            childNode.setIcon(0,self.dirIcon)
    def set_project_tree(self, projectTreeDict,treeNow):
        self.comTreeNodeFileList = []
        #treeNow.setHeaderLabel("Workspace now :" + os.path.basename(self.workspacePath))
        treeNow.setHeaderLabel("")
        treeNow.setColumnCount(1)
        # logging.debug("now tree:"+str(projectTreeDict))
        nodeName = projectTreeDict.get("node", None)
        nodeDirs = projectTreeDict.get("dirs", "")
        filesNow = projectTreeDict.get("files", "")
        rootNode = QTreeWidgetItem(treeNow)
        rootNode.setText(0, nodeName)
        rootNode.dictNow = projectTreeDict
        rootNode.setIcon(0,self.dirIcon)
        # rootNode.setIcon()
        if  nodeName:
            for eachFile in filesNow:
                # logging.debug("rootFiles:"+str(eachFile))
                childNode = QTreeWidgetItem()

                childNode.dictNow = eachFile
                fullName = eachFile.get("fullPath",None)

                childNode.setText(0, eachFile.get("name", ""))
                childNode.dictNow["currentNode"] = childNode
                childNode.dictNow["compile"] = 1
                self.comTreeNodeFileList.append(eachFile)
                rootNode.addChild(childNode)
                logging.debug("childNode:"+str(childNode))
                self.set_file_icon(childNode,childNode.dictNow)
                functionList = []
                if os.path.exists(fullName) :
                    if eachFile.get("fileSuffix") == "c":
                        CFunctionSelector = GetFunctionInC(fullName)
                        functionList = CFunctionSelector.fuctionList

                for eachFunction in functionList:
                    functionNode = QTreeWidgetItem()
                    functionNode.dictNow = eachFile
                    functionNode.setText(0,eachFunction)
                    functionNode.setIcon(0,self.functionIcon)
                    childNode.addChild(functionNode)



                # childNode.setIcon()
            for eachDir in nodeDirs:
                childNode = QTreeWidgetItem()
                dirDict = eachDir.get("child", "")
                # logging.debug("dirDict"+str(dirDict).replace("\'","\""))
                childNode.setText(0, eachDir.get("name", ""))
                rootNode.addChild(childNode)
                childNode.dictNow = eachDir
                childNode.dictNow["currentNode"] = childNode
                self.set_child_tree(childNode, dirDict)
                childNode.setIcon(0,self.dirIcon)
            subWindowList = self.mdi.subWindowList()#在每次tree更新后能保证window 的currentnode更新
            for eachWindow in subWindowList:
                widgetNow = eachWindow.widget()
                dictNow = widgetNow.dictNow
                # logging.debug(dictNow)
                fullPath = dictNow.get("fullPath", None)
                if not fullPath is None:
                    for eachFile in self.comTreeNodeFileList :
                        if eachFile.get("fullPath","") == fullPath :
                            #logging.debug("::::...change",fullPath)
                            widgetNow.dictNow["currentNode"] = eachFile.get("currentNode")
                            treeNow.setCurrentItem(eachFile.get("currentNode"))


            # for eachChild in

    def set_file_icon(self,nodeNow,nodeDict):
        fileSuffix = nodeDict.get("fileSuffix","")
        #logging.debug(fileSuffix)
        if fileSuffix=="c" or fileSuffix == "cpp":
            nodeNow.setIcon(0,self.cLanguageIcon)
        elif fileSuffix == "h":
            nodeNow.setIcon(0,self.headerIcon)
        elif fileSuffix == "v" or fileSuffix == "sv":
            nodeNow.setIcon(0,self.verilogIcon)
        elif fileSuffix == "bin" or fileSuffix == "coe" or fileSuffix == "mif" or fileSuffix == "o":
            nodeNow.setIcon(0,self.binIcon)
        elif fileSuffix == "mk" :
            nodeNow.setIcon(0,self.makefileIcon)
        elif fileSuffix == "S" or fileSuffix == "s":
            nodeNow.setIcon(0,self.assembleIcon)


    def set_child_tree(self, rootNode, childDict):
        nodeName = childDict.get("node", "")
        dirsDict = childDict.get("dirs", "")
        filesNow = childDict.get("files", "")
        for eachFile in filesNow:
            # logging.debug("rootFiles:"+str(eachFile))
            childNode = QTreeWidgetItem()
            childNode.dictNow = eachFile
            childNode.dictNow["currentNode"] = childNode
            childNode.dictNow["compile"]  = 1
            childNode.setText(0, eachFile.get("name", ""))
            self.comTreeNodeFileList.append(eachFile)
            rootNode.addChild(childNode)
            self.set_file_icon(childNode,childNode.dictNow)
            fullName = eachFile.get("fullPath", None)
            functionList = []
            if os.path.exists(fullName) :
                if eachFile.get("fileSuffix") == "c":
                    CFunctionSelector = GetFunctionInC(fullName)
                    functionList = CFunctionSelector.fuctionList
            print("functionList:"+str(functionList))
            for eachFunction in functionList:
                functionNode = QTreeWidgetItem()
                functionNode.dictNow = eachFile
                functionNode.setText(0,eachFunction)
                functionNode.setIcon(0,self.functionIcon)
                childNode.addChild(functionNode)


        for eachDir in dirsDict:
            childNode = QTreeWidgetItem()
            dirDict = eachDir.get("child", "")
            # logging.debug("dirDict"+str(dirDict).replace("\'","\""))
            childNode.setText(0, eachDir.get("name", ""))
            rootNode.addChild(childNode)
            childNode.dictNow = eachDir
            childNode.dictNow["currentNode"] = childNode
            self.set_child_tree(childNode, dirDict)
            childNode.setIcon(0,self.dirIcon)

        pass

    def current_editor_changed(self, win):
        # logging.debug(win)
        moduleNow = self.leftWidget.currentModule
        moduleName = moduleNow.name
        logging.debug(moduleName)

        activeWindow = self.mdi.activeSubWindow()
        if activeWindow:
            currentEditor = activeWindow.widget()
            currentDict = currentEditor.dictNow
            if currentDict.get("compile",0):
                try:
                    self.treeWidget.setCurrentItem(currentDict.get("currentNode", None))
                except Exception as e:
                    logging.debug(e)
            elif currentDict.get("simulate",0):
                try:
                    self.simulateTreeWidget.setCurrentItem(currentDict.get("currentNode", None))
                except Exception as e:
                    logging.debug(e)
            # logging.debug(currentDict)


            # logging.debug(activeWindow.titleNow)
    def initIcon(self):
        self.dirIcon = QIcon()
        self.dirIcon.addFile(u":/pic/dir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.headerIcon = QIcon()
        self.headerIcon.addFile(u":/pic/header.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cLanguageIcon = QIcon()
        self.cLanguageIcon.addFile(u":/pic/cLanguage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.makefileIcon = QIcon()
        self.makefileIcon.addFile(u":/pic/makefile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verilogIcon = QIcon()

        self.verilogIcon.addFile(u":/pic/verilog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.binIcon = QIcon()
        self.binIcon.addFile(u":/pic/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moduleIcon = QIcon()
        self.moduleIcon.addFile(u":/pic/module.png", QSize(), QIcon.Normal, QIcon.Off)
        self.submoduleIcon = QIcon()
        self.submoduleIcon.addFile(u":/pic/submodule.png", QSize(), QIcon.Normal, QIcon.Off)
        self.functionIcon = QIcon()
        self.functionIcon.addFile(u":/pic/function.png",QSize(), QIcon.Normal, QIcon.Off)
        self.assembleIcon = QIcon()
        self.assembleIcon.addFile(u":/pic/asm.png",QSize(), QIcon.Normal, QIcon.Off)


    def initUi(self):
        self.setupUi(self)
        self.initIcon()
        self.leftWidget = LeftModuleWidget()
        self.leftWidget.setMinimumSize(180, 600)
        self.mdi = QMdiArea()
        self.mdi.setViewMode(QMdiArea.TabbedView)
        self.mdi.setTabsClosable(1)
        self.setWindowTitle("EveIDE_LIGHT")
        self.mdi.setTabsMovable(1)
        self.LeftDockWidget = QDockWidget("Modules", self)
        self.LeftDockWidget.setWidget(self.leftWidget)
        # self.RightDockWidget = QDockWidget("Values",self)
        # self.RightDockWidget.resize(150,150)
        # self.RifghtDockWidget.setWidget(self.leftWidget)
        self.TextOutput = OutputWidget(self)  # 内置于信息输出视图
        self.TextOutput.setReadOnly(True)  # 仅作为信息输出，设置“只读”属性
        self.OutputDock = QDockWidget("Output", self)
        # self.OutputDock.setMinimumSize(600,150)
        self.OutputDock.setWidget(self.TextOutput)

        self.TextOutput.setText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
+" EveIDE_LIGHT with monaco editor")
        splitter1 = QSplitter(Qt.Vertical)
        # editorNow = EditorWidget()
        splitter1.addWidget(self.mdi)  # 多文档视图占布局右上
        splitter1.addWidget(self.OutputDock)  # 信息输出视图占布局右下
        self.addDockWidget(Qt.LeftDockWidgetArea, self.LeftDockWidget)  # 工程视图占布局左边
        # self.addDockWidget(Qt.RightDockWidgetArea,self.RightDockWidget)
        self.setCentralWidget(splitter1)

    def view_dock_closeEvent(self):  # 当dock关闭时触发
        self.OutputDock.closeEvent = self.dock_output_close
        self.LeftDockWidget.closeEvent = self.dock_LeftDockWidget_close

    def dock_output_close(self, p):
        # logging.debug(p)
        self.actionOutputs.setChecked(0)

    def dock_LeftDockWidget_close(self, p):
        # logging.debug(p)
        self.actionModules.setChecked(0)

        """
        自定义ui
        """
        # self.set_project_tree()
        '''self.midEditorTabWidget = QTabWidget()
        self.sub = QMdiSubWindow()
        self.sub.setWidget(self.midEditorTabWidget)
        self.mdi.addSubWindow(self.sub)
        self.sub.showMaximized()
        self.sub.setWindowFlags(Qt.FramelessWindowHint)'''

    def addEditorWidget(self, fileDict=None):

        # fileNameNow = fileName.replace("\\","/")
        # if fileName == "untitled":
        # fileNameNow = "untitled-"+str(self.untitledNum)
        # self.untitledNum+=1
        # else:
        # pass
        # logging.debug("OpeningFile:"+fileName)
        logging.debug(fileDict)
        if fileDict == None:
            fileNameNow = "untitled-" + str(self.untitledNum)
            self.untitledNum += 1
            fileDict = {'fullPath': None, 'name': fileNameNow, 'type': 'file', 'fileSuffix': None,'newFile':1}
        else:
            fileNameNow = fileDict.get("name", "")
        fileDict["openTime"] = int(time.time())
        subWindowList = self.mdi.subWindowList()
        fileOpened = 0
        # 检查是否已经打开
        for eachWindow in subWindowList:
            editor = eachWindow.widget()
            if editor.dictNow.get("fullPath", "") == fileDict.get("fullPath", ""):
                fileOpened = 1
                self.mdi.setActiveSubWindow(eachWindow)

        if not fileOpened:
            try:

                editorNow = EditorWidget()
                editorNow.dictNow = fileDict
                logging.debug("editor open file dict :"+str(fileDict))
                # self.midEditorTabWidget.addTab(editorNow,fileNameNow)
                self.mdi.addSubWindow(editorNow)
                editorNow.titleNow = fileNameNow
                editorNow.bridge.valueChanged.connect(lambda: self.editor_value_change_handler(editorNow))
                editorNow.setWindowTitle(fileNameNow)
                # logging.debug(self.mdi.activeSubWindow())
                fullPath = fileDict.get("fullPath", None)
                code = ""
                if not fullPath is None:
                    with open(fullPath, "r",encoding="utf-8") as openFile:
                        code = openFile.read()
                        # logging.debug("\""+code+"\"")
                editorNow.add_codes(code)
                suffixNow = fileDict.get("fileSuffix","")
                if suffixNow== "c" or suffixNow == "cpp" :
                    editorNow.set_language("c")

                elif suffixNow== "v" or suffixNow == "sv" :
                    editorNow.set_language("verilog")
                elif suffixNow== "py" :
                    editorNow.set_language("python")
                elif suffixNow == "asm" or suffixNow == "S":
                    editorNow.set_language("mips")


                editorNow.show()

                # editorNow.add_change_handler(lambda :editorNow.setWindowTitle(fileNameNow+" *"))


            except Exception as e:
                logging.debug(e)

                QMessageBox.warning(self, "EveIDE_LIGHT -- OPEN Error",
                                    "Failed to open {0}".format(fileDict.get("fullPath", "")))



    def editor_value_change_handler(self, editorNow):
        if editorNow.finishInit == 1:
            if not editorNow.titleNow == editorNow.dictNow.get("name", "") + " *":
                editorNow.setWindowTitle(editorNow.dictNow.get("name", "") + " *")
        else:
            logging.debug("initing")
            valueNow = editorNow.bridge.value
            # logging.debug("\""+valueNow+"\"")
            if valueNow == editorNow.initialCode:
                editorNow.finishInit = 1


def initDark():
    from qtmodernredux import QtModernRedux
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWinUi(),
                            titlebar_color=QColor('#555555'),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_RIGHT)
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # initDark()
    app = QApplication(sys.argv)
    mainWin = MainWinUi()
    mainWin.show()
    app.exec_()

'''import sys
from PySide2 import QtWidgets
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')
from qt_material import list_themes

list_themes()
# run
window.show()
app.exec_()'''
