from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu

"""
最基础的框架
"""


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menubar = self.menuBar()

        self.openFile = QAction('打开文件')
        self.closeFile = QAction('关闭文件')

        self.fileMenu = QMenu('文件')
        # self.setMenu = QMenu('设置')

        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.closeFile)

        self.menubar.addMenu(self.fileMenu)
        # self.menubar.addMenu(self.setMenu)

        self.openFile.triggered.connect(lambda: print('open'))
        self.closeFile.triggered.connect(lambda: print('close'))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
