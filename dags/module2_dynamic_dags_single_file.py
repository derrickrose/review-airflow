from airflow import DAG
from datetime import datetime, timedelta
from airflow.sdk import task


def create_dag(filename):
    with DAG(
        start_date=datetime(2021, 1, 1),
        catchup=False,
        dagrun_timeout=timedelta(minutes=60),
        dag_id=f"module2_dynamic_dags_single_file_{filename}",
        schedule="@daily",
    ) as dag:

        @task
        def download_file():
            print(f"downloading file from {filename}")

        @task
        def load_data_to_db():
            print(f"loading data to db from {filename}")

        download_file() >> load_data_to_db()

        return dag


for file in [
    "filea.csv",
    "fileb.csv",
]:
    ## define the global variable table, basically a dictionary which contains all variables defined on top level of a file
    ## Airflow discovers DAGs by looking at global variables that contain DAG objects.
    globals()[f"dag_{file}"] = create_dag(file)
