import collections
from datetime import datetime, timedelta

import os

from airflow.models import Variable
from airflow.models.dag import DAG
from airflow.providers.amazon.aws.operators.s3_bucket import S3CreateBucketOperator
from airflow.operators.python_operator import PythonOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'frelin-ampilahy-test-airflow-s3-bucket')

import logging

SIDP_IWD_CONF_DICT = Variable.get("TEST_VARIABLE_JSON", deserialize_json=True)

SidpIwdConf = collections.namedtuple("SidpIwdConf",
                                     "hello greeting")
SIDP_IWD_CONF = SidpIwdConf(
    SIDP_IWD_CONF_DICT["hola"],
    SIDP_IWD_CONF_DICT["greeting"]
)

test_variable = Variable.get("TEST_VARIABLE")


def take_execution_date(execution_date, variable, **kwargs):
    datedate = execution_date.replace("-", "/")
    print("datedate", datedate)
    logging.info(" datedate", datedate)
    logging.info(" aaaaaa", execution_date)
    print("execution_date", execution_date)
    print("test_variable", variable)
    print("hello from variable tupe", SIDP_IWD_CONF.hello)
    print("greeting from variable tupe", SIDP_IWD_CONF.greeting)


with DAG(
        dag_id="create_s3_bucket",
        max_active_runs=1,
        schedule_interval="@once",
        # schedule_interval="@hourly",
        default_args=default_arguments,
        catchup=True
) as dag:
    create_bucket = S3CreateBucketOperator(
        task_id='create_bucket',
        bucket_name=BUCKET_NAME,
        region_name='us-east-1',
    )

    test_dag = PythonOperator(
        task_id='test_dag',
        python_callable=take_execution_date,

        op_kwargs={'execution_date': '{{ ds }}',
                   'test_variable': test_variable}
    )

test_dag >> create_bucket
