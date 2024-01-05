from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from botocore.errorfactory import ClientError

default_arguments = {
    'owner': "frils",
    'start_date': datetime(2021, 5, 21, 0, 0, 0),
    'retry_delay': timedelta(seconds=10)
}

import logging as log


class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        log.info(f"{self.__class__.__name__} execute with param {self.param}")


from airflow.sensors.base_sensor_operator import BaseSensorOperator
from datetime import datetime
import boto3


# TODO affiner

class S3FileSensor(BaseSensorOperator):
    @apply_defaults
    def __init__(self, poke_interval_minutes, bucket, key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poke_interval_minutes = poke_interval_minutes
        self.bucket = bucket
        self.key = key

    """
    def poke(self, context):
        if datetime.now().minute % self.poke_interval_minutes != 0:
            s3 = boto3.client('s3')
            try:
                s3.head_object(Bucket=self.bucket, Key=self.key)
                return True
            except Exception:
                # Not found
                log.warning("{}/{} not found".format(self.bucket, self.key))
                return False

        return False
    """

    def poke(self, context):
        current_minute = datetime.now().minute
        if current_minute % 2 != 0:
            return False
        return True


with DAG(
        dag_id="custom_sensor_in_local",
        max_active_runs=1,
        schedule_interval='@hourly',
        default_args=default_arguments,
        catchup=True
) as dag:
    sensor = S3FileSensor(
        task_id="s3_file_sensor",
        poke_interval_minutes=5,
        bucket="frelin-ampilahy-test-airflow-s3-bucket",
        key="_SUCCESS_.txt"
    )

    custom_operator_2 = CustomOperator(
        task_id="custom_operator_2",
        param="custom operator 2"
    )
    sensor >> custom_operator_2
