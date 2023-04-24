from db import collection
from models import CreateGame, ReadGame
from datetime import datetime


class GameRepository:
    def get_games(self) -> list[ReadGame]:
        return [ReadGame(**game) for game in collection.find()]

    def get_game_by_id(self, game_id) -> ReadGame:
        game = collection.find_one({"game_id": game_id})
        if game is None:
            return None
        return ReadGame(**game)

    def create_game(self, game: CreateGame) -> ReadGame:
        game_id = collection.count_documents({}) + 1
        game = ReadGame(**game.dict(), game_id=game_id, datetime=datetime.utcnow())
        collection.insert_one(game.dict())
        return game

    def get_latest_games(self, nr: int) -> list[ReadGame]:
        return [
            ReadGame(**game)
            for game in collection.find().sort("datetime", -1).limit(nr)
        ]
