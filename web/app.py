from flask import Flask, render_template, request
import os
import requests
import psycopg2
import redis
import logging

app = Flask(__name__)

# Environment variables
db_url = os.environ.get('DATABASE_URL')
redis_url = os.environ.get('REDIS_URL')
api_key = os.environ.get('API_KEY')

# Initialize PostgreSQL connection
conn = psycopg2.connect(db_url)
cur = conn.cursor()

# Initialize Redis connection
r = redis.Redis.from_url(redis_url)

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY,
        city VARCHAR(50),
        temperature FLOAT,
        description VARCHAR(100),
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        logging.info(f'Received city: {city}')
        weather_data = get_weather(city)
        if weather_data:
            logging.info(f'Received weather data: {weather_data}')
            store_weather_data(city, weather_data['temp'], weather_data['description'])

    return render_template('index.html', weather=weather_data)

def get_weather(city):
    cache_key = f'weather:{city}'
    cached_data = r.get(cache_key)
    if cached_data:
        logging.info(f'Cache hit for {city}')
        return eval(cached_data)

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    logging.info(f'Making request to {url}')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.info(f'Received response: {data}')
        weather_data = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        r.setex(cache_key, 300, str(weather_data))
        return weather_data
    logging.error(f'Error fetching weather data: {response.status_code}')
    return None

def store_weather_data(city, temp, description):
    logging.info(f'Storing weather data for {city}: {temp}, {description}')
    cur.execute("""
        INSERT INTO weather (city, temperature, description)
        VALUES (%s, %s, %s)
    """, (city, temp, description))
    conn.commit()
    logging.info(f'Data stored successfully')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5000) 
