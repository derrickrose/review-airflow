from airflow.plugins_manager import AirflowPlugin

from operators.custom_operator import CustomOperator
from sensors.custom_s3_key import CustomS3KeySensor


class IzybePlugin(AirflowPlugin):
    name = "IzybePlugin"
    version = "0.0.1"
    operators = [CustomOperator]
    hooks = []
    sensors = [CustomS3KeySensor]
