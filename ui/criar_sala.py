from __future__ import annotations

from typing import TYPE_CHECKING

import customtkinter as ctk
import requests

from systems.network import NetworkManager
from ui.base_screen import BaseScreen

if TYPE_CHECKING:
    from systems.navigation import NavigationManager


class CriarSalaScreen(BaseScreen):
    """Screen for creating a room through the online backend."""

    def __init__(self, master: ctk.CTk, navigator: NavigationManager) -> None:
        super().__init__(master, navigator)
        self.network = NetworkManager()
        self.create_button: ctk.CTkButton | None = None
        self.result_label: ctk.CTkLabel | None = None
        self._build_layout()

    def _build_layout(self) -> None:
        container = self.create_centered_panel(width=420)

        title = ctk.CTkLabel(
            container,
            text="Criar Sala",
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        title.grid(row=0, column=0, padx=40, pady=(36, 12))

        description = ctk.CTkLabel(
            container,
            text="Gere um c\u00f3digo de sala pelo servidor online.",
            text_color="#A8A8A8",
            font=ctk.CTkFont(size=15),
        )
        description.grid(row=1, column=0, padx=40, pady=(0, 24))

        self.create_button = ctk.CTkButton(
            container,
            text="Criar Sala",
            command=self._create_room,
            height=46,
            corner_radius=14,
            font=ctk.CTkFont(size=15, weight="bold"),
        )
        self.create_button.grid(row=2, column=0, padx=40, pady=(0, 16), sticky="ew")

        self.result_label = ctk.CTkLabel(
            container,
            text="",
            text_color="#D6D6D6",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        self.result_label.grid(row=3, column=0, padx=40, pady=(0, 20))

        back_button = ctk.CTkButton(
            container,
            text="Voltar",
            command=self._go_back,
            height=46,
            corner_radius=14,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#343638",
            hover_color="#3F4144",
        )
        back_button.grid(row=4, column=0, padx=40, pady=(0, 36), sticky="ew")

    def _create_room(self) -> None:
        if self.result_label is None:
            return

        self._set_loading_state(is_loading=True)

        try:
            room_code = self.network.create_room()
        except requests.RequestException:
            self.result_label.configure(text="Erro ao conectar ao servidor")
            self._set_loading_state(is_loading=False)
            return

        self.result_label.configure(text=f"C\u00f3digo da Sala: {room_code}")
        self._set_loading_state(is_loading=False)
        print(f"Sala criada: {room_code}")

    def _set_loading_state(self, is_loading: bool) -> None:
        if self.create_button is None or self.result_label is None:
            return

        if is_loading:
            self.create_button.configure(state="disabled", text="Criando...")
            self.result_label.configure(text="Carregando...")
            self.update_idletasks()
            return

        self.create_button.configure(state="normal", text="Criar Sala")

    def _go_back(self) -> None:
        from ui.main_menu import MainMenuScreen

        print("Voltando para o menu principal.")
        self.navigator.show(MainMenuScreen)
