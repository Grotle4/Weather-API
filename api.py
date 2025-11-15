from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import redis
from cache_data import check_cache


app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")
redis_port = os.getenv("REDIS_PORT")
redis_name = os.getenv("REDIS_HOST")
print(redis_port)

r = redis.StrictRedis(host=redis_name, port=redis_port, db=0, decode_responses=True) #Remember to start redis manually before running, wont work otherwise
#TODO: Look into unit testing as well

def ping_test(r):
    try:
        r.ping()
        print("connected")
    except redis.exceptions.ConnectionError as e:
        print(f"could not connect: {e}")

ping_test(r)

def check_rate(r):
    request_limit = 10
    time_period = 10

    pipe = r.pipeline()
    pipe.incr("default")
    pipe.expire("default" ,time_period)
    try:
        count, _ = pipe.execute()
    except redis.exceptions.ConnectionError as e:
        print(f"Connection Error")
        return True

    if count > request_limit:
        print("Connection Allowed")
        return False
    else:
        return True


@app.route('/weather', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        if check_rate(r):
            location = request.args.get('location')
            print(location)
            cached_value = r.get(location)
            decoded_value = check_cache(cached_value, location)
            return jsonify(decoded_value)
        else:
            print("Too many requests")
            return jsonify("Too many requests, try again in a few seconds")
    if request.method == "POST": #TODO: Get the post request to send back data from the Weather API to send processed weather data back.
        return jsonify({"message": "this is a post test"})
    

if __name__ == '__main__':
    app.run(debug=True)