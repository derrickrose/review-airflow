import collections
import sys
from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG

current_directory = os.getcwd()
relative_path = "../lib/"
absolute_path = os.path.join(current_directory, relative_path)
sys.path.append(absolute_path)
from s3_multipart_copy_operator import S3MultiPartCopyObjectOperator

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
        dag_id="s3_multipart_copy_object",
        max_active_runs=1,
        schedule_interval=None,
        default_args=default_arguments,
) as dag:
    s3_multipart_copy_object = S3MultiPartCopyObjectOperator(
        task_id="s3_multipart_copy_object",
        source_bucket_name="dev-miaradia-s3-bucket",
        dest_bucket_name="frils-aws-bucket",
        source_bucket_key="test_airflow.zip",
        dest_bucket_key="test_airflow.zip"
    )
