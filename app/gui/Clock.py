import asyncio
import flet as ft
import time


class Clock(ft.Text):
    def __init__(self, **kwargs):
        super().__init__()
        self.running = False
        self.font_family = kwargs.get('font_family', None)
        self.color = '#FFD43B'
        self.size = 40
        self.text_align = ft.TextAlign.CENTER

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_time)

    def will_unmount(self):
        self.running = False

    async def update_time(self):
        while self.running:
            now = time.strftime('%H:%M:%S %p %d/%m/%Y')
            self.value = now
            self.update()
            await asyncio.sleep(1)

