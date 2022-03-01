"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-23 08:53:01
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:09:57
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
import subprocess
import os
import sys
import shutil
import datetime
from qtpy.QtCore import QTimer,QThread,Signal

class CompileThread(QThread):
    updateTextOutput = Signal(str,str)
    compileEndSignal = Signal()
    C51compileEndSignal = Signal()
    def __init__(self):
        super(CompileThread, self).__init__()
    def init_thread(self,compileList,cmdPath = "./"):
        self.compileList = compileList
        self.cmdPath =cmdPath
 
    def do_cmd(self,cmdStr):
        print(cmdStr)
        self.updateTextOutput.emit("<font color=black>%s </font> ",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                   +" : "+ cmdStr)
        p = subprocess.Popen(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True, cwd=self.cmdPath)  # , bufsize=1
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
    def run_C51compile(self):
        for eachCmd in self.compileList:
            self.do_cmd(eachCmd)
        self.compileEndSignal.emit()
    def run(self):
        for eachCmd in self.compileList:
            self.do_cmd(eachCmd)
        self.compileEndSignal.emit()
