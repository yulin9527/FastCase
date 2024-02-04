from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout

import settings as st
from view.left_menu_view import LeftMenuWidget
from view.right_box import RightBoxWidget


class FastCaseWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.drag_pos = None
        self.__init_set()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.left_menu = LeftMenuWidget()
        self.layout.addWidget(self.left_menu)
        self.right_box = RightBoxWidget()
        self.layout.addWidget(self.right_box)

        self.definitions()

    def btn_maximized(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def definitions(self):
        def _click_maximize_restore(event):
            """
            设置鼠标双击事件
            :param event:
            :return:
            """
            QTimer.singleShot(250, self.btn_maximized)

        self.right_box.top_info.mouseDoubleClickEvent = _click_maximize_restore

        def move_windows(event):
            # 设置鼠标移动事件
            if event.button() == Qt.NoButton:
                self.move(self.pos() + event.globalPos() - self.drag_pos)
                self.drag_pos = event.globalPos()
                event.accept()

        self.right_box.top_info.mouseMoveEvent = move_windows

        self.right_box.btn_msg.clicked.connect(lambda: print('点击了 msg 按钮'))
        self.right_box.btn_minimize_app.clicked.connect(self.showMinimized)
        self.right_box.btn_maximize_app.clicked.connect(self.btn_maximized)
        self.right_box.btn_close_app.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()
        if event.button() == Qt.LeftButton:
            print('左键点击')
        elif event.button() == Qt.RightButton:
            print('右键点击')

    def __init_set(self):
        self.resize(st.MAIN_WIDTH, st.MAIN_HEIGHT)
        self.setMinimumSize(QSize(st.MAIN_MIN_WIDTH, st.MAIN_MIN_HEIGHT))
        self.setWindowFlags(Qt.FramelessWindowHint)
