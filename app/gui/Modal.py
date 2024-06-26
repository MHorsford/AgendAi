import flet as ft
from app.gui.DateTime import DateTime
from app.gui.RadioButton import RadioButton
from app.gui.Inputs import Inputs
from app.dao.taskDAO import TaskDAO


class Modal(ft.UserControl):
    def __init__(self, page, on_task_modified):
        super().__init__()
        self.page = page
        self.on_task_modified = on_task_modified
        self.task = {}
        self.dao = TaskDAO()
        self.name = Inputs("Nome")
        self.description = Inputs("Descricão")
        self.date_time = DateTime()
        self.daly_alarm = RadioButton()
        self.modal = ft.AlertDialog(
            modal=True,
            adaptive=True,
            title=ft.Container(
                content=ft.Text("Modo Edição"),
                alignment=ft.alignment.center,
                margin=ft.margin.only(0, 0, 0, 0),
            ),
            content=ft.Column(
                [
                    ft.Container(
                        content=self.name,
                        width=750,
                        alignment=ft.alignment.center,
                        adaptive=True,
                    ),
                    ft.Container(
                        content=self.description,
                        width=750,
                        alignment=ft.alignment.center,
                        adaptive=True,
                    ),
                    ft.Container(
                        content=self.date_time,
                        width=750,
                        alignment=ft.alignment.center,
                        adaptive=True,
                    ),
                    ft.Container(
                        content=self.daly_alarm,
                        width=750,
                        alignment=ft.alignment.center,
                        adaptive=True,
                    ),
                ]
            ),
            actions=[
                ft.TextButton("Salvar", on_click=self.save_task),
                ft.TextButton("Cancelar", on_click=self.close_modal),
            ],
            on_dismiss=lambda e: print("Modal dismissed!"),
        )
        self.update()

    def set_task(self):
        self.name.set_value(self.task['Name'])
        self.description.set_value(self.task['Description'])
        self.date_time.set_value(self.task['DateTime'])
        self.daly_alarm.set_value(self.task['DalyAlarm'])
        self.update()

    def reload_task(self):
        pass

    def open_modal(self, e):
        self.set_task()
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()

    def save_task(self, e):
        self.dao.modify_task(
            ID=self.task['ID'],
            Name=self.name.get_value(),
            Description=self.description.get_value(),
            DateTime=self.date_time.get_value(),
            DalyAlarm=self.daly_alarm.get_value(),
        )
        self.modal.open = False
        self.on_task_modified()
        self.page.update()

    def close_modal(self, e):
        self.modal.open = False
        self.page.update()
