import collections
from datetime import datetime, timedelta

import os

from airflow import AirflowException
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule

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
    if execution_date.weekday() == 5:
        return "saturday"
    else:
        return "other_day"


def test_saturday(**context):
    execution_date = context["ds_nodash"]
    execution_date = datetime.strptime(execution_date, "%Y%m%d")
    if execution_date.weekday() == 5:
        print("it is saturday")
        raise AirflowException("it is saturday")
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
        schedule_interval="@daily",
        start_date=datetime(2024, 1, 1),
        default_args=default_arguments,
        catchup=True,
) as dag:
    is_saturday = BranchPythonOperator(
        task_id="is_saturday",
        provide_context=True,
        python_callable=check_saturday

    )

    saturday = DummyOperator(task_id="saturday")

    other_day = DummyOperator(task_id="other_day")

    monday_to_saturday_task1 = DummyOperator(task_id="monday_to_saturday_task1")

    monday_to_saturday_task2 = PythonOperator(
        task_id="monday_to_saturday_task2",
        python_callable=test_saturday,
        provide_context=True
    )

    monday_to_friday_task1 = DummyOperator(task_id="monday_to_friday_task1")

    monday_to_friday_task2 = DummyOperator(task_id="monday_to_friday_task2")

    final_task = DummyOperator(task_id="final_task", trigger_rule=TriggerRule.NONE_FAILED)

    is_saturday >> saturday >> final_task

    is_saturday >> other_day >> monday_to_friday_task1

    monday_to_saturday_task1 >> monday_to_saturday_task2

    monday_to_friday_task1 >> monday_to_friday_task2

    monday_to_saturday_task2 >> final_task

    monday_to_friday_task2 >> final_task
