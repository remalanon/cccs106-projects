# CCCS 106 - Week 2 Lab Exercise
# Enhanced GUI Calculator using Flet
# Student: Remar Malanon

import flet as ft

def main(page: ft.Page):
    page.title = "Enhanced Calculator"
    page.window.width = 350
    page.window.height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Display area
    display = ft.TextField(
        value="",
        text_align=ft.TextAlign.RIGHT,
        width=300,
        read_only=True,
        border_color=ft.Colors.BLUE_300,
        bgcolor=ft.Colors.GREY_100,
        color=ft.Colors.BLACK,
        height=60
    )

    # Function to update display
    def update_display(value):
        display.value += value
        page.update()

    # Function to clear display
    def clear_display(e):
        display.value = ""
        page.update()

    # Function to backspace
    def backspace(e):
        display.value = display.value[:-1]
        page.update()

    # Function to calculate result
    def calculate(e):
        try:
            result = str(eval(display.value))
            display.value = result
        except ZeroDivisionError:
            display.value = "Error: Div by 0"
        except Exception:
            display.value = "Error"
        page.update()

    # Button builder
    def create_button(text, on_click, bgcolor=ft.Colors.BLUE_600):
        return ft.ElevatedButton(
            text,
            on_click=on_click,
            width=60,
            height=60,
            bgcolor=bgcolor,
            color=ft.Colors.WHITE
        )

    # Create buttons with events
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    button_rows = []
    for row in buttons:
        row_buttons = []
        for btn in row:
            if btn == "=":
                row_buttons.append(create_button(btn, calculate, bgcolor=ft.Colors.GREEN_600))
            else:
                row_buttons.append(
                    create_button(btn, lambda e, b=btn: update_display(b))
                )
        button_rows.append(ft.Row(row_buttons, alignment=ft.MainAxisAlignment.CENTER, spacing=10))

    # Extra controls row
    controls_row = ft.Row([
        create_button("C", clear_display, bgcolor=ft.Colors.RED_600),
        create_button("⌫", backspace, bgcolor=ft.Colors.GREY_700),
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    # Layout
    page.add(
        ft.Column([
            ft.Text("Enhanced Calculator", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            display,
            ft.Divider(),
            controls_row,
            *button_rows
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
