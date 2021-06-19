from datetime import datetime, timedelta

from airflow.models.dag import DAG
from operators.custom_operator import CustomOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

with DAG(
        dag_id="custom_operator_test",
        max_active_runs=1,
        schedule_interval='@hourly',
        default_args=default_arguments,
        catchup=True
) as dag:
    custom_operator_1 = CustomOperator(
        task_id="custom_operator_1",
        param="custom operator 1",

    )

    custom_operator_2 = CustomOperator(
        task_id="custom_operator_2",
        param="custom operator 2"

    )
    custom_operator_1 >> custom_operator_2
