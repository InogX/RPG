from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Sala:
    """Base room model."""

    nome: str = ""
    jogadores: list[str] = field(default_factory=list)
