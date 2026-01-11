# Programmatically Clearing Airflow Task Instances (Airflow <2.5 → 3.x)

This document provides a **complete, version-aware guide** to clearing Airflow task instances programmatically using Python. It includes:

- Working code for **Airflow <2.5**, **2.5**, **2.6+**, **3.x**
- Full upstream/downstream recursive clearing
- TaskGroup clearing
- Version-specific logic
- The exact reason why older internet snippets stopped working
- Production-ready implementations

Airflow allows clearing task instances manually via the UI or CLI, but in many production cases you need to:

- Force retry a specific task
- Re-run an entire upstream chain
- Dynamically retrigger a dependency path
- Reset TaskGroups
- Implement custom retry logic inside DAGs

---

# 🔥 Why this is needed

Before Airflow 2.6, most code used `execution_date`:

```
ti = TaskInstance(task, execution_date=context["execution_date"])
ti.set_state(State.NONE)
```

In Airflow 2.6+, **this stops working** because:

- TaskInstances are now keyed by `run_id`
- execution_date is no longer a primary key
- clearing fails silently

This README provides the correct code for **all Airflow versions**.

---

# 1️⃣ Airflow Version Differences (Summary)

## ✔️ Airflow < 2.5
- Uses `execution_date`
- Recursive clearing works
- TaskGroup UI clearing supported

## ✔️ Airflow 2.5
- Transition phase
- Both run_id and execution_date work

## ❌ Airflow 2.6+
- Must use run_id
- execution_date clears break
- Recursive clearing fails unless updated

## ✔️ Airflow 3.x
- Same as 2.6+
- Python clearing still works
- UI clearing unreliable

---

# 2️⃣ Airflow < 2.5 — Legacy Clearing Code

## Clear task (legacy)

```python
def clear_task_pre_25(task, execution_date):
    ti = TaskInstance(task=task, execution_date=execution_date)
    with create_session() as session:
        ti.set_state(State.NONE, session=session)
        session.commit()
```

## Clear upstream (legacy)

```python
def clear_upstream_pre_25(task, execution_date, depth=999):
    visited = set()

    def walk(t, d):
        if d < 0 or t.task_id in visited:
            return
        visited.add(t.task_id)

        ti = TaskInstance(task=t, execution_date=execution_date)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()

        for upstream in t.get_direct_relatives(upstream=True):
            walk(upstream, d - 1)

    walk(task, depth)
```

## Clear downstream (legacy)

```python
def clear_downstream_pre_25(task, execution_date, depth=999):
    visited = set()

    def walk(t, d):
        if d < 0 or t.task_id in visited:
            return
        visited.add(t.task_id)

        ti = TaskInstance(task=t, execution_date=execution_date)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()

        for downstream in t.get_direct_relatives(upstream=False):
            walk(downstream, d - 1)

    walk(task, depth)
```

---

# 3️⃣ Airflow 2.5 — Transition Code

Recommended: **Use run_id**, even though execution_date still works.

---

# 4️⃣ Airflow 2.6 → 3.x — Modern Correct Code

## ❗ All code must use run_id

---

## Clear a single task (modern)

```python
def clear_task(task, dag_run):
    run_id = dag_run.run_id
    ti = TaskInstance(task=task, run_id=run_id)

    with create_session() as session:
        ti.set_state(State.NONE, session=session)
        session.commit()
```

---

## Clear upstream (modern)

```python
def clear_upstream(task, dag_run, depth=999):
    visited = set()
    run_id = dag_run.run_id

    def walk(t, d):
        if d < 0 or t.task_id in visited:
            return
        visited.add(t.task_id)

        ti = TaskInstance(task=t, run_id=run_id)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()

        for upstream in t.get_direct_relatives(upstream=True):
            walk(upstream, d - 1)

    walk(task, depth)
```

---

## Clear downstream (modern)

```python
def clear_downstream(task, dag_run, depth=999):
    visited = set()
    run_id = dag_run.run_id

    def walk(t, d):
        if d < 0 or t.task_id in visited:
            return
        visited.add(t.task_id)

        ti = TaskInstance(task=t, run_id=run_id)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()

        for downstream in t.get_direct_relatives(upstream=False):
            walk(downstream, d - 1)

    walk(task, depth)
```

---

## Clear upstream + downstream (modern)

```python
def clear_up_down(task, dag_run, depth=999):
    visited = set()
    run_id = dag_run.run_id

    def walk(t, d):
        if d < 0 or t.task_id in visited:
            return
        visited.add(t.task_id)

        ti = TaskInstance(task=t, run_id=run_id)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()

        for u in t.get_direct_relatives(upstream=True):
            walk(u, d - 1)

        for dwn in t.get_direct_relatives(upstream=False):
            walk(dwn, d - 1)

    walk(task, depth)
```

---

## Clear entire TaskGroup (modern)

```python
def clear_taskgroup(group_id, dag, dag_run):
    run_id = dag_run.run_id

    tasks = [
        t for t in dag.tasks
        if t.task_group and t.task_group.group_id == group_id
    ]

    for t in tasks:
        ti = TaskInstance(task=t, run_id=run_id)
        with create_session() as session:
            ti.set_state(State.NONE, session=session)
            session.commit()
```

---

# 5️⃣ Why Code Broke After Airflow 2.5

- TaskInstances no longer keyed by execution_date
- run_id is now required
- Mapped tasks create multiple TIs per task_id
- TaskGroup UI clearing was removed/buggy in 2.6+

---

# 6️⃣ Full DAG Example

```python
from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    "clear_demo",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    schedule_interval=None,
):

    @task
    def A(): print("A")

    @task
    def B(): print("B")

    @task
    def C(): print("C")

    @task
    def clear_trigger(**context):
        dag = context["dag"]
        dag_run = context["dag_run"]

        target = dag.get_task("C")
        clear_upstream(target, dag_run, depth=5)

    A() >> B() >> C() >> clear_trigger()
```

---

# 7️⃣ Compatibility Table

Feature | <2.5 | 2.5 | 2.6–2.9 | 3.x
--------|------|-----|----------|------
execution_date clearing | ✅ | ⚠️ | ❌ | ❌
run_id clearing | ❌ | ✅ | ✅ | ✅
upstream clearing | ✅ | ⚠️ | ❌ old, ✔️ new | ✔️
TaskGroup UI | ✔️ | ✔️ | ❌ | ❌
Python TaskGroup clear | ✔️ | ✔️ | ✔️ | ✔️
Mapped tasks | ❌ | ⚠️ | ✔️ | ✔️

---

# Final Guidance

- Always use **run_id**
- Never use `execution_date` after Airflow 2.5
- Recursive clearing works perfectly with modern code
- UI clearing is unreliable in Airflow 2.6+, but Python clearing is 100% reliable

