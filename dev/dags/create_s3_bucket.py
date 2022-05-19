import collections
from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator

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


def take_execution_date(execution_date, variable, **kwargs):
    date = execution_date.replace("-", "/")
    print("date", date)
    logging.info("Received date", date)
    print("execution_date", execution_date)
    print("test_variable", variable)
    print("hello from variable tupe", IZYBE_TUPLE.hello)


with DAG(
        dag_id="create_s3_bucket",
        max_active_runs=1,
        schedule_interval=None,
        default_args=default_arguments,
) as dag:
    create_bucket = S3CreateBucketOperator(
        task_id='create_bucket',
        bucket_name=BUCKET_NAME,
        region_name='eu-west-1',
    )

    test_dag = PythonOperator(
        task_id='test_dag',
        python_callable=take_execution_date,

        op_kwargs={'execution_date': '{{ ds }}',
                   'variable': BUCKET_NAME}
    )

    test_dag >> create_bucket
