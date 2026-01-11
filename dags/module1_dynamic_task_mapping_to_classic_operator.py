from datetime import datetime, timedelta
from random import randint

from airflow import DAG
from airflow.sdk import task
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="module1_dynamic_task_mapping_to_classic_operator",
    start_date=datetime(2024, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
) as dag:

    @task(task_id="dummy_tasks")
    def dummy_task():
        print("Dummy task")

    dummy_task()

    @task
    def create_file():
        return [f"file{i}" for i in range(randint(3, 7))]

    files = create_file()

    imprimir = BashOperator(
        task_id="imprimir",
        bash_command="echo {{ task_instance.xcom_pull(task_ids='create_file') }}",
    )

    imprimir_with_list = BashOperator(
        task_id="imprimir_with_list",
        bash_command="echo {{ task_instance.xcom_pull(task_ids='create_file') | List }}",
    )

    @task
    def build_bash_command(file: str):
        return f"ls -l {file}; exit 0"

    commands = build_bash_command.expand(file=files)

    @task
    def regroup_commands(**context):
        ## no need to set the key='return_value' here since it is the default
        return ";\n".join(
            context["task_instance"].xcom_pull(task_ids="build_bash_command")
        )

    regrouped = regroup_commands()

    bashOperator = BashOperator(
        task_id="bash_operator",
        bash_command="{{ task_instance.xcom_pull(task_ids='regroup_commands') }}",
    )

    commands >> regrouped >> bashOperator
    files >> [imprimir, imprimir_with_list]
