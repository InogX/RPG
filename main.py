from __future__ import annotations

import customtkinter as ctk

from systems.navigation import NavigationManager
from ui.main_menu import MainMenuScreen


def main() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("RPG App")
    app.geometry("1000x700")
    app.minsize(1000, 700)

    navigator = NavigationManager(app)
    navigator.show(MainMenuScreen)

    app.mainloop()


if __name__ == "__main__":
    main()
