# Weather API

This project is a simple Flask-based web API that provides weather data for a specified location. It integrates with the Visual Crossing Weather API to fetch real-time and forecast data. To optimize performance and reduce external API calls, it utilizes Redis for caching responses and implementing a basic rate-limiting mechanism.

## Features

- **Weather Data Retrieval:** Fetches current weather data for any location via the `/weather` endpoint.
- **Redis Caching:** Caches successful API responses in Redis for 10 minutes to provide faster subsequent lookups and reduce external API load.
- **Rate Limiting:** Implements a simple request counter in Redis, limiting clients to 10 requests per 10-second window to prevent abuse.

## Technology Stack

- **Backend:** Python, Flask
- **Caching & Rate Limiting:** Redis
- **Data Source:** Visual Crossing Weather API

## Setup and Installation

### Prerequisites

- Python 3.x
- A running Redis instance
- An API key from [Visual Crossing Weather](https://www.visualcrossing.com/weather-api)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/grotle4/weather-api.git
    cd weather-api
    ```

2.  **Install dependencies:**
    This project requires `Flask`, `redis`, `python-dotenv`, and `requests`. You can install them using pip:
    ```bash
    pip install Flask redis python-dotenv requests
    ```

3.  **Set up environment variables:**
    Create a file named `.env` in the root directory and add credentials and configuration for the Redis server and the weather API.
    ```
    API_KEY="YOUR_VISUAL_CROSSING_API_KEY"
    REDIS_HOST="localhost"
    REDIS_PORT=6379
    ```

## Running the Application

To start the Flask development server, ensure your Redis server is running and then execute the `api.py` script:

```bash
python api.py
```

The application will start on `http://127.0.0.1:5000`.

## API Usage

### GET /weather

Fetches weather data for a given location. The first request for a location retrieves data from the Visual Crossing API, and the response is then cached. Subsequent requests for the same location within 10 minutes are served from the cache.

**Query Parameters:**
- `location` (string, required): The city or area for which to retrieve weather data (e.g., `Paris`, `Tokyo`).

**Example Request:**
```bash
curl "http://127.0.0.1:5000/weather?location=London"
```

**Success Response:**
A JSON object containing detailed weather data from the Visual Crossing API.

**Error Response (Rate Limit Exceeded):**
If more than 10 requests are made within a 10-second window, the API will return a JSON message:
```json
"Too many requests, try again in a few seconds"
```

## Testing

The repository includes basic unit tests to verify the Redis connection and the validity of the provided weather API key.

To run the tests, execute the `test_api.py` script:
```bash
python test_api.py
```
## Inspiration
https://roadmap.sh/projects/weather-api-wrapper-service