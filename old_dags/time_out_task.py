import os
from datetime import datetime, timedelta
from time import sleep

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'dev-izybe-s3-airflow-bucket')
with DAG(
        dag_id="time_out_task",
        start_date=datetime(2024, 3, 10),
        schedule_interval="@daily",
        dagrun_timeout=timedelta(minutes=1),
        tags=["frils"],
        default_args={"owner": "frils"},
        description="Timeout DAG",
        catchup=False,
) as dag:
    check_file_presence = S3KeySensor(
        task_id='check_file_presence',
        bucket_name=BUCKET_NAME,
        bucket_key="DataIn/Infomart_20210715_120023.txt",
        mode="poke",
        poke_interval=60 * 1,
        timeout=1 * 60

    )
    dummy = DummyOperator(task_id="dummy")
    check_file_presence >> dummy
