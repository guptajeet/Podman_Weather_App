
---

# app.py Summary
This file is the core of the Flask application for the Weather Dashboard. It manages the application logic, data retrieval, and storage. Below is a summary of the code and its functionality:
File will sets up a Flask web application that interacts with PostgreSQL and Redis to manage and cache weather data.

1. **Imports**: Required libraries for Flask, database connections, caching, and logging.
   ```python
   from flask import Flask, render_template, request
   import os
   import requests
   import psycopg2
   import redis
   import logging
   ```

2. **Environment Variables**:
  - `DATABASE_URL`: PostgreSQL connection string.
  - `REDIS_URL`: Redis connection string.
  - `API_KEY`: OpenWeatherMap API key.  
       
   ```python
   db_url = os.environ.get('DATABASE_URL')
   redis_url = os.environ.get('REDIS_URL')
   api_key = os.environ.get('API_KEY')
   ```

4. **Database Setup**:
  - Connects to PostgreSQL.
  - Creates a `weather` table if it doesn't exist.
        
   ```python
   conn = psycopg2.connect(db_url)
   cur = conn.cursor()
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
   ```

6. **Redis Setup**: Connects to Redis for caching weather data.
   ```python
   r = redis.Redis.from_url(redis_url)
   ```

7. **Routes**:
  - `/`: Handles GET and POST requests. Fetches weather data based on user input and stores it in the database.
      
   ```python
   @app.route('/', methods=['GET', 'POST'])
   def index():
       weather_data = None
       if request.method == 'POST':
           city = request.form.get('city')
           weather_data = get_weather(city)
           if weather_data:
               store_weather_data(city, weather_data['temp'], weather_data['description'])
       return render_template('index.html', weather=weather_data)
   ```

9. **Functions**:
  - `get_weather(city)`: Retrieves weather data from cache or API.
  - `store_weather_data(city, temp, description)`: Stores weather data in PostgreSQL.
   - **Fetch Weather Data**:
     ```python
     def get_weather(city):
         cache_key = f'weather:{city}'
         cached_data = r.get(cache_key)
         if cached_data:
             return eval(cached_data)

         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
         response = requests.get(url)
         if response.status_code == 200:
             data = response.json()
             weather_data = {
                 'temp': data['main']['temp'],
                 'description': data['weather'][0]['description']
             }
             r.setex(cache_key, 300, str(weather_data))
             return weather_data
         return None
     ```
   - **Store Weather Data**:
     ```python
     def store_weather_data(city, temp, description):
         cur.execute("""
             INSERT INTO weather (city, temperature, description)
             VALUES (%s, %s, %s)
         """, (city, temp, description))
         conn.commit()
     ```

11. **Logging**: Provides logging for debugging and tracking.
   ```python
   logging.basicConfig(level=logging.INFO)
   ```

11. **Run Application**: Runs the Flask app on default port 5000.
   ```python
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```


```
---
