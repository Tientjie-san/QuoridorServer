from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_USER: str
    MONGO_PASSWORD: str


config = Config()
