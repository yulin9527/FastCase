from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFrame, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QColor, QPalette

"""
最基础的框架
"""


class MyQFrame(QFrame):
    def __init__(self):
        super().__init__()
        # self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class LeftMenuLayout(QVBoxLayout):
    def __init__(self, ):
        super().__init__()
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        btn = QPushButton("按钮 1")
        btn.setContentsMargins(0, 0, 0, 0)
        # btn.setSpacing(0)
        btn2 = QPushButton("按钮 2")
        btn3 = QPushButton("按钮 3")
        self.addWidget(btn)
        # self.addWidget(btn2)
        # self.addWidget(btn3)


class RightMenuLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.addWidget(Color('red'))
        self.layout.addWidget(Color('blue'))
        self.layout.addWidget(Color('red'))

        self.setLayout(self.layout)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        # self.setSpacing(0)
        self.left_menu = QFrame()
        self.left_menu.setContentsMargins(0, 0, 0, 0)
        # self.left_menu.setMinimumSize(60, 100)
        self.left_menu.setMaximumSize(60, 1000)
        # self.left_menu.setFrameShape(QFrame.NoFrame)
        # self.left_menu.setFrameShadow(QFrame.Raised)
        left_layout = LeftMenuLayout()

        self.left_menu.setLayout(left_layout)

        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(1, 10, 0, 0)
        main_layout.addWidget(self.left_menu)
        main_layout.addWidget(RightMenuLayout())
        #

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
