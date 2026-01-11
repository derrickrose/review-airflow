# branching

## problem

- blindly processing everything even empty files
- inflexible logic
- poor error handling

## solution

- branching enables workflows to be more flexible and robust
- intelligent decision upon runtime
- choosing execution paths dynamically based on data, time, or external factors

## example

```text
- before: extract -> transform -> load
- after: extract -> check -> transform -> load
                           > clean ----> load
```

## use cases

- data validation: quality checks
- environment logic: different execution paths for different environments
- time-based decision: weekend, weekday
- resource optimization: high performance vs standard processing

## different approaches to achieve branching

- decorators: @task.branch , python function that returns task_ids
- @task.short_circuit , run or skip downstream tasks based on condition
- specialized operators: SQL, datetime, day-of-week branching

## how it works

- branching task evaluates condition
- returns task_id(s) to execute next
- other downstream tasks are skipped (not failed)
- trigger rules determine downstream behavior
- return a list of task ids in a list when condition are met
- return None will skip all downstream tasks
- works also with taskgroups
- access airflow context (logicaldate ...)
- query external systems at runtime
- use XCom values from upstream tasks
- environment-dependent logic

## @task.branch or BranchPythonOperator

- most flexible branching method in airflow
- modern taskflow api approach
- transforms python functions into branching operators
- custom logic -> task id decisions

## code

```python
@task.branch 
def branch_function(x):
    return "task_id_1" if x > 0 else "task_id_2"
    
with task_id_1 and task_id_2 must be valid task ids in the dag
```

## best practices

- branching processing should be lightweight
- pass heavy stuff to upstream tasks and pass values downs
- use XComs to pass data to branching tasks

## @task.short_circuit

- simple run or dont run decision
- like checkpoint
- return True or False
    - True continue normally
    - False skip
- use cases :
    - data availability: file exists ? new records ? then run task with heavy computation hunger
- all downstream tasks are skipped when the function returns False

## when to use short_circuit other branching

- short_circuit : when you have go and no go decision to make
- branching : when you have multiple paths to choose from

## special branch operators (actually built-on ones for common scenarios)

- prebuilt branch operators for common scenarios
- less code , optimized for specific scenarios
- SQL queries, date/time conditions, environments
- alternative to custom Python functions

### BranchSQLOperator

- makes decision based on SQL query results
- true results follow_task_true, false follow_task_false
- works with any airflow database connection
- use cases :
    - check data exists in a table
    - verify metrics meet thresholds
    - confirm dependent data processing is complete
- works with any sql dialect that airflow supports through it connection system
- the query must return a single column of boolean value or can be evaluated as true or false

```python
from airflow.providers.common.sql.operators.sql import BranchSQLOperator

branch_sql = BranchSQLOperator(
task_id="check_data_quality", 
conn_id="postgres_default", 
sql="SELECT count(*) > 1000 from daily_data where date = current_date;", #sql query conditional 
follow_task_ids_if_true=["load_data]", 
follow_task_ids_if_false=["clean_data"]
)
```

### BranchDayOfWeekOperator

- branch by day of week
- selected days inside a set follow_task_true, others follow_task_false
- use cases :
    - process data on weekends differently
    - process data on specific days differently

```python
from airflow.providers.standard.operators.branch import BranchDayOfWeekOperator 

is_weekend = BranchDayOfWeekOperator(
task_id="is_weekend",
week_day={5,6}, # Saturday and Sunday trigger the true branch and all others the false branch
follow_task_ids_if_true=["weekend_processing"], 
follow_task_ids_if_false=["weekday_processing"], 
follow_task_ids=["clean_data", "load_data"]
)
```

### BranchDateTimeOperator

- branch by time range
- must define lower and upper time boundaries
- operators checks if current time falls within the current time window
- use cases :
    - process data at specific times of day (epic hours)
    - process data at maintenance time windows or business hours

```python
from airflow.providers.standard.operators.branch import BranchDateTimeOperator 

is_night_time = BranchDateTimeOperator(
task_id="is_night_time", 
target_lower=datetime.time(22, 0), #10 PM 
target_upper=datetime.time(6, 0), #6 AM
follow_task_ids_if_true=["night_processing"], 
follow_task_ids_if_false=["day_processing"]
)
```

### for more complex scenarios

- BranchExternalPythonOperator
    - pre-existing virtual environment (if the logic needs special packages that are not available in airflow
      environment)
    - specific package dependencies
- BranchPythonVirtualenvOperator
    - new virtual environment per execution (creates a new python environment for each execution, when dealing with
      conflicted packages)
    - complete isolation and reproducibility
- they share the common behavior as
    - follow_task_ids_if_true and follow_task_ids_if_false
    - trigger rule, etc

## branch operators by use cases

| use case                  | branch operator                      |
|:--------------------------|:-------------------------------------|
| database-driven behaviors | BranchSQLOperator                    |
| day of week logic         | BranchDayOfWeekOperator              |
| time window processing    | BranchDateTimeOperator               |
| package dependencies      | BranchExternalPythonOperator         |
| complex custom logic      | @task.branch or BranchPythonOperator |
| simple validation         | @task.short_circuit                  |

## branching and trigger rules

- trigger rules determine when tasks run based on upstream tasks
- essential for robust branching workflows
- not expected behavior if not set correctly (may be skipped or failed when the should continue)
- default : all_success (all upstream have succeeded)

  ```text
  extract -> check -> transform -> load
                      -> clean ----> load
  ```

    - the problem is when you have a downstream task that depends on a branching
    - here one between clean and transform will be skipped so will be the downstream task too (load)

| rule                          | when task runs                                                                      |
|:------------------------------|:------------------------------------------------------------------------------------|
| all_success         (default) | all upstream tasks succeeded                                                        |
| none_failed_min_one_success   | no failures + at least one success                                                  |
| all_done                      | all upstream tasks finished (any state) e.g. final reporting that should always run |
| none_failed                   | no upstream task failed                                                             |
| one_success                   | at least one upstream succeeded                                                     |

## tips for branching and trigger rules

- plan trigger rules upfront
- keep branching logic simple
- use descriptive task ids
- add clear documentation
- test all branch paths
- consider using task groups to organize tasks