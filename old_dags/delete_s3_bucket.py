from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.providers.amazon.aws.operators.s3 import S3DeleteBucketOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'dev-izybe-s3-airflow-bucket')

with DAG(
        dag_id="delete_s3_bucket",
        max_active_runs=1,
        schedule_interval=None,
        # schedule_interval="@hourly",
        default_args=default_arguments,
        catchup=True
) as dag:
    delete_bucket = S3DeleteBucketOperator(
        task_id='delete_bucket',
        bucket_name=BUCKET_NAME,
        force_delete=True,
    )

    delete_bucket
