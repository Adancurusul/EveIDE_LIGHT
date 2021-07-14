import logging

from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit,QTabWidget,QMdiArea,QTextEdit,QDockWidget,QSplitter,QMdiSubWindow,QTreeWidgetItem
from qtpy.QtCore import Qt,Signal,QTimer
from qtpy.QtGui import QPalette,QBrush,QColor
import qtpy
from qtpy import QtGui
from qtpy import QtCore
import sys
import functools
import os
from ui.ui_main_window import Ui_MainWindow
from LeftModuleWidget import LeftModuleWidget
from OutputWidget import OutputWidget
from EditorWidget import EditorWidget
from eve_module.cfgRead import cfgRead
from ProjectManage import ProjectManage
__main_cfg_path =  "..\configure\cfgMainPath"
__project_cfg_path = "../configure/cfgPorjectList.evecfg"


def read_cfg(cfgPath) -> dict:
    cfgReader = cfgRead(cfgPath)
    return cfgReader.get_dict()


def write_cfg(cfgPath, writeDict) :
    cfgReader = cfgRead(cfgPath)
    cfgReader.write_dict(writeDict)
    #return cfgReader.get_dict()


class MainWinUi(QMainWindow,Ui_MainWindow):
    __main_cfg_path = cfgMainPath = "..\configure\cfgMainPath"
    __project_cfg_path = "../configure/cfgPorjectList.evecfg"
    projectTreeDictList =[]
    def __init__(self):
        super(MainWinUi,self).__init__()
        #self.testUi()
        self.initUi()
        self.initLogic()
        self.untitledNum = 1


    def initLogic(self):
        self.treeWidget =  self.leftWidget.projectWidget.projectFile_treeWidget
        self.workspacePath = read_cfg(self.__main_cfg_path)["workspaceNow"]
        logging.debug("workspace now is:"+self.workspacePath)
        self.set_workspace_tree()
        #刷新树状列表

        self.view_dock_closeEvent()
        self.connect_signal()
    def connect_signal(self):
        self.leftWidget.projectWidget.pushButton.clicked.connect(self.set_workspace_tree)
        self.actionnew.triggered.connect(lambda  : self.addEditorWidget(fileDict=None))
        self.actionopen.triggered.connect(self.openFile)
        self.actionModules.toggled.connect( functools.partial( self.view_handler,"Modules"))
        self.actionOutputs.toggled.connect(functools.partial(  self.view_handler,"Outputs"))
        self.treeWidget.itemDoubleClicked.connect(self.open_project_file)
        #.parent
        #setItem

    def view_handler(self,which,state):
        #print(state)
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

        #self.timerUpdateUi = QTimer()
        #self.timerUpdateUi.timeout.connect(self.updateUI)
        #self.timerUpdateUi.start(100)
    def open_project_file(self,currentTree):
        currentTreeDict = currentTree.dictNow
        print(currentTreeDict)
        if currentTreeDict.get("type","") == "file":
            self.addEditorWidget(currentTreeDict)

    def openFile(self):
        editorNow = self.mdi.currentSubWindow().widget()
        valueNow = ""
        #editorNow.get_value(valueNow)
        print(valueNow)
    @property
    def check_projects(self):
        cfgPath  = self.workspacePath+"./cfgPorjectList.evecfg"

        if os.path.exists(cfgPath):
            cfg = cfgRead(self.workspacePath+"./cfgPorjectList.evecfg")
            cfgDict = cfg.get_dict()
            cfgDict = read_cfg(self.__project_cfg_path)
            projectList = cfgDict["projectPathList"]
            for eachProject in projectList:
                if not os.path.exists(eachProject):
                    logging.debug("project :"+eachProject+" is not exist")
                    cfgDict["projectPathList"].remove(eachProject)
                else :
                    logging.debug("find project :"+eachProject)
            #cfg.write_dict(cfgDict)
            write_cfg(self.__project_cfg_path,cfgDict)
            return projectList
        else  :
            logging.debug("without workspacecfg , create new one")
            with open(cfgPath,"w+"):
                pass
            return []



    def saveFile(self):
        self.mdi
    def saveAsFile(self):
        pass

    def updateUI(self):
        pass
    def testUi(self):
        self.setupUi(self)
        editorNow = EditorWidget()
        self.LeftDockWidget = QDockWidget("Modules",self)
        self.LeftDockWidget.setWidget(editorNow)
        self.addDockWidget(Qt.RightDockWidgetArea,self.LeftDockWidget)

    def get_workspace_path(self):
        pass
    def set_workspace_tree(self):
        self.treeWidget.clear()
        self.projectList = self.check_projects
        for eachProject in self.projectList:
            projectManager = ProjectManage(eachProject)
            projectTreeDict = projectManager.porject_dict
            self.projectTreeDictList.append(projectTreeDict)
            print(str(projectTreeDict).replace("\'","\""))
            #创建工程树
            self.set_project_tree(projectTreeDict)
    def set_project_tree(self,projectTreeDict):
        self.treeWidget.setHeaderLabel("Workspace now :" + os.path.basename(self.workspacePath))
        self.treeWidget.setColumnCount(1)
        #print("now tree:"+str(projectTreeDict))
        nodeName = projectTreeDict.get("node","")
        nodeDirs = projectTreeDict.get("dirs","")
        filesNow = projectTreeDict.get("files","")
        rootNode = QTreeWidgetItem(self.treeWidget)
        rootNode.setText(0,nodeName)
        rootNode.dictNow = projectTreeDict
        #rootNode.setIcon()
        for eachFile in filesNow:
            #print("rootFiles:"+str(eachFile))
            childNode = QTreeWidgetItem()
            childNode.dictNow = eachFile
            childNode.setText(0,eachFile.get("name",""))
            childNode.dictNow["treeNode"] = rootNode
            rootNode.addChild(childNode)
            #childNode.setIcon()
        for eachDir in nodeDirs:
            childNode = QTreeWidgetItem()
            dirDict = eachDir.get("child","")
            #print("dirDict"+str(dirDict).replace("\'","\""))
            childNode.setText(0,eachDir.get("name",""))
            rootNode.addChild(childNode)
            childNode.dictNow = eachDir
            childNode.dictNow["treeNode"] = rootNode
            self.set_child_tree(childNode,dirDict)

        #for eachChild in
    def set_child_tree(self,rootNode,childDict):
        nodeName = childDict.get("node","")
        dirsDict = childDict.get("dirs","")
        filesNow = childDict.get("files","")
        for eachFile in filesNow:
            #print("rootFiles:"+str(eachFile))
            childNode = QTreeWidgetItem()
            childNode.dictNow = eachFile
            childNode.dictNow["treeNode"] = rootNode
            childNode.setText(0,eachFile.get("name",""))
            rootNode.addChild(childNode)
        for eachDir in dirsDict:
            childNode = QTreeWidgetItem()
            dirDict = eachDir.get("child","")
            #print("dirDict"+str(dirDict).replace("\'","\""))
            childNode.setText(0,eachDir.get("name",""))
            rootNode.addChild(childNode)
            childNode.dictNow = eachDir
            childNode.dictNow["treeNode"] = rootNode
            self.set_child_tree(childNode,dirDict)

        pass



    def initUi(self):
        self.setupUi(self)
        self.leftWidget = LeftModuleWidget()
        self.leftWidget.setMinimumSize(180,600)
        self.mdi = QMdiArea()
        self.mdi.setViewMode(QMdiArea.TabbedView)
        self.mdi.setTabsClosable(1)
        self.setWindowTitle("EveIDE_LIGHT")
        self.mdi.setTabsMovable(1)
        self.LeftDockWidget = QDockWidget("Modules",self)
        self.LeftDockWidget.setWidget(self.leftWidget)
        #self.RightDockWidget = QDockWidget("Values",self)
        #self.RightDockWidget.resize(150,150)
        #self.RifghtDockWidget.setWidget(self.leftWidget)
        self.TextOutput = OutputWidget(self) #内置于信息输出视图
        self.TextOutput.setReadOnly(True)     #仅作为信息输出，设置“只读”属性
        self.OutputDock = QDockWidget("Output",self)
        #self.OutputDock.setMinimumSize(600,150)
        self.OutputDock.setWidget(self.TextOutput)
        self.TextOutput.setText("2021-7-10 21:34 EveIDE_LIGHT with monaco editor")
        splitter1 = QSplitter(Qt.Vertical)
        #editorNow = EditorWidget()
        splitter1.addWidget(self.mdi)           #多文档视图占布局右上
        splitter1.addWidget(self.OutputDock)     #信息输出视图占布局右下
        self.addDockWidget(Qt.LeftDockWidgetArea,self.LeftDockWidget)#工程视图占布局左边
        #self.addDockWidget(Qt.RightDockWidgetArea,self.RightDockWidget)
        self.setCentralWidget(splitter1)

    def view_dock_closeEvent(self):  # 当dock关闭时触发
        self.OutputDock.closeEvent = self.dock_output_close
        self.LeftDockWidget.closeEvent = self.dock_LeftDockWidget_close

    def dock_output_close(self, p):
        # print(p)
        self.actionOutputs.setChecked(0)

    def dock_LeftDockWidget_close(self, p):
        # print(p)
        self.actionModules.setChecked(0)


        """
        自定义ui
        """
        #self.set_project_tree()
        '''self.midEditorTabWidget = QTabWidget()
        self.sub = QMdiSubWindow()
        self.sub.setWidget(self.midEditorTabWidget)
        self.mdi.addSubWindow(self.sub)
        self.sub.showMaximized()
        self.sub.setWindowFlags(Qt.FramelessWindowHint)'''


    def addEditorWidget(self,fileDict= None ):

        #fileNameNow = fileName.replace("\\","/")
        #if fileName == "untitled":
            #fileNameNow = "untitled-"+str(self.untitledNum)
            #self.untitledNum+=1
        #else:
            #pass
        #logging.debug("OpeningFile:"+fileName)
        print(fileDict)
        if  fileDict == None:
            fileNameNow = "untitled-"+str(self.untitledNum)
            self.untitledNum+=1
            fileDict = {'fullPath': None, 'name': fileNameNow, 'type': 'file', 'fileSuffix': None}
        else:
            fileNameNow = fileDict.get("name","")

        editorNow = EditorWidget()
        editorNow.dictNow = fileDict
        #self.midEditorTabWidget.addTab(editorNow,fileNameNow)
        self.mdi.addSubWindow(editorNow)
        editorNow.titleNow = fileNameNow
        editorNow.bridge.valueChanged.connect(lambda :self.editor_value_change_handler(editorNow))
        editorNow.setWindowTitle(fileNameNow)
        editorNow.show()

        #editorNow.add_change_handler(lambda :editorNow.setWindowTitle(fileNameNow+" *"))
        fullPath = fileDict.get("fullPath",None)
        if not fullPath == None:
            with open(fullPath,"r") as openFile:
                code = openFile.read()
                print(code)
        editorNow.add_codes(code)

    def editor_value_change_handler(self,editorNow):

        if editorNow.finishInit == 1:
            if not editorNow.titleNow == editorNow.dictNow.get("name","")+" *":
                editorNow.setWindowTitle(editorNow.dictNow.get("name","")+" *")
        else:
            if editorNow.bridge.value == editorNow.initialCode:
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
    #initDark()
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