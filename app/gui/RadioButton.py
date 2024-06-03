import flet as ft


class RadioButton(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.radio = ft.RadioGroup(
            value=None,
            on_change=lambda e: self.submit(e),
            content=ft.Column(
                [
                    ft.Text("Alarme Diario?"),
                    ft.Radio(label="Sim", value="True"),
                    ft.Radio(label="Não", value="False"),
                ]
            )
        )
        self.save_button = ft.ElevatedButton(
            text="SAVE",
            on_click=self.save
        )
        self.edit_button = ft.ElevatedButton(
            text="EDIT",
            on_click=self.edit,
            disabled=True,
            visible=False
        )
        """
        bug: ao cickar sem selecionar o radio altera o valor para 0 mesmo com true selecionado
        """

    def build(self):
        return ft.Column(
            [
                self.radio,
                self.save_button,
                self.edit_button
            ]
        )

    def submit(self, e):
        self.radio.value = 1 if self.radio.value == "True" else 0
        print(self.radio.value)

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
        print(self.radio.value)
        return self.radio.value
