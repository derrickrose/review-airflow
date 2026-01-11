# XCom 101

## what is xcom

- way to sharing data between tasks
- stored in metadata db
- identified by (key, run_id, task_id, execution_date, map_index, index, dag_id,...) to make it unique between runs and
  all xcoms

## sharing data using task instance xcom_push and pull

- using context
- with just ti=None as parameter of the decorated function
- with return values (all those we already seen in the previous chapters taskflow api)

```python

@task
def task_1(**context:Context):
    context['ti'].xcom_push(key='my_key', value='my_value')
@task
def task_2(**context:Context):
    print(context['ti'].xcom_pull(task_ids="task_1", key='my_key'))


```

## limitations

- json serializable
- size of xcoms

  | db | value |
    |----------|---------------------------------------------|
  | Postgres | 1gb |
  | SQLite | 2gb |
  | MySQL | 64MB per XCom from airflow 2.9, before 64KB | 


