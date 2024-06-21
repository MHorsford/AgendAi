import flet as ft
from app.gui.DateTime import DateTime
from app.gui.RadioButton import RadioButton
from app.gui.Inputs import Inputs


class Modal(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Modo Edição"),
            content=ft.Text("Edite a Tarefa"),
            actions=[
                ft.TextButton("Salvar", on_click=self.save_task),
                ft.TextButton("Cancelar", on_click=self.close_modal),
            ],
            on_dismiss=lambda e: None,
        )

    def open_modal(self, e):
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()

    def save_task(self, e):
        self.modal.open = False
        self.page.update()

    def close_modal(self, e):
        self.modal.open = False
        self.page.update()

