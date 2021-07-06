
'''
simulate module

'''


from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
import qtpy
from qtpy import QtGui
from qtpy import QtCore
import sys
import logging
from eve_module.cfgRead import cfgRead

from SelectWorkspace import SelectWorkspace

cfgPath = "..\configure\cfgSImulater.evecfg"




def i():
    r = cfgRead(cfgPath)
    dictn= {"able":1}
    r.write_dict(dictNow=dictn)
def init ():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',)
    app = QApplication(sys.argv)
    mainWin = SelectWorkspace()
    mainWin.init()
    mainWin.show()
    sys.exit(app.exec_())
if __name__ == '__main__':



