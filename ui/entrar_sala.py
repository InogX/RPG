from __future__ import annotations

from typing import TYPE_CHECKING

import customtkinter as ctk
import requests

from systems.config import SERVER_URL
from ui.base_screen import BaseScreen

if TYPE_CHECKING:
    from systems.navigation import NavigationManager


class EntrarSalaScreen(BaseScreen):
    """Screen for entering a room code before joining."""

    def __init__(self, master: ctk.CTk, navigator: NavigationManager) -> None:
        super().__init__(master, navigator)
        self.codigo_entry: ctk.CTkEntry | None = None
        self.feedback_label: ctk.CTkLabel | None = None
        self._build_layout()

    def _build_layout(self) -> None:
        container = self.create_centered_panel(width=420)

        title = ctk.CTkLabel(
            container,
            text="Entrar na Sala",
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        title.grid(row=0, column=0, padx=40, pady=(36, 12))

        description = ctk.CTkLabel(
            container,
            text="Digite o c\u00f3digo da sala para entrar.",
            text_color="#A8A8A8",
            font=ctk.CTkFont(size=15),
        )
        description.grid(row=1, column=0, padx=40, pady=(0, 24))

        self.codigo_entry = ctk.CTkEntry(
            container,
            width=280,
            height=44,
            corner_radius=12,
            placeholder_text="C\u00f3digo da Sala",
            font=ctk.CTkFont(size=15),
        )
        self.codigo_entry.grid(row=2, column=0, padx=40, pady=(0, 20), sticky="ew")

        self.feedback_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#A8A8A8",
        )
        self.feedback_label.grid(row=3, column=0, padx=40, pady=(0, 16))

        entrar_button = ctk.CTkButton(
            container,
            text="Entrar",
            command=self._enter_room,
            height=46,
            corner_radius=14,
            font=ctk.CTkFont(size=15, weight="bold"),
        )
        entrar_button.grid(row=4, column=0, padx=40, pady=(0, 10), sticky="ew")

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
        back_button.grid(row=5, column=0, padx=40, pady=(0, 36), sticky="ew")

    def _enter_room(self) -> None:
        if self.codigo_entry is None or self.feedback_label is None:
            return

        codigo = self.codigo_entry.get().strip().upper()

        if not codigo:
            self._set_feedback("Digite um código de sala", "#E05A5A")
            return

        self._set_feedback("Conectando...", "#A8A8A8")

        try:
            response = requests.post(
                f"{SERVER_URL}/join_room",
                json={"room_code": codigo},
                timeout=5,
            )
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as e:
            print(f"Erro de conexão: {e}")
            self._set_feedback("Erro ao conectar ao servidor", "#E05A5A")
            return

        if data and data.get("status") == "ok":
            self._set_feedback("Código válido! Entrando...", "#52C779")
            from ui.lobby import LobbyScreen
            self.navigator.show(LobbyScreen, room_code=codigo)
            return

        self._set_feedback("Código inválido", "#E05A5A")

    def _set_feedback(self, message: str, color: str) -> None:
        if self.feedback_label is None:
            return

        self.feedback_label.configure(text=message, text_color=color)

    def _go_back(self) -> None:
        from ui.main_menu import MainMenuScreen

        print("Voltando para o menu principal.")
        self.navigator.show(MainMenuScreen)
