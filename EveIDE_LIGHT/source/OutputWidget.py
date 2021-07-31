from qtpy.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog,QFormLayout,QLineEdit,QTabWidget,QMdiArea,QTextEdit

class OutputWidget(QTextEdit):
    def __init__(self,parent=None):
        super(OutputWidget,self).__init__(parent)