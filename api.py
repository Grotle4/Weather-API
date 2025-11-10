from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import redis
import json



app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")

location = "New Jersey" #TODO: Change this to be user inputted using query parameters

r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True) #Remember to start redis manually before running, wont work otherwise
#TODO: Add redis information to .env to allow for easy configuration
#TODO: Add a ping when redis is called in the script to test for proper connectivity, look into unit testing as well

try:
    r.ping()
    print("connected")
except redis.exceptions.ConnectionError as e:
    print(f"could not connect: {e}")
    


def fetch_weather_data(): #TODO: Check to make sure location is a valid location and return 400 Bad Requests for an incorrect location
    print("running") #TODO: Split logic into seperate python files for easy control and managment
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json" #add back location later
    
    print(request_url)

    response = requests.get(request_url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data



@app.route('/weather', methods=['GET', 'POST']) #TODO: Add error handling in cases where api crashes, times out or returns an error code and return to client
def handle_data(): #TODO: Add a limit to how many times a user can make a request in quick succession to keep traffic managable
    if request.method == 'GET':
        cached_value = r.get(location) #TODO: Set seperate python file to handle caching to redis then return data to API
        if cached_value:
            print(f"recieved from cache") #TODO: Clean up print statements and look into proper logging
            decoded_value = json.loads(cached_value)
            return jsonify(decoded_value)
        else:
            weather = fetch_weather_data()
            weather_json = json.dumps(weather)
            r.set(location, weather_json, ex=43200) #TODO: Make this shorter for testing
            print("new location found")
            return jsonify(weather) #TODO: Look into proper wrapping for responses that will includes fields like location, source or data.
    if request.method == "POST": #TODO: Get the post request to send back data from the Weather API to send processed weather data back.
        return jsonify({"message": "this is a post test"})
    

if __name__ == '__main__':

    app.run(debug=True)