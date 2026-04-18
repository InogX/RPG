from __future__ import annotations

import customtkinter as ctk

from systems.navigation import NavigationManager


class BaseScreen(ctk.CTkFrame):
    """Base class shared by all screens."""

    def __init__(self, master: ctk.CTk, navigator: NavigationManager) -> None:
        super().__init__(master, fg_color="#1a1a1a")
        self.navigator = navigator
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_centered_panel(self, width: int = 360) -> ctk.CTkFrame:
        """Create a reusable centered card-style container."""
        panel = ctk.CTkFrame(
            self,
            width=width,
            corner_radius=24,
            fg_color="#242424",
            border_width=1,
            border_color="#313131",
        )
        panel.grid(row=0, column=0)
        panel.grid_columnconfigure(0, weight=1)
        return panel
