from pydantic import BaseModel
from datetime import datetime


class CreateGame(BaseModel):
    pgn: str


class ReadGame(BaseModel):
    game_id: int
    pgn: str
    datetime: datetime
