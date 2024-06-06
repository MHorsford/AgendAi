import flet as ft


class Inputs(ft.Row):
    def __init__(self, text_input, **kwargs):
        super().__init__()
        self.expand = True
        self.icon_name = kwargs.get('icon', None)
        self.text_field = ft.TextField(
            label=text_input, disabled=True, multiline=True,
            border_radius=ft.border_radius.all(10),
            adaptive=True, expand=True,
            icon=self.icon_selector(), border_color='#316FA4',
            max_length=kwargs.get('max_length', None),
        )
        self.edit_button = ft.IconButton(
            icon=ft.icons.EDIT,
            visible=True,
            disabled=False,
            on_click=self.edit,
            adaptive=True,
        )
        self.save_button = ft.IconButton(
            icon=ft.icons.SAVE,
            visible=False,
            disabled=True,
            on_click=self.save,
            adaptive=True,
        )
        self.controls = [
            self.text_field,
            self.edit_button,
            self.save_button,
        ]

    def save(self, e):
        self.save_button.visible = False
        self.save_button.disabled = True
        self.edit_button.visible = True
        self.edit_button.disabled = False
        self.text_field.disabled = True
        self.update()

    def edit(self, e):
        self.edit_button.visible = False
        self.edit_button.disabled = True
        self.save_button.visible = True
        self.save_button.disabled = False
        self.text_field.disabled = False
        self.text_field.value = self.text_field.value
        self.update()

    def icon_selector(self):
        if self.icon_name is not None:
            icon = getattr(ft.icons, self.icon_name)
            return icon
        icon = ft.icons.DRIVE_FILE_RENAME_OUTLINE_SHARP
        return icon

    def get_value(self):
        return self.text_field.value


