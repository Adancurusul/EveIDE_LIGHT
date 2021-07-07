
'''
LeftSideTab

'''


from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit
from qtpy.QtCore import Qt
import qtpy
from qtpy import QtGui
from qtpy import QtCore

import sys
import logging
from eve_module.cfgRead import cfgRead
from ui.ui_module_project_tree import Ui_ProjectTree
from ui.ui_left_module_widget import  Ui_leftModuleWidget
from SelectWorkspace import SelectWorkspace


cfgPath = "..\configure\cfgSImulater.evecfg"
eachModuleDict = {"modules":[{ "project":{"basicProperty":{"defaultWidth":300,"currentWidth":200}}},{ "compile":{"basicProperty":{"defaultWidth":300,"currentWidth":200}}},{"simulate":{"basicProperty":{"defaultWidth":300,"currentWidth":200},}}]}
dictLeftTab = {
    "moduleList":[]
}

class LeftModuleWidget(QWidget,Ui_leftModuleWidget):
    def __init__(self):
        super(LeftModuleWidget,self).__init__()

        #self.setMinimumSize(0,0)
        # self.resize(0,10)
        self.compileWidget =  moduleProjectTree()
        self.projectWidget = moduleProjectTree()
        self.simulateWidget = moduleProjectTree()
        self.moduleList = [self.projectWidget,self.compileWidget,self.simulateWidget]
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
       # self.compile_tab.setHidden(0)

    def add_module_project_widget(self):
        layout = QFormLayout()
        layout.addWidget(self.projectWidget)
        self.project_tab.setLayout(layout)
        self.project_tab.moduleWidget = self.projectWidget
        self.projectWidget.setHidden(1)
        #self.project_tab.setHidden(0)


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
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',)
    app = QApplication(sys.argv)
    #mainWin = moduleProjectTree()
    mainWin = LeftModuleWidget()
    #mainWin.init()
    mainWin.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    init()



