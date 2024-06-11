import flet as ft


class RadioButton(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.radio = ft.RadioGroup(
            value="True",
            on_change=lambda e: self.replace_value(e),
            content=ft.Column(
                [
                    ft.Text("Alarme Diario?"),
                    ft.Radio(label="Sim", value="True"),
                    ft.Radio(label="Não", value="False"),
                ]
            )
        )
        self.save_button = ft.ElevatedButton(
            text="SALVAR",
            on_click=self.save,
            bgcolor='#316FA4',
            color='#FFFFFF',
        )
        self.edit_button = ft.ElevatedButton(
            text="EDITAR",
            on_click=self.edit,
            disabled=True,
            visible=False,
            bgcolor='#316FA4',
            color='#FFFFFF',
        )
        self.replace_value(None)

    def build(self):
        return ft.Column(
            [
                self.radio,
                #self.save_button,
                #self.edit_button
            ]
        )

    def replace_value(self, e):
        self.radio.value = 1 if self.radio.value == "True" else 0

    def save(self, e):
        self.radio.disabled = True
        self.save_button.disabled = True
        self.edit_button.disabled = False
        self.save_button.visible = False
        self.edit_button.visible = True
        self.update()

    def edit(self, e):
        self.radio.disabled = False
        self.save_button.disabled = False
        self.edit_button.disabled = True
        self.save_button.visible = True
        self.edit_button.visible = False
        self.update()

    def get_value(self):
        return self.radio.value
