from PySide6.QtWidgets import QApplication, QMainWindow

from core.lifespan import Lifespan
from layout.layout_main import FastCaseWindowsLayout


class FastCaseWindows(FastCaseWindowsLayout):
    def __init__(self, ):
        super().__init__()


if __name__ == '__main__':
    with Lifespan() as loop:
        app = QApplication([])
        window = FastCaseWindows()
        window.show()
        app.exec()
