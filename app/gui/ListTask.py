import flet as ft
from app.dao.taskDAO import TaskDAO


class ListTask(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.dao = TaskDAO()
        self.tasks = self.dao.get_task()
        self.colors = [ft.colors.BLUE, ft.colors.RED]
        self.search = ft.TextField(label="Pesquisar", on_change=self.search_task)
        self.datanotfound = ft.Text("Nenhuma Tarefa Encontrada")
        self.data_table = ft.DataTable(
            width=1000,

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

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.search,
                    padding=ft.padding.all(10),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=self.datanotfound,
                    padding=ft.padding.all(10),
                    alignment=ft.alignment.center,
                    visible=False
                ),
                ft.Container(
                    content=self.data_table,
                    padding=ft.padding.all(10),
                    alignment=ft.alignment.center
                )
            ]
        )

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

    def search_task(self, e):
        search_name = self.search.value
        list_task = list(filter(lambda _: search_name in _['Name'], self.tasks))
        self.data_table.rows = []
        if not self.search.value == "":
            if len(list_task) > 0:
                self.datanotfound.visible = False
                for task in list_task:
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
                    self.update()
            else:
                self.datanotfound.visible = True
                self.update()
        else:
            self.datanotfound.visible = False
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

            self.update()
