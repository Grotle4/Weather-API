import json
from flask import jsonify, request
from get_weather_api import fetch_weather_data
import redis
from dotenv import load_dotenv
import os


def check_cache(cached_value, location):
    load_dotenv()

    api_key = os.getenv("API_KEY")
    redis_port = os.getenv("REDIS_PORT")
    redis_name = os.getenv("REDIS_HOST")

    r = redis.StrictRedis(host=redis_name, port=redis_port, db=0, decode_responses=True)

    cached_value = r.get(location)

    if cached_value:
        print(f"recieved from cache") #TODO: Clean up print statements and look into proper logging
        decoded_value = json.loads(cached_value)
        return decoded_value
    else:
        weather = fetch_weather_data(location, api_key)
        weather_json = json.dumps(weather)
        r.set(location, weather_json, ex=600) #Remember to set this back to 12 hours after testing complete
        print("new location found")
        return weather
    

