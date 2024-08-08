
---

# Dockerfile Summary
This Dockerfile sets up a Python environment, installs dependencies, and runs the application.
## Dockerfile

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### Details

1. **`FROM python:3.9-slim`**: Uses a lightweight Python 3.9 image as the base.
2. **`WORKDIR /app`**: Sets `/app` as the working directory inside the container.
3. **`COPY requirements.txt requirements.txt`**: Copies `requirements.txt` to the container.
4. **`RUN pip install -r requirements.txt`**: Installs Python dependencies.
5. **`COPY . .`**: Copies the application code into the container.
6. **`CMD ["python", "app.py"]`**: Runs `app.py` when the container starts.

---
