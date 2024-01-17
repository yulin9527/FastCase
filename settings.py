import collections
import flet as ft
from flet_core import icons
from view.exec_case_view.exec_case_page import ExecCasePage
from view.home_view.home_page import HomePage
from view.set_view.set_page import SetPage


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
    RailPage(label=' 首 页 ', icon=icons.HOME_MINI, selected_icon=icons.HOME_MINI_OUTLINED, page=HomePage()),
    RailPage(label='查看用例', icon=icons.HOME_MINI, selected_icon=icons.HOME_MINI_OUTLINED, page=HomePage()),
    RailPage(label='用例执行', icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, page=ExecCasePage()),
    RailPage(label='组网信息', icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, page=Demo()),
    RailPage(label=' 工 具 ', icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, page=Demo()),
    RailPage(label=' 设 置 ', icon=icons.SETTINGS, selected_icon=icons.SETTINGS_OUTLINED, page=SetPage()),
]
