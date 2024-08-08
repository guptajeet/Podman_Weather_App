CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    description VARCHAR(100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

