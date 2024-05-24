import os.path

import flet as ft
from DateTime import DateTime
from os import path
from Clock import Clock
from RadioButton import RadioButton
from Inputs import Inputs


class GUI:
    def __init__(self, page: ft.Page):
        super().__init__()
        page.title = "AgendAi"
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.window_min_width = 360
        page.window_min_height = 290
        page.adaptive = True
        print(f'Tema: {page.theme_mode.value}')

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
        self.home_ = self.home()
        self.add_task_ = self.add_task()
        self.about_ = self.about()
        page.add(
            self.home_,
            self.add_task_,
            self.about_,
        )
        self.page.update()

    def change_page(self, e):
        index = self.page.navigation_bar.selected_index
        self.home_.visible = True if index == 0 else False
        self.home_.disabled = False if index == 0 else True
        self.add_task_.visible = True if index == 1 else False
        self.add_task_.disabled = False if index == 1 else True
        self.about_.visible = True if index == 3 else False
        self.about_.disabled = False if index == 3 else True
        self.page.update()

    def home(self):
        return ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Text(
                        "Home",
                        size=35,
                        weight=ft.FontWeight.BOLD,
                    ),
                    padding=ft.padding.only(top=10),
                ),
                ft.Container(
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
                    alignment=ft.alignment.center,
                    col={"xs": 14, "sm": 10, "md": 8, "lg": 7, "xl": 5}
                ),
            ],
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
                    content=Inputs("Adicionar Tarefa"),
                    margin=ft.margin.only(10, 20, 0, 0),
                ),
                ft.Container(
                    content=Inputs("Descrição"),
                    margin=ft.margin.only(10, 40, 0, 0),
                ),
                ft.Container(
                    content=DateTime(),
                    margin=ft.margin.only(10, 40, 0, 0),
                ),
                ft.Container(
                    content=RadioButton(),
                    margin=ft.margin.only(10, 50, 0, 0),
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


ft.app(target=GUI)