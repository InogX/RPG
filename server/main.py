from __future__ import annotations

import random
import string

from fastapi import FastAPI

app = FastAPI()

rooms: dict[str, dict] = {}


def generate_room_code(length: int = 6) -> str:
    alphabet = string.ascii_uppercase + string.digits
    while True:
        code = "".join(random.choices(alphabet, k=length))
        if code not in rooms:
            return code


@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "online"}


@app.post("/create_room")
def create_room() -> dict[str, str]:
    room_code = generate_room_code()
    rooms[room_code] = {}
    return {"room_code": room_code}


@app.post("/join_room")
def join_room(room_code: str) -> dict[str, str]:
    if room_code in rooms:
        return {"status": "ok"}
    return {"status": "error", "message": "Room not found"}


# 🚀 Rodar localmente (opcional)
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server.main:app", host="0.0.0.0", port=port)