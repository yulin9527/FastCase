from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QWidget, QLabel, QSplitter


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MyFrame(QFrame):
    """
    自定义边框基类,其余所有布局均继承此类
    """""

    def __init__(self):
        super().__init__()


class LeftMenuLayout(MyFrame):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(60)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(Color('blue'))


class ContentTapLayout(MyFrame):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(40)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(QLabel('arya'))
        self.layout.addWidget(RightButtonsLayout())


class RightButtonsLayout(MyFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.btn1 = QPushButton('设置')
        self.btn2 = QPushButton('最小化')
        self.btn3 = QPushButton('最大化')
        self.btn4 = QPushButton('关闭')
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)


class RightContentLayout(MyFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(ContentTapLayout())
        self.layout.addWidget(Color('red'))


class FastCaseWindowsLayout(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面默认大小与最小值
        self.resize(1280, 720)
        self.setMinimumSize(QSize(940, 560))
        # 设置默认边框
        self.bg_frame = QFrame()
        # 设置主体布局与内外边距
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 设置左侧菜单栏
        self.left_menu_layout = LeftMenuLayout()
        self.layout.addWidget(self.left_menu_layout)
        # 设置右侧内容中心
        self.layout.addWidget(RightContentLayout())
