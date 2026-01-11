from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="dst_to_standard_time",
    catchup=False,
    start_date=datetime(2025, 10, 25, 22),
    dagrun_timeout=timedelta(minutes=15),
):
    dummy = EmptyOperator(task_id="dummy")
