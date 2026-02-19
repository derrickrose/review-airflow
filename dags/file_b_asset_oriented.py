from airflow.sdk import asset

@asset(
    name="file_b_asset_oriented",
    uri="file:///opt/airflow/data/b.txt",
    description="Asset representing file B",
    schedule=None,  # Only runs when triggered by an event
)
def file_b_asset_oriented(file_metadata):
    """
    Asset DAG triggered when file metadata is available.
    """
    print("Asset DAG triggered!")
    print("File info:", file_metadata)
