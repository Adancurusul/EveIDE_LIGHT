"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-23 08:53:01
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:05:57
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """

#####
#按键信号未添加
####
'''
LeftSideTab

'''
C51COMPILE = 1

from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit,QHBoxLayout,QTabWidget
from qtpy.QtCore import Qt,Signal
from qtpy.QtGui import QPalette,QBrush,QColor
import qtpy
from qtpy import QtGui
from qtpy import QtCore
from Simulator import Simulator

import sys
import logging
from eve_module.cfgRead import cfgRead
from ui.ui_module_project_tree import Ui_ProjectTree
from ui.ui_left_module_widget import  Ui_leftModuleWidget
from ui.ui_module_compile_widget import Ui_CompileWidget
from C51CompileWidget import moduleC51CompileWidget
from SelectWorkspace import SelectWorkspace
import os



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
        self.simulateWidget = Simulator()
        self.moduleList = [self.projectWidget,self.compileWidget,self.simulateWidget]
        self.compileWidget.compile_pushButton.clicked.connect(self.compileWidget.do_compile)
        self.init_ui()
        if C51COMPILE ==1:
            self.init_C51()



    def init_C51(self):
        self.C51CompileWidget = moduleC51CompileWidget()
        self.C51compile_tab = QWidget()
        self.C51compile_tab.setObjectName(u"C51compile_tab")
        self.leftModuleWidgetIn.addTab(self.C51compile_tab, "")
        self.leftModuleWidgetIn.setTabText(self.leftModuleWidgetIn.indexOf(self.C51compile_tab),"C51 compile")


        layout = QFormLayout()
        layout.addWidget(self.C51CompileWidget)
        self.C51compile_tab.setLayout(layout)
        self.C51compile_tab.moduleWidget = self.C51CompileWidget

        self.C51CompileWidget.setHidden(1)
        self.C51CompileWidget.c51compile_pushButton.clicked.connect(self.C51CompileWidget.do_compile)



    def init_ui(self):
        self.setupUi(self)
        self.add_module_project_widget()
        self.add_module_compile_widget()
        self.add_module_simulate_widget()
        self.leftModuleWidgetIn.currentChanged.connect(self.change_tab_module)
        #self.currentWidget = ""
        self.currentModule = self.project_tab.moduleWidget

        #self.leftModuleWidgetIn.setTabPosition(QTabWidget.South)

    def change_tab_module(self):
        for eachModule in self.moduleList :
            eachModule.setHidden(1)
        currentTab= self.leftModuleWidgetIn.currentWidget()
        self.currentModule = currentTab.moduleWidget
        #self.currentModule = self.currentWidget.moduleWidget

        self.currentModule.setHidden(0)

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
        #self.compileWidget.addSettingsDictList(compileSettingDefaultListEx)
    # self.compile_tab.setHidden(0)

    def add_module_project_widget(self):
        layout = QFormLayout()
        layout.addWidget(self.projectWidget)
        self.project_tab.setLayout(layout)
        self.project_tab.moduleWidget = self.projectWidget
        self.projectWidget.setHidden(0)
        self.currentModule = self.projectWidget
        #self.project_tab.setHidden(0)


'''
#指定sdcc编译器路径（注：请改为自己的路径）
sdcc  := sdcc\bin\sdcc.exe
packihx := sdcc\bin\packihx.exe

#指定stcflash烧录器路径（注：请改为自己的路径）
stcflash := stcflash/stcflash.py

#指定.c文件（注：请将工程中所有的.c文件添加进来）
SRCS = \
User/main.c \

#指定.h文件（注：请将工程中所有.h文件所在的文件夹添加进来）
INCS = \
-IUser \
-ILibraries \
-IHardware \

#指定输出hex文件的路径与文件名
outdir = Build
outname = output

all: $(outdir)/$(outname).hex download

#将所有的.c->.rel，存入OBJECT
OBJECTS = $(addprefix $(outdir)/,$(notdir $(SRCS:.c=.rel)))
vpath %.c $(sort $(dir $(SRCS)))

#（注：请对照自己的芯片调整以下几条语句的--iram-size、--xram-size参数）
$(outdir)/%.rel: %.c Makefile | $(outdir)
	$(sdcc) --code-size 64000 --iram-size 256 --xram-size 8192 --stack-auto -c $(INCS) $< -o $@

$(outdir)/$(outname).ihx: $(OBJECTS)
	$(sdcc) --code-size 64000 --iram-size 256 --xram-size 8192 --stack-auto $^ -o $(outdir)/$(outname).ihx

$(outdir)/%.hex: $(outdir)/%.ihx | $(outdir)
	$(packihx) $< $@ > $(outdir)/$(outname).hex

#调用stcflash进行烧录（注：请对照自己的设备修改COM口）
download:
	python $(stcflash) Build/output.hex --port COM7 --lowbaud 2400 --highbaud 460800

#定义清除操作
.PHONY : clean
clean :
  del $(outdir)\*.* /q

'''


class moduleCompileWidget(Ui_CompileWidget,QWidget):
    compileSignal = Signal(list,str)
    def __init__(self):
        super(moduleCompileWidget,self).__init__()
        self.setupUi(self)
        self.currentProjectDict = {}
        self.setMinimumSize(419,499)
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
        self.compileSettingDictList = []
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
            logging.debug(indexNow)
            if currentProjectName == self.compileSettingDictList[indexNow].get("projectName","nothing") :
                self.compileSettingDictList[indexNow] = self.compileSettingDictDefault
                logging.debug("change into default settings")
                #eachDict = self.compileSettingDictDefault
                break
        for eachDict in self.compileSettingDictList :
            if eachDict.get("projectName","nothing") == currentProjectName :
                self.currentProjectDict = eachDict
                self.toolchain_lineEdit.setText(os.path.abspath(eachDict.get("gccPath","nothing")))
                self.toolchain_lineEdit.setToolTip(os.path.abspath(eachDict.get("gccPath","nothing")))
                self.outputDir_lineEdit.setText(os.path.abspath(eachDict.get("outputPath","nothing")))
                self.outputDir_lineEdit.setToolTip(os.path.abspath(eachDict.get("outputPath","nothing")))
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
        for eachDictIndex in range(len(self.compileSettingDictList)):

            compileSettingDefaultEx = {"projectName":ex_proName,"projectPath":ex_projectPath,"gccPath":currentDir+"/modules/bin","outputPath":ex_projectPath+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
                                       "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-","if64bit":1}
            if currentProjectName == self.compileSettingDictList[eachDictIndex].get("projectName","nothing") :
                self.compileSettingDictList[eachDictIndex]["gccPath"] = os.path.relpath(self.toolchain_lineEdit.text())
                self.compileSettingDictList[eachDictIndex]["outputPath"] =  os.path.relpath(self.outputDir_lineEdit.text())
                self.compileSettingDictList[eachDictIndex]["binaryOutput"] = self.binaryOutput_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["mifOutput"] = self.mifOutput_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["coeOutput"] = self.coeOutput_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["normalOutput"] = self.normalOutput_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["i"] = self.i_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["m"] = self.m_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["a"] = self.a_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["c"] = self.c_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["f"] = self.f_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["autoMakefile"] = self.autoMakefile_checkBox.isChecked()
                self.compileSettingDictList[eachDictIndex]["if64bit"] = self.bit64_checkBox.isChecked()
                logging.debug("finish updating projectDictList")
                break
        print("commit")
        self.compileSignal.emit(self.compileSettingDictList,currentProjectName)



    def set_tool_tips(self,moduleNow,tipStr):

        pathNow = tipStr.replace("\\","/")
        logging.debug(tipStr)
        logging.debug(pathNow)
        moduleNow.setToolTip(pathNow)

        #logging.debug("'"+pathNow+"'")
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
        #logging.debug(projectName)
        for eachDict in self.compileSettingDictList :
            if eachDict.get("projectName","nothing") == projectNameNow :
                self.currentProjectDict = eachDict
                self.toolchain_lineEdit.setText(os.path.abspath(eachDict.get("gccPath","nothing")))
                self.toolchain_lineEdit.setToolTip(os.path.abspath(eachDict.get("gccPath","nothing")))
                self.outputDir_lineEdit.setText(os.path.abspath(eachDict.get("outputPath","nothing")))
                self.outputDir_lineEdit.setToolTip(os.path.abspath(eachDict.get("outputPath","nothing")))
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
        self.project_comboBox.clear()
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
        self.expand_pushButton.clicked.connect(self.expand_tree)
        self.collapse_pushButton.clicked.connect(self.collapse_tree)
        self.comboBox.addItem("Project View")
        #self.setMinimumSize(0,0)
        #self.resize(0,0)
        #self.setWindowFlags(Qt.FramelessWindowHint)

    def expand_tree(self):
        self.projectFile_treeWidget.expandAll()

    def collapse_tree(self):
        self.projectFile_treeWidget.collapseAll()






def i():
    r = cfgRead(cfgPath)
    dictn= {"able":1}
    r.write_dict(dictNow=dictn)

def init ():

    app = QApplication(sys.argv)
    mainWin = LeftModuleWidget()
    #from qt_material import apply_stylesheet

    #mainWin = LeftModuleWidget()

    #mainWin.init()
    #apply_stylesheet(app, theme='light_blue.xml')
    mainWin.show()
    sys.exit(app.exec_())
if __name__ == '__main__':

    logging.debug("close choosing workspace ui")
    init()



