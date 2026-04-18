from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Personagem:
    """Base character model."""

    nome: str = ""
    classe: str = ""
