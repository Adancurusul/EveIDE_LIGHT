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
