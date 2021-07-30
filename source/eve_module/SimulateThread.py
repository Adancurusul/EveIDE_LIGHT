
import subprocess
import os
import sys
import shutil
import datetime
from qtpy.QtCore import QTimer,QThread,Signal

class SimulateThread(QThread):
    updateTextOutput = Signal(str,str)#p1 颜色 #p2 文字
    def __init__(self):
        super(SimulateThread, self).__init__()
    def init_thread(self,simulateList,dumpFileInitPath,dumpFilePath,projectToSim):
        self.simulateList = simulateList
        self.dumpFileInitPath = dumpFileInitPath
        self.dumpFilePath = dumpFilePath
        self.projectToSim = projectToSim
    def do_cmd(self,cmdStr):
        self.updateTextOutput.emit("<font color=black>%s </font> ",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
+" : "+ cmdStr)
        p = subprocess.Popen(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True, cwd=self.projectToSim)  # , bufsize=1
        for line in iter(p.stderr.readline, b''):
            if b'warning' in line:
                status = True
                self.updateTextOutput.emit("<font color=hotpink>%s </font> ",line.decode("gbk", "ignore"))
            else:
                status = False
                self.updateTextOutput.emit("<font color=red>%s </font> " ,line.decode("gbk", "ignore"))
                p.stdout.close()
                p.wait()
                #return status
            #QApplication.processEvents()
        for line in iter(p.stdout.readline, b''):
            self.updateTextOutput.emit("<font color=black>%s </font> ",line.decode("gbk","ignore"))


    def run(self):
        #self.do_cmd(self.simulateList)
        self.do_cmd(self.simulateList[0])
        self.do_cmd(self.simulateList[1])
        '''if os.path.exists(self.dumpFileInitPath):
            shutil.copyfile(self.dumpFileInitPath, self.dumpFilePath)'''
        self.do_cmd(self.simulateList[2])
        pass



