# Weather Data Project

A weather data collection and storage project using Python, PostgreSQL, Docker, and the Weatherstack API.

## Prerequisites

- Docker & Docker Compose
- Python 3.9+
- WSL (Windows Subsystem for Linux) if on Windows

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd weather-data-project
```

### 2. Create Environment Variables
Copy the example file and fill in your values:
```bash
cp .env.example .env
```

Then edit `.env` and add your actual values:
```
WEATHERSTACK_API_KEY=your_actual_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db
DB_USER=db_user
DB_PASSWORD=your_database_password
```

### 3. Install Python Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  
pip install python-dotenv requests psycopg2-binary
```

### 4. Start PostgreSQL with Docker
```bash
docker-compose up -d
```

This will start a PostgreSQL container on `localhost:5432`

### 5. Run the Application
```bash
cd api-request
python api_request.py
```

## Getting API Keys

### Weatherstack API
1. Go to [weatherstack.com](https://weatherstack.com/)
2. Sign up for a free account
3. Copy your API key from the dashboard
4. Paste it in your `.env` file under `WEATHERSTACK_API_KEY`

## Project Structure
```

