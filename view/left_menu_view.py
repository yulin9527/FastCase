from PySide6.QtCore import QRect, QSize, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPalette, QColor, QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QPushButton

import settings as st


class LeftMenuWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.max_width = 160
        self.logo_width = 60
        self.layout = QVBoxLayout(self)
        self.__init_set()

        # 设置顶部 logo
        self.top_logo_info = QFrame()
        self._set_top_logo()

        self.left_menu_info = QFrame()
        self.btn_hide = QPushButton("Hide")
        self.btn_home = QPushButton("Home")
        self.btn_settings = QPushButton("Settings")
        self._set_left_menu()

        self.animation = QPropertyAnimation(self, b'minimumWidth')

        self.btn_connect()

    def btn_connect(self):
        self.btn_hide.clicked.connect(self.btn_hide_clicked)

    def _set_top_logo(self):
        self.top_logo_info.setMaximumHeight(self.logo_width)
        self.top_logo_info.setMinimumHeight(self.logo_width)
        logo = QLabel(self.top_logo_info)
        show_size = self.logo_width - 10
        logo.setGeometry(QRect(5, 5, show_size, show_size))
        pixmap = QPixmap("78968273.jpeg").scaled(QSize(show_size, show_size), Qt.KeepAspectRatio,
                                                 Qt.SmoothTransformation)
        logo.setPixmap(pixmap)

        title_top = QLabel(self.top_logo_info)
        title_top.setGeometry(QRect(self.logo_width, 0, self.max_width - self.logo_width, self.logo_width))
        title_top.setText(st.FAST_CASE_NAME)
        title_top.setAlignment(Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)

        self.layout.addWidget(self.top_logo_info)

    def _set_left_menu(self):
        self.left_menu_info.move(0, self.logo_width)
        palette = self.left_menu_info.palette()
        palette.setColor(QPalette.Window, QColor(215, 192, 203))
        self.left_menu_info.setPalette(palette)
        self.left_menu_info.setAutoFillBackground(True)

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        left_layout.addWidget(self.btn_hide)
        left_layout.addWidget(self.btn_home)
        left_layout.addStretch()
        left_layout.addWidget(self.btn_settings)

        self.left_menu_info.setLayout(left_layout)

        self.layout.addWidget(self.left_menu_info)

    def __init_set(self):
        self.setMaximumWidth(self.logo_width)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 192, 203))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def btn_hide_clicked(self):
        width = self.width()
        if width == self.max_width:
            width_extended = self.logo_width
        elif width == self.logo_width:
            width_extended = self.max_width
        else:
            return
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width_extended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
