from typing import Optional
from fastapi import FastAPI
import uvicorn
from config import config
from repository import GameRepository
from models import CreateGame, ReadGame

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/games", response_model=list[ReadGame])
async def get_games():
    return GameRepository().get_games()


@app.post("/games", response_model=ReadGame)
async def create_game(game: CreateGame):
    return GameRepository().create_game(game)


@app.get("/games/latest", response_model=list[ReadGame])
async def get_latest_game(nr: int = 1):
    """Returns the latest game(s) specified by the nr parameter."""
    return GameRepository().get_latest_games(nr)


@app.get("/games/{game_id}", response_model=Optional[ReadGame])
async def get_game(game_id: int):
    return GameRepository().get_game_by_id(game_id)


def main():
    uvicorn.run(
        app="main:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
