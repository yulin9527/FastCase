import flet as ft

import settings


class LeftRail(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.pages = []
        self.dest_list = []
        self.expand = True
        for rail in settings.rail_page:
            self.dest_list.append(
                ft.NavigationRailDestination(
                    icon=rail.icon,
                    selected_icon=rail.selected_icon,
                    label=rail.label
                ),
            )
            self.pages.append(rail.page)

        self.rail = None

    def build(self):
        self.rail = ft.NavigationRail(
            selected_index=0,
            # extended=True,
            label_type=ft.NavigationRailLabelType.ALL,
            destinations=self.dest_list,
            on_change=self.dest_change,
        )
        return ft.Row(
            controls=[
                self.rail,
                ft.VerticalDivider(width=1),
                ft.Column(self.pages),
            ],
            expand=True,
            spacing=1,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

    async def dest_change(self, *args):
        for index, p in enumerate(self.pages):
            p.visible = True if index == self.rail.selected_index else False
        await self.update_async()
