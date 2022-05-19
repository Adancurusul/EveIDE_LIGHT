import os.path

from ui.ui_c51_compile_widget import Ui_C51CompileWidget
from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit,QHBoxLayout,QTabWidget
from qtpy.QtCore import Qt,Signal
from qtpy.QtGui import QPalette,QBrush,QColor
import qtpy
from qtpy import QtGui
from qtpy import QtCore
from Simulator import Simulator

import sys
import logging
compileSettingDefaultEx = {"projectName":"","projectPath":"","gccPath":"currentDir"+"/modules/bin","outputPath":"ex_projectPath"+"/build","binaryOutput":1,"mifOutput":0,"coeOutput":0,"normalOutput":1,
                           "i":1,"m":0,"a":0,"c":0,"f":0,"autoMakefile":1,"gccPrefix":"riscv-nuclei-elf-addr2line","if64bit":1}

compileC51SettingDictEx = {"projectName":"","MCUtype":"","projectPath":"","toolChainPath":"","outputPath":"",
                           "xramSize":"256","iramSize":"65536"}
class moduleC51CompileWidget(Ui_C51CompileWidget,QWidget):
    compileC51Signal = Signal(list,str)
    def __init__(self):

        super(moduleC51CompileWidget,self).__init__()
        self.name = "C51compile"
        self.setupUi(self)
        self.currentC51ProjectDict = {}
        self.compileC51SettingDictList = []
        self.c51toolchain_lineEdict.textChanged.connect(
            lambda: self.set_tool_tips(self.c51toolchain_lineEdict, self.c51toolchain_lineEdict.text()))
        self.c51outputDir_lineEdit.textChanged.connect(
            lambda: self.set_tool_tips(self.c51outputDir_lineEdit, self.c51outputDir_lineEdit.text()))

        self.c51project_comboBox.currentIndexChanged.connect(lambda : self.change_C51project(self.c51project_comboBox.currentText()))
        self.c51outputDir_lineEdit.textChanged.connect(
            lambda: self.set_tool_tips(self.c51outputDir_lineEdit, self.c51outputDir_lineEdit.text()))
        self.c51moreToolchain_pushButton.clicked.connect(lambda: self.change_dir_by_file_selector(self.c51toolchain_lineEdict))
        self.c51moreOutputDir_pushButton.clicked.connect(lambda: self.change_dir_by_file_selector(self.c51outputDir_lineEdit))
    def set_tool_tips(self,moduleNow,tipStr):

        pathNow = tipStr.replace("\\","/")
        logging.debug(tipStr)
        logging.debug(pathNow)
        moduleNow.setToolTip(pathNow)
    def change_dir_by_file_selector(self,currentLineEdit):
        pathNow = QFileDialog.getExistingDirectory(None, "Choose Dict Path", "../")
        currentLineEdit.setText(pathNow)
    def change_C51project(self,projectNameNow):
        for eachDict in self.compileC51SettingDictList:
            print(eachDict)
            if eachDict.get("projectName","nothing") == projectNameNow:
                #print("*****************************")
                #print(eachDict)
                #print((eachDict.get("outputPath","nothing")))
                #print("\r\n"*3)
                self.currentC51ProjectDict = eachDict
                self.c51toAolchain_lineEdict.setText(os.path.abspath(eachDict.get("toolChainPath","nothong")))
                self.xramSize_lineEdit.setText(eachDict.get("xramSize","256"))
                self.iramSize_lineEdit.setText(eachDict.get("iramSize","4096"))
                self.c51outputDir_lineEdit.setText(os.path.abspath(eachDict.get("outputPath","nothing")))
                self.c51outputDir_lineEdit.setToolTip(os.path.abspath(eachDict.get("outputPath","nothing")))
    def addC51ProjectDictList(self,listNow):
        # init compileC51SettingDictList
        self.compileC51SettingDictList = listNow
        self.c51project_comboBox.clear()

        for eachDict in self.compileC51SettingDictList :
            nameNow = eachDict.get("projectName","")
            self.c51project_comboBox.addItem(nameNow)



    def do_compile(self):
        '''
        Todo:
        增加编译以及自动makefile
        :return:
        '''

        compileC51SettingDictEx = {"projectName": "", "MCUtype": "", "projectPath": "", "toolChainPath": "",
                                   "outputPath": "",
                                   "xramSize": "256", "iramSize": "65536"}
        currentProjectName = self.c51project_comboBox.currentText()
        for eachDictIndex in range(len(self.compileC51SettingDictList)):

            if currentProjectName == self.compileC51SettingDictList[eachDictIndex].get("projectName","nothing") :
                self.compileC51SettingDictList[eachDictIndex]["toolChainPath"] = os.path.relpath(self.c51toolchain_lineEdict.text())
                self.compileC51SettingDictList[eachDictIndex]["outputPath"] =  os.path.relpath(self.c51outputDir_lineEdit.text())
                self.compileC51SettingDictList[eachDictIndex]["xramSize"] = self.xramSize_lineEdit.text()
                self.compileC51SettingDictList[eachDictIndex]["iramSize"] = self.iramSize_lineEdit.text()
                logging.debug("finish updating projectDictList")
                break

        self.compileC51Signal.emit(self.compileC51SettingDictList, currentProjectName)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    C51win = moduleC51CompileWidget()
    C51win.show()
    sys.exit(app.exec_())
