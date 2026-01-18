# Weather Data Project

A fully containerized ETL pipeline that automates real-time weather data ingestion from the Weatherstack API into PostgreSQL, orchestrated with Apache Airflow.

**Tech Stack:** Python, Apache Airflow, PostgreSQL, Docker Compose, WSL2

## Prerequisites

- Docker & Docker Compose
- Git
- WSL2 (Windows) or Linux

## Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd weather-data-project
```

### 2. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```ini
# Required: Get from https://weatherstack.com
WEATHERSTACK_API_KEY=your_actual_api_key

# Optional: Customize data collection
WEATHERSTACK_QUERY=Louisiana,US
WEATHERSTACK_UNITS=m  # m (Celsius), f (Fahrenheit), s (Scientific)
```

### 3. Start the Infrastructure
```bash
docker compose up -d
```

This starts:
- **PostgreSQL** database on `localhost:5000` (internal 5432)
- **Apache Airflow** UI on `http://localhost:8000`
- **dbt** transformation service (optional)

### 4. Verify Setup

Access Airflow at **http://localhost:8000**:
- Username: `admin`
- Password: `admin`

The DAG `weather-api-orchestrator` will run every 5 minutes automatically.



## How It Works

1. **Airflow Scheduler** triggers the `weather-api-orchestrator` DAG every 5 minutes
2. **API Request Task** calls Weatherstack API with configured location/units
3. **Database Ingestion** validates credentials and inserts records into `dev.raw_weather_data`
4. **PostgreSQL** persists weather observations with timestamps

### Data Schema

```sql
CREATE TABLE dev.raw_weather_data (
    id SERIAL PRIMARY KEY,
    city TEXT,
    temperature FLOAT,
    weather_descriptions TEXT,
    wind_speed FLOAT,
    time TIMESTAMP,
    inserted_at TIMESTAMP DEFAULT NOW(),
    utc_offset TEXT
);
```

## API Configuration

### Weatherstack API Key
1. Sign up at [weatherstack.com](https://weatherstack.com/)
2. Copy your API key from the dashboard
3. Add to `.env` as `WEATHERSTACK_API_KEY=<your_key>`

### Query Parameters
- `WEATHERSTACK_QUERY`: Location (e.g., `New York,US`, `London`, `Tokyo,JP`)
- `WEATHERSTACK_UNITS`: Temperature scale (`m`, `f`, or `s`)

## Database Access

Connect to PostgreSQL locally:
```bash
docker compose exec db psql -U db_user -d db
```

Query weather data:
```sql
SELECT * FROM dev.raw_weather_data 
```


### Port Conflicts
If ports 5000 or 8000 are in use, edit `docker-compose.yaml`:
```yaml
ports:
  - "5001:5432"  # Change 5000 to 5001
  - "8001:8080"  # Change 8000 to 8001
```

## Development

### Install Local Dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install python-dotenv requests psycopg2-binary
```

### Stop Services
```bash
docker compose down
```

### View Logs
```bash
docker compose logs -f af    # Airflow
docker compose logs -f db    # PostgreSQL
docker compose logs -f dbt   # dbt
```

## License

MIT

