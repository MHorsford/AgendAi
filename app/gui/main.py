import os.path

import flet as ft
from DateTime import DateTime
from Clock import Clock
from RadioButton import RadioButton
from Inputs import Inputs
from ListTask import ListTask
from app.dao.taskDAO import TaskDAO
from Notification import Notification


class GUI:
    def __init__(self, page: ft.Page):
        super().__init__()
        page.title = "AgendAi"
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.window_min_width = 360
        page.window_min_height = 290
        page.adaptive = True
        page.scroll = ft.ScrollMode.AUTO

        page.fonts = {
            'Alarm Clock': os.path.join('../assets/fonts/alarm clock/alarm_clock.ttf'),
        }

        page.navigation_bar = ft.NavigationBar(
            selected_index=0,
            on_change=self.change_page,
            bgcolor=ft.colors.BACKGROUND,
            height=60,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.HOME,
                    label="Home",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.ADD,
                    label="Adicionar Tarefa",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.LIST,
                    label="Tarefas",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.INFO,
                    label="Sobre",
                    disabled=True,
                ),
            ],
        )
        self.page = page
        self.name_input = Inputs("Nome")
        self.description_input = Inputs("Descrição")
        self.date_time_input = DateTime()
        self.radio_button_input = RadioButton()

        self.home_ = self.home()
        self.add_task_ = self.add_task()
        self.about_ = self.about()
        self.list_task_ = self.list_task()

        self.notification = Notification()
        page.dialog = self.notification.notification

        page.add(
            self.home_,
            self.add_task_,
            self.about_,
            self.list_task_,
            self.notification,
        )
        self.page.update()

    def change_page(self, e):
        index = self.page.navigation_bar.selected_index
        self.home_.visible = True if index == 0 else False
        self.home_.disabled = False if index == 0 else True
        self.add_task_.visible = True if index == 1 else False
        self.add_task_.disabled = False if index == 1 else True
        self.list_task_.visible = True if index == 2 else False
        self.list_task_.disabled = False if index == 2 else True
        self.about_.visible = True if index == 3 else False
        self.about_.disabled = False if index == 3 else True
        self.page.update()

    def home(self):
        return ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Image(
                        src=os.path.join('../assets/img/logohome.png'),
                        width=30,
                        height=90,
                    ),
                    bgcolor='red',
                    padding=ft.padding.only(top=10),
                    col={"xs": 12, "sm": 12, "md": 12, "lg": 12, "xl": 12}
                ),
                ft.Container(
                    adaptive=True,
                    content=Clock(font_family="Alarm Clock"),
                    padding=ft.padding.only(10, 10, 10, 10),
                    border=ft.border.all(2, '#FFFFFF'),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=1,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color='#306998',
                    ),
                    bgcolor='#306998',
                    col={"xs": 10, "sm": 9, "md": 7.5, "lg": 6.5, "xl": 5.5}
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def add_task(self):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "Adicionar Tarefa",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                    ),
                    alignment=ft.alignment.top_center,
                ),
                ft.Container(
                    content=self.name_input,
                    margin=ft.margin.only(10, 20, 0, 0),
                ),
                ft.Container(
                    content=self.description_input,
                    margin=ft.margin.only(10, 40, 0, 0),
                ),
                ft.Container(
                    content=self.date_time_input,
                    margin=ft.margin.only(10, 40, 0, 0),
                ),
                ft.Container(
                    content=self.radio_button_input,
                    margin=ft.margin.only(10, 50, 0, 0),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        "Adicionar Tarefa",
                        on_click=self.add_task_event,
                    ),
                    margin=ft.margin.only(10, 20, 0, 10),
                ),
            ],
            visible=False
        )

    def list_task(self):
        return ft.Column(
            [
                ft.Container(
                    content=ListTask(),
                )
            ],
            visible=False
        )

    def about(self):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "Sobre o AgendAí",
                        size=35,
                        weight=ft.FontWeight.BOLD,
                    ),
                    alignment=ft.alignment.top_left,
                    margin=ft.margin.only(0, 20, 0, 0)
                ),
                ft.Container(
                    content=ft.Text(
                        "O AgendAí é uma aplicação desenvolvida para facilitar a organização de suas tarefas e "
                        "compromissos diários. Nosso objetivo é fornecer uma ferramenta intuitiva e eficiente para "
                        "ajudar você a gerenciar seu tempo e aumentar sua produtividade.",
                        size=20,
                        weight=ft.FontWeight.NORMAL,
                        text_align=ft.TextAlign.JUSTIFY,
                        width=850,
                    ),
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(0, 100, 0, 0)
                ),
                ft.Container(
                    content=ft.Text(
                        value="Equipe:",
                        size=20,
                        weight=ft.FontWeight.NORMAL,
                        text_align=ft.TextAlign.JUSTIFY,
                        width=850,
                    ),
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(0, 100, 0, 0)
                ),
                ft.Container(
                    content=ft.Text(
                        value="Versão Atual: 1.1.1",
                        size=20,
                        weight=ft.FontWeight.NORMAL,
                        text_align=ft.TextAlign.JUSTIFY,
                        width=850,
                    ),
                    alignment=ft.alignment.bottom_left,
                    margin=ft.margin.only(0, 100, 0, 0)
                ),
            ],
            visible=False
        )

    def system(self):
        pass

    def add_task_event(self, e):
        dao = TaskDAO()
        task_exists = False
        for task in dao.get_task():
            if (task['Name'] == self.name_input.get_value() and
                    task['DateTime'] == self.date_time_input.get_value() and
                    bool(task['DalyAlarm']) == self.radio_button_input.get_value()):
                task_exists = True
                break

        if not task_exists:
            dao.set_task(
                self.name_input.get_value(),
                self.description_input.get_value(),
                self.date_time_input.get_value(),
                self.radio_button_input.get_value()
            )
            self.clear_event()
            self.notification.update_value('Sistema', 'Tarefa adicionada com sucesso!')
            self.notification.open_notification(e)
            self.page.update()
        else:
            self.clear_event()
            self.notification.update_value('Sistema', 'Tarefa ja existe!')
            self.notification.open_notification(e)
            self.page.update()
        dao.load_task()

    def clear_event(self):
        self.name_input.value = ""
        self.description_input.value = ""
        self.date_time_input.value = ""
        self.radio_button_input.value = ""


ft.app(target=GUI)
