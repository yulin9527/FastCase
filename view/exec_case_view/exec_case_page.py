import flet as ft


class ExecCasePage(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.new_task = ft.TextField(hint_text='New Task', expand=True)
        self.tasks = ft.Column()
        return ft.Column(
            width=600, controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        # ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)
                    ]
                ),
                self.tasks
            ]
        )
