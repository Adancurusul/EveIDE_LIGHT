"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-19 15:50:05
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:10:39
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

class SimulateThread(QThread):
    updateTextOutput = Signal(str,str)#p1 颜色 #p2 文字
    def __init__(self):
        super(SimulateThread, self).__init__()
    def init_thread(self,simulateList,dumpFileInitPath,dumpFilePath,projectToSim):
        self.simulateList = simulateList
        self.dumpFileInitPath = dumpFileInitPath
        self.dumpFilePath = dumpFilePath
        self.projectToSim = projectToSim
        self.wrongSubprocess = 0
    def init_MyHDL_thread(self,filePath):
        self.MyHDLPath = os.path.abspath(filePath)
    def do_MyHDL_Simulate(self):
        cmdStr = "python "+self.MyHDLPath
        self.updateTextOutput.emit("<font color=black>%s </font> ",
                                   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                   + " : " + cmdStr)
        #p = subprocess.Popen(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        #                     shell=True, cwd='./', bufsize=1000)  # , bufsize=1

        pipe = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, cwd=os.path.dirname(self.MyHDLPath),
                                stderr=subprocess.PIPE)
        for line in iter(pipe.stdout.readline, 'b'):
            self.updateTextOutput.emit("<font color=black>%s </font> ", line.decode("gbk", "ignore"))
            if not subprocess.Popen.poll(pipe) is None:
                if line == b'':
                    break
        pipe.stdout.close()
        if pipe.stderr:
            for line in iter(pipe.stderr.readline, 'b'):
                # i = str(i, encoding='utf-8')
                self.updateTextOutput.emit("<font color=red>%s </font> ", line.decode("gbk", "ignore"))

                if not subprocess.Popen.poll(pipe) is None:
                    if line == b'':
                        break
    def show_GTKWave(self,cmdStr,filePath):
        self.updateTextOutput.emit("<font color=black>%s </font> ",
                                   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                   + " : " + cmdStr)
        pipe = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, cwd=os.path.dirname(filePath),
                                stderr=subprocess.PIPE)
        for line in iter(pipe.stdout.readline, 'b'):
            self.updateTextOutput.emit("<font color=black>%s </font> ", line.decode("gbk", "ignore"))
            if not subprocess.Popen.poll(pipe) is None:
                if line == b'':
                    break
        pipe.stdout.close()
        if pipe.stderr:
            for line in iter(pipe.stderr.readline, 'b'):
                # i = str(i, encoding='utf-8')
                self.updateTextOutput.emit("<font color=red>%s </font> ", line.decode("gbk", "ignore"))

                if not subprocess.Popen.poll(pipe) is None:
                    if line == b'':
                        break

    def do_cmd(self,cmdStr):
        '''
                            TODO:
            #p.stdout.close()#这里不知该不该去掉
                            '''



        self.updateTextOutput.emit("<font color=black>%s </font> ",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
+" : "+ cmdStr)
        p = subprocess.Popen(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True, cwd=self.projectToSim)  # , bufsize=1
        try:
            for line in iter(p.stderr.readline, b''):
                if b'warning' in line:
                    status = True
                    self.updateTextOutput.emit("<font color=hotpink>%s </font> ",line.decode("gbk", "ignore"))
                else:
                    status = False
                    self.updateTextOutput.emit("<font color=red>%s </font> " ,line.decode("gbk", "ignore"))
                    self.wrongSubprocess = 1
                    print("worng !in iverilog")
                    #p.stdout.close()#这里不知该不该去掉

                    #p.wait()
                    p.communicate()  # now wait

        except Exception as e:
            print(e)
        try:
            for line in iter(p.stdout.readline, b''):
                self.updateTextOutput.emit("<font color=black>%s </font> ",line.decode("gbk","ignore"))
        except Exception as e:
            print(e)

        '''
        pipe = subprocess.Popen(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True, cwd=self.projectToSim)  # , bufsize=1
        for line in iter(pipe.stdout.readline, 'b'):
            self.updateTextOutput.emit("<font color=black>%s </font> ", line.decode("gbk", "ignore"))
            if not subprocess.Popen.poll(pipe) is None:
                if line == b'':
                    break
        pipe.stdout.close()
        if pipe.stderr:
            for line in iter(pipe.stderr.readline, 'b'):
                # i = str(i, encoding='utf-8')
                self.updateTextOutput.emit("<font color=red>%s </font> ", line.decode("gbk", "ignore"))

                if not subprocess.Popen.poll(pipe) is None:
                    if line == b'':
                        break
        '''
    def run(self):
        #self.do_cmd(self.simulateList)
        self.do_cmd(self.simulateList[0])
        if self.wrongSubprocess == 0:
            self.do_cmd(self.simulateList[1])
            '''if os.path.exists(self.dumpFileInitPath):
                shutil.copyfile(self.dumpFileInitPath, self.dumpFilePath)'''
            self.do_cmd(self.simulateList[2])
        pass



