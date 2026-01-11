from airflow.sdk import asset


@asset(
    name="my_first_asset",
    uri="file:///opt/airflow/data/a.txt",
    description="my first asset",
    schedule="@hourly",
)
def asset_function():
    print("Hello world")
    print("my asset is here")
