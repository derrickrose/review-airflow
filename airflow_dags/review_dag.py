from airflow import DAG
from datetime import datetime, timedelta

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(
    dag_id="review_dag",
    max_active_runs=1,
    schedule_interval='@hourly',
    default_args=default_arguments,
    catchup=False
)
