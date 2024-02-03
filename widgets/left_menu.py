import qtawesome as qta
from PySide6.QtCore import QPropertyAnimation, QSize, QRect, Qt
from PySide6.QtGui import QPalette, QColor, QCursor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QSizePolicy
import settings as st
from widgets.functions import UiFunctions


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class LeftMenuWidget(QFrame):

    def __init__(self):
        super().__init__()
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 192, 203))  # 使用RGB颜色值设置背景颜色
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.setMaximumWidth(60)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.top_logo_info = QFrame(self)
        self.top_logo_info.setMaximumHeight(50)

        self.top_logo = QFrame(self.top_logo_info)
        self.top_logo.setGeometry(QRect(10, 5, 42, 42))
        self.top_logo.setMinimumSize(QSize(42, 42))
        self.top_logo.setMaximumSize(QSize(42, 42))

        self.title_left_app = QLabel(self.top_logo_info)
        self.title_left_app.setText(st.FAST_CASE_NAME)
        self.title_left_app.setGeometry(QRect(70, 8, 160, 20))
        self.title_left_app.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.title_left_desc = QLabel(self.top_logo_info)
        self.title_left_desc.setText(st.FAST_CASE_DESCRIPTION)
        self.title_left_desc.setGeometry(QRect(70, 27, 160, 16))
        self.title_left_desc.setMaximumHeight(16)
        self.title_left_desc.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.layout.addWidget(self.top_logo_info)

        # 左侧菜单栏
        self.toggle_box = QFrame(self)
        self.toggle_box.setMaximumHeight(45)
        self.toggle_box_Layout = QVBoxLayout(self.toggle_box)
        self.toggle_box_Layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_box_Layout.setSpacing(0)

        self.toggle_button = QPushButton(self.toggle_box)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(size_policy)
        self.toggle_button.setMinimumSize(QSize(0, 45))
        # self.toggle_button.setFont(font)
        self.toggle_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_button.setLayoutDirection(Qt.LeftToRight)
        self.toggle_button.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggle_box_Layout.addWidget(self.toggle_button)
        self.layout.addWidget(self.toggle_box)

        self.top_menu = QFrame(self)
        self.top_menu_layout = QVBoxLayout(self.top_menu)
        self.top_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.top_menu_layout.setSpacing(0)

        self.btn_home = QPushButton(self.top_menu)
        size_policy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(size_policy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        self.top_menu_layout.addWidget(self.btn_home)

        self.top_menu_layout.addWidget(QFrame())
        self.layout.addWidget(self.top_menu)
        self.layout.addWidget(QFrame())

        # self.btn_home = QPushButton()
        # self.btn_home.setStyleSheet("""
        #     QPushButton {
        #         border: none; /* 或者 border-width: 0; */
        #     }
        # """)
        #
        # # icon = QIcon(QPixmap(':/icons/images/icons/icon_menu.png'))
        # icon = qta.icon('mdi.home-analytics')
        # print(icon)
        # self.btn_home.setIcon(icon)
        # self.btn_home.setIconSize(QSize(24, 24))
        # self.btn_home.clicked.connect(lambda: UiFunctions.extend_animation(self, 120, 60))
        # self.layout.addWidget(self.btn_home)
        # self.layout.addWidget(Color('red'))
        # # self.layout.addWidget(QWidget())
        # # self.layout.spacerItem()
        # self.btn_settings = QPushButton('Settings', )
        # animation = qta.Spin(self.btn_settings)
        # spin_icon = qta.icon('fa5s.spinner', color='red', animation=animation)
        # self.btn_settings.setIcon(spin_icon)
        #
        # styling_icon = qta.icon('fa5s.camera', 'fa5s.ban',
        #                         options=[{'scale_factor': 0.5,
        #                                   'active': 'fa5s.balance-scale'},
        #                                  {'color': 'red'}])
        # self.layout.addWidget(QPushButton(styling_icon, 'stying'))
        #
        # self.layout.addWidget(self.btn_settings)
        #
        # self.animation = QPropertyAnimation(self, b"minimumWidth")
