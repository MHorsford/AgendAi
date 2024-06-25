import flet as ft


class Notification(ft.UserControl):
    def __init__(self, title: str = '', content: str = '', page=None):
        super().__init__()
        self.page = page
        self.notification = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(content),
            actions=[
                ft.TextButton("Ok", on_click=self.close_notification),
            ],
            on_dismiss=lambda e: None,
        )

    def build(self):
        return self.notification

    def open_notification(self, e):
        self.page.dialog = self.notification
        self.notification.open = True
        self.update()

    def close_notification(self, e):
        self.notification.open = False
        self.update()

    def update_value(self, title: str, content: str):
        self.notification.title.value = title
        self.notification.content.value = content


