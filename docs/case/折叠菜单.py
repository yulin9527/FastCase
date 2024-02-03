import sys

import qdarkstyle
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QWidget, QToolBox, QVBoxLayout, QLabel, QPushButton
from qdarkstyle import LightPalette
from qt_material import apply_stylesheet


class AddTabLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(QLabel('---'))
        self.mainLayout.addWidget(QPushButton('按钮'))

        self.setLayout(self.mainLayout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.toolBox = QToolBox()

        def createSubWindow(tab_label):
            subwindow = AddTabLayout()
            # subwindow.setAutoFillBackground(True)
            # subwindow.setBackgroundRole(
            #     QPalette.Background)
            # subwindow.setFixedHeight(50)
            # subwindow.setStyleSheet(
            #     "QToolBox::tab{background-color: blue; color: white;}")

            self.toolBox.addItem(subwindow, tab_label)

        # self.toolBox.addItem(AddTabLayout(), '选项卡 1')
        # self.toolBox.addItem(AddTabLayout(), '2')
        # self.toolBox.addItem(AddTabLayout(), '3')
        createSubWindow('Tab 1')
        createSubWindow('Tab 2')
        createSubWindow('Tab 3')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.toolBox)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    # apply_stylesheet(window, theme='dark_blue.xml')
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette))
    window.show()
    sys.exit(app.exec())
