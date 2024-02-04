from PySide6.QtCore import QRect, QSize, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPalette, QColor, QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget

import settings as st
from view.functions import Functions


class ContentBox(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QStackedWidget(self)

        widget1 = QFrame()
        widget1_layout = QHBoxLayout(widget1)
        widget1_layout.addWidget(QPushButton('第一个页面'))
        widget2 = QFrame()
        widget2_layout = QHBoxLayout(widget2)
        widget2_layout.addWidget(QPushButton('第二个页面'))
        widget3 = QFrame()
        widget3_layout = QHBoxLayout(widget3)
        widget3_layout.addWidget(QPushButton('第三个页面'))
        self.layout.addWidget(widget1)
        self.layout.addWidget(widget2)
        self.layout.addWidget(widget3)

        self.layout.setCurrentIndex(2)


class RightBoxWidget(QFrame):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        Functions.set_widget_marg(obj=self.layout)

        self.top_info = QFrame(self)
        self.top_layout = QHBoxLayout(self.top_info)

        self.lab_des = QLabel()
        self.lab_des.setText(st.FAST_CASE_DESCRIPTION)

        self.btn_msg = QPushButton()
        self.btn_minimize_app = QPushButton()
        self.btn_maximize_app = QPushButton()
        self.btn_close_app = QPushButton()

        self.foot_info = QFrame(self)
        self.foot_layout = QHBoxLayout(self.foot_info)

        self.lab_credits = QLabel()
        self.lab_credits.setText(st.CREDITS)

        self.lab_version = QLabel()
        self.lab_version.setText(st.VERSIONS)

        self.top_box_layout()

        self.layout.addWidget(ContentBox())

        self.foot_box_layout()

    def top_box_layout(self):
        self.top_info.setFixedHeight(40)
        Functions.set_widget_marg(obj=self.top_layout, left=15, right=15)

        self.top_layout.addWidget(self.lab_des)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.btn_msg)
        self.top_layout.addWidget(self.btn_minimize_app)
        self.top_layout.addWidget(self.btn_maximize_app)
        self.top_layout.addWidget(self.btn_close_app)

        self.layout.addWidget(self.top_info)

    def foot_box_layout(self):
        self.foot_info.setFixedHeight(30)
        Functions.set_widget_marg(obj=self.foot_layout, left=15, right=15)

        self.foot_layout.addWidget(self.lab_credits)
        self.foot_layout.addStretch()
        self.foot_layout.addWidget(self.lab_version)
        self.layout.addWidget(self.foot_info)
