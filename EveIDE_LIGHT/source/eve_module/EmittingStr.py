"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-19 14:18:49
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:10:12
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
from qtpy import QtCore
from qtpy.QtCore import QTimer,QEventLoop
#from qtpy.QtWidgets import *
class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
 