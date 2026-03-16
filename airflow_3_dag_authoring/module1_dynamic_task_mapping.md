# course objective partial and expand

- differentiate task mapping and dynamic tasks
- create tasks at runtime based upon current data

## history

- prior to airflow 2.3 we need to know in advance how many tasks to create
- there comes the dynamic task mapping if you dont know how many files to process in advance
- it might be files or output from SQL query ...

## how it works

- example fetching files on s3 and based on the output task are created
- create tasks at runtime based upon current data

## expand()

- map your tasks
- it is the first method of the dynamic task mapping concept
- it multiplies the task calling for it according to the arguments

  ```text
  Operator.expand(arg=[]) #list of values
  Operator.expand(arg={}) #dictionary of values
  Operator.expand(arg=XComArg) #XCom coming from previous task and still those XComs should be list of values or dico of
  values
  ```

  ```python3
  from airflow import DAG
  from airflow.sdk import task
  from datetime import datetime, timedelta
  with DAG(
      dag_id="dynamic_task_mapping",
      start_date=datetime(2023, 1, 1),
      schedule="@daily",
      dagrun_timeout=timedelta(minutes=60),
      description="dynamic task mapping",
      catchup=False,
  ) as dag:
  
      @task
      def download_files(file: str):
          print(f"downloading file {file}")
  
      # file1, file2, file3 are the files I want to download
      files = download_files.expand(file=["file1", "file2", "file3"])```
  ```

- on the UI we will see one task "download_files []" with a pair of empty bracket
- so if on the UI we see a task ended with pair of brackets it means the task is using expand

  ```text
  +---------------------+
  | download_files []   |
  +---------------------+
  
  ```

- upon running the dag, the value of tasks will be updated which is 3 (3 tasks have been mapped according to the list of
  files passed to expand)

## expand() but not knowing the number of files

- the real power of expand() comes from the fact that you dont know in advance how many files you will have to process
- to simulate this we will have to use random and add new function that returns a list of files
- the function will return a list of files passed through XComArg to the download_files.expand() task

  ```python3
  from airflow import DAG
  from airflow.sdk import task
  from datetime import datetime, timedelta
  import random # here
  with DAG(
      dag_id="dynamic_task_mapping",
      start_date=datetime(2023, 1, 1),
      schedule="@daily",
      dagrun_timeout=timedelta(minutes=60),
      description="dynamic task mapping",
      catchup=False,
  ) as dag:
  
      @task# here added a new function get_files()
      def get_files():
          return [f"file{nb} for nb in range(random.randint(3, 5))
  
      @task
      def download_files(file: str):
          print(f"downloading file {file}")
  
      # file1, file2, file3 are the files I want to download
      files = download_files.expand(file=get_files())
  ```

- so on the UI we will see 2 tasks "get_files" and "download_files"

  ```text
  +-----------+                    +---------------------+
  | get_files |    ------->        | download_files []   |
  +-----------+                    +---------------------+
  ```

- upon running the dag, the value of tasks will be updated which is 5 (5 tasks have been mapped according to the list of
  files returned by the get_files() function)
- if we run the dag again, the number of tasks will be different (3 for example)

## limit of expand()

- AIRFLOW__CORE__MAX_MAP_LENGTH=1024
    - this is the maximum number of tasks that can be mapped to expand()
- max_active_tis_per_dag (default=16)
    - this is the maximum number of active tasks run (task instances) from that mapping (on dag level)
    ```python3
      Operator.partial(max_active_tis_per_dag=10).expand(arg=XComArg)
    ```

## partial()

- to introduce a constant value to the expand() function

  ```python3
  Operator.partial().expand(arg=XComArg)
  ```
- let say we have the files randomly but the bucket and the folder does not change

  ```python3
  from airflow import DAG
  from airflow.sdk import task
  from datetime import datetime, timedelta
  import random # here
  with DAG(
      dag_id="dynamic_task_mapping",
      start_date=datetime(2023, 1, 1),
      schedule="@daily",
      dagrun_timeout=timedelta(minutes=60),
      description="dynamic task mapping",
      catchup=False,
  ) as dag:
  
      @task# here
      def get_files():
          return [f"file{nb} for nb in range(random.randint(3, 5))
  
      @task
      def download_files(folder: str, file: str): ##here added new parameter folder
          print(f"downloading file {file} from folder {folder} {folder}/{file}")
  
      # file1, file2, file3 are the files I want to download 
      # here added partial() to introduce a constant value to the expand() function
      # argument folder is passed to partial()
      files = download_files.partial(folder="/usr/local").expand(file=get_files())
  ```

## partial() with non-Taskflow Operator

- non taskflow operator
  ```python3
    #Correct
    test = BashOperator.partial(
    task_id="test"
    ).expand(bash_command=['echo "hi"', 'echo "world"'])
    
    #Wont working
    BashOperator(task_id="test2").expand(bash_command=['echo'])
  ```
- taskflow operator
  ```python3
    #Correct
    @task(task_id="test")
    def download_file(file:str):
        print(file)
    files = download_file.expand(file=get_files())
    
    #Wont working
    @task
    def download_file(file:str):
        print(file)
    files = download_file.partial(task_id="test").expand(file=get_files())
  ```

## mapping with a non-Taskflow Operator

- need to import BashOperator

  ```python
    from airflow.operators.bash import BashOperator 
    from airflow import DAG
    from airflow.sdk import task
    from datetime import datetime, timedelta
    import random # here
    with DAG(
        dag_id="dynamic_task_mapping",
        start_date=datetime(2023, 1, 1),
        schedule="@daily",
        dagrun_timeout=timedelta(minutes=60),
        description="dynamic task mapping",
        catchup=False,
    ) as dag:
    
        @task# here
        def get_files():
            return [f"file{nb} for nb in range(random.randint(3, 5))
    
        @task
        def process_file(folder: str, file: str): ##here added new parameter folder
            print(f"process file {file} from folder {folder} {folder}/{file}")
            return f"ls {folder}/{file}; exit O" # changed here to return the bash command to execute
    
        # file1, file2, file3 are the files I want to download 
        # here added partial() to introduce a constant value to the expand() function
        # argument folder is passed to partial()
        files = process_file.partial(folder="/usr/local").expand(file=get_files())
        
        BashOperator.partial(task_id="ls_file").expand(bash_command=files)
  
  ```
- so on the UI we will see 3 tasks "get_files", "process_file" and "ls_file"

  ```text
  +-----------+                    +---------------------+                   +---------------------+
  | get_files |    ------->        | process_file []     |   ------->        | list_file []        |
  +-----------+                    +---------------------+                   +---------------------+
  ```
- upon on running the dag, the tasks update values inside the brackets:

  ```text
  +-----------+                    +---------------------+                   +---------------------+
  | get_files |    ------->        | process_file []     |   ------->        | list_file []        |
  +-----------+                    +---------------------+                   +---------------------+
  ```
- what we did is using expand()
- use the output of dynamically mapped tasks to input of non taskflow operator

## from mapped tasks to classic operator

- from expand(), one can create tasks based on current data
- how to expand a taskflow operator @task and a classic operator e.g. BashOperator
- how to use the output of a mapped task into a classic operator to expand it
- now, what if we want to use the output of a mapped task into a non taskflow operator instead of using expand() again
  ```text
  # previous use case
   get_files --> download_file[0] --> BashOperator[0]
                download_file[1]      BashOperator[1]
                download_file[2]      BashOperator[2]
  
  
  # this use case 
  get_files --> download_file[0] --> BashOperator
                download_file[1]
                download_file[2]
  
  ```