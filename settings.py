import collections
import flet as ft
from flet_core import icons


class Demo(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.visible = False

    def build(self):
        return ft.Column(
            controls=[
                ft.Text('arya'),
                ft.Icon('arrow-left'),
                ft.Icon('arrow-right'),
                ft.Text('arya'),
                ft.Text('arya'),
            ]
        )


RailPage = collections.namedtuple('RailPage', ['label', 'icon', 'selected_icon', 'page'])
rail_page = [
    RailPage(label='首页', icon=icons.HOME_MINI, selected_icon=icons.HOME_MINI_OUTLINED, page=Demo()),
    RailPage(label='用例执行', icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, page=Demo()),
    RailPage(label='demo', icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, page=Demo()),
    RailPage(label='设置', icon=icons.SETTINGS, selected_icon=icons.SETTINGS_OUTLINED, page=Demo()),
]
