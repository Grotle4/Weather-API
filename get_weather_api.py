import requests

def fetch_weather_data(location, api_key):
    try:
        base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

        request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json"
        
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

def weather_test(location, api_key):
        base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

        request_url = f"{base_url}{location}?unitGroup=us&key={api_key}&contentType=json"
        
        print(request_url)

        response = requests.get(request_url)

        if response.status_code == 401:
             return False
        else:
             return True