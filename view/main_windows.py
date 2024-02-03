from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout
import settings as st
from view.left_menu_view import LeftMenuWidget
from view.right_box import RightBoxWidget


class FastCaseWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_set()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.left_menu = LeftMenuWidget()
        self.layout.addWidget(self.left_menu)
        self.right_box = RightBoxWidget()
        self.layout.addWidget(self.right_box)

        self.right_box.top_info.btn_close_app.clicked.connect(self.close)

    def __init_set(self):
        self.resize(st.MAIN_WIDTH, st.MAIN_HEIGHT)
        self.setMinimumSize(QSize(st.MAIN_MIN_WIDTH, st.MAIN_MIN_HEIGHT))

        # 设置主体布局与内外边距
        # self.layout = QHBoxLayout(self)