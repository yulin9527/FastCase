import flet as ft
from core.lifespan import Lifespan
from view.left_rail import LeftRail


async def main(page: ft.Page):
    # 设置标题
    page.title = "TestCase"
    # 设置窗口大小
    page.window_width = 800
    page.window_height = 600
    # 设置窗口居中
    await page.window_center_async()
    # 设置主题模式
    page.theme_mode = ft.ThemeMode.LIGHT
    # 设置水平与垂直对齐
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # 设置边距
    page.padding = 0

    left_view = LeftRail()
    await page.add_async(left_view)
    await page.update_async()


if __name__ == '__main__':
    with Lifespan():
        ft.app(target=main)
