# Airflow 3 Dynamic Task Mapping — Rules of Thumb

A comprehensive guide to understanding and implementing dynamic task mapping in Apache Airflow 3.x.

---

## Table of Contents
1. [Rule #1 — TaskFlow maps function arguments directly](#rule-1)
2. [Rule #2 — Classic Operators map via `op_kwargs` OR `op_args`](#rule-2)
3. [Rule #3 — XComArg is NOT iterable at parse time](#rule-3)
4. [Rule #4 — Return appropriate list types](#rule-4)
5. [Rule #5 — Use `.partial()` for constant arguments](#rule-5)
6. [Rule #6 — Chain mapped tasks naturally](#rule-6)
7. [Rule #7 — Parse Time vs Runtime Execution ⚠️](#rule-7)
8. [Rule #8 — Map multiple parameters simultaneously](#rule-8)
9. [Rule #9 — Classic operators remain compatible](#rule-9)
10. [Rule #10 — Best Practices Summary](#rule-10)

---

## <a name="rule-1"></a>⭐ Rule #1 — TaskFlow (`@task`) maps function arguments directly

TaskFlow supports mapping any argument defined in the function signature.

### ✔ Example
```python
from airflow.sdk import task

@task
def process(file: str):
    print(f"Processing {file}")

process.expand(file=["A", "B", "C"])
```

### What Airflow executes:
- `process[0] → process(file="A")`
- `process[1] → process(file="B")`
- `process[2] → process(file="C")`

---

## <a name="rule-2"></a>⭐ Rule #2 — Classic Operators map via `op_kwargs` OR `op_args`

Classic operators **cannot** map function parameters directly.  
They map through **`op_kwargs`** (keyword arguments) or **`op_args`** (positional arguments).

### ✔ Using `op_kwargs` (recommended - more explicit)
```python
from airflow.providers.standard.operators.python import PythonOperator

def imprimir(file, **context):
    print(f"Processing: {file}")

PythonOperator.partial(
    task_id="imprimir_task", 
    python_callable=imprimir
).expand(op_kwargs=[
    {"file": "A"},
    {"file": "B"},
    {"file": "C"},
])
```

### ✔ Using `op_args` (positional arguments)
```python
def imprimir(filepath: str):
    print(f"Processing: {filepath}")

PythonOperator.partial(
    task_id="imprimir_task",
    python_callable=imprimir
).expand(op_args=[
    ["file_A"],  # Note: each element is a list
    ["file_B"],
    ["file_C"],
])
```

### Key difference:
- **`op_kwargs`** → list of **dictionaries** → `[{"arg": val}, ...]`
- **`op_args`** → list of **lists** → `[["val1"], ["val2"], ...]`

---

## <a name="rule-3"></a>⭐ Rule #3 — XComArg is NOT iterable at parse time

You **cannot loop** over an XComArg during DAG parsing.

### ❌ Wrong
```python
files = build_file()  # Returns XComArg
for f in files:  # ERROR at parse time
    print(f)
```

### ✔ Right — Pass XComArg directly to `.expand()`
```python
@task
def build_file():
    return ["file1", "file2", "file3"]

files = build_file()  # This is an XComArg

@task
def process(file: str):
    print(file)

process.expand(file=files)  # Airflow unpacks at runtime
```

### ✔ Right — Transform XComArg with another task
```python
@task
def build_file():
    return ["file1", "file2"]

@task
def to_kwargs_list(files):
    return [{"file": f} for f in files]

files = build_file()
kwargs_list = to_kwargs_list(files)

PythonOperator.partial(
    task_id="process",
    python_callable=imprimir
).expand(op_kwargs=kwargs_list)
```

---

## <a name="rule-4"></a>⭐ Rule #4 — Return appropriate list types for dynamic mapping

The upstream task must return the correct list format based on how you're mapping.

### For TaskFlow (`@task`)
Return a **flat list**:
```python
@task
def get_files():
    return ["A", "B", "C"]  # ✔ Correct
```

### For PythonOperator with `op_kwargs`
Return a **list of dictionaries**:
```python
@task
def get_files():
    return [{"file": "A"}, {"file": "B"}, {"file": "C"}]  # ✔ Correct
```

### For PythonOperator with `op_args`
Return a **list of lists**:
```python
@task
def get_files():
    return [["A"], ["B"], ["C"]]  # ✔ Correct
```

---

## <a name="rule-5"></a>⭐ Rule #5 — Use `.partial()` for constant arguments

When mapping, use `.partial()` to set arguments that **don't change** across tasks.

### ✔ Example with TaskFlow
```python
@task
def download(folder: str, file: str):
    print(f"Downloading {folder}/{file}")

download.partial(folder="/data").expand(file=["A", "B", "C"])
```

**What happens:**
- `download[0] → download(folder="/data", file="A")`
- `download[1] → download(folder="/data", file="B")`
- `download[2] → download(folder="/data", file="C")`

### ✔ Example with PythonOperator
```python
def process_file(base_path: str, filename: str):
    print(f"Processing {base_path}/{filename}")

PythonOperator.partial(
    task_id="process",
    python_callable=process_file
).expand(op_kwargs=[
    {"base_path": "/data", "filename": "A"},
    {"base_path": "/data", "filename": "B"},
])
```

---

## <a name="rule-6"></a>⭐ Rule #6 — Chain mapped tasks naturally with TaskFlow

Mapped tasks can be chained; Airflow automatically handles dependencies.

### ✔ Example
```python
@task
def build_files():
    return ["file1", "file2", "file3"]

@task
def build_path(folder: str, file: str):
    return f"{folder}/{file}"

@task
def download(path: str):
    print(f"Downloading: {path}")

# Chaining mapped tasks
files = build_files()
paths = build_path.partial(folder="/data").expand(file=files)
download.expand(path=paths)  # Automatically depends on paths
```

**Flow:**
```
build_files() 
    → build_path[0], build_path[1], build_path[2]
        → download[0], download[1], download[2]
```

---

## <a name="rule-7"></a>⭐ Rule #7 — Parse Time vs Runtime Execution ⚠️

### 🚨 CRITICAL: Always use `@task` for data generation

**Golden Rule:** If a function generates data for dynamic task mapping, **ALWAYS** use `@task` decorator.

### ❌ Wrong — Parse Time Execution
```python
# This function runs when Airflow LOADS the DAG (every 30 seconds!)
def old_create_paths_list():
    return [[f"file{i}"] for i in range(randint(3, 7))]

paths_list = old_create_paths_list()  # ← Executes immediately at parse time

PythonOperator.partial(
    task_id="old_python_operator",
    python_callable=imprimir
).expand(op_args=paths_list)  # ← Uses static/frozen data
```

**Problems:**
- `randint()` runs **once** when DAG is parsed, result is **frozen**
- Every DAG run uses the **same static list**
- If function has API calls, database queries, etc., they run **every 30 seconds** during DAG parsing
- Can cause performance issues and unnecessary resource usage

### ✔ Right — Runtime Execution
```python
# This function runs when the DAG EXECUTES
@task
def create_paths_list():
    return [[f"file{i}"] for i in range(randint(3, 7))]

paths_list = create_paths_list()  # ← Returns XComArg, executes at runtime

PythonOperator.partial(
    task_id="python_operator",
    python_callable=imprimir
).expand(op_args=paths_list)  # ← Uses fresh runtime data
```

**Benefits:**
- `randint()` runs **every DAG execution**, generating fresh data
- Each DAG run can have different number of dynamic tasks
- No performance impact on scheduler
- Can access runtime context (execution date, variables, XComs)

### When to use `@task` vs plain function

| Scenario | Use `@task`? | Reason |
|----------|--------------|--------|
| Generating dynamic lists | ✅ YES | Runs at runtime, fresh data every execution |
| Using `randint()`, `datetime.now()` | ✅ YES | Need runtime evaluation |
| API calls, database queries | ✅ YES | Should run during execution, not parsing |
| Reading files, checking conditions | ✅ YES | Runtime data needed |
| Static hardcoded list `["a", "b"]` | ❌ No (but OK) | Data never changes |
| Constants/configuration | ❌ No | Truly static values |

### Exception: Static Data Only
```python
# ✔ OK - Truly static, hardcoded data
STATIC_FILES = ["file1", "file2", "file3"]

@task
def process(file: str):
    print(file)

process.expand(file=STATIC_FILES)  # This is acceptable
```

**Best Practice:** When in doubt, use `@task`. It doesn't hurt and ensures runtime execution.

---

## <a name="rule-8"></a>⭐ Rule #8 — Map multiple parameters simultaneously

You can map multiple parameters at once using `.expand()`.

### ✔ Cross-Product Mapping
```python
@task
def process(file: str, format: str):
    print(f"Processing {file} as {format}")

process.expand(
    file=["A", "B"],
    format=["csv", "json"]
)
# Creates 4 tasks: A+csv, A+json, B+csv, B+json (cross-product)
```

### ✔ Paired/Zipped Mapping
For paired mapping (not cross-product), return dictionaries with multiple keys:

```python
@task
def get_pairs():
    return [
        {"file": "A", "format": "csv"},
        {"file": "B", "format": "json"},
        {"file": "C", "format": "parquet"}
    ]

@task
def process(file: str, format: str):
    print(f"{file} → {format}")

# Use expand_kwargs for dictionary unpacking
process.expand_kwargs(get_pairs())
# Creates 3 tasks: A+csv, B+json, C+parquet (paired)
```

---

## <a name="rule-9"></a>⭐ Rule #9 — Classic operators remain compatible in Airflow 3

Your existing DAGs using PythonOperator, BashOperator, etc. remain fully compatible.

### ✔ Example with BashOperator
```python
from airflow.providers.standard.operators.bash import BashOperator

@task
def get_commands():
    return [{"bash_command": f"echo Processing file {i}"} for i in range(3)]

BashOperator.partial(
    task_id="bash_dynamic"
).expand(op_kwargs=get_commands())
```

### ✔ Example with PythonOperator
```python
def my_function(value: int):
    print(f"Value: {value}")

@task
def get_values():
    return [{"value": i} for i in range(5)]

PythonOperator.partial(
    task_id="python_dynamic",
    python_callable=my_function
).expand(op_kwargs=get_values())
```

---

## <a name="rule-10"></a>⭐ Rule #10 — Best Practices Summary

### ✅ DO:
- ✔ Always use `@task` decorator for functions that generate mapping data
- ✔ Use `.partial()` for constant arguments across mapped tasks
- ✔ Return appropriate list types (`list` for TaskFlow, `list of dicts` for `op_kwargs`, `list of lists` for `op_args`)
- ✔ Pass XComArg directly to `.expand()` without iterating
- ✔ Chain mapped tasks naturally — let Airflow handle dependencies
- ✔ Use `op_kwargs` over `op_args` for clarity (named arguments)

### ❌ DON'T:
- ✖ Don't call functions directly without `@task` for dynamic data generation
- ✖ Don't iterate over XComArg at parse time (`for f in files:`)
- ✖ Don't mix TaskFlow patterns with classic operator patterns
- ✖ Don't forget that `op_args` needs **list of lists**, not flat list
- ✖ Don't use parse-time logic for runtime data (API calls, database queries, random values)

---

## 📊 Quick Reference Table

| Feature | TaskFlow `@task` | PythonOperator (Classic) |
|---------|------------------|--------------------------|
| **Mapping style** | `.expand(arg=value)` | `.expand(op_kwargs=list_of_dicts)` or `.expand(op_args=list_of_lists)` |
| **Function args mapping** | Direct | Through `op_kwargs` or `op_args` |
| **Upstream return for simple list** | `["A", "B"]` | `[{"file":"A"}, {"file":"B"}]` or `[["A"], ["B"]]` |
| **Can map `file=` directly?** | ✔ Yes | ❌ No (use `op_kwargs={"file": ...}`) |
| **Requires `op_kwargs`/`op_args`?** | ❌ No | ✔ Yes |
| **Can iterate XComArg at parse time?** | ❌ Never | ❌ Never |
| **Use `.partial()` for constants?** | ✔ Yes | ✔ Yes |
| **Chain mapped tasks?** | ✔ Automatic | ✔ Via XComArg |
| **Parse vs Runtime** | Always runtime with `@task` | Runtime with `@task`, parse without |

---

## 🎯 Complete Working Example

```python
from datetime import datetime, timedelta
from random import randint
from airflow import DAG
from airflow.sdk import task
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="dynamic_task_mapping_complete",
    start_date=datetime(2024, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
) as dag:

    # ========== TaskFlow Dynamic Mapping ==========
    
    @task
    def build_files():
        """Generate random number of files (runtime execution)"""
        return [f"file_{i}.txt" for i in range(randint(3, 7))]

    files = build_files()

    @task
    def build_filepath(folder: str, file: str):
        """Build full file paths"""
        return f"{folder}/{file}"

    # Using .partial() for constant 'folder' argument
    paths = build_filepath.partial(folder="/data/raw").expand(file=files)

    @task
    def download_file(path: str):
        """Simulate file download"""
        print(f"Downloading: {path}")
        return path

    # Chain mapped tasks
    downloaded = download_file.expand(path=paths)

    @task
    def process_file(path: str):
        """Process downloaded files"""
        print(f"Processing: {path}")

    process_file.expand(path=downloaded)

    # ========== Classic Operator with op_kwargs ==========
    
    @task
    def create_processing_configs():
        """Generate processing configurations (runtime execution)"""
        return [
            {"filepath": f"config_{i}.json", "priority": i} 
            for i in range(randint(2, 5))
        ]

    def process_config(filepath: str, priority: int, **context):
        """Process configuration file"""
        print(f"Processing {filepath} with priority {priority}")

    PythonOperator.partial(
        task_id="process_configs",
        python_callable=process_config
    ).expand(op_kwargs=create_processing_configs())

    # ========== Classic Operator with op_args ==========
    
    @task
    def create_report_paths():
        """Generate report paths (runtime execution)"""
        return [[f"report_{i}.pdf"] for i in range(randint(2, 4))]

    def generate_report(report_path: str):
        """Generate report"""
        print(f"Generating report: {report_path}")

    PythonOperator.partial(
        task_id="generate_reports",
        python_callable=generate_report
    ).expand(op_args=create_report_paths())

    # ========== Multiple Parameter Mapping ==========
    
    @task
    def get_processing_pairs():
        """Get file-format pairs for processing"""
        return [
            {"file": "data_1", "format": "csv"},
            {"file": "data_2", "format": "json"},
            {"file": "data_3", "format": "parquet"}
        ]

    @task
    def convert_file(file: str, format: str):
        """Convert file to specified format"""
        print(f"Converting {file} to {format}")

    convert_file.expand_kwargs(get_processing_pairs())
```

---

## 🔍 Common Pitfalls and Solutions

### Pitfall #1: Calling function at parse time
```python
# ❌ WRONG
def get_data():
    return [1, 2, 3]
data = get_data()  # Runs at parse time

# ✔ RIGHT
@task
def get_data():
    return [1, 2, 3]
data = get_data()  # Runs at runtime
```

### Pitfall #2: Wrong list format for PythonOperator
```python
# ❌ WRONG
@task
def get_files():
    return ["file1", "file2"]  # Flat list

PythonOperator.partial(...).expand(op_kwargs=get_files())  # ERROR!

# ✔ RIGHT
@task
def get_files():
    return [{"file": "file1"}, {"file": "file2"}]  # List of dicts

PythonOperator.partial(...).expand(op_kwargs=get_files())  # WORKS!
```

### Pitfall #3: Iterating XComArg
```python
# ❌ WRONG
files = get_files()
for f in files:  # ERROR: XComArg not iterable
    process(f)

# ✔ RIGHT
files = get_files()
process.expand(file=files)  # Let Airflow handle iteration
```

---

## 📚 Additional Resources

- [Official Airflow Documentation - Dynamic Task Mapping](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html)
- [Airflow TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
- [Airflow Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html)

---

## 🎓 Key Takeaways

1. **Always use `@task`** for functions generating dynamic mapping data
2. **TaskFlow is simpler** — prefer it over classic operators when possible
3. **Use `.partial()`** for constant arguments in mapped tasks
4. **XComArg cannot be iterated** — pass directly to `.expand()`
5. **Match list format** to mapping method (`list`, `list of dicts`, or `list of lists`)
6. **Parse time ≠ Runtime** — understand when code executes
7. **Chain naturally** — Airflow handles mapped task dependencies automatically

---
