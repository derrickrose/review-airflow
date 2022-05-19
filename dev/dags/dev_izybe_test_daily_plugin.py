from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from izybe_timetable_plugin import DailyTimetable

import logging


def take_execution_date(**kwargs):
    print(kwargs["execution_date"])
    print(kwargs["variable"])
    logging.info(kwargs["execution_date"])
    logging.info(kwargs["variable"])


with DAG(
        start_date=datetime(2022, 5, 10),
        timetable=DailyTimetable(),
        catchup=True,
        dag_id="dev_izybe_test_daily_plugin"
) as dag:
    operator = PythonOperator(
        task_id='test_dag',
        python_callable=take_execution_date,

        op_kwargs={'execution_date': '{{ ds }}',
                   'variable': "test_variable"}
    )
