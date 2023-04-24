from pymongo import MongoClient
from config import config

username = config.MONGO_USER
password = config.MONGO_PASSWORD
host = config.MONGO_HOST
port = config.MONGO_PORT
client: MongoClient = MongoClient(
    f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
)
db = client.quoridor_environment
collection = db.games
