import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QColor
from qtmodernredux import QtModernRedux
from mainwindow_ui import Ui_MainWindow


"""
This example demonstates the styling of the QSplitter element.
"""


__author__ = "Robert Kist"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setWindowTitle('QSplitter Test')


if __name__ == "__main__":
    app = QtModernRedux.QApplication(sys.argv)
    mw = QtModernRedux.wrap(MainWindow(),
                            titlebar_color=QColor('#555555'),
                            window_buttons_position=QtModernRedux.WINDOW_BUTTONS_LEFT)
    desktop = QApplication.desktop()
    mw.show()
    sys.exit(app.exec_())