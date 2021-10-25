from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

with DAG(
        dag_id="dag_2",
        start_date=datetime(2021, 10, 1),
        schedule_interval="@daily"
) as dag:
    task1 = DummyOperator(task_id="task1")
    task2 = DummyOperator(task_id="task2")
    task3 = DummyOperator(task_id="task3")

    task1 >> task2 >> task3
