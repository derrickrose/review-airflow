from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

import logging as log


class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        log.info(f"{self.__class__.__name__} execute with param {self.param}")

with DAG(
        dag_id="custom_operator_in_local",
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
