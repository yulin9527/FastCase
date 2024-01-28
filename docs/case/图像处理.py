from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from PIL import Image, ImageDraw, ImageFont, ImageQt

"""
最基础的框架
"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("导入图片", )
        self.btn.clicked.connect(self.get_img)

        self.show_img = QLabel()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.show_img)
        self.setLayout(self.main_layout)
    def get_img(self):
        print(123)
        self.img = Image.open(QFileDialog.getOpenFileName(self, '')[0])
        self.show_img.setPixmap(ImageQt.toqpixmap(self.img))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
