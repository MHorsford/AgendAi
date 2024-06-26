import flet as ft
from app.dao.taskDAO import TaskDAO
from app.gui.Modal import Modal


class ListTask(ft.UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dao = TaskDAO()
        self.tasks = self.dao.get_task()
        self.modal = Modal(page, self.reload_task)
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

        self.action_sheet = ft.CupertinoActionSheet(
            title=ft.Text("Ações"),
            message=ft.Text("Escolha uma ação"),
            cancel=ft.CupertinoActionSheetAction(
                content=ft.Text("Cancelar"),
                on_click=lambda e: self.page.close_bottom_sheet()
            ),
            actions=[
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Editar"),
                    on_click=self.modal.open_modal
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Excluir", color="red"),
                    on_click=self.delete_task
                ),
            ]
        )
        self.load_task()
        self.update()

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
        self.data_table.rows.clear()
        for task in self.tasks:
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(content=ft.Text(str(task['ID']))),
                        ft.DataCell(content=ft.Text(task['Name'])),
                        ft.DataCell(content=ft.Text(task['DateTime'])),
                        ft.DataCell(content=ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                        ft.DataCell(
                            content=ft.IconButton(
                                icon=ft.icons.SETTINGS,
                                tooltip="Configurações",
                                icon_color=ft.colors.BLACK,
                                on_click=self.show_action_sheet,
                                data=task['ID'],
                            )
                        )
                    ],
                    color=self.colors[row_index % len(self.colors)],
                )
            )
            row_index += 1
            self.update()

    def reload_task(self):
        new_tasks = self.dao.get_task()
        if len(new_tasks) > len(self.tasks) or len(new_tasks) < len(self.tasks):
            self.tasks.clear()
            self.data_table.rows.clear()
            self.tasks = new_tasks
            self.load_task()
        if new_tasks != self.tasks:
            self.tasks.clear()
            self.tasks = new_tasks
            self.load_task()
        self.update()

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
                                ft.DataCell(content=ft.Text(str(task['ID']))),
                                ft.DataCell(content=ft.Text(task['Name'])),
                                ft.DataCell(content=ft.Text(task['DateTime'])),
                                ft.DataCell(content=ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                                ft.DataCell(
                                    content=ft.IconButton(
                                        icon=ft.icons.SETTINGS,
                                        tooltip="Configurações",
                                        icon_color=ft.colors.BLACK,
                                        on_click=self.show_action_sheet,
                                        data=task['ID'],
                                    )
                                )
                            ],
                            color=self.colors[row_index % len(self.colors)]
                        )
                    )
                    row_index += 1
                    self.update()
                    self.page.update()
            else:
                self.datanotfound.visible = True
                self.update()
                self.page.update()
        else:
            self.datanotfound.visible = False
            row_index = 1
            for task in self.tasks:
                self.data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(content=ft.Text(str(task['ID']))),
                            ft.DataCell(content=ft.Text(task['Name'])),
                            ft.DataCell(content=ft.Text(task['DateTime'])),
                            ft.DataCell(content=ft.Text("Sim" if task['DalyAlarm'] else "Não")),
                            ft.DataCell(
                                content=ft.IconButton(
                                    icon=ft.icons.SETTINGS,
                                    tooltip="Configurações",
                                    icon_color=ft.colors.BLACK,
                                    on_click=self.show_action_sheet,
                                    data=task['ID'],
                                )
                            )
                        ],
                        color=self.colors[row_index % len(self.colors)]
                    )
                )
                row_index += 1
            self.update()
            self.page.update()
        self.update()

    def show_action_sheet(self, e: ft.ControlEvent):
        self.tasks_id = e.control.data
        self.selected_task()
        self.page.show_bottom_sheet(
            ft.CupertinoBottomSheet(self.action_sheet)
        )
        self.update()

    def selected_task(self):
        for task in self.tasks:
            if task['ID'] == self.tasks_id:
                self.modal.task = task
                break

    def delete_task(self, e):
        self.dao.del_task(self.tasks_id)
        self.reload_task()
        self.update()
