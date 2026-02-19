import os
import logging
from datetime import datetime

from airflow.sdk import dag, task, PokeReturnValue
from file_b_asset_oriented import file_b_asset_oriented  # import the asset object

logger = logging.getLogger("airflow.task")

FILE_PATH = "/opt/airflow/data/b.txt"  # Path to monitor

@dag(
    dag_id="file_b_sensor",
    start_date=datetime(2021, 1, 1),
    schedule=None,
    description="File sensor DAG that triggers my_first_asset via outlets",
    catchup=False,
)
def file_a_sensor_taskflow_dag():

    @task.sensor(
        poke_interval=5,  # check every 5 seconds
        timeout=30,       # give up after 30 seconds
        mode="poke",      # keep worker busy
        task_id="file_a_sensor",
    )
    def wait_for_file():
        """
        Wait for FILE_PATH to exist and return metadata via XCom.
        """
        if os.path.exists(FILE_PATH):
            file_metadata = {
                "path": FILE_PATH,
                "size": os.path.getsize(FILE_PATH),
                "modified_time": os.path.getmtime(FILE_PATH),
            }
            logger.info("[SENSOR] File found: %s", file_metadata)
            return file_metadata  # This XCom will be passed to the asset

        logger.info("[SENSOR] File not found yet: %s", FILE_PATH)
        return PokeReturnValue(is_done=False)

    @task(outlets=[file_b_asset_oriented])
    def emit_asset(file_metadata):
        """
        Emit an asset event to trigger the asset DAG.
        """
        logger.info("[ASSET] Emitting asset event for file A: %s", file_metadata)
        # The asset DAG will be triggered automatically by Airflow

    # Chain tasks: sensor -> asset emitter
    emit_asset(wait_for_file())

# Instantiate DAG
file_a_sensor_taskflow_dag()
