from airflow.sdk import asset
from asset import asset_function


@asset(
    schedule=asset_function,
)
def asset_consumer(asset_events):
    print("Hello world")
    print("my asset is here")
    print("asset events", asset_events)
