from __future__ import annotations

import customtkinter as ctk


class AdminHUD(ctk.CTkFrame):
    """Placeholder HUD for admin-specific controls."""

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master, fg_color="transparent")
