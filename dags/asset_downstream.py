from datetime import datetime, timedelta

from airflow import Asset
from airflow.sdk import task, dag


@dag(
    dag_id="my_downstream_dag",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    schedule=[Asset("my_first_asset", uri="file:///opt/airflow/data/a.txt")],
)
def my_downstream_dag():

    @task(inlets=[Asset("my_first_asset", uri="file:///opt/airflow/data/a.txt")])
    def get_extra_inlet(inlet_events):
        for asset, asset_list in inlet_events.items():
            if asset_list[-1].timestamp > asset_list[0].timestamp:
                print(f"Asset {asset} was updated at {asset_list[-1].timestamp}")
                print(asset, asset_list)
                print(asset, asset_list[-1].extra)
                print(asset, asset_list[-1].timestamp)
                print(asset, asset_list[0].source_run_id)

    get_extra_inlet()


my_downstream_dag()
