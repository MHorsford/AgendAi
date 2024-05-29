import flet as ft
from app.dao.taskDAO import TaskDAO


class ListTask(ft.UserControl):

    def __init__(self):
        super().__init__()

        self.tasks = TaskDAO().get_task()

        self.data_table = ft.DataTable(
            border=ft.border.all(2, "#FFFFFF"),
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Data e Hora")),
                ft.DataColumn(ft.Text("Alarme Diário?")),
                ft.DataColumn(ft.Text("Ações")),
            ],
            rows=[

            ]
        )
        self.load_task()
        self.controls = [
            self.data_table
        ]

    def load_task(self):
        for task in self.tasks:
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(task['ID']))),
                        ft.DataCell(ft.Text(task['Name'])),
                        ft.DataCell(ft.Text(task['Description'])),
                        ft.DataCell(ft.Text(task['DateTime'])),
                        ft.DataCell(ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                        ft.DataCell(ft.Text("Editar/Deletar"))
                    ]
                )
            )


