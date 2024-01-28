import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QApplication


class WorkThread(QThread):
    signal = Signal(object)

    def run(self):
        for i in range(10):
            self.signal.emit(str(i))
            time.sleep(1)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.lb = QLabel(f'当前的值为:0')

        self.work = WorkThread()
        self.work.signal.connect(lambda x: self.lb.setText(x))

        self.work.started.connect(lambda: print('线程开始执行'))
        self.work.finished.connect(lambda: print('线程执行结束'))
        self.work.finished.connect(lambda: self.work.deleteLater())

        self.work.start()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lb)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
