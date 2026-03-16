# TaskFlow API

## Why TaskFlow API?

- before TaskFlow API it is difficult to share data between tasks
    - XCom push on the fist task to share data
    - XCom pull on the ones who need it
- there come the taskflow API to automate this process by injecting dependencies

## What is TaskFlow API?

- like a framework that brings functionalities to make DAG authoring easier
- components :
    - decorators to create tasks in faster and easier way
    - XComArgs to efficiently share data between tasks
    - XCom Backend (Optional) go beyond the limit of (2GB for Postgres) by putting S3 bucket instead of the DB

## Decorators

- Improve Dag authoring experience by removing boilerplate code
- list of decorators with corresponding operators

 decorator           | operator                 
---------------------|-------------------------- 
 @task               | PythonOperator           
 @task_group         | TaskGroup                
 @task.virtualenv    | PythonVirtualEnvOperator 
 @task.branch        | BranchPythonOperator     
 @task.short_circuit | ShortCircuitOperator     
 @task.sensor        | PythonSensor             
 @task.docker        | DockerOperator           
 @task.kubernetes    | KubernetesPodOperator    

- note: there is no decorator for s3 access fo example, to do that we can use @task followed by S3Hook

## build cleanest dag

```python
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
```

## configuring task

- where to put the parameters like retries, retry delay ?
- pretty simple, inside the decorator

```python
@task(retries=3, retry_delay=timedelta(minutes=5))
def dummy_task():
    print("Hello world, using decorators")
```

## accessing context from decorator

- 3 ways to access context
    - 1st way is to pass the parameters as key argument
    - 2nd way is to use the context parameter
    - 3rd way is to use the function get_current_context()

```python

# not forget to assign those variables to None since they are passed at runtime
# otherwise they will be considered as positional argument and parsing error will be raised
@task
def dummy_task(ti=None, ds=None):
    print(ti.task_id, ds)


to collect the context, we can use the context parameter
@task
def dummy_task(**context):
    print(context["task_instance"].task_id)
    
    
@task
def dummy_task():
    ti = get_current_context()["task_instance"]
    print(ti.task_id)

```

## XComArgs

- reference to an XCom value pushed from a previous task
- abstracts the logic of pulling the XCom value from the database and share value between tasks
- with XComArgs we have access to 2 amazing methods map() and zip()
- with classic operator, we have to abstract the task object with XComArg() or get the task's output variable
- but with the taskflow API we can directly access the XCom value without having to abstract the task object nor using
  the output attribute, just calling the decorated task will already return the XComArg Object

```python 
# this code will push an XCom value with default key "return_value" with value 1
operator = PythonOperator(task_id="task_id", python_callable=lambda:1) #  <Task(PythonOperator): python_operator>
xcom = XComArg(operator) #  <class 'airflow.sdk.definitions.xcom_arg.PlainXComArg'> 
print(xcom) # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }} 
print(xcom["my_key"]) # => {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='my_key') }} 
# but no need to absract the operator in order to have its XCom value; it is present in the task instance as output variable
print(operator.output) # { task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }}
```

- with the task decorator it automatically returns a XComArg object

```python 
# with the taskflow API we can do this
@task()
def task1():
    return 100
    
print(task1()) # {{ task_instance.xcom_pull(task_ids='task1', dag_id='xcom_args', key='return_value') }} 
```

```python
from datetime import datetime, timedelta

from airflow.sdk import dag, task
from airflow.providers.standard.operators.python import (
    PythonOperator,
)
from airflow.models.xcom_arg import XComArg


def push_and_return_v2(value, **context):
    ti = context["task_instance"]
    ti.xcom_push(key="my_key", value=value)
    return value


def push_and_return(op, **context):
    print(f"Printing the operator {op}")  # <Task(PythonOperator): python_operator>
    print(
        f"Printing the xcomarg(op)  {XComArg(op)}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }}, default value
    print(
        f"Printing the xcomarg(op) class  {XComArg(op).__class__}"
    )  # <class 'airflow.sdk.definitions.xcom_arg.PlainXComArg'>
    print(
        f"Printing the operator output {op.output}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='return_value') }}
    print(
        f"Printing the operator output class " f"{op.output.__class__}"
    )  # <class 'airflow.sdk.definitions.xcom_arg.PlainXComArg'>
    print(
        f"Printing the operator XComArg(op)['my_key']){XComArg(op)['my_key']}"
    )  # {{ task_instance.xcom_pull(task_ids='python_operator', dag_id='xcom_args', key='my_key') }}
    ti = context["task_instance"]
    print(f"pushing xcom with key my_key")
    ti.xcom_push(key="my_key", value=42)

    return 42


@dag(
    dag_id="xcom_args",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    schedule="@once",
)
def xcom_args():
    @task()
    def task1():
        return 100

    # this will push an XCom with the return_value 42
    python_operator = PythonOperator(
        task_id="python_operator", python_callable=push_and_return_v2, op_args=[42]
    )

    python_operator_2 = PythonOperator(
        task_id="python_operator_2",
        python_callable=push_and_return,
        op_args=[python_operator],  ## this will print the XComArg object
    )

    python_operator >> python_operator_2


xcom_args()

```

## sharing many XComs via TaskFlow API

- what we know actually is to share value between tasks using taskflom API and XComArgs

```python
@task(do_xcom_push=True)
def task1():
    return 100 # the return value will push the XCom directly to XCom
```

- to pull value from previous task

```python
@task
def task2(val: int):
    print(val)
task2(task1()) # here pulling the value from task1
```

- push XCom with different keyword and also pulling it

```python
@task(do_xcom_push=True)
def task3():
    return {"key": 100}  # return a dict with key "key"

@task
def task4(val: str):
    print(val)

task4(task3()["key"])
```

- now we are going to see how to share many Variables and pull them in the same task

```python
@task(multiple_outputs=True)
def task5():
    return {"key1": 100, "key2": 200}  # return a dict with keys "key" and "key2"

@task
def task6(val1: int, val2: int):
    print(val1 + val2)
ta = task5()
task6(ta["key1"], ta["key2"])

def task7(val):
    print(val["key1"] + val["key2"])
task7(ta)
```

## most efficient way to share data between tasks

- returning a dict with all the values we want to share
- can be done in 2 ways :
    - using multiple_outputs decorator
    - using specifying the return type of the decorated function

## sharing data between classic operators

- note dont forget that not all parameters are available for templating
- and this should be done with templating since the value is injected at runtime

```python
    python_op = PythonOperator(
        task_id="python_op", python_callable=lambda: 100
    )

    python_op2 = PythonOperator(
        task_id="python_op2", python_callable=lambda x: print("here printing", x),
        op_args=[python_op.output]
    )

    python_op >> python_op2
```

## sharing data from classic operator to taskflow API operator

```python
python_op = PythonOperator(
    task_id="python_op", python_callable=lambda: 100
)

@task
def tata(val: int):
    print(val)
    
tata(python_op.output)

```

## modifying the dag output

- method map() of the XComArg

```python
python_op = PythonOperator(
    task_id="python_op", python_callable=lambda: ["file1", "file2"]
)

file_path = XComArg(python_op).map(lambda x: f"/tmp/{x}")
@task
def tata(val: int):
    print(val)
    
tata(file_path)

```

- zip() method of the XComArg , actually apply same as python zip() function

```python
a = [1, 2, 3]
b = [4, 5, 6,1]
c = [4, 5, 6,1]
print(zip(a,b)) => [(1, 4), (2, 5), (3, 6)]

samething for XComArg
print(XComArg(a).zip(XComArg(b), XComArg(c))) => [(1, 4, 4), (2, 5, 5), (3, 6,6)]
```4