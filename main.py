import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Погода"
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme_mode = 'dark'
    page.theme = ft.Theme(font_family="FulboArgenta")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def get_citi(e):
        api = 'd85caf3173240e68f83e5aa3fde096ce'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_cyti.value}&appid={api}&units=metric'
        res = requests.get(url).json()
        temp = res['main']['temp']
        name = res['name']
        windspeed = res['wind']['speed']
        cloud_count = res['clouds']['all']
        weath.value = f'Город: {name} Темпиратура: {temp} Скорость ветра: {windspeed} Облоков: {cloud_count}'
        print(res)
        page.update()

    user_cyti = ft.TextField(label='Ваш город', width=444)
    weath = ft.Text('')

    def chan_th(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.MODE, on_click=chan_th, icon_color='grey')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_cyti], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weath], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.TextButton(text='Какая погода?', on_click=get_citi)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
