import flet as ft
import mysql.connector
from db_connection import connect_db

def main(page: ft.Page):
    # Page setup
    page.title = "User Login"
    page.window_width = 400
    page.window_height = 350
    page.window_frameless = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_ACCENT

    # UI controls
    title = ft.Text("User Login", size=20, weight=ft.FontWeight.BOLD, font_family="Arial", color=ft.Colors.BLACK)

    username = ft.TextField(
        label="User name",
        hint_text="Enter your user name",
        helper_text="This is your unique identifier",
        width=300,
        autofocus=True,
        icon=ft.Icon(name=ft.Icons.PERSON, color=ft.Colors.BLACK),
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        helper_style=ft.TextStyle(color=ft.Colors.BLACK),
        hint_style=ft.TextStyle(color=ft.Colors.BLACK)
    )

    password = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        helper_text="This is your secret key",
        width=300,
        password=True,
        can_reveal_password=True,
        icon=ft.Icon(name=ft.Icons.LOCK, color=ft.Colors.BLACK),
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        helper_style=ft.TextStyle(color=ft.Colors.BLACK),
        hint_style=ft.TextStyle(color=ft.Colors.BLACK)

    )

    def login_click(e):
        user = username.value.strip()
        pwd = password.value.strip() 
        color=ft.Colors.BLACK

        # Dialogs
        success_dialog = ft.AlertDialog(
            title=ft.Text("Login Successful"),
            content=ft.Text(f"Welcome, {user}!", text_align=ft.TextAlign.CENTER), 
            actions=[ft.TextButton("OK", on_click=lambda _: page.close(control= success_dialog))],
            icon=ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN),
        )
        failure_dialog = ft.AlertDialog(
            title=ft.Text("Login Failed"),
            content=ft.Text("Invalid username or password", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda _: page.close(control= failure_dialog))],
            icon=ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED),
        )
        invalid_input_dialog = ft.AlertDialog(
            title=ft.Text("Input Error"),
            content=ft.Text("Please enter username and password", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=lambda _: page.close(control= invalid_input_dialog))],
            icon=ft.Icon(ft.Icons.INFO, color=ft.Colors.BLUE),
        )
        database_error_dialog = ft.AlertDialog(
            title=ft.Text("Database Error"),
            content=ft.Text("An error occurred while connecting to the database"),
            actions=[ft.TextButton("OK", on_click=lambda _: page.close(control= database_error_dialog))],
        )

        if not user or not pwd:
            page.open(invalid_input_dialog)
            return

        try:
            conn = connect_db()
            if conn is None:
                page.open(database_error_dialog)
                return

            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (user, pwd))
            result = cursor.fetchone()
            conn.close()

            if result:
                page.open(success_dialog)

            else:
                page.open(failure_dialog)



        except mysql.connector.Error:
            page.open(database_error_dialog)

    login_btn = ft.ElevatedButton(
        text="Login",
        icon=ft.Icons.LOGIN,
        width=100,
        on_click=login_click,
    )

    # Layout
    page.add(
        title,
        ft.Container(
            content=ft.Column([username, password], spacing=20)
        ),
        ft.Container(
            content=login_btn,
            margin=ft.margin.only(top=20, right=40),
            alignment=ft.alignment.top_right,
        )
    )

ft.app(target=main)
