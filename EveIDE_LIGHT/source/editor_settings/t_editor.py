import os
from qtpy import QtWidgets
from qtpy.QtWidgets import QWidget,QHBoxLayout,QMainWindow
from qtpy.QtCore import QUrl,QThread
from qtpy.QtWebEngineWidgets import QWebEngineView,QWebEnginePage

import json
import os

from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseBridge(QtCore.QObject):
    initialized = QtCore.Signal()
    sendDataChanged = QtCore.Signal(str, str)

    def send_to_js(self, name, value):
        data = json.dumps(value)
        self.sendDataChanged.emit(name, data)

    @QtCore.Slot(str, str)
    def receive_from_js(self, name, value):
        data = json.loads(value)
        self.setProperty(name, data)

    @QtCore.Slot()
    def init(self):
        self.initialized.emit()


class EditorBridge(BaseBridge):
    valueChanged = QtCore.Signal()
    languageChanged = QtCore.Signal()
    themeChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(EditorBridge, self).__init__(parent)
        self._value = ""
        self._language = ""
        self._theme = ""

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        self.valueChanged.emit()

    def getLanguage(self):
        return self._language

    def setLanguage(self, language):
        self._language = language
        self.languageChanged.emit()

    def getTheme(self):
        return self._theme

    def setTheme(self, theme):
        self._theme = theme
        self.themeChanged.emit()

    value = QtCore.Property(str, fget=getValue, fset=setValue, notify=valueChanged)
    language = QtCore.Property(
        str, fget=getLanguage, fset=setLanguage, notify=languageChanged
    )
    theme = QtCore.Property(str, fget=getTheme, fset=setTheme, notify=themeChanged)


class EditorWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EditorWidget, self).__init__(parent)
        self._view = QtWebEngineWidgets.QWebEngineView()
        channel = QtWebChannel.QWebChannel(self)
        self.view.page().setWebChannel(channel)
        self._bridge = EditorBridge()
        channel.registerObject("bridge", self.bridge)
        #self.setCentralWidget(self.view)
        from qtpy.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
        layout = QGridLayout()
        layout.addWidget(self.view, 0, 0)
        #layout.addWidget(self.lineEdit, 1, 0)
        self.setLayout(layout)

        filename = os.path.join(CURRENT_DIR, "t_index.html")
        self.view.load(QtCore.QUrl.fromLocalFile(filename))

        self.bridge.initialized.connect(self.handle_initialized)
        self.bridge.valueChanged.connect(self.handle_valueChanged)
        self.bridge.languageChanged.connect(self.handle_languageChanged)
        self.bridge.themeChanged.connect(self.handle_themeChanged)
        #self.showFullScreen()

    @property
    def view(self):
        return self._view

    @property
    def bridge(self):
        return self._bridge

    def handle_initialized(self):
        print("init")
        code = "\n".join(["function x() {", '\tconsole.log("Hello world!");', "}"])
        # Do not use self.bridge.value = code or self.bridge.setValue(code)
        #self.bridge.send_to_js("value", code)
        self.bridge.send_to_js("language", "verilog")
        self.bridge.send_to_js("theme", "")

    def handle_valueChanged(self):
        print("value:", self.bridge.value)

    def handle_languageChanged(self):
        print("language:", self.bridge.language)

    def handle_themeChanged(self):
        print("theme", self.bridge.theme)






class EditorWidgetv(QWidget):
    def __init__(self, ):
        super().__init__()
        self.loadA()
    def loadB(self):
        self.view = QWebEngineView()
        self.editor_index = "C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\editor_settings\\index.html"
        self.view.load(QUrl.fromLocalFile(self.editor_index))
        layout = QHBoxLayout()
        layout.addWidget(self.view, 0)
        self.setLayout(layout)
    def loadA(self):
        self.editor_flag = []

        # self.browser.load(QUrl.fromLocalFile(self.editor_index))
        self.view = QWebEngineView()
        # channel = QtWebChannel.QWebChannel(self)
        # self.view.page().setWebChannel(channel)
        # self._bridge = EditorBridge()
        # channel.registerObject("bridge", self.bridge)
        filename = os.path.join(CURRENT_DIR, "t_index.html")
        self.view.load(QtCore.QUrl.fromLocalFile(filename))
        from qtpy.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout
        layout = QHBoxLayout()
        layout.addWidget(self.view, 0)
        self.setLayout(layout)

    @property
    def bridge(self):
        return self._bridge



if __name__ == "__main__":
    import sys

    sys.argv.append("--remote-debugging-port=8000")

    app = QtWidgets.QApplication(sys.argv)

    w = EditorWidget()
    w.show()

    sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    w = EditorWidget()
    w.setWindowTitle('Editor')
    w.show()
    #w.set_value("ababa")
    sys.exit(app.exec_())