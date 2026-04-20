from __future__ import annotations

import requests


class NetworkManager:
    """Handles HTTP communication with the backend server."""

    def __init__(self, base_url: str = "https://revenge.up.railway.app") -> None:
        self.base_url = base_url.rstrip("/")

    def create_room(self) -> str:
        """Request a new room code from the backend."""
        response = requests.post(f"{self.base_url}/create_room", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["room_code"]
