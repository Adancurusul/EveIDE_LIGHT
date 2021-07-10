import os
from qtpy import QtWidgets
from qtpy.QtWidgets import QWidget,QHBoxLayout,QMainWindow
from qtpy.QtCore import QUrl
from qtpy.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('百度')  #窗口标题
        self.setGeometry(5,30,1355,730)  #窗口的大小和位置设置
        self.browser=QWebEngineView()
        self.page = QWebEnginePage()
        self.editor_index = "D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\editor_settings\\index.html"
        self.page.setUrl(QUrl.fromLocalFile(self.editor_index))
        #加载外部的web界面
        self.browser.setPage(self.page)
        self.setCentralWidget(self.browser)
'''self.webview = QWebEngineView(self)
self.page = QWebEnginePage()
self.webview.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)  # 支持视频播放
self.page.windowCloseRequested.connect(self.on_windowCloseRequested)  # 页面关闭请求
self.page.profile().downloadRequested.connect(self.on_downloadRequested)  # 页面下载请求
# ------------监听 加载内容url
self.t = WebEngineUrlRequestInterceptor()
self.page.setUrl(QUrl("https://www.baidu.com"))
self.webview.setPage(self.page)
self.page.profile().setUrlRequestInterceptor(self.t)
self.webview.loadProgress.connect(self.processLoad)
self.frmWebview.setStyleSheet("border-top:1px solid #ccc;"
                              "border-bottom:1px solid #ccc;border-left:1px solid #ccc")
self.webview.show()'''

class EditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.horizontalLayout_2 = QHBoxLayout()
        self.browser=QWebEngineView()
        self.resize(300,300)
        #加载外部的web界面
        self.browser.load(QUrl('https://www.baidu.com'))
        self.horizontalLayout_2.addWidget(self.browser)

class Editor(QWebEngineView):
    def __init__(self, ):
        super().__init__()
        self.editor_flag = []
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://www.baidu.com'))
        #self.setCentralWidget(self.browser)
        # 这里是本地html路径,需根据实际情况进行修改.
        #self.editor_index = "D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\editor_settings\\index.html"
        #self.load(QUrl.fromLocalFile(self.editor_index))

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle('Editor')
    w.show()
    #w.set_value("ababa")
    sys.exit(app.exec_())