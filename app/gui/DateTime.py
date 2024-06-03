
from datetime import datetime
import flet as ft


class DateTime(ft.UserControl):
    def __init__(self):
        super().__init__()
        # Date
        self.date_selector = ft.DatePicker(
            first_date=datetime(2020, 1, 1),
            last_date=None,
            confirm_text="Confirmar",
            cancel_text="Cancelar",
            on_change=self.change_date_time,
        )
        self.date_button = ft.ElevatedButton(
            text="Data", icon=ft.icons.CALENDAR_MONTH, on_click=self.on_date_button_click,
            bgcolor=ft.colors.BLUE, icon_color=ft.colors.WHITE, color=ft.colors.WHITE,
            width=200, height=40,
            adaptive=True,
            expand=True,
            expand_loose=True
        )
        # Time
        self.time_selector = ft.TimePicker(
            confirm_text="Confirmar",
            cancel_text="Cancelar",
            on_change=self.change_date_time,
        )
        self.time_button = ft.ElevatedButton(
            text="Hora", icon=ft.icons.ACCESS_TIME, on_click=self.on_time_button_click,
            bgcolor=ft.colors.BLUE, icon_color=ft.colors.WHITE, color=ft.colors.WHITE,
            width=200, height=40,
            adaptive=True,
            expand=True,
            expand_loose=True

        )
        # Field
        self.field = ft.TextField(
            label="Data & Hora", disabled=True,
            border_radius=ft.border_radius.all(10),
            icon=ft.icons.CALENDAR_MONTH, border=ft.InputBorder.OUTLINE,
            width=None, height=40,
            adaptive=True,
        )

        self.responsive = ft.ResponsiveRow(
            [
                ft.Column(
                    controls=[
                        self.field
                    ],
                    col={"xs": 12, "sm": 8, "md": 6, "lg": 5, "xl": 4},
                ),
                ft.Column(
                    controls=[
                        self.date_button,
                    ],
                    col={"xs": 6, "sm": 4, "md": 3, "lg": 2.5, "xl": 2},

                    adaptive=True

                ),
                ft.Column(
                    controls=[
                        self.time_button,
                    ],
                    col={"xs": 6, "sm": 4, "md": 3, "lg": 2.5, "xl": 3},
                    adaptive=True
                ),
            ],
            spacing=10,
        )
        # Controls
        self.controls = [
            self.responsive,
            self.time_selector,
            self.date_selector,
        ]

    async def on_date_button_click(self, e):
        await self.date_selector.pick_date_async()

    async def on_time_button_click(self, e):
        await self.time_selector.pick_time_async()

    def change_date_time(self, e):
        time_value = self.time_selector.value
        date_value = self.date_selector.value.date()
        if time_value is not None:
            time_value = time_value.strftime("%H:%M:%S")
        if date_value is not None:
            date_value = date_value.strftime("%Y-%m-%d")
        self.field.value = f"{date_value} {time_value}"
        self.update()

    def get_value(self):
        return self.field.value


