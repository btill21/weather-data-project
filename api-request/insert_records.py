import psycopg2
from api_request import mock_fetch_data, fetch_data

def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        raise

def create_table(conn):

    print("Creating weather_data table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature float,
                weather_descriptions TEXT,
                wind_speed float,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table created.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise



def insert_records(conn, data):
    print("Inserting weather data into the database...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            Insert INTO dev.raw_weather_data (
            city,
            temperature,
            weather_descriptions,
            wind_speed,
            time,
            inserted_at,
            utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            data['location']['name'],
            data['current']['temperature'],
            data['current']['weather_descriptions'][0],
            data['current']['wind_speed'],
            data['location']['localtime'],
            data['location']['utc_offset']


        ))

        conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        raise


def main():
    conn = None
    try:
        # data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred in main: {e}")
        raise
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")    


  

