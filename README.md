# 🌦️ Multi-Container Weather Dashboard Application with Podman/Docker

Welcome to the **Weather Dashboard App**! This is a simple Flask-based web application that provides current weather information for cities around the world.

It uses -
1. PostgreSQL for storing data
2. Redis for caching
3. The OpenWeather API to get weather data
```mardown
📚 Table of Contents

- Project Overview
- Project Structure
- Setup Instructions
- How to Use
- Development & Debugging
- License
- Acknowledgements
- Contact
```
### 🚀 Project Overview

This project shows how to deploy a multi-container app using **Podman Compose**. It includes:

- **Container 1 - Web Server:** Runs the Flask app and handles user requests.
- **Container 2 - PostgreSQL Database:** Stores weather data.
- **Container 3 - Redis Cache:** Caches recent weather data to speed up responses.

**Features:**

- Fetches and shows current weather.
- Uses Redis for fast access to recent data.
- Stores weather data in PostgreSQL.
- Scales services with Podman Compose.

### 🎨 Project Structure

Here’s a quick look at how the project is organized:

```markdown
weather_dashboard_app/
│
├── db/
│   └── init.sql
│
├── redis/
│
├── web/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
└── podman-compose.yml
```

### 🛠️ Setup Instructions

#### 1. **Clone the Repository**

Get the code from GitHub:

```bash
git clone https://github.com/guptajeet/Podman_Weather_App.git
cd weather_dashboard_app
```

#### 2. **Configure Environment Variables**

Replace `your_openweather_api_key` in the `podman-compose.yml` file with your actual API key from OpenWeather.

Go to `https://openweathermap.org/` > Profile > Api Keys > Click on Generate

<img width="842" alt="image" src="https://github.com/user-attachments/assets/02568759-8c2a-4fae-a6a4-11063c961c9f">


#### 3. **Update `podman-compose.yml`**

Edit the file to set your API key:

```yaml
version: '3.7'

services:
  web:
    build: ./web
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/weatherdb
      - REDIS_URL=redis://redis:6379
      - API_KEY=your_openweather_api_key
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=weatherdb
    volumes:
      - db_data:/var/lib/postgresql/data

  redis:
    image: redis:6
    ports:
      - "6379:6379"

volumes:
  db_data:
```

#### 4. **Build and Start Containers**

Build and start the containers with these commands:

```bash
podman-compose up --build -d    # -d for detached mode 
podman-compose down
```

#### 5. **Access the Application**

Open your browser and go to `http://localhost:5000` or `http://serverip:5000` to use the Weather Dashboard App.

<img width="878" alt="image" src="https://github.com/user-attachments/assets/ad70062b-708d-4e28-9526-7196289674b5">


### 🧑‍💻 How to Use

1. **Enter a City Name:** Type the city you want weather information for.
2. **Submit the Form:** Click the submit button to get weather data.
3. **View Results:** The app will show the current temperature and weather description.

### 🔧 Development & Debugging

- **View Logs:** Check the logs for the `web` service to see what’s happening:
  ```bash
  podman-compose logs web
  ```
  
- **Test API Integration:** Use tools like `curl` or Postman to test the OpenWeather API.
  ```bash
  curl "http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=your_openweather_api_key"
  ```
  ```bash
  podman@test ~/weather_dashboard_app$ curl "http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=............api key..........."
  {"coord":{"lon":73.8553,"lat":18.5196},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main": 
  {"temp":29.34,"feels_like":33.48,"temp_min":28.65,"temp_max":29.49,"pressure":1007,"humidity":70,"sea_level":1007,"grnd_level":946},"visibility":10000,"wind": 
  {"speed":5.94,"deg":270,"gust":8.21},"clouds":{"all":100},"dt":1723113250,"sys": 
  {"type":2,"id":2096426,"country":"IN","sunrise":1723077865,"sunset":1723124164},"timezone":19800,"id":1259229,"name":"Pune","cod":200}
  ```
  
- **Check Environment Variables:** Make sure the API key is set correctly:
  ```bash
  podman exec -it <container_name> env
  ```
  ```bash
  podman@test ~/weather_dashboard_app$ podman ps
  CONTAINER ID  IMAGE                                       COMMAND        CREATED            STATUS            PORTS                             NAMES
  93c2d7a61586  docker.io/library/postgres:13               postgres       About an hour ago  Up About an hour  5432/tcp                          weather_dashboard_app_db_1
  9349f61fa084  docker.io/library/redis:6                   redis-server   About an hour ago  Up About an hour  0.0.0.0:6379->6379/tcp, 6379/tcp  
  weather_dashboard_app_redis_1
  4e74a1ddb3f1  localhost/weather_dashboard_app_web:latest  python app.py  About an hour ago  Up About an hour  0.0.0.0:5000->5000/tcp            weather_dashboard_app_web_1
  podman@test ~/weather_dashboard_app$ podman exec -it 4e74a1ddb3f1 env | grep API_KEY
  API_KEY=.........api key..................
  ```

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

### 🙏 Acknowledgements

- **OpenWeather API:** For providing weather data.
- **PostgreSQL:** For storing data.
- **Redis:** For caching recent weather data.
- **Podman Compose:** For managing multi-container setups.
- **Github:** Hosting and version control platform for the project's repository.
- **OpenAI:** For generating quick static and templates section.

## 📧 Contact

For any questions or feedback Feel free to connect with me :

- [**LinkedIn**](https://www.linkedin.com/in/guptajeet).
- [**GitHub**](https://github.com/guptajeet)

---

Thank you for using the Weather Dashboard App! 🌦️✨
