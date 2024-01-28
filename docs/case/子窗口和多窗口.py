from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from PIL import Image, ImageDraw, ImageFont, ImageQt

"""
最基础的框架
"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.head = QLabel('主窗口')
        self.show_windows = ShowWin()

        self.btn_close = QPushButton('关闭')
        self.btn_close.clicked.connect(lambda: self.show_windows.close())

        self.btn_show = QPushButton('显示')
        self.btn_show.clicked.connect(lambda: self.show_windows.show())

        self.btn_hide = QPushButton('隐藏')
        self.btn_hide.clicked.connect(lambda: self.show_windows.hide())

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.head)
        self.main_layout.addWidget(self.btn_close)
        self.main_layout.addWidget(self.btn_show)
        self.main_layout.addWidget(self.btn_hide)
        self.setLayout(self.main_layout)


class ShowWin(QWidget):
    def __init__(self):
        super().__init__()

        self.head = QLabel('子窗口')
        self.setMinimumSize(400, 300)
        self.btn = QPushButton('alsgjdk', self)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
