import flet as ft


class HomePage(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Text("Hello World")
