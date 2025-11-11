from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import redis
import json
from get_weather_api import fetch_weather_data
from cache_data import check_cache



app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")
redis_port = os.getenv("REDIS_PORT")
redis_name = os.getenv("REDIS_HOST")
print(redis_port)

location = "Oregon" #TODO: Change this to be user inputted using query parameters

r = redis.StrictRedis(host=redis_name, port=redis_port, db=0, decode_responses=True) #Remember to start redis manually before running, wont work otherwise
#TODO: Add redis information to .env to allow for easy configuration
#TODO: Look into unit testing as well

try:
    r.ping()
    print("connected")
except redis.exceptions.ConnectionError as e:
    print(f"could not connect: {e}")
    

@app.route('/weather', methods=['GET', 'POST'])
def handle_data(): #TODO: Add a limit to how many times a user can make a request in quick succession to keep traffic managable
    if request.method == 'GET':
        cached_value = r.get(location) #TODO: Set seperate python file to handle caching to redis then return data to API
        decoded_value = check_cache(cached_value, location, api_key, redis_port, redis_name)
        return jsonify(decoded_value)
    if request.method == "POST": #TODO: Get the post request to send back data from the Weather API to send processed weather data back.
        return jsonify({"message": "this is a post test"})
    

if __name__ == '__main__':
    app.run(debug=True)