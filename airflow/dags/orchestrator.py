import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta


sys.path.append('/opt/airflow/api-request')

def main_callable():
    from insert_records import main   
    return main()

default_args = {
    'description': 'Orchestrator DAG for Weather API data ingestion',
    'start_date': datetime(2026, 1, 16),
    'catchup': False,

}

dag = DAG(
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5)

)

with dag:
    task1 = PythonOperator(
        task_id='ingest_weather_data',
        python_callable=main_callable
    )