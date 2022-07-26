#arduino-cli core list --format json
#arduino-cli board list --format json


#arduino-cli --config-file ./arduino-cli.yaml core -v install arduino:avr
#arduino-cli config -v init --dest-dir ./
#arduino-cli --config-file ./arduino-cli.yaml core -v update-index
#arduino-cli lib install --zip-path /path/to/WiFi101.zip /path/to/ArduinoBLE.zip
#arduino-cli --config-file ./arduino-cli.yaml（配置文件） upload -p COM15（com口） --fqbn esp32:esp32:twatch（板子） Lvgl_Base（工程文件夹位置）
#arduino-cli compile --fqbn esp32:esp32:esp32-poe-iso .
#arduino-cli upload -p /dev/cu.usbserial-1310 --fqbn esp32:esp32:esp32-poe-iso .
#esp32:esp32:twatch
#arduino-cli compile --config-file C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\modules\arduino-cli\arduino-cli.yaml --fqbn esp32:esp32:twatch ./Lvgl_Base
#arduino-cli compile --config-file C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\modules\arduino-cli\arduino-cli.yaml --fqbn esp32:esp32:twatch ./Lvgl_Base
import os.path
import subprocess
import sys
from ui.ui_arduino_compile_widget import Ui_arduinoCompileWidget
from ui.ui_module_project_tree import Ui_ProjectTree
from ProjectManage import ProjectManage
from qtpy.QtWidgets import QApplication, QMainWindow,\
    QWidget,QFileDialog,QTreeWidgetItem,QVBoxLayout,QFormLayout,\
    QLineEdit,QHBoxLayout,QTabWidget,QMenu,QAction,QMessageBox
from qtpy.QtCore import Qt,Signal,QSize,QTimer,QThread,Signal
from qtpy.QtGui import QPalette,QBrush,QColor,QIcon,QCursor
from eve_module.GetFunctionInC import GetFunctionInC
from eve_module.CompileThread import CompileThread
import json
import serial
import shutil
import datetime
import qtpy
from qtpy import QtGui
from qtpy import QtCore




arduinoCompileSettingDictExold = {"projectName":"",
                               "projectPath":"",
                               "core":"",
                               "board":"",
                               "arduinoCliPath":"",
                               }
arduinoCompileSettingDictEx = {"projectName":"",
                               "projectPath":"",
                               }

class ArduinoProjectTree(Ui_ProjectTree,QWidget):
    def __init__(self):
        super(ArduinoProjectTree,self).__init__()
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

class moduleArduinoCompileWidget(Ui_arduinoCompileWidget,QWidget):
    compileArduinoSignal = Signal(list,str)
    arduinoProjectChangeSignal = Signal(str)
    arduinoProjectCreatedSignal = Signal(str)
    arduinoProjectTreeRefreshSignal = Signal(str)# str :pathNow
    arduinoOpenFileSignal  = Signal(dict)
    arduinoDeleteFileSignal = Signal()
    def __init__(self):
        super(moduleArduinoCompileWidget, self).__init__()
        self.name = "ArduinoCompile"
        self.setupUi(self)
        self.init_all()
        self.arduinoCompileThread = CompileThread()
        self.arduinoCliDefaultPath = "module/arduino-cli/arduino-cli.exe"
    def init_workspace(self,workspacePath):
        self.workspacePath = os.path.abspath(workspacePath)
    def init_project_tree(self):
        self.arduinoProjectTreeWidget = ArduinoProjectTree()
        groupLayout = QVBoxLayout()
        groupLayout.addWidget(self.arduinoProjectTreeWidget)
        self.ArduinoProjectTree_groupBox.setLayout(groupLayout)
        self.arduinoProjectTreeWidget.pushButton.clicked.connect(self.refresh_arduino_tree)

    def refresh_arduino_tree(self):
        self.arduinoProjectTreeRefreshSignal.emit(self.projectSelect_comboBox.currentText())
    def start_arduino_compile(self,cmdStr,cwdPath):
        compileList = [cmdStr]
        self.arduinoCompileThread.init_thread(compileList,cwdPath)
        self.arduinoCompileThread.start()
    def init_all(self):
        self.signal_connect()
        self.init_project_tree()
        self.init_icon()
        self.projectList = []
        self.projectComboBoxList = []
        self.coreDictList = []
        self.coreList = []# ["esp32:esp32"]
        self.currentBoardList = []#[]
        #self.boardList = []
        self.projectSettingNow = {"projectName":"",
                               "projectPath":"",
                               }
        self.check_arduino_project_exist()
        #self.arduinoProjectTreeWidget.projectFile_treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.arduinoProjectTreeWidget.projectFile_treeWidget.customContextMenuRequested.connect(self.project_tree_right_click)

    def set_arduino_project_tree(self,mdiNow,treeNow,projectPath):
        self.comTreeNodeFileList = []
        projectManager = ProjectManage(projectPath)
        projectTreeDict = projectManager.porject_dict

        treeNow.setHeaderLabel("Workspace now :" + os.path.basename(self.workspacePath))
        treeNow.setHeaderLabel("")
        treeNow.setColumnCount(1)
        nodeName = projectTreeDict.get("node", None)
        nodeDirs = projectTreeDict.get("dirs", "")
        filesNow = projectTreeDict.get("files", "")
        rootNode = QTreeWidgetItem(treeNow)
        rootNode.setText(0, nodeName)
        rootNode.dictNow = projectTreeDict
        rootNode.setIcon(0, self.dirIcon)
        print(projectTreeDict)
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

                self.set_file_icon(childNode,childNode.dictNow)
                functionList = []
                if os.path.exists(fullName) :
                    if eachFile.get("fileSuffix") == "c" or eachFile.get("fileSuffix") == "ino":
                        CFunctionSelector = GetFunctionInC(fullName)
                        functionList = CFunctionSelector.fuctionList

                for eachFunction in functionList:
                    functionNode = QTreeWidgetItem()
                    functionNode.dictNow = eachFile
                    functionNode.setText(0,eachFunction)
                    functionNode.setIcon(0,self.functionIcon)
                    childNode.addChild(functionNode)
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

            subWindowList = mdiNow.subWindowList()
            #subWindowList = self.mdi.subWindowList()#在每次tree更新后能保证window 的currentnode更新
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

    def project_tree_right_click(self,pos):
        nodeNow = self.treeWidget.itemAt(pos)
        #nodeNow = self.simulateTreeWidget.itemAt(pos)
        currentDict = nodeNow.dictNow
        if not (currentDict.get("ifSubmodule", 0)):
            if (currentDict.get("fileSuffix", "") == "ino") or (currentDict.get("fileSuffix", "") == "h"):
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

    def project_right_click_handler(self,q):
        treeNode = self.treeWidget.currentItem()
        currentDict = treeNode.dictNow

        textNow = q.text()

        if "open file" in textNow:

            self.addEditorWidget(currentDict)
        elif "delete " in textNow:
            fullPath = os.path.abspath(currentDict.get("fullPath", ""))
            choose = QMessageBox.warning(self, "EveIDE_LIGHT -- FILE warning",
                                         "Sure to delete {0} from file system ? This action cannot be undone ".format(fullPath),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose == QMessageBox.Yes:
                try:
                    os.remove(fullPath)
                except:
                    shutil.rmtree(fullPath)
                self.check_file()
                self.update_sim_tree()
                self.set_workspace_tree()
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
            #print("functionList:"+str(functionList))
            for eachFunction in functionList:
                functionNode = QTreeWidgetItem()
                functionNode.dictNow = eachFile
                functionNode.setText(0,eachFunction)
                functionNode.setIcon(0,self.functionIcon)
                childNode.addChild(functionNode)
    def set_file_icon(self,nodeNow,nodeDict):
        fileSuffix = nodeDict.get("fileSuffix","")
        #logging.debug(fileSuffix)
        if fileSuffix=="c" or fileSuffix == "cpp" or fileSuffix == "ino":
            nodeNow.setIcon(0,self.cLanguageIcon)
        elif fileSuffix == "h":
            nodeNow.setIcon(0,self.headerIcon)
        elif fileSuffix == "bin" or fileSuffix == "coe" or fileSuffix == "mif" or fileSuffix == "o":
            nodeNow.setIcon(0,self.binIcon)
        elif fileSuffix == "mk" :
            nodeNow.setIcon(0,self.makefileIcon)
        elif fileSuffix == "S" or fileSuffix == "s":
            nodeNow.setIcon(0,self.assembleIcon)

    def add_zip_lib(self):
        fileName, _buf = QFileDialog.getOpenFileName(self, 'ZipFilePath', self.workspacePath, 'zip files (*.zip)')
        #print(fileName)
        if (not fileName is None):
            cwdPath = os.path.dirname(os.path.abspath(self.arduinoCliPath_lineEdit.text()))
            cmdStr = "arduino-cli --format json --config-file " + self.arduinoCfgPath + " lib install --zip-path " + fileName
            processNow = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, cwd=cwdPath, encoding='utf-8')
            processData = processNow.stdout.read()
            print(cmdStr)
            print(processData)
    def get_fqbn(self,arduinoCliPath,arduinoProjectPath):
        coreDictListNow = self.get_core_and_board(arduinoCliPath, self.arduinoCfgPath)
        # print(coreDictListNow)
        fqbnNow = None
        for eachCore in coreDictListNow:
            if eachCore.get("id", "") == self.core_comboBox.currentText():
                for eachBoard in eachCore.get("boards", []):
                    if eachBoard.get("name", "") == self.board_comboBox.currentText():
                        fqbnNow = eachBoard.get("fqbn", None)
        return fqbnNow
    def upload_project(self,arduinoCliPath,arduinoProjectPath):
        cwdPath = os.path.dirname(os.path.abspath(self.arduinoCliPath_lineEdit.text()))
        self.comNow = self.serialSelect_comboBox.currentText()
        # arduino-cli upload -p /dev/cu.usbserial-1310 --fqbn esp32:esp32:esp32-poe-iso .
        fqbnNow = self.get_fqbn(arduinoCliPath, arduinoProjectPath)
        if (fqbnNow != None):
            # print(fqbnNow)
            cmdStr = "arduino-cli upload -p "+self.comNow+" --config-file " + self.arduinoCfgPath + " --fqbn " + fqbnNow + " " + os.path.abspath(
                arduinoProjectPath)  # esp32:esp32:twatch ./Lvgl_Base "
            self.start_arduino_compile(cmdStr,
                                       cwdPath)
    def compile_arduino_project(self,arduinoCliPath,arduinoProjectPath):
        cwdPath = os.path.dirname(os.path.abspath(self.arduinoCliPath_lineEdit.text()))
        fqbnNow = self.get_fqbn(arduinoCliPath,arduinoProjectPath)

        if(fqbnNow != None):
            #print(fqbnNow)
            cmdStr = "arduino-cli compile --config-file "+self.arduinoCfgPath+" --fqbn "+ fqbnNow + " "+os.path.abspath(arduinoProjectPath)#esp32:esp32:twatch ./Lvgl_Base "
            self.start_arduino_compile(cmdStr,
                                       cwdPath)
        #cwdPath = os.path.dirname(os.path.abspath(self.arduinoCliPath_lineEdit.text()))
        #cmdStr = "arduino-cli --format json --config-file " + self.arduinoCfgPath + " lib install --zip-path " + dirNow
        #pass
    #arduino - cli lib install - -zip - path / path / to / WiFi101.zip / path / to / ArduinoBLE.zip
    def signal_connect(self):
        self.arduinoProjectSelect_pushButton.clicked.connect(self.arduino_project_select)
        self.arduinoCliSelect_pushButton.clicked.connect(self.arduinoCli_path_select)
        self.projectSelect_comboBox.currentIndexChanged.connect(self.change_project)
        self.searchLib_pushButton.setEnabled(0)
        self.addZipLib_pushButton.clicked.connect(self.add_zip_lib)
        self.compile_pushButton.clicked.connect(lambda :
                                                self.compile_arduino_project(self.arduinoCliPath_lineEdit.text(),self.projectSelect_comboBox.currentText()))
        #self.core_comboBox.currentIndexChanged.connect() #connect after init
        self.upload_pushButton.clicked.connect(lambda :
                                               self.upload_project(self.arduinoCliPath_lineEdit.text(),self.projectSelect_comboBox.currentText()))
        self.checkCOM_pushButton.clicked.connect(self.search_available_COM)
        self.arduinoCliPath_lineEdit.textChanged.connect(
            lambda: self.arduinoCliPath_lineEdit.set_tool_tips(self.arduinoCliPath_lineEdit, self.arduinoCliPath_lineEdit.text()))
        #self.addLib_lineEdit.textChanged.connect(
        #    lambda: self.addLib_lineEdit.set_tool_tips(self.addLib_lineEdit, self.addLib_lineEdit.text()))
    def search_available_COM(self):
        self.serialSelect_comboBox.clear()
        portList = list(serial.tools.list_ports.comports())
        for eachPort in portList:
            self.serialSelect_comboBox.addItem(eachPort[0])
    def arduinoCli_path_select(self):
        fileName, _buf = QFileDialog.getOpenFileName(self, 'ArduinoCliPath', self.workspacePath, 'All (*.*)')
        if (not fileName is None):
            fileName = os.path.abspath(fileName)
            #print(fileName)
            self.projectSettingNow["arduinoCliPath"] = fileName
    def change_project(self):
        self.projectSelect_comboBox.setToolTip(self.projectSelect_comboBox.currentText())
        self.arduinoProjectChangeSignal.emit(self.projectSelect_comboBox.currentText())
        #self.set_arduino_project_tree({},self.arduinoProjectTreeWidget.projectFile_treeWidget,self.projectSelect_comboBox.currentText())
    def check_arduino_project_exist(self):
        for eachDict in self.projectList:
            if not os.path.exists(eachDict["projectPath"]):
                self.projectList.remove(eachDict)
    def arduino_project_select(self,pathNow = None):
        pathNow = os.path.relpath(QFileDialog.getExistingDirectory(None, "Choose Arduino Project Path", self.workspacePath))
        pathNow = os.path.abspath(pathNow)
        print(pathNow,self.workspacePath)
        #if os.path.normcase(pathNow) == os.path.normcase(self.workspacePath):
        #print("same")
        if (not pathNow is None) and not (os.path.normcase(pathNow) == os.path.normcase(self.workspacePath)):# and not (os.path.samefile(self.workspacePath, pathNow)):
            #print(pathNow)
            self.projectSettingNow["projectPath"] = pathNow
            self.projectSettingNow["projectName"] = os.path.basename(pathNow)
            print(self.projectSettingNow)
            for eachDict in self.projectList:
                if eachDict.get("projectPath") == pathNow:
                    self.projectList.remove(eachDict)
                self.projectComboBoxList.append(eachDict["projectPath"])

            self.projectList.insert(0, self.projectSettingNow)
            self.projectComboBoxList.insert(0,self.projectSettingNow.get("projectPath",""))
            print(self.projectComboBoxList)
            self.projectSelect_comboBox.addItems(self.projectComboBoxList)
            self.projectSelect_comboBox.setToolTip(self.projectSelect_comboBox.currentText())

    def new_arduino_project(self, dirNow):
        cwdPath = os.path.dirname(os.path.abspath(self.arduinoCliPath_lineEdit.text()))

        cmdStr = "arduino-cli --format json --config-file " + self.arduinoCfgPath + " sketch new "+dirNow
        processNow = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, cwd=cwdPath, encoding='utf-8')
        processData = processNow.stdout.read()
        #print(processData)
        self.arduinoProjectChangeSignal.emit(dirNow)

    def get_core_and_board(self,arduinoCliPath,arduinoCfgPath)->dict:#全用绝对路径
        if os.path.exists(arduinoCfgPath) and os.path.exists(arduinoCliPath):
            #arduino-cli --format json --config-file ./arduino-cli.yaml core list
            self.arduinoCliPath = arduinoCliPath
            self.arduinoCfgPath = arduinoCfgPath
            cwdPath = os.path.dirname(arduinoCliPath)
            #print(cwdPath)
            cmdStr = "arduino-cli  --format json --config-file " + arduinoCfgPath+ " core list "
            processNow = subprocess.Popen(cmdStr,shell=True,stdout=subprocess.PIPE,cwd=cwdPath,encoding='utf-8')
            processData = processNow.stdout.read()
            #print(q)
            self.coreDictList = json.loads(processData)
            #print(self.coreDictList)
            return self.coreDictList
        else :
            return {"error":"yes"}
    def change_core_comboBox(self,indexNow):
        #print(indexNow)
        dictNow = self.coreDictList[indexNow]
        self.currentBoardList = []  # clearList
        for eachBoardDict in dictNow.get("boards",[]):
            #print(eachBoardDict)
            self.currentBoardList.append(eachBoardDict.get("name",None))
        self.board_comboBox.clear()
        self.currentBoardList.sort()
        self.board_comboBox.addItems(self.currentBoardList)




    def update_comboBox(self,coreDictList = None):
        if coreDictList == None:
            coreDictList = self.coreDictList

        for eachDict in coreDictList:
            self.coreList.append(eachDict.get("id",None))
        if self.coreDictList != []:
            self.currentBoardList = []# clearList
            for eachBoardDict in self.coreDictList[0].get("boards",[]) :
                self.currentBoardList.append(eachBoardDict.get("name",None))
        #print(self.currentBoardList)
        self.currentBoardList.sort()
        self.board_comboBox.clear()
        self.core_comboBox.clear()
        self.core_comboBox.addItems(self.coreList)
        self.board_comboBox.addItems(self.currentBoardList)
        self.core_comboBox.currentIndexChanged.connect(self.change_core_comboBox)

            #self.currentBoardList



    def get_arduino_cli_path(self)->str:
        return os.path.abspath(self.arduinoCliPath_lineEdit.text())
    def get_arduino_cfg_path(self)->str:
        return os.path.abspath(os.path.dirname(self.arduinoCliPath_lineEdit.text())+"/arduino-cli.yaml")
    def init_icon(self):
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
        self.EveIDEIcon = QIcon()
        self.EveIDEIcon.addFile(u":/pic/RVAT.png",QSize(), QIcon.Normal, QIcon.Off)
        self.pythonIcon = QIcon()
        self.pythonIcon.addFile(u":/pic/python.png",QSize(), QIcon.Normal, QIcon.Off)
        self.vcdIcon = QIcon()
        self.vcdIcon.addFile(u":/pic/wave.png", QSize(), QIcon.Normal, QIcon.Off)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ArduinoWin = moduleArduinoCompileWidget()
    ArduinoWin.init_workspace(r"C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source")
    #ArduinoWin.projectList.append(arduinoCompileSettingDictEx)
    #ArduinoWin.projectList.append(arduinoCompileSettingDictEx)
    ArduinoWin.show()
    sys.exit(app.exec_())