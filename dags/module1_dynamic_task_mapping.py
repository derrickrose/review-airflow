from datetime import datetime, timedelta
from random import randint

from airflow import DAG
from airflow.sdk import task
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="module1_dynamic_task_mapping",
    start_date=datetime(2024, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
) as dag:

    @task(task_id="dummy_tasks")
    def dummy_task():
        print("Dummy task")

    dummy_task()

    # dynamic task mapping minimal example
    @task
    def print_file(file: str):
        print(f"File: {file}")

    # the function is actually considered as an operator
    # to make it a task, we need to call the function print_file()
    # but with the dynamic task mapping concept, the .expand() method is calling the function also
    # the expand() method here is waiting a list of arguments to be passed to the function
    print_file.expand(file=["file1", "file2"])

    # automatic chaining for dynamic task mapping
    # let say we dont know how many files we have to download
    # let use random and randint to simulate this
    # build file name
    # download file
    # notion of partial(), to send constant argument(s) to the function
    @task
    def build_file():
        return [f"file{i}" for i in range(randint(3, 7))]

    # this is not a list of files, this is actually XCom wrapping a list of files
    files = build_file()

    @task
    def build_filepath(folder: str, file):
        return f"{folder}/{file}"

    # we can assign the return value of the function to a variable
    # then use it as an argument to a new task
    # by the power of TaskFlow API, sending a return value of a task as parameter to another task
    # is the way to pass XComs directly to the second task
    paths = build_filepath.partial(folder="TEST").expand(file=files)

    @task
    def download_file(path: str):
        print(f"Downloading file: {path}")

    downs = download_file.expand(path=paths)

    # dynamic task mapping with old Operator
    # with or without @task decorator here it will work fine
    # but with @task decorator, the function will run at runtime not parse-time so best practice is to use it
    @task
    def old_create_paths_list():
        return [[f"file{i}"] for i in range(randint(3, 7))]

    paths_list = old_create_paths_list()

    def imprimir(filepath: str):
        print(f"Imprimiendo archivo: {filepath}")

    # notice that op_args will send a list to the function assigned to python_callable
    # with expand, op_args will wait for a list of lists
    PythonOperator.partial(
        task_id="old_python_operator", python_callable=imprimir
    ).expand(op_args=paths_list)

    # notice that op_kwargs will send a list of dictionaries to the function assigned to python_callable
    # with expand, op_kwargs will wait for a list of dictionaries
    # without the expand, an error will be raised stating that XComArg is not iterable
    @task
    def old_create_path_dict_list(pl: list[str]):
        return {"filepath": pl[0]}

    list_of_dicts = old_create_path_dict_list.expand(pl=paths_list)

    PythonOperator.partial(
        task_id="old_python_operator_dict", python_callable=imprimir
    ).expand(op_kwargs=list_of_dicts)

    @task
    def old_create_path_2():
        return [f"file_bash_{i}" for i in range(randint(3, 7))]

    files_bash = old_create_path_2()

    @task
    def create_bash_command(filepath: str):
        return f"ls -l {filepath}; exit 0"

    bash_commands = create_bash_command.expand(filepath=files_bash)

    BashOperator.partial(task_id="old_bash_operator").expand(bash_command=bash_commands)
