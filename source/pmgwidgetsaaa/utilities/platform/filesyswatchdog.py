"""
作者(Author)：1295752786@qq.com
文件系统看门狗-(Watchdog for filesystem)
来源- (source)
https://stackoverflow.com/questions/35874217/watchdog-pythons-library-how-to-send-signal-when-a-file-is-modified
源代码为PyQt4,本人整理、移植到qtpy。(Originally code was in PyQt4 and I transplanted to PySide2.)
"""
import os

from PySide2.QtCore import Signal, QThread
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileMovedEvent, \
    FileCreatedEvent, FileDeletedEvent
from watchdog.observers import Observer


class MyEventHandler(FileSystemEventHandler, QThread):
    signal_file_modified = Signal(str)
    signal_file_created = Signal(str)
    signal_file_deleted = Signal(str)
    signal_file_moved = Signal(str, str)

    def __init__(self):
        super(MyEventHandler, self).__init__()

    def on_deleted(self, event: FileDeletedEvent):
        self.signal_file_modified.emit(event.src_path)

    def on_modified(self, event: FileModifiedEvent):
        self.signal_file_modified.emit(event.src_path)

    def on_created(self, event: FileCreatedEvent):
        self.signal_file_created.emit(event.src_path)

    def on_moved(self, event: FileMovedEvent):
        self.signal_file_moved.emit(event.src_path, event.dest_path)


class PMGFileSystemWatchdog(QThread):
    def __init__(self, path):
        super(PMGFileSystemWatchdog, self).__init__()

        self.path = path
        self.observer = Observer()
        self.event_handler = MyEventHandler()
        self.signal_file_modified: Signal = self.event_handler.signal_file_modified
        self.signal_file_created: Signal = self.event_handler.signal_file_created
        self.signal_file_deleted: Signal = self.event_handler.signal_file_deleted
        self.signal_file_moved: Signal = self.event_handler.signal_file_moved
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        # self.event_handler.signal_file_modified.connect(self.on_modified)

    def run(self):
        pass

    # def on_modified(self, event):
    #     print('modified!', event)
    # self.emit(QtCore.SIGNAL("fileModified1"))


if __name__ == '__main__':
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            d = os.path.dirname(__file__)
            path = os.path.join(d, 'test')  # 对其下的test文件夹进行看门狗监控
            self.label = QLabel('aaaa')
            self.fileWatcher = PMGFileSystemWatchdog(path)
            # self.fileWatcher.start()
            self.setCentralWidget(self.label)
            self.fileWatcher.event_handler.signal_file_modified.connect(self.fileModified)
            self.show()

        def fileModified(self, text: str):
            self.label.setText(text)


    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
