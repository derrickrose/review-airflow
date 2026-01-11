from datetime import datetime, timedelta

from airflow.sdk import dag, task
from airflow.exceptions import AirflowException


@dag(
    dag_id="my_decorator_dag",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    schedule="@once",  # this is after airflow 2.4
)
def dag_decorator():
    @task
    def dummy_task():
        print("Hello world, using decorators")
        return "John"

    @task.branch
    def branch_task(name: str):
        today = datetime.now().date().weekday()
        print(f"Today is {today} {name}")
        return "weekend_task" if today in [5, 6] else "weekday_task"

    @task
    def weekend_task(name: str):
        print(f"It's weekend {name}")
        raise AirflowException("It's weekend")

    @task
    def weekday_task(name: str):
        print(f"It's weekday {name}")

    @task(trigger_rule="none_failed")
    def final_task(name: str):
        print(f"Good bye {name}")

    dummy = dummy_task()

    (
        branch_task(dummy)
        >> [weekend_task(dummy), weekday_task(dummy)]
        >> final_task(dummy)
    )


dag_decorator()
