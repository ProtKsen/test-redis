import json
from http import HTTPStatus, client

import redis
from flask import Blueprint, request

from src.config import config
from src.db import db_session
from src.models import Temperature

view = Blueprint('weather', __name__)


@view.get('/')
def get_weather():
    args = request.args.to_dict()
    city = args['city']
    conn = client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': config.weather_api.key,
        'X-RapidAPI-Host': config.weather_api.host
    }

    conn.request("GET", f"/current.json?q={city}", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read())
    tempreture = data['current']['temp_c']

    return f'Temperature: {tempreture}C', HTTPStatus.OK


@view.get('/cache/')
def get_cached_weather():
    args = request.args.to_dict()
    city = args['city']

    redis_client = redis.Redis(
        host=config.cache.host,
        port=config.cache.port
    )

    # if exist return caching value
    if redis_client.exists(city):
        tempreture = redis_client.get(city).decode('utf-8')
        return f'Temperature: {tempreture}C', HTTPStatus.OK

    # send request to api
    conn = client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': config.weather_api.key,
        'X-RapidAPI-Host': config.weather_api.host
    }

    conn.request("GET", f"/current.json?q={city}", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read())
    tempreture = data['current']['temp_c']

    # cache data
    redis_client.set(city, tempreture, ex=120)

    return f'Temperature: {tempreture}C', HTTPStatus.OK


@view.get('/postgres/')
def get_weather_from_db():
    args = request.args.to_dict()
    city = args['city']

    temperature = Temperature.query.filter(Temperature.city == city).all()

    if temperature:
        return f'Temperature: {temperature[0].value}C', HTTPStatus.OK

    conn = client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': config.weather_api.key,
        'X-RapidAPI-Host': config.weather_api.host
    }

    conn.request("GET", f"/current.json?q={city}", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read())
    temperature = data['current']['temp_c']

    new_temperature = Temperature(city=city, value=temperature)
    db_session.add(new_temperature)
    db_session.commit()

    return f'Temperature: {temperature}C', HTTPStatus.OK
