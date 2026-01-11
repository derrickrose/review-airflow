# taskgroup

- taskgroup organize related tasks into logical containers
- instead of seeing dozens of individual tasks, you see high-level business processes
- before : extract_customers -> validate_customers -> clean_customers -> load_customers
- after : customer_pipeline -> orders_pipeline -> product_pipeline -> reporting

## basics

- like organizing folders on the computer
- organizational tool for grouping related tasks
- visual containers in the Airflow UI
- No separate DAGs, all tasks stay in the same DAG
- collapsible sections for better readability
- logical business process grouping

## before taskgroups

- subdags but
    - separate DAGs instances
    - heavy overhead
    - complex setup
    - performance issues
    - harder to debug

## common use cases

- ETL pipelines: Extract, Transform, Load
- ML Workflows: preprocessing, training, evaluation
- Multi-team DAGs: team specific taskgroups
- Repeating patterns: template groups for similar processes
- complex workflows: hierarchical organization

## benefits of using taskgroups

- visual clarity: easy to read
- maintainability: organized code and logic
- reusability: template patterns across DAGs
- scoped configuration: group level settings
- better debugging: clear error isolation
- taskgroup is different from separated DAGs united by assets (may be different schedules, owned by different teams)

## creating taskgroups

- taskgroup decorator
- taskgroup in a context manager

### taskgroup decorator

- modern way to create taskgroups
- pythonic syntax
- works fine with the taskflow API with all its features

```python
@task_group(group_id="process_data")
def process_data():
    task1 = EmptyOperator(task_id="extract_customers")
    task2 = EmptyOperator(task_id="validate_customers")
    task1 >> task2
# must call the function to create the group    
process_data()
```

### taskgroup in a context manager

- works with traditional classic operators

```python 
with TaskGroup(group_id="process_data") as tg:
    task1 = EmptyOperator(task_id="extract_customers")
    task2 = EmptyOperator(task_id="validate_customers")
    task1 >> task2
# group is created immediately
```

## parameters that are supported by both approaches

- group_id
- default_args {"retries": 3}
- tooltip="Processes customer data" #UI documentation
- prefix_group_id=True => group_id.task_id referencing

## dependencies

- Task -> TaskGroup : connects to all root tasks (no upstream within the group)
- TaskGroup -> Task : all leaf tasks (no downstream within the group) connect
- no manual wiring needed: Airflow handles connections automatically

## when to use one to another approach

- when you need to use the decorators
    - modern, pythonic
    - functional based
    - taskflow api integration
    - must call function
    - great for reusable patterns
- when you need to use contex managers
    - traditional, explicit
    - block-based
    - works with all operators
    - immediate creation
    - clear visual boundaries

## dataflow and dependencies

- TaskGroups as data processing units
- input -> internal processing -> output
- seamless integration with TaskFlow API
- clean data contracts between components

```python
@task
def get_file_path():
    return "/path/to/file.csv"
   
@task_group
def process_file(file_path: str):
    @task
    def read_file(path:str):
        return data
    
    @task
    def clean_data(raw_data):
        return cleaned_data
    
    return clean_data(read_file(file_path))
process_file(get_file_path())
```

- TaskFlow API: direct parameter passing
    - result = task_a(input) -> task_b(result)
- traditional operators: XCom references
    - task_ids = "group_id.task_id"
- encapsulation: external tasks don't see internal structure
- real power of TaskGroups:
    - return data to downstream tasks using the decorator approach just like regular tasks
    - return value can be the return of a task or a dictionary containing multiple outputs allowing downstream tasks to
      access them easily and selectively

## best practices

- simple interfaces: clear inputs and outputs
- descriptive returns: use dictionaries with meaningful keys
- type hints:: document expected data types
- error handling: validate inputs and outputs
- testing: verify data flow under different scenarios

## dynamic and nested taskgroups

- advanced patterns for complex workflows
- dynamic generation: create taskgroups programmatically
- nested hierarchies: multi-level organization
- sequential dependencies: control execution order

## how to dynamically generate taskgroups

- variable data: unknown number of files to process
- multi-tenant : individual pipelines per customer
- batch processing: parallel processing of data partitions
- configuration-driven: taskgroups based on config files
- always append dynamically generated taskgroups in a list => this allows to reference easily

## dynamic task mapping with taskgroup

- it is possible to use expand() with taskgroups same as with regular individual tasks

## nested taskgroups

- create hierarchical taskgroups by nesting taskgroups inside other taskgroups to any depth
- maintain clear separation of concerns

## parallel and sequential processing 

## to watch out 
- dag parsing time: too many taskgroups slow parsing
- ui responsiveness: complex nesting affects visualization
- resource contention: parallel groups competing for resources 
- memory usage: large dynamic structures 

## best practices 
- monitoring dag performance metrics 
- use Airflow pools for resource management 
- consider separate DAGs for very large workflows 
- test with realistic data volumes 

