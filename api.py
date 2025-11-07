from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")

location = None


def fetch_weather_data():
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json" #TODO: Get Weather API to return organized weather information in a dict from the JSON



@app.route('/weather', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET': #TODO: Work on getting API to get requests for different cities in the URL
        return jsonify({"Message": "this is a get test"})
    if request.method == "POST": #TODO: Get the post request to send back data from the Weather API to send processed weather data back.
        return jsonify({"message": "this is a post test"})
    

if __name__ == '__main__':
    app.run(debug=True)