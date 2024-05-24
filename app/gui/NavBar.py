def home(self):
    return ft.Column(
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
                width=500,

            ),
        ],
        adaptive=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,

    )