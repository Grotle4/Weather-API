from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import redis
import json



app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")

location = "New York"

r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True) #Remember to start redis manually before running, wont work otherwise


try:
    r.ping()
    print("connected")
except redis.exceptions.ConnectionError as e:
    print(f"could not connect: {e}")
    


def fetch_weather_data():
    print("running")
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json" #add back location later
    
    print(request_url)

    response = requests.get(request_url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data



@app.route('/weather', methods=['GET', 'POST'])
def handle_data():
    for key in r.scan_iter():
        print(key)
    if request.method == 'GET': #TODO: Work on getting API to get requests for different cities in the URL
        cached_value = r.get(location)
        if cached_value:
            print(f"recieved from cache")
            return jsonify({f"Message cached"})
        else:
            weather = fetch_weather_data() #TODO: Fix this, no worky
            r.set(location, weather, ex=43200)
            print(r.get(location))
            return jsonify({f"Message": weather})
    if request.method == "POST": #TODO: Get the post request to send back data from the Weather API to send processed weather data back.
        return jsonify({"message": "this is a post test"})
    

if __name__ == '__main__':

    app.run(debug=True)