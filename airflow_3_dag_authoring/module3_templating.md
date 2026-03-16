# templating

## why templating?

- allows idempotent execution (executions for same date will retrieve same data)
- allows using date/datetime at runtime

## what is templating?

- templating is a way to inject dynamic information into task instances at runtime
- put in double curly braces `{{ }}`
- evaluated at runtime
- example: create a file with current date in it
    - DATA/file_{{ ds_nodash }}.txt => DATA/file_20210322.txt
- based on jinja templating engine, everything doable in jinja is almost doable in airflow

## runtime variables

| Variable                           | Description                     | Exemple                              |
|------------------------------------|---------------------------------|--------------------------------------|
| {{ ds }}                           | Date d’exécution (YYYY-MM-DD)   | 2025-11-18                           |
| {{ ds_nodash }}                    | Date sans tirets                | 20251118                             |
| {{ ts }}                           | Timestamp complet (UTC ISO8601) | 2025-11-18T00:00:00+00:00            |
| {{ ts_nodash }}                    | Timestamp sans tirets           | 20251118T000000                      |
| {{ run_id }}                       | Identifiant unique du run       | scheduled__2025-11-18T00:00:00+00:00 |
| {{ dag_run.conf }}                 | Paramètres du trigger           | {{ dag_run.conf["country"] }}        |
| {{ macros.ds_add(ds, n) }}         | Décalage de date                | macros.ds_add(ds, -1)                |
| {{ data_interval_start }}          | Début fenêtre data              | ...                                  |
| {{ data_interval_end }}            | Fin fenêtre data                | ...                                  |
| {{ task_instance.xcom_pull(...) }} | Lire un XCom                    | ...                                  |

## real case example

- requesting data from PostgresSQL database based on date
- let say the frequency is every day
- first execution will retrieve data from yesterday for example
- then next execution will retrieve data from today

## limitations of templating

- not all arguments of an operator are available for templating
    - template_fields defines which arguments are available for templating
    - template_ext is defines which file extensions are templatable
- for example for BashOperator, only bash_command and env are available for templating

```python
class BashOperator(BaseOperator):
    template_fields = ("bash_command","env")
    template_ext = (".sh",".bash")
    
# more dag code here 
run_this=BashOperator(
    task_id="run_this",
    bash_command="scripts/script.sh",
    env={"FOO": "bar"})
  
```

```bash 
#!/bin/bash
# content of scripts/script.sh
echo "today is {{ date_interval_start.format('dddd') }}" 
  
# this will print "today is DayOfWeek"
```

## best practices

- not to put scripts under the folder `dags`
- put scripts in a folder `include/scripts`, because folder dags is parsed by the scheduler, it will be parsed everytime
  the
  scheduler runs
- then add an argument to the dag "template_searchpath" with the path to the folder `include` as follows:

```python
with DAG(
    "my_dag",
    template_searchpath=["include"], # here setting the parameter template_searchpath
):
```

## Airflow Runtime Functions (Macros)

- macros allow to expose objects and une functions in the template
- some pre-injected functions are available

| Fonction                  | Description         | Exemple                                      |
|---------------------------|---------------------|----------------------------------------------|
| macros.ds_add(ds, n)      | Décaler une date    | macros.ds_add(ds, -1)                        |
| macros.datetime()         | Créer une datetime  | macros.datetime(2025, 11, 18)                |
| macros.timedelta(days=n)  | Delta de temps      | macros.timedelta(days=2)                     |
| macros.unixtime(dt)       | Vers Unix timestamp | macros.unixtime(ts)                          |
| macros.json.dumps(obj)    | JSON dump           | macros.json.dumps(dag_run.conf)              |
| macros.regex_search(p, s) | Regex search        | macros.regex_search('[0-9]+','file_123.csv') |
| macros.slugify(text)      | Slugify             | macros.slugify("Hello World!")               |
| macros.ds_format(...)     | Changer format date | macros.ds_format(ds,"%Y-%m-%d","%Y%m%d")     |
| macros.pendulum.parse()   | Parse date          | macros.pendulum.parse(ds).add(days=7)        |
| ti.xcom_pull()            | Lire XCom (Python)  | ti.xcom_pull("extract")                      |

## creating own macro

```python

def days_ago(data_interval_start, start_date):
    return (data_interval_start-start_date).days

with DAG(
    "my_dag",
    template_searchpath=["include"], # here setting the parameter template_searchpath,
    user_defined_macros={"days_ago": days_ago}
):
    run_this=BashOperator(
        task_id="run_this",
        bash_command="echo {{ days_ago(ds, macros.ds_add(ds, dag.start_date)) }} days ago",
        env={"FOO": "bar"})


```
