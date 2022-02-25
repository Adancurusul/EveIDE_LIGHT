"""
    	***************************
    	--------EveIDE_LIGHT--------
 	 Author: Adancurusul
 	 Date: 2021-07-19 18:34:30
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-08-02 14:27:31
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#pyinstaller -F -w -i serial.ico SerialPortAssistant.py
from PySide2 import QtCore, QtGui, QtWidgets
from serialUI import Ui_serialUI
from PySide2.QtWidgets import QMessageBox,QFileDialog
from PySide2.QtCore import QTimer,QCoreApplication,Qt

import serial
import serial.tools.list_ports
import logging
import chardet
from datetime import datetime
#print(datetime.now())
PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE = 'N', 'E', 'O', 'M', 'S'
STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO = (1, 1.5, 2)
stopBitCheckDict = {
    "1":STOPBITS_ONE,
    "1.5":STOPBITS_ONE_POINT_FIVE,
    "2":STOPBITS_TWO,
}
parityDictCheckDict = {
    "None":PARITY_NONE,
    "Even":PARITY_EVEN,
    "Odd":PARITY_ODD,
    "Mark":PARITY_MARK,
    "Space":PARITY_SPACE,
}
logging.basicConfig( level=logging.INFO)
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

AUTHOR = "Adancurusul"
VERSION = "V0.0.1"
WEB = "https://github.com/Adancurusul/SerialPortAssistant"
RECEIVECHECKTIME = 2
ENCODING = "utf-8"#编码

class serialLogic(QtWidgets.QWidget, Ui_serialUI):
    def __init__(self):
        super(serialLogic, self).__init__()
        self.setupUi(self)

        self.init()

    def init(self):
        self.openSerial_pushButton.setEnabled(True)
        self.closeSerial_pushButton.setEnabled(False)
        self.serial = serial.Serial()
        self.setWindowTitle("串口助手  -- "+WEB)
        self.receiveTimer = QTimer(self)
        self.timerSendTimer = QTimer(self)

        self.init_data()
        self.init_button()
        self.init_other_signal()
        self.check_port()

    def checkSerial(func):
        def newfunc(self,serialNow):
            if serialNow.isOpen():
                #print("O")
                return func(self,serialNow)
            else:
                print('SerialIsNotOpen')
                return None
        return newfunc
    def init_data(self):
        self.serialComDict = {}
        self.receiveDataNum = 0
        self.sendDataNum = 0
        self.byteBuffer = b""#中文可能接收出错，用buffer来临时存储
        self.useByteBuffer = 0
    def init_button(self):
        #QtCore.QMetaObject.connectSlotsByName(self)
        self.checkSerial_pushButton.clicked.connect(self.check_port)
        self.openSerial_pushButton.clicked.connect(self.open_port)
        self.closeSerial_pushButton.clicked.connect(self.close_port)
        self.send_pushButton.clicked.connect(self.data_send)
        self.clearReceive_pushButton.clicked.connect(self.clear_receive)
        self.clearSend_pushButton.clicked.connect(self.clear_send)
        self.selectSendFile_pushButton.clicked.connect(self.select_send_file)
        self.selectReceiveFile_pushButton.clicked.connect(self.select_receive_file)
        self.sendFile_pushButton.clicked.connect(self.send_from_file)
        self.saveFile_pushButton.clicked.connect(self.save_to_file)
    def init_other_signal(self):
        #self.serial.
        self.serialSelect_comboBox.currentIndexChanged.connect(self.serial_selection_change)
        self.timerSendTimer.timeout.connect(lambda: self.data_send(self.serial))
        self.receiveTimer.timeout.connect(lambda: self.data_receive(self.serial))
        self.timerSend_checkBox.stateChanged.connect(self.timer_send)
        self.chineseEncode_comboBox.currentIndexChanged.connect(self.change_chinese_encode)
    def serial_selection_change(self,i):
        strComboBox =self.serialComDict.get(self.serialSelect_comboBox.currentText(),"无串口")
        self.state_label.setToolTip(strComboBox)
        self.serialSelect_comboBox.setToolTip(strComboBox)
        self.state_label.setText(strComboBox)

    def open_port(self):
        try:
            self.serial.port = self.serialSelect_comboBox.currentText()
            self.serial.baudrate = int(self.baudRate_comboBox.currentText())
            self.serial.bytesize = int(self.dataBit_comboBox.currentText())
            self.serial.stopbits = stopBitCheckDict.get(self.stopBit_comboBox.currentText(),STOPBITS_ONE)
            self.serial.parity = parityDictCheckDict.get(self.checkBit_comboBox.currentText(),PARITY_NONE)
            self.serial.open()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Port Error", str(e))
            return None
        self.receiveTimer.start(RECEIVECHECKTIME)
        if self.serial.isOpen():
            self.openSerial_pushButton.setEnabled(False)
            self.closeSerial_pushButton.setEnabled(True)
            self.serialConnection_label.setText("串口已连接")
    #@checkSerial
    def change_chinese_encode(self):
        global ENCODING
        ENCODING = self.chineseEncode_comboBox.currentText()
    def send_from_file(self):
        filePath = self.sendFile_lineEdit.text()
        if os.path.exists(filePath):
            with open(filePath, "rb") as f:
                bytesNow = f.read()

            sourceEncoding = chardet.detect(bytesNow).get("encoding")
            with open(filePath, "r", encoding=sourceEncoding) as f:#获取文件编码
                strNow = f.read()
                self.send_edit.clear()
                self.send_edit.setText(strNow)
        else:
            QMessageBox.critical(self, "File Error", "文件错误")


    def save_to_file(self):
        filePath = self.receiveFile_lineEdit.text()
        if os.path.exists(filePath):
            strNow = self.receive_edit.toPlainText()
            with open(filePath,"w",encoding="utf-8") as f:
                f.write(strNow)
            QMessageBox.information(self,"Save","成功保存")
        else:
            QMessageBox.critical(self, "File Error", "文件错误")
    def select_send_file(self):
        pathNow = (QFileDialog.getOpenFileName(None, "Choose Dict Path", "../","All Files(*);;Wav(*.wav);;Txt (*.txt)"))
        if pathNow != None :
            self.sendFile_lineEdit.setText(pathNow[0])
    def select_receive_file(self):
        pathNow = (QFileDialog.getOpenFileName(None, "Choose Dict Path", "../","All Files(*);;Wav(*.wav);;Txt (*.txt)"))
        if pathNow != None :
            #print(pathNow)
            self.receiveFile_lineEdit.setText(pathNow[0])

    def clear_send(self):
        self.send_edit.setText("")
    def clear_receive(self):
        self.receive_edit.setText("")
    def timer_send(self):
        if self.timerSend_checkBox.isChecked():
            self.timerSendTimer.start(int(self.sendTimer_lineEdit.text()))
            self.sendTimer_lineEdit.setEnabled(False)
        else:
            self.timerSendTimer.stop()
            self.sendTimer_lineEdit.setEnabled(True)
    def data_send(self,seialNow):
        dataToSend = self.send_edit.toPlainText()
        dataTemp = dataToSend
        if dataToSend != "":
            if self.hexSend_checkBox.isChecked():
                dataToSend = dataToSend.strip()
                sendList = []
                while dataToSend != "":
                    try:
                        hexNum = int(dataToSend[0:2],16)
                    except ValueError:
                        QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                        self.timerSend_checkBox.setChecked(0)
                        return None
                    dataToSend = dataToSend[2:].strip()
                    sendList.append(hexNum)
                dataToSend = bytes(sendList)

            else:
                #dataToSend = (dataToSend + "\r\n").encode(ENCODING)
                dataToSend = (dataToSend).encode(ENCODING)
            #print(ENCODING)

            try:
                sendNum = self.serial.write(dataToSend)
                self.sendDataNum += sendNum
                self.sendCounter_label.setText(str(self.sendDataNum))
                if self.showReceiveTime_checkBox.checkState():
                    timeStr = str(datetime.now())
                    printStr = "\r\n--" + timeStr + "-- send:\r\n"
                    self.receive_edit.insertPlainText(printStr)
                    strSend = dataTemp+"\r\n"
                    self.receive_edit.insertPlainText(strSend)

            except Exception as e:
                QMessageBox.critical(self, "Port Error", str(e))
                self.close_port()

    def data_receive(self,serialNow):
        try:
            numToShow = self.serial.inWaiting()
        except Exception as e:
            QMessageBox.critical(self, "Port Error", str(e))
            self.close_port()
            return None
        if numToShow > 0:

            dataNow = self.serial.read(numToShow)
            #print(numToShow)
            if self.showReceiveTime_checkBox.checkState():
                timeStr = str(datetime.now())
                printStr = "\r\n--"+timeStr+"-- receive:\r\n"
                self.receive_edit.insertPlainText(printStr)

            if self.hexReceive_checkBox.checkState():
                stringToPrint = ""

                for _ in range(0,numToShow) :
                    stringToPrint += '{:02X}'.format(dataNow[_]) + ' '
                    #print(stringToPrint)
                self.receive_edit.insertPlainText(stringToPrint)
                self.receiveDataNum += numToShow
                self.receiveCounter_label.setText(str(self.receiveDataNum))
                textCursorNow = self.receive_edit.textCursor()
                textCursorNow.movePosition(textCursorNow.End)
                self.receive_edit.setTextCursor(textCursorNow)
            else:
                if self.useByteBuffer:
                    self.byteBuffer+=dataNow
                    try:
                        self.receive_edit.insertPlainText(self.byteBuffer.decode(ENCODING))
                        self.byteBuffer = b""
                        self.useByteBuffer = 0


                    except UnicodeError:
                        self.useByteBuffer = 1


                try:
                    self.receive_edit.insertPlainText(dataNow.decode(ENCODING))
                    self.useByteBuffer = 0
                    self.byteBuffer = b""
                except UnicodeError :
                    self.useByteBuffer = 1
                    self.byteBuffer += dataNow
                self.receiveDataNum += numToShow
                self.receiveCounter_label.setText(str(self.receiveDataNum))
                textCursorNow = self.receive_edit.textCursor()
                textCursorNow.movePosition(textCursorNow.End)
                self.receive_edit.setTextCursor(textCursorNow)


            '''self.receiveDataNum += numToShow
            self.receiveCounter_label.setText(str(self.receiveDataNum))
            textCursorNow = self.receive_edit.textCursor()
            textCursorNow.movePosition(textCursorNow.End)
            self.receive_edit.setTextCursor(textCursorNow)'''
        else:
            pass
    def close_port(self):
        self.receiveDataNum = 0
        self.sendDataNum = 0
        self.openSerial_pushButton.setEnabled(True)
        self.closeSerial_pushButton.setEnabled(False)
        self.serialConnection_label.setText("串口未连接")
        self.receiveCounter_label.setText("0")
        self.sendCounter_label.setText("0")
        self.receiveTimer.stop()
        self.timerSendTimer.stop()
        if self.serial.isOpen():
            self.serial.close()
        pass
    def check_port(self):
        self.serialSelect_comboBox.clear()
        portList = list(serial.tools.list_ports.comports())
        for eachPort in portList:
            self.serialComDict["%s" % eachPort[0]] = "%s" % eachPort[1]
            self.serialSelect_comboBox.addItem(eachPort[0])
            #logging.INFO(str(eachPort[0]))
            #print(eachPort[0])
            #print(eachPort[1])
            #print(eachPort[2])
        if len(self.serialComDict) == 0:
            self.state_label.setText(" 无串口")

    #def closeEvent(self, event):
    #    try:
    #        self.serial.close()
    #    except:
    #        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = serialLogic()
    myshow.show()
    sys.exit(app.exec_())