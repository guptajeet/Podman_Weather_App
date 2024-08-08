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
  <img width="938" alt="image" src="https://github.com/user-attachments/assets/bd763a58-a3cc-4871-a6fd-390a43b9006b">

- **Test API Integration:** Use tools like `curl` or Postman to test the OpenWeather API.
  ```bash
  curl "http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=your_openweather_api_key"
  ```

  <img width="941" alt="image" src="https://github.com/user-attachments/assets/3c3297ed-ed20-4282-81f3-266b0a719aef">


- **Check Environment Variables:** Make sure the API key is set correctly:
  ```bash
  podman exec -it <container_name> env
  ```
  <img width="904" alt="image" src="https://github.com/user-attachments/assets/6e0542c6-c755-41a1-8340-107b145eed90">

  

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
