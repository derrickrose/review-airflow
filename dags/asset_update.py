from datetime import datetime, timedelta

import random
from airflow.sdk import dag, Asset, task, Metadata


@dag(
    dag_id="asset_update",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
)
def asset_update():
    @task(outlets=[Asset("my_first_asset", uri="file:///opt/airflow/data/a.txt")])
    def update_asset():
        print("Hello world")

        with open("/opt/airflow/data/a.txt", "w") as f:
            f.write(f"Hello world {datetime.now()} \n")
        num = random.randint(1, 10)
        yield Metadata(
            Asset("my_first_asset", uri="file:///opt/airflow/data/a.txt"),
            {"my_extra_data": num},
        )  ## this send add an extra
        print("file updated")

    update_asset()


asset_update()
