import collections
from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'dev-izybe-s3-airflow-bucket')

import logging

IZYBE_CONF = {'hola': "hola", "greeting": "greeting"}

IzybeTuple = collections.namedtuple("IzybeTuple", "hello greeting")

IZYBE_TUPLE = IzybeTuple(
    IZYBE_CONF["hola"],
    IZYBE_CONF["greeting"]
)


def check_saturday(**context):
    execution_date = context["ds_nodash"]
    execution_date = datetime.strptime(execution_date, "%Y%m%d")
    if execution_date.weekday() == 0:
        return "saturday"
    else:
        return "other_day"


def take_execution_date(execution_date, variable, **kwargs):
    date = execution_date.replace("-", "/")
    print("date", date)
    logging.info("Received date", date)
    print("execution_date", execution_date)
    print("test_variable", variable)
    print("hello from variable tupe", IZYBE_TUPLE.hello)


with DAG(
        dag_id="branching_operator_test",
        max_active_runs=1,
        schedule_interval=None,
        default_args=default_arguments,
) as dag:
    is_saturday = BranchPythonOperator(
        task_id="is_saturday",
        provide_context=True,
        python_callable=check_saturday

    )

    saturday = DummyOperator(task_id="saturday")

    other_day = DummyOperator(task_id="other_day")

    work_day_task_1 = DummyOperator(task_id="work_day_task_1")

    work_day_task_2 = DummyOperator(task_id="work_day_task_2")

    work_day_and_saturday_task_1 = DummyOperator(task_id="work_day_and_saturday_task_1")

    work_day_and_saturday_task_2 = DummyOperator(task_id="work_day_and_saturday_task_2")

    # test_dag = PythonOperator(
    #     task_id='test_dag',
    #     python_callable=take_execution_date,
    #
    #     op_kwargs={'execution_date': '{{ ds }}',
    #                'variable': BUCKET_NAME}
    # )
    is_saturday >> saturday

    is_saturday >> other_day
