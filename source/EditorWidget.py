import os
from qtpy import QtWidgets
from qtpy.QtWidgets import QWidget,QHBoxLayout,QMainWindow
from qtpy.QtCore import QUrl,QThread
from qtpy.QtWebEngineWidgets import QWebEngineView,QWebEnginePage





class EditorWidget(QWebEngineView):
    def __init__(self, ):
        super().__init__()
        self.editor_flag = []
        #self.browser=QWebEngineView()
        #加载外部的web界面
        #self.load(QUrl('https://www.baidu.com'))
        #self.setCentralWidget(self.browser)
        # 这里是本地html路径,需根据实际情况进行修改.

        #th = (self)
        #th.start()
        self.editor_index = "D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\editor_settings\\index.html"
        self.load(QUrl.fromLocalFile(self.editor_index))



    def get_value(self, callback):
        """设置编辑器内容"""
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def set_value(self, data):
        """获取编辑器内容"""
        import base64
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript("monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(data))

    def change_language(self, lan):
        """切换智能提示语言"""
        self.page().runJavaScript("monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{}')".format(lan))

class EditorUiThread(QThread):
    def __init__(self,EditorWidget):
        super(EditorUiThread, self).__init__(EditorWidget)
        self.Editor = EditorWidget
    def run(self):
        self.editor_index = "D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\editor_settings\\index.html"
        self.Editor.load(QUrl.fromLocalFile(self.editor_index))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = EditorWidget()
    w.setWindowTitle('Editor')
    w.set_value("aa")
    w.show()
    #w.set_value("ababa")
    sys.exit(app.exec_())