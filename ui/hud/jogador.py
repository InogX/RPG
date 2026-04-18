from __future__ import annotations

import customtkinter as ctk


class JogadorHUD(ctk.CTkFrame):
    """Placeholder HUD for player-specific controls."""

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master, fg_color="transparent")
