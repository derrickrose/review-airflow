import logging
import time
from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10),

}

IZYBE_CONF = {'hola': "hola", "greeting": "greeting"}


def sleep_function(**context) -> None:
    if "duration" in context.keys():
        print("duration from context", context["duration"])
        time.sleep(int(context["duration"]))
    else:
        time.sleep(120)


def notify_sla_miss(*args, **context) -> None:
    print("SLA MISS HERE")  # scheduler log
    logging.info("SLA_MISS_HERE")


with DAG(
        dag_id="sla",
        max_active_runs=1,
        schedule_interval="@daily",
        start_date=datetime(2024, 1, 1),
        default_args=default_arguments,
        catchup=True,
        # sla_miss_callback=notify_sla_miss
) as dag:
    dummy = DummyOperator(task_id="dummy")

    sleep = PythonOperator(
        task_id="sleep",
        provide_context=True,
        python_callable=sleep_function,
        sla=timedelta(seconds=10)
    )

    after_sleep = PythonOperator(
        task_id="after_sleep",
        provide_context=True,
        python_callable=sleep_function,
        op_kwargs={'duration': 15}
    )
    final_task = DummyOperator(task_id="final_task")

    dummy >> sleep >> after_sleep >> final_task
