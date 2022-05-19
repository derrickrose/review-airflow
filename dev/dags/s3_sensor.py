from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor
from airflow.providers.amazon.aws.operators.s3_list import S3ListOperator
from sensors.custom_s3_key import CustomS3KeySensor

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'dev-izybe-s3-airflow-bucket')

with DAG(
        dag_id="custom_s3_sensor",
        max_active_runs=1,
        schedule_interval=None,
        default_args=default_arguments,
        catchup=True
) as dag:
    check_file_presence = S3KeySensor(
        task_id='check_file_presence',
        bucket_name=BUCKET_NAME,
        bucket_key="DataIn/Infomart_20210715_120023.txt",
        mode="reschedule",
        poke_interval=60 * 1

    )

    check_file_presence_wild = S3KeySensor(
        task_id='check_file_presence_wild',
        bucket_name=BUCKET_NAME,
        bucket_key="DataIn/Infomart_20210715_*",
        wildcard_match=True,
        mode="reschedule",
        poke_interval=60 * 1

    )

    list_operator = S3ListOperator(
        task_id='list_operator',
        bucket=BUCKET_NAME,
        delimiter='/',
        prefix="DataIn/"
    )

    custom_key_sensor = CustomS3KeySensor(
        task_id="custom_key_sensor",
        bucket_key="DataIn/Infomart_20210715_*",
        poke_interval=60 * 1,
        bucket_name=BUCKET_NAME,
    )

    check_file_presence >> check_file_presence_wild >> list_operator
    list_operator >> custom_key_sensor
