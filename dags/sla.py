from datetime import datetime, timedelta

from airflow.models.dag import DAG

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}


IZYBE_CONF = {'hola': "hola", "greeting": "greeting"}


with DAG(
        dag_id="branching_operator_test",
        max_active_runs=1,
        schedule_interval="@daily",
        start_date=datetime(2024, 1, 1),
        default_args=default_arguments,
        catchup=True,
) as dag: