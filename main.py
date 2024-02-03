from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from view.main_windows import FastCaseWindows


class FastCaseApp(QApplication):
    def __init__(self):
        super().__init__()
        self.__init_set()

        self.layout = FastCaseWindows()
        self.layout.show()

    def __init_set(self):
        """
        初始化app设置
        :return:
        """
        self.setWindowIcon(QIcon('icon.ico'))
        # self.setQuitOnLastWindowClosed(False)
        self.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)


if __name__ == '__main__':
    app = FastCaseApp()
    app.exec()
