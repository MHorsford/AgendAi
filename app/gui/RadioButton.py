import flet as ft


class RadioButton(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.radio = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Text("Alarme Diario?"),
                    ft.Radio(label="Sim", value="True"),
                    ft.Radio(label="Não", value="False"),
                    ft.ElevatedButton(text="Submit", on_click=self.submit)
                ]
            )
        )

        self.controls = [
            self.radio,
        ]

    def submit(self, e):
        self.radio.value = True if self.radio.value == "True" else False
