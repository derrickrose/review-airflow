from datetime import datetime, timedelta

import os

from airflow.models.dag import DAG
from airflow.providers.amazon.aws.operators.s3_bucket import S3CreateBucketOperator, S3DeleteBucketOperator

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(seconds=10)
}

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'frelin-ampilahy-test-airflow-s3-bucket')

with DAG(
        dag_id="create_delete_s3_bucket",
        max_active_runs=1,
        schedule_interval='@hourly',
        default_args=default_arguments,
        catchup=True
) as dag:
    # [START howto_operator_s3_bucket]
    create_bucket = S3CreateBucketOperator(
        task_id='s3_bucket_dag_create',
        bucket_name=BUCKET_NAME,
        region_name='us-east-1',
    )

    delete_bucket = S3DeleteBucketOperator(
        task_id='s3_bucket_dag_delete',
        bucket_name=BUCKET_NAME,
        force_delete=True,
    )
    # [END howto_operator_s3_bucket]

    create_bucket >> delete_bucket
