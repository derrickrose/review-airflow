# dynamic dags

## why dynamic dags?

- almost always the same process for each dag but with little differences
- instead of writing a code for each dag, we can write a code once and just change the parameters
- increasing maintainability
- reducing code duplication and odds of bugs

## difference between dynamic dags and dynamic tasks

- dynamic dags allow to create multiple dags based on predefined values
- dynamic tasks mapping allow to create multiple tasks bases on tasks outputs

## different ways to create dynamic dags:

- single file approach
- drawbacks of the single file approach
- the best approach

### creating dynamic dags using the single file approach

```python
from airflow import DAG
from datetime import datetime, timedelta
from airflow.sdk import task

def create_dag(filename):
    with DAG(
        task_id=filename,
        schedule_interval='@daily',
        start_date=datetime(2021, 1, 1),
        catchup=False, 
        dagrun_timeout=timedelta(minutes=60)
    ) as dag:
        
        @task
        def download_file():
            print(f"downloading file from {filename}")
            
        @def load_data_to_db():
            print(f"loading data to db from {filename}")
            
        download_file() >> load_data_to_db()

    return dag

# to  add a new dag, just add a new file to the list and that's it
for file in ["filea.csv", "fileb.csv", "filec.csv"]:
    ## define the global variable table, basically a dictionary which contains all variables defined on top level of a file
    ## Airflow discovers DAGs by looking at global variables that contain DAG objects.
    globals()[f"dag_{file}] = create_dag(file)
```

### drawbacks of the single file approach

- no access to the generated DAG code <=> not easy to debug
- not really scalable if you have many values as arguments to generate DAGs, because the scheduler parses all files each
  30 seconds by default
    - min_file_process_interval parameter can be used to change this interval
- confusing since after removing a parameter from the list, the DAG will still exist on the Airflow UI

### the best approach, multiple files with a template and a script generator

- template file which contains the DAG definition
- folder which contains json data files equivalent to the parameters to generate DAGs
  - script which generates the DAGs based on the template file and replacing the parameters in the template file with the
    values from the json files