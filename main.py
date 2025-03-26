import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera aplicación con Flet"
    page.add(ft.Text("¡Hola, gente de la informática!"))


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=30002)