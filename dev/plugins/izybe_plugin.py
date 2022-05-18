from airflow.plugins_manager import AirflowPlugin


class IzybePlugin(AirflowPlugin):
    name = "IzybePlugin"
    version = "0.0.1"
    operators = []
    hooks = []
    sensors = []
