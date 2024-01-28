from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, \
    QLineEdit
from PIL import Image, ImageDraw, ImageFont, ImageQt

"""
创建一个信号

类中定义信号

信号绑定

激活信号
"""


class MyWindow(QWidget):
    send_value = Signal(object)

    def __init__(self):
        super().__init__()

        self.lineEdit = QLineEdit()
        self.btn = QPushButton("发送")
        self.show_windows = ShowWin()

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.lineEdit)
        self.main_layout.addWidget(self.btn)

        self.setLayout(self.main_layout)

        self.bind()

    def bind(self):
        self.subwindows = ShowWin()
        self.subwindows.show()

        self.send_value.connect(self.subwindows.lineEdit.setText)
        self.btn.clicked.connect(self.sendvalue)

    def sendvalue(self):
        text = self.lineEdit.text()
        self.send_value.emit(text)

class ShowWin(QWidget):
    def __init__(self):
        super().__init__()

        self.head = QLabel('子窗口')
        self.lineEdit = QLineEdit(self)
        self.setMinimumSize(400, 300)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()


