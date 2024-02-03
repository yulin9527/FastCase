from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QWidget, QLabel, QMainWindow

from settings import Settings
from widgets.left_menu import LeftMenuWidget


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class ContentTapLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(40)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(QLabel('arya'))
        self.layout.addWidget(RightButtonsLayout())


class RightButtonsLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.btn1 = QPushButton('设置')
        self.btn2 = QPushButton('最小化')
        self.btn3 = QPushButton('最大化')
        self.btn_close = QPushButton('关闭')
        self.layout.addWidget(self.btn1)
        self.layout.spacerItem()
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn_close)


class RightContentLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(ContentTapLayout())
        self.layout.addWidget(Color('red'))


class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面默认大小与最小值
        self.resize(Settings.MAIN_WIDTH, Settings.MAIN_HEIGHT)
        self.setMinimumSize(QSize(Settings.MAIN_MIN_WIDTH, Settings.MAIN_MIN_HEIGHT))

        # 设置主体布局与内外边距
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.left_menu = LeftMenuWidget()
        self.layout.addWidget(self.left_menu)
        self.layout.addWidget(QWidget())



        # self.btn_home.setStyleSheet("""
        #     QPushButton {
        #         border: none; /* 或者 border-width: 0; */
        #     }
        # """)
        # font = QFont()
        # font.setFamily('Segoe UI')
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # self.style_sheet.setFont(font)

        # self.app_margins = QVBoxLayout(self)
        # self.app_margins.setSpacing(0)
        # self.app_margins.setObjectName('app_margins')
        # self.app_margins.setContentsMargins(10, 10, 10, 10)
        #
        # self.back_ground = QFrame(self)
        # self.back_ground.setObjectName('back_ground')
        # self.back_ground.setStyleSheet('')
        # self.back_ground.setFrameShape(QFrame.Box)
        # self.back_ground.setFrameShadow(QFrame.Raised)
        #
        # self.app_layout = QHBoxLayout(self.back_ground)
        # self.app_layout.setSpacing(0)
        # self.app_layout.setContentsMargins(0, 0, 0, 0)
        # self.app_layout.setObjectName('app_layout')
        #
        # self.left_menu_back = QFrame(self.back_ground)
        # self.left_menu_back.setObjectName('left_menu_back')
        # self.left_menu_back.setMinimumHeight(60)
