from airflow.plugins_manager import AirflowPlugin


class ReviewPlugin(AirflowPlugin):
    name = "ReviewPlugin"
    operators = []
    hooks = []
    sensors = []
