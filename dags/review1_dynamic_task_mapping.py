# si on ne sait pas au debut combien de fichiers il va avoir dans le traitement par exemple
# LazyXComSequence generayl previous task is dynamic task mapping then the current task is general, error skipped

from datetime import datetime, timedelta

from airflow.sdk import task, dag
from airflow.providers.standard.operators.python import PythonOperator


def print_and_return_file(fic: str):
    print(f"Printing file: {fic}")
    return fic


def download_and_return(file: str):
    print("downloading file")
    return file


@dag(
    dag_id="review1_dynamic_task_mapping",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    schedule="@daily",
)
def review1_dynamic_task_mapping():
    @task
    def build_file():
        return [f"File{i}" for i in range(3)]

    files = build_file()  # without file= positional error

    @task
    def print_file(to_print: str):
        print(f"Printing file: {to_print}")
        return to_print

    # print_file(files) # Printing file: LazyXComSequence so should always be expanded
    # if you see a LazyXComSequence, it means that the task might not be expanded yet
    print_and_return_files = print_file.expand(to_print=files)

    @task
    def download_file(file: str):
        print(f"Downloading file: {file}")
        return file

    down_file_task = download_file.expand(file=print_and_return_files)

    op = PythonOperator.partial(
        task_id="op", python_callable=lambda x: print("loading", x)
    ).expand(op_args=down_file_task.map(lambda x: [x]))
    down_file_task >> op

    #################################### fin dynamic task mapping taskflow api to taskflow api
    # classic tasks and expand
    python_operator = PythonOperator(
        task_id="python_operator", python_callable=lambda: 3
    )

    build_files = PythonOperator(
        task_id="build_files",
        python_callable=lambda x: [f"File_op_{i}" for i in range(x)],
        op_args=[python_operator.output],
    )

    print_files = PythonOperator.partial(
        task_id="print_files", python_callable=lambda val: print_and_return_file(val)
    ).expand(op_args=build_files.output.map(lambda x: [x]))

    download_files_op = PythonOperator.partial(
        task_id="download_files_op", python_callable=lambda x: download_and_return(x)
    ).expand(op_args=print_files.output.map(lambda x: [x]))

    @task
    def load_data(fic: str):
        print("loading_data", fic)

    (
        python_operator
        >> build_files
        >> print_files
        >> download_files_op
        >> load_data(fic=download_files_op.output)
    )


review1_dynamic_task_mapping()
