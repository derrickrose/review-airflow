from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.providers.amazon.aws.operators.s3_bucket import S3CreateBucketOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'frelin-ampilahy-test-airflow-s3-bucket')

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

    create_bucket
