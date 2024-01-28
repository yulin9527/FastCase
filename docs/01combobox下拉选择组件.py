from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QWidget, QVBoxLayout

"""
最基础的框架
"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QComboBox()
        cb.addItems(['arya', '9527'])
        cb1 = QComboBox()
        cb1.addItems(['11', '21', '31', '51', '61'])
        main_layout = QVBoxLayout()
        main_layout.addWidget(cb)
        main_layout.addWidget(cb1)
        self.setLayout(main_layout)

        cb.currentIndexChanged.connect(self.show_name)
        cb1.currentTextChanged.connect(self.show_name)

    def show_name(self, name):
        print(name)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
