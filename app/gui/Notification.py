import flet as ft


class Notification(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.notification = ft.AlertDialog(
            modal=True,
            title=ft.Text("Notificação"),
            content=ft.Text("Conteudo da notificação"),
            actions=[
                ft.TextButton("Fechar", on_click=self.close_notification),
            ],
        )
        pass

    def open_notification(self, e, title, content):
        self.notification.title = ft.Text(title)
        self.notification.content = ft.Text(content)
        self.page.dialog = self.notification
        self.notification.open = True
        self.page.update()

    def close_notification(self, e):
        self.notification.open = False
        self.page.update()




