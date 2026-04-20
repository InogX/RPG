from __future__ import annotations

from typing import TYPE_CHECKING

import customtkinter as ctk

from ui.base_screen import BaseScreen

if TYPE_CHECKING:
    from systems.navigation import NavigationManager


class LobbyScreen(BaseScreen):
    """Lobby screen prepared for future dynamic room data."""

    def __init__(
        self,
        master: ctk.CTk,
        navigator: NavigationManager,
        room_code: str,
    ) -> None:
        super().__init__(master, navigator)
        self.room_code = room_code
        self.players = ["Player 1", "Player 2", "Player 3"]
        self._build_layout()

    def _build_layout(self) -> None:
        container = self.create_centered_panel(width=460)

        title = ctk.CTkLabel(
            container,
            text="Lobby da Sala",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        title.grid(row=0, column=0, padx=40, pady=(36, 12))

        room_code_label = ctk.CTkLabel(
            container,
            text=f"Código da Sala: {self.room_code}",
            text_color="#D6D6D6",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        room_code_label.grid(row=1, column=0, padx=40, pady=(0, 24))

        players_section = self._build_players_section(container)
        players_section.grid(row=2, column=0, padx=40, pady=(0, 24), sticky="ew")

        leave_button = ctk.CTkButton(
            container,
            text="Sair da Sala",
            command=self._leave_room,
            height=46,
            corner_radius=14,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#343638",
            hover_color="#3F4144",
        )
        leave_button.grid(row=3, column=0, padx=40, pady=(0, 36), sticky="ew")

    def _build_players_section(self, master: ctk.CTkFrame) -> ctk.CTkFrame:
        section = ctk.CTkFrame(
            master,
            corner_radius=18,
            fg_color="#1E1E1E",
            border_width=1,
            border_color="#2D2D2D",
        )
        section.grid_columnconfigure(0, weight=1)

        section_title = ctk.CTkLabel(
            section,
            text="Jogadores",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        section_title.grid(row=0, column=0, padx=24, pady=(20, 16), sticky="w")

        for index, player_name in enumerate(self.players, start=1):
            player_label = ctk.CTkLabel(
                section,
                text=player_name,
                anchor="w",
                font=ctk.CTkFont(size=16),
            )
            player_label.grid(row=index, column=0, padx=24, pady=6, sticky="ew")

        return section

    def _leave_room(self) -> None:
        from ui.main_menu import MainMenuScreen

        print("Saindo da sala.")
        self.navigator.show(MainMenuScreen)
