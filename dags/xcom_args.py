from datetime import datetime, timedelta

from airflow.sdk import dag, task
from airflow.providers.standard.operators.python import (
    PythonOperator,
)
from airflow.models.xcom_arg import XComArg


def push_and_return_v2(value, **context):
    ti = context["task_instance"]
    ti.xcom_push(key="my_key", value=value)
    return value


def push_and_return(op, **context):
    print(f"Printing the operator {op}")  # <Task(PythonOperator): python_operator>
    print(
        f"Printing the xcomarg(op)  {XComArg(op)}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }}, default value
    print(
        f"Printing the xcomarg(op) class  {XComArg(op).__class__}"
    )  # <class 'airflow.sdk.definitions.xcom_arg.PlainXComArg'>
    print(
        f"Printing the operator output {op.output}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }}
    print(
        f"Printing the operator output class " f"{op.output.__class__}"
    )  # <class 'airflow.sdk.definitions.xcom_arg.PlainXComArg'>
    print(
        f"Printing the operator XComArg(op)['my_key']){XComArg(op)['my_key']}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='my_key') }}
    ti = context["task_instance"]
    print(f"pushing xcom with key my_key")
    ti.xcom_push(key="my_key", value=42)

    return 42


@dag(
    dag_id="xcom_args",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    schedule="@once",
)
def xcom_args():
    @task()
    def task1():
        return 100

    # this will push an XCom with the return_value 42
    python_operator = PythonOperator(
        task_id="python_operator", python_callable=push_and_return_v2, op_args=[42]
    )

    python_operator_2 = PythonOperator(
        task_id="python_operator_2",
        python_callable=push_and_return,
        op_args=[python_operator],  ## this will print the XComArg object
    )

    python_operator >> python_operator_2

    @task
    def task1():
        return 100

    @task(
        multiple_outputs=True,
    )
    # without multiple_outputs setting the following approach raises an error since the task pushes xcom with key return_value and value the actual dict
    def task2(val: int):
        print(f"The value from the task is {val}")
        return {"key": val, "second_key": 2 * val}

    values = task2(task1())

    @task
    def task3(mapa: dict):
        print("first val ", mapa["key"])
        print("second val ", mapa["second_key"])

    @task
    def task4(key: int, second_key: int):
        print(f"The value from the task is {key}")
        print(f"The value from the task is {second_key}")

    task3(values)

    task4(values["key"], values["second_key"])

    ## best way of sharing data between tasks
    @task
    def t1() -> dict[str, int]:
        return {"my_valu": 100}

    @task
    def t2(val: int):
        print(f"The value from the task is {val}")
        return val

    t2(t1()["my_valu"])

    # between classic operators
    python_op = PythonOperator(task_id="python_op", python_callable=lambda: 100)

    python_op2 = PythonOperator(
        task_id="python_op2",
        python_callable=lambda x: print("here printing", x),
        op_args=[python_op.output],
    )

    # classic to taskflow
    @task
    def ta(val: int):
        print("here printing xcom from classic inside taskflow", val)
        return val

    # taskflow to classic
    rat = ta(python_op.output)
    operator_x = PythonOperator(
        task_id="operator_x",
        python_callable=lambda x: print(
            "here printing xcom from classic inside taskflow", x
        ),
        op_args=[rat],
    )

    python_op >> python_op2
    rat >> operator_x

    py = PythonOperator(task_id="py", python_callable=lambda: ["file1", "file2"])
    filepaths = py.output.map(lambda x: f"/tmp/{x}")

    @task
    def print_filepaths(filepaths: list[str]):
        for filepath in filepaths:
            print(filepath)

    print_filepaths(filepaths)


xcom_args()
