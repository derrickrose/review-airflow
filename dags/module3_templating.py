from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def sum_numbers(*args):
    print(f"AKI SUMIR {sum(args)}")


def process(**context):
    ds = context["ds"]
    yesterday = context["macros"].ds_add(ds, -1)
    country = context["dag_run"].conf.get("country", "FR")
    value = context["ti"].xcom_pull("extract")

    print(ds, yesterday, country, value)


with DAG(
    dag_id="module3_templating",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    # This argument takes a boolean value which determines whether to render templates with
    # Jinja’s default Environment or
    # NativeEnvironment.
    # render_template_as_native_obj=True, python native objects
    # without this, airflow will return a list of strings
    schedule="@daily",
) as dag:
    print_date = PythonOperator(
        task_id="print_date",
        python_callable=process,
    )

    python_operator = PythonOperator(
        task_id="python_operator",
        python_callable=sum_numbers,
        op_args="{{ dag_run.conf['numbers'] }}",
    )
