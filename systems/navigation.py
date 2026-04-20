from __future__ import annotations

from typing import Any, Type

import customtkinter as ctk


class NavigationManager:
    """Handles screen creation and ensures only one is visible at a time."""

    def __init__(self, root: ctk.CTk) -> None:
        self.root = root
        self.current_screen: ctk.CTkFrame | None = None

    def show(
        self,
        screen_class: Type[ctk.CTkFrame],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Replace the current frame with the requested screen."""
        self._clear_current_screen()
        self.current_screen = screen_class(self.root, self, *args, **kwargs)
        self.current_screen.pack(fill="both", expand=True)

    def _clear_current_screen(self) -> None:
        if self.current_screen is not None:
            self.current_screen.destroy()
            self.current_screen = None

    def close_app(self) -> None:
        self.root.destroy()
