from datetime import datetime, timedelta

import os

from airflow import AirflowException
from airflow.models import BaseOperator
from airflow.models.dag import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.decorators import apply_defaults
import logging
import pypd

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}



with DAG(
        dag_id="pager_duty_test_dag",
        max_active_runs=1,
        schedule_interval=None,
        # schedule_interval="@hourly",
        default_args=default_arguments,
        catchup=True
) as dag:
    dummy = DummyOperator(task_id="dummy")
