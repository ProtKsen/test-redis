import os

from pydantic import BaseModel


class Server(BaseModel):
    port: int
    host: str


class WeatherApi(BaseModel):
    key: str
    host: str


class Redis(BaseModel):
    port: str
    host: str


class DataBase(BaseModel):
    url: str


class AppConfig(BaseModel):
    server: Server
    weather_api: WeatherApi
    cache: Redis
    db: DataBase


def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    weather_api_kye = os.environ['X_RapidAPI_Key']
    weather_api_host = os.environ['X_RapidAPI_Host']
    redis_port = os.environ['REDIS_PORT']
    redis_host = os.environ['REDIS_HOST']
    db_url = os.environ['DB_URL']
    return AppConfig(
        server=Server(port=app_port, host=app_host),
        weather_api=WeatherApi(key=weather_api_kye, host=weather_api_host),
        cache=Redis(port=redis_port, host=redis_host),
        db=DataBase(url=db_url)
        )


config = load_from_env()
