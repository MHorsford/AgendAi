import flet as ft
from app.dao.taskDAO import TaskDAO


class ListTask(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.dao = TaskDAO()
        self.tasks = self.dao.get_task()
        self.adaptive = True
        self.colors = ['#316FA4', '#F0CA33']
        self.search = ft.TextField(
            label="Pesquisar",
            border_color="#245076",
            border=ft.border.all(1, '#245076'),
            border_radius=ft.border_radius.only(10, 10, 0, 0),
            on_change=self.search_task,
            width=1000
        )
        self.datanotfound = ft.Text("Nenhuma Tarefa Encontrada")
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nome")),
                #ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Data e Hora")),
                ft.DataColumn(ft.Text("Alarme Diário?")),
                ft.DataColumn(ft.Text("Ações")),
            ],
            rows=[

            ],
            border=ft.border.all(1, '#245076'),
            expand=True,
            expand_loose=True,
            show_bottom_border=True,
            width=1000,
            heading_row_color='#245076',
            data_text_style=ft.TextStyle(color=ft.colors.BLACK),
        )
        self.load_task()

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.search,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.only(10, 20, 10, 0),
                    padding=ft.padding.only(0, 10, 0, 0),
                ),
                ft.Container(
                    content=self.datanotfound,
                    alignment=ft.alignment.center,
                    visible=False,
                    margin=ft.margin.only(0, 0, 0, 0),
                    padding=ft.padding.all(0),
                ),
                ft.Container(
                    content=self.data_table,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(10, 0, 10, 0),
                )
            ],
            spacing=0,
        )

    def load_task(self):
        row_index = 1
        for task in self.tasks:
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(task['ID']))),
                        ft.DataCell(ft.Text(task['Name'])),
                        #ft.DataCell(ft.Text(task['Description'])),
                        ft.DataCell(ft.Text(task['DateTime'])),
                        ft.DataCell(ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                        ft.DataCell(ft.Text("Editar/Deletar"))
                    ],
                    color=self.colors[row_index % len(self.colors)],
                )
            )
            row_index += 1

    def reload_task(self):
        new_tasks = self.dao.get_task()
        if len(new_tasks) > len(self.tasks) or len(new_tasks) < len(self.tasks):
            self.tasks = new_tasks
            self.load_task()

    def search_task(self, e):
        self.reload_task()
        search_name = self.search.value
        list_task = list(filter(lambda _: search_name in _['Name'], self.tasks))
        self.data_table.rows = []
        if not self.search.value == "":
            if len(list_task) > 0:
                self.datanotfound.visible = False
                row_index = 1
                for task in list_task:
                    self.data_table.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(str(task['ID']))),
                                ft.DataCell(ft.Text(task['Name'])),
                                #ft.DataCell(ft.Text(task['Description'])),
                                ft.DataCell(ft.Text(task['DateTime'])),
                                ft.DataCell(ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                                ft.DataCell(ft.Text("Editar/Deletar"))
                            ],
                            color=self.colors[row_index % len(self.colors)]
                        )
                    )
                    row_index += 1
                    self.update()
            else:
                self.datanotfound.visible = True
                self.update()
        else:
            self.datanotfound.visible = False
            row_index = 1
            for task in self.tasks:
                self.data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(task['ID']))),
                            ft.DataCell(ft.Text(task['Name'])),
                            #ft.DataCell(ft.Text(task['Description'])),
                            ft.DataCell(ft.Text(task['DateTime'])),
                            ft.DataCell(ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                            ft.DataCell(ft.Text("Editar/Deletar"))
                        ],
                        color=self.colors[row_index % len(self.colors)]
                    )
                )
                row_index += 1

            self.update()
