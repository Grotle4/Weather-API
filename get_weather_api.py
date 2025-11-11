import requests

def fetch_weather_data(location, api_key): #TODO: Check to make sure location is a valid location and return 400 Bad Requests for an incorrect location
    try:
        base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

        request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json" #add back location later
        
        print(request_url)

        response = requests.get(request_url)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            return data
    except requests.exceptions.Timeout as errt:
        print(f"A Timeout Error occurred: {errt}")
    except requests.exceptions.ConnectionError as errc:
        print(f"A Connection Error occurred: {errc}")
    except requests.exceptions.HTTPError as errh:
        print(f"A HTTP Error occurred: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"An Unknown Error occurred: {err}")
