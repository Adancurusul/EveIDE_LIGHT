
#####
#按键信号未添加
####
'''
LeftSideTab

'''


from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit
from qtpy.QtCore import Qt
from qtpy.QtGui import QPalette,QBrush,QColor
import qtpy
from qtpy import QtGui
from qtpy import QtCore

import sys
import logging
from eve_module.cfgRead import cfgRead
from ui.ui_module_project_tree import Ui_ProjectTree
from ui.ui_left_module_widget import  Ui_leftModuleWidget
from ui.ui_module_compile_widget import Ui_CompileWidget
from SelectWorkspace import SelectWorkspace
import os
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)


currentDir = os.getcwd()
currentDir = currentDir.replace("\\","/")
defaultGccPath = currentDir+"/module/gcc/bin"
logging.debug("currentDir: "+currentDir)
cfgPath = "..\configure\cfgSImulater.evecfg"




eachModuleDict = {"modules":[{ "project":{"basicProperty":{"defaultWidth":300,"currentWidth":200}}},{ "compile":{"basicProperty":{"defaultWidth":300,"currentWidth":200}}},{"simulate":{"basicProperty":{"defaultWidth":300,"currentWidth":200},}}]}
dictLeftTab = {
    "moduleList":[]
}

ex_projectPath = r"D:/codes/EveIDE_Plus/EveIDE_Plus/source/t_exCpro"
ex_proName ="t_exCpro"
compileSettingDefault = {"gccPath":"none"}
compileSettingDefaultEx = {"projectName":ex_proName,"projectPath":ex_projectPath,"gccPath":currentDir+"/modules/bin","outputPath":ex_projectPath+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
                           "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-addr2line","if64bit":1}
compileSettingDefaultListEx = []
compileSettingDefaultListEx.append(compileSettingDefaultEx)
#或许可以增加一个检查是否是原始配置
#需要增加一步配置原始路径
#记得增加\转\\
#list中 每次编译改变顺序

projectCExample = {"projectType":"C"}
projectASMExample = {"projectType":"ASM"}
projectSimulateExample = {"projectType":"simulate"}
#projectDictExample = {"C":projectCExample,"ASM":projectASMExample,"simulate":projectSimulateExample}
class LeftModuleWidget(QWidget,Ui_leftModuleWidget):
    def __init__(self):
        super(LeftModuleWidget,self).__init__()

        #self.setMinimumSize(0,0)
        # self.resize(0,10)
        self.compileWidget =  moduleCompileWidget()
        self.projectWidget = moduleProjectTree()
        self.simulateWidget = moduleProjectTree()
        self.moduleList = [self.projectWidget,self.compileWidget,self.simulateWidget]
        self.compileWidget.compile_pushButton.clicked.connect(self.compileWidget.do_compile)
        self.init_ui()
    def init_ui(self):
        self.setupUi(self)
        self.add_module_project_widget()
        self.add_module_compile_widget()
        self.add_module_simulate_widget()
        self.leftModuleWidgetIn.currentChanged.connect(self.change_tab_module)
    def change_tab_module(self):
        for eachModule in self.moduleList :
            eachModule.setHidden(1)
        currentTab= self.leftModuleWidgetIn.currentWidget()
        currentWidget = currentTab.moduleWidget
        logging.debug("currentLeftTab: "+currentTab.moduleWidget.name)
        currentWidget.setHidden(0)

    def add_module_simulate_widget(self):
        layout = QFormLayout()
        layout.addWidget(self.simulateWidget)
        self.simulate_tab.setLayout(layout)
        self.simulate_tab.moduleWidget = self.simulateWidget
        self.simulateWidget.setHidden(1)

    def add_module_compile_widget(self):
        layout = QFormLayout()
        layout.addWidget(self.compileWidget)
        self.compile_tab.setLayout(layout)
        self.compile_tab.moduleWidget = self.compileWidget
        self.compileWidget.setHidden(1)
        #下面为测试代码
        self.compileWidget.addSettingsDictList(compileSettingDefaultListEx)
    # self.compile_tab.setHidden(0)

    def add_module_project_widget(self):
        layout = QFormLayout()
        layout.addWidget(self.projectWidget)
        self.project_tab.setLayout(layout)
        self.project_tab.moduleWidget = self.projectWidget
        self.projectWidget.setHidden(0)
        #self.project_tab.setHidden(0)


class moduleCompileWidget(Ui_CompileWidget,QWidget):
    def __init__(self):
        super(moduleCompileWidget,self).__init__()
        self.setupUi(self)
        self.currentProjectDict = {}
        self.name = "moduleCompileWidget"
        #下为测试代码
        self.compileSettingDictDefault = compileSettingDefaultEx
        self.project_comboBox.currentIndexChanged.connect(lambda : self.change_project(self.project_comboBox.currentText()))
        self.bit64_checkBox.stateChanged.connect(lambda : self.compile_bit_change_64())
        self.bit32_checkBox.stateChanged.connect(lambda : self.compile_bit_change_32())
        self.toolchain_lineEdit.textChanged.connect(lambda : self.set_tool_tips(self.toolchain_lineEdit,self.toolchain_lineEdit.text()))
        self.outputDir_lineEdit.textChanged.connect(lambda:self.set_tool_tips(self.outputDir_lineEdit,self.outputDir_lineEdit.text()))
        self.moreToolchain_pushButton.clicked.connect(lambda : self.change_dir_by_file_selector(self.toolchain_lineEdit))
        self.moreOutputDir_pushButton.clicked.connect(lambda : self.change_dir_by_file_selector(self.outputDir_lineEdit))
        self.useDefault_pushButton.clicked.connect(self.change_into_default_settings)
        #self.compile_pushButton.clicked.connect(self.do_compile)
        self.init_name()
    def change_dir_by_file_selector(self,currentLineEdit):
        pathNow = QFileDialog.getExistingDirectory(None, "Choose Dict Path", "../")
        currentLineEdit.setText(pathNow)
    def init_name(self):
        pass
    def create_makefile(self):
        pass
    def make_and_show(self):
        pass
    def change_into_default_settings(self):
        currentProjectName = self.project_comboBox.currentText()
        for indexNow in range(len(self.compileSettingDictList)):
            print(indexNow)
            if currentProjectName == self.compileSettingDictList[indexNow].get("projectName","nothing") :
                self.compileSettingDictList[indexNow] = self.compileSettingDictDefault
                logging.debug("change into default settings")
                #eachDict = self.compileSettingDictDefault
                break
        for eachDict in self.compileSettingDictList :
            if eachDict.get("projectName","nothing") == currentProjectName :
                self.currentProjectDict = eachDict
                self.toolchain_lineEdit.setText(eachDict.get("gccPath","nothing"))
                self.toolchain_lineEdit.setToolTip(eachDict.get("gccPath","nothing"))
                self.outputDir_lineEdit.setText(eachDict.get("outputPath","nothing"))
                self.outputDir_lineEdit.setToolTip(eachDict.get("outputPath","nothing"))
                self.binaryOutput_checkBox.setChecked(eachDict.get("binaryOutput",0))
                self.mifOutput_checkBox.setChecked(eachDict.get("mifOutput",0))
                self.coeOutput_checkBox.setChecked(eachDict.get("coeOutput",0))
                self.normalOutput_checkBox.setChecked(eachDict.get("normalOutput",0))
                self.i_checkBox.setChecked(eachDict.get("i",0))
                self.a_checkBox.setChecked(eachDict.get("a",0))
                self.m_checkBox.setChecked(eachDict.get("m",0))
                self.c_checkBox.setChecked(eachDict.get("c",0))
                self.f_checkBox.setChecked(eachDict.get("f",0))
                self.autoMakefile_checkBox.setChecked((eachDict.get("autoMakefile",1)))
                self.bit64_checkBox.setChecked(eachDict.get("if64bit",0))
                self.bit32_checkBox.setChecked(not eachDict.get("if64bit",0))
                break
    def do_compile(self):
        '''
        Todo:

        :return:
        '''
        currentProjectName = self.project_comboBox.currentText()
        for eachDict in self.compileSettingDictList:
            compileSettingDefaultEx = {"projectName":ex_proName,"projectPath":ex_projectPath,"gccPath":currentDir+"/modules/bin","outputPath":ex_projectPath+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
                                       "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-addr2line","if64bit":1}
            if currentProjectName == eachDict.get("projectName","nothing") :
                eachDict["gccPath"] = self.toolchain_lineEdit.text()
                eachDict["outputPath"] =  self.outputDir_lineEdit.text()
                eachDict["binaryOutput"] = self.binaryOutput_checkBox.isChecked()
                eachDict["mifOutput"] = self.mifOutput_checkBox.isChecked()
                eachDict["coeOutput"] = self.coeOutput_checkBox.isChecked()
                eachDict["normalOutput"] = self.normalOutput_checkBox.isChecked()
                eachDict["i"] = self.i_checkBox.isChecked()
                eachDict["m"] = self.m_checkBox.isChecked()
                eachDict["a"] = self.a_checkBox.isChecked()
                eachDict["c"] = self.c_checkBox.isChecked()
                eachDict["f"] = self.f_checkBox.isChecked()
                eachDict["autoMakefile"] = self.autoMakefile_checkBox.isChecked()
                eachDict["if64bit"] = self.bit64_checkBox.isChecked()
                logging.debug("finish updating projectDictList")
                break

    def set_tool_tips(self,moduleNow,tipStr):

        pathNow = tipStr.replace("\\","/")
        print(tipStr)
        print(pathNow)
        moduleNow.setToolTip(pathNow)

        #print("'"+pathNow+"'")
        '''       if  not os.path.exists(pathNow):

            logging.debug("fail to find path :"+pathNow)
            #moduleNow.setTextColor("red")
            palette = QPalette()
            brush = QBrush(QColor(255, 0, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Text, brush)
            palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
            brush1 = QBrush(QColor(120, 120, 120, 255))
            brush1.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
            moduleNow.setPalette(palette)
        else :
            logging.debug(" find path :"+pathNow)
            #moduleNow.setTextColor("red")
            palette = QPalette()
            brush = QBrush(QColor(0, 0, 0, 255))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Text, brush)
            palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
            brush1 = QBrush(QColor(120, 120, 120, 255))
            brush1.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
            self.toolchain_lineEdit.setPalette(palette)'''
    def compile_bit_change_64(self):
        if self.bit64_checkBox.isChecked():
            self.bit32_checkBox.setChecked(0)
        else:
            self.bit32_checkBox.setChecked(1)

    def compile_bit_change_32(self):
        if self.bit32_checkBox.isChecked():
            self.bit64_checkBox.setChecked(0)
        else:
            self.bit64_checkBox.setChecked(1)

    def change_project(self,projectNameNow):
        #print(projectName)
        for eachDict in self.compileSettingDictList :
            if eachDict.get("projectName","nothing") == projectNameNow :
                self.currentProjectDict = eachDict
                self.toolchain_lineEdit.setText(eachDict.get("gccPath","nothing"))
                self.toolchain_lineEdit.setToolTip(eachDict.get("gccPath","nothing"))
                self.outputDir_lineEdit.setText(eachDict.get("outputPath","nothing"))
                self.outputDir_lineEdit.setToolTip(eachDict.get("outputPath","nothing"))
                self.binaryOutput_checkBox.setChecked(eachDict.get("binaryOutput",0))
                self.mifOutput_checkBox.setChecked(eachDict.get("mifOutput",0))
                self.coeOutput_checkBox.setChecked(eachDict.get("coeOutput",0))
                self.normalOutput_checkBox.setChecked(eachDict.get("normalOutput",0))
                self.i_checkBox.setChecked(eachDict.get("i",0))
                self.a_checkBox.setChecked(eachDict.get("a",0))
                self.m_checkBox.setChecked(eachDict.get("m",0))
                self.c_checkBox.setChecked(eachDict.get("c",0))
                self.f_checkBox.setChecked(eachDict.get("f",0))
                self.autoMakefile_checkBox.setChecked((eachDict.get("autoMakefile",1)))
                self.bit64_checkBox.setChecked(eachDict.get("if64bit",0))
                self.bit32_checkBox.setChecked(not eachDict.get("if64bit",0))
                break

    def addSettingsDictList(self,listNow):
        self.compileSettingDictList = listNow
        for eachDict in self.compileSettingDictList :
            nameNow = eachDict.get("projectName","nothing")
            self.project_comboBox.addItem(nameNow)

    def addSettingsDict(self,dictNow):
        self.compileSettingDict = dictNow


class moduleProjectTree(Ui_ProjectTree,QWidget):
    def __init__(self):
        super(moduleProjectTree,self).__init__()
        self.setupUi(self)
        self.name = "moduleProjectTree"
        #self.setMinimumSize(0,0)
        #self.resize(0,0)
        #self.setWindowFlags(Qt.FramelessWindowHint)









def i():
    r = cfgRead(cfgPath)
    dictn= {"able":1}
    r.write_dict(dictNow=dictn)

def init ():

    app = QApplication(sys.argv)
    #mainWin = moduleProjectTree()
    mainWin = LeftModuleWidget()
    #mainWin.init()
    mainWin.show()
    sys.exit(app.exec_())
if __name__ == '__main__':

    logging.debug("close choosing workspace ui")
    init()



