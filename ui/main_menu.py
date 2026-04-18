from __future__ import annotations

from typing import TYPE_CHECKING

import customtkinter as ctk

from ui.base_screen import BaseScreen

if TYPE_CHECKING:
    from systems.navigation import NavigationManager


class MainMenuScreen(BaseScreen):
    """Main menu screen for the application."""

    def __init__(self, master: ctk.CTk, navigator: NavigationManager) -> None:
        super().__init__(master, navigator)
        self._build_layout()

    def _build_layout(self) -> None:
        container = self.create_centered_panel(width=360)

        title = ctk.CTkLabel(
            container,
            text="RPG App",
            font=ctk.CTkFont(size=34, weight="bold"),
        )
        title.grid(row=0, column=0, padx=40, pady=(36, 10))

        subtitle = ctk.CTkLabel(
            container,
            text="Menu Principal",
            text_color="#A8A8A8",
            font=ctk.CTkFont(size=15),
        )
        subtitle.grid(row=1, column=0, padx=40, pady=(0, 28))

        buttons = [
            ("Modo Offline", self._on_offline_mode),
            ("Entrar na Sala", self._on_join_room),
            ("Criar Sala", self._on_create_room),
            ("Configura\u00e7\u00f5es", self._on_settings),
            ("Sair", self._on_exit),
        ]

        for index, (label, command) in enumerate(buttons, start=2):
            button = ctk.CTkButton(
                container,
                text=label,
                command=command,
                width=260,
                height=48,
                corner_radius=14,
                font=ctk.CTkFont(size=16, weight="bold"),
            )
            button.grid(row=index, column=0, padx=40, pady=8, sticky="ew")

        container.grid_rowconfigure(len(buttons) + 2, minsize=28)

    def _on_offline_mode(self) -> None:
        print("Modo Offline clicado.")

    def _on_join_room(self) -> None:
        from ui.entrar_sala import EntrarSalaScreen

        print("Entrar na Sala clicado.")
        self.navigator.show(EntrarSalaScreen)

    def _on_create_room(self) -> None:
        from ui.criar_sala import CriarSalaScreen

        print("Criar Sala clicado.")
        self.navigator.show(CriarSalaScreen)

    def _on_settings(self) -> None:
        print("Configura\u00e7\u00f5es clicado.")

    def _on_exit(self) -> None:
        print("Sair clicado.")
        self.navigator.close_app()
