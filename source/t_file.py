from qtpy.QtCore import *
from qtpy.QtWidgets import *
from qtpy.QtGui import *

import sys, os
import subprocess


class QTProcessThread(QThread):
    updateSig = Signal(str)

    def __init__(self, parent=None):
        super(QTProcessThread, self).__init__(parent)
        self.cmd = ""
    def run(self):

        #print(cmd)
        mytask = subprocess.Popen(self.cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        while True:
            line = mytask.stdout.readline()
            if not line:
                break
            x = line.decode('gb2312')
            print("x=%s" % x)
            self.updateSig.emit(x)


class MainFrame(QDialog):
    def __init__(self):
        super(MainFrame, self).__init__()

        self.textEdit = QTextEdit(self)

        self.myButton = QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.startThread)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.myButton)
        layout.addWidget(self.textEdit)

        self.cmdThread = QTProcessThread()
        self.cmdThread.updateSig.connect(self.upDateMessage)

    def startThread(self):
        print("start Thread")
        self.cmdThread.cmd = "ping baidu.com"
        self.cmdThread.start()

    def upDateMessage(self, message):
        self.textEdit.append(message)


if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    sys.exit(qApp.exec_())
