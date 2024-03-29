from datetime import datetime, timedelta
from time import sleep

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

with DAG(
        dag_id="execution_timeout_task",
        start_date=datetime(2024, 3, 10),
        schedule_interval="@daily",
        tags=["frils"],
        default_args={"owner": "frils"},
        description="Timeout DAG",
        catchup=False,
) as dag:
    python_operator = PythonOperator(
        task_id="python_operator", python_callable=lambda: sleep(60 * 5),
        execution_timeout=timedelta(minutes=1),
    )
    dummy = DummyOperator(task_id="dummy")
    python_operator >> dummy
