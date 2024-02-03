import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QWidget, QVBoxLayout, QCheckBox
from PySide6.QtCore import QCoreApplication, QFile, QTextStream
from qdarkstyle import LightPalette

"""
最基础的框架
"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QCheckBox()
        cb.stateChanged.connect(lambda x: print(x))
        main_layout = QVBoxLayout()
        btn = QPushButton("状态检测")
        main_layout.addWidget(cb)
        main_layout.addWidget(btn)
        btn.clicked.connect(lambda :print(cb.isChecked()))
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette))
    window.show()
    app.exec()
