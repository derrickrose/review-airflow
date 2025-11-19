# Airflow CeleryExecutor Parallelism Configuration Guide

## Table of Contents
- [Overview](#overview)
- [Key Parameters Explained](#key-parameters-explained)
- [Calculation Strategy](#calculation-strategy)
- [Docker Compose Configuration](#docker-compose-configuration)
- [Practical Examples](#practical-examples)
- [Troubleshooting](#troubleshooting)
- [Monitoring](#monitoring)

---

## Overview

This guide helps you properly configure parallelism settings for Apache Airflow 3.x running with CeleryExecutor in Docker Compose.

### Why This Matters
- **Too low**: Tasks stuck in queue, wasted resources
- **Too high**: Out-of-memory errors, worker crashes
- **Just right**: Optimal throughput and resource utilization

---

## Key Parameters Explained

### 1. `AIRFLOW__CELERY__WORKER_CONCURRENCY`
- **What**: Number of tasks ONE worker can run simultaneously
- **Default**: 16
- **Controls**: Task slots per worker container
- **Formula**: `CPU cores per worker × 2 to 4`

### 2. `AIRFLOW__CORE__PARALLELISM`
- **What**: Maximum TOTAL tasks across ALL workers at once
- **Default**: 32
- **Controls**: System-wide task execution limit
- **Formula**: `worker_concurrency × number_of_workers × 1.25`

### 3. `AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG`
- **What**: Max tasks from a SINGLE DAG running at once
- **Default**: 16
- **Controls**: Prevents one DAG from monopolizing resources
- **Formula**: `parallelism / expected_concurrent_dags`

### 4. `AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG`
- **What**: Max simultaneous DAG runs for one DAG
- **Default**: 16
- **Controls**: How many instances of same DAG can run
- **Recommendation**: 3-10 depending on DAG complexity

### 5. `AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT`
- **What**: Size of the default task pool
- **Default**: 128
- **Controls**: Available slots for task execution
- **Formula**: Should be ≥ `parallelism`

---

## Calculation Strategy

### Step 1: Determine Docker Resources

Check your Docker allocation:
```bash
# Check Docker resources
docker info | grep -E "CPUs|Total Memory"

# Monitor container usage
docker stats
```

### Step 2: Calculate Worker Concurrency

```
worker_concurrency = Available_CPUs_per_Worker × Multiplier
```

**Multiplier Guidelines:**
- **CPU-bound tasks** (data processing, ML): Use `1 to 2`
- **I/O-bound tasks** (API calls, file operations): Use `2 to 4`
- **Mixed workload**: Use `2 to 3`

**Memory Check:**
```
Memory_per_Task = Total_Worker_Memory / worker_concurrency
```
Ensure each task has at least 256MB-512MB RAM.

### Step 3: Calculate Total Parallelism

```
parallelism = worker_concurrency × number_of_workers × 1.25
```

The 1.25 multiplier provides scheduling headroom.

### Step 4: Set Per-DAG Limits

```
max_active_tasks_per_dag = parallelism / expected_concurrent_dags
```

Example: If you typically run 4 DAGs simultaneously:
```
max_active_tasks_per_dag = 32 / 4 = 8
```

---

## Docker Compose Configuration

### Find Your Current Configuration

Your docker-compose.yml file should have an `x-airflow-common` section with environment variables.

### Configuration Template

Add these environment variables to your `airflow-common-env` section:

```yaml
x-airflow-common:
  &airflow-common
  build: .
  image: ${AIRFLOW_IMAGE_NAME:-extending_airflow:latest}
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: CeleryExecutor
    AIRFLOW__CORE__AUTH_MANAGER: airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
    AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK: 'true'
    
    # ============================================
    # PARALLELISM SETTINGS - ADJUST THESE VALUES
    # ============================================
    AIRFLOW__CELERY__WORKER_CONCURRENCY: 8
    AIRFLOW__CORE__PARALLELISM: 16
    AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG: 8
    AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG: 3
    AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 16
    # ============================================
    
    _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-}
    AIRFLOW__WEBSERVER__RELOAD_ON_PLUGIN_CHANGE: 'true'
    AIRFLOW__CORE__RELOAD_ON_PLUGIN_CHANGE: 'true'
    AIRFLOW__CORE__LAZY_LOAD_PLUGINS: 'true'
    AIRFLOW__API__AUTH_BACKEND: airflow.api.auth.backend.basic_auth
```

### Optional: Add Resource Limits (Recommended)

Add resource limits to prevent container resource contention:

```yaml
x-airflow-common:
  &airflow-common
  build: .
  image: ${AIRFLOW_IMAGE_NAME:-extending_airflow:latest}
  deploy:
    resources:
      limits:
        cpus: '2.0'       # Maximum CPUs per container
        memory: 4G        # Maximum memory per container
      reservations:
        cpus: '1.0'       # Guaranteed CPUs
        memory: 2G        # Guaranteed memory
  environment:
    &airflow-common-env
    # ... rest of config
```

---

## Practical Examples

### Example 1: Small Development Setup
**Resources**: 1 worker, 4 CPU cores, 8GB RAM  
**Workload**: Mostly I/O-bound tasks (API calls, file operations)

```yaml
AIRFLOW__CELERY__WORKER_CONCURRENCY: 8          # 4 CPUs × 2
AIRFLOW__CORE__PARALLELISM: 16                  # 8 × 1 worker × 2
AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG: 8
AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG: 3
AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 16
```

**Reasoning**:
- 4 CPUs × 2 = 8 concurrent tasks (I/O-bound multiplier)
- Single worker, so parallelism = 8 × 2 = 16
- Conservative per-DAG limits for development

---

### Example 2: Medium Production Setup
**Resources**: 1 worker, 8 CPU cores, 16GB RAM  
**Workload**: Mixed CPU and I/O tasks

```yaml
AIRFLOW__CELERY__WORKER_CONCURRENCY: 16         # 8 CPUs × 2
AIRFLOW__CORE__PARALLELISM: 32                  # 16 × 1 worker × 2
AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG: 16
AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG: 5
AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 32
```

**Reasoning**:
- 8 CPUs × 2 = 16 concurrent tasks (mixed workload)
- Higher per-DAG limits for production throughput
- Memory per task: 16GB / 16 = 1GB per task

---

### Example 3: Large Production with Multiple Workers
**Resources**: 3 workers, 8 CPU cores each, 16GB RAM each  
**Workload**: Heavy I/O operations

```yaml
AIRFLOW__CELERY__WORKER_CONCURRENCY: 16         # 8 CPUs × 2
AIRFLOW__CORE__PARALLELISM: 64                  # 16 × 3 workers × 1.33
AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG: 32
AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG: 8
AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 64
```

**Scale workers**:
```bash
docker-compose up -d --scale airflow-worker=3
```

**Reasoning**:
- 16 concurrent tasks per worker
- 3 workers × 16 = 48, with 1.33x headroom = 64
- Higher limits to leverage multiple workers

---

### Example 4: CPU-Intensive Workload
**Resources**: 1 worker, 16 CPU cores, 32GB RAM  
**Workload**: Data processing, ML model training

```yaml
AIRFLOW__CELERY__WORKER_CONCURRENCY: 16         # 16 CPUs × 1 (CPU-bound)
AIRFLOW__CORE__PARALLELISM: 24                  # 16 × 1.5
AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG: 12
AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG: 2
AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 24
```

**Reasoning**:
- CPU-bound tasks: 1:1 ratio with CPU cores
- Lower DAG run limit to prevent resource exhaustion
- Memory per task: 32GB / 16 = 2GB per task

---

## Troubleshooting

### Problem: "No working slots anymore"

**Symptoms**: Tasks stuck in queue, workers idle

**Diagnosis**:
```bash
# Check worker status
docker-compose ps airflow-worker

# Check worker logs
docker-compose logs -f airflow-worker

# Check Celery worker info
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect stats
```

**Solutions**:

1. **Workers not running**:
   ```bash
   docker-compose up -d airflow-worker
   ```

2. **Parallelism too low**:
   - Increase `AIRFLOW__CORE__PARALLELISM`
   - Increase `AIRFLOW__CELERY__WORKER_CONCURRENCY`
   - Restart: `docker-compose down && docker-compose up -d`

3. **Scale workers**:
   ```bash
   docker-compose up -d --scale airflow-worker=3
   # Then update PARALLELISM accordingly
   ```

4. **Clear stuck tasks**:
   ```bash
   docker-compose exec airflow-scheduler airflow tasks clear <dag_id>
   ```

---

### Problem: Workers Crashing (OOM)

**Symptoms**: Worker containers restarting, memory errors in logs

**Diagnosis**:
```bash
# Check memory usage
docker stats airflow-worker

# Check worker logs for OOM
docker-compose logs airflow-worker | grep -i "memory\|oom\|killed"
```

**Solutions**:

1. **Reduce concurrency**:
   ```yaml
   AIRFLOW__CELERY__WORKER_CONCURRENCY: 8  # Reduce from 16
   ```

2. **Add memory limits**:
   ```yaml
   deploy:
     resources:
       limits:
         memory: 8G
   ```

3. **Calculate memory per task**:
   ```
   Memory_per_Task = Container_Memory / worker_concurrency
   ```
   Ensure ≥ 512MB per task

4. **Scale horizontally instead**:
   ```bash
   # Instead of 1 worker with concurrency=32
   # Use 2 workers with concurrency=16
   docker-compose up -d --scale airflow-worker=2
   ```

---

### Problem: Tasks Not Being Picked Up

**Symptoms**: Tasks stay in "queued" state, workers show as healthy

**Diagnosis**:
```bash
# Check Redis connection
docker-compose exec airflow-worker redis-cli -h redis ping

# Check Celery broker connection
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect active

# Check pool slots
docker-compose exec airflow-scheduler airflow pools list
```

**Solutions**:

1. **Check pool configuration**:
   ```yaml
   AIRFLOW__CORE__DEFAULT_POOL_TASK_SLOT_COUNT: 32  # Must be ≥ parallelism
   ```

2. **Verify task queue**:
   ```bash
   docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect reserved
   ```

3. **Restart all services**:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

4. **Check DAG-level limits**:
   - Verify `max_active_tasks_per_dag` isn't too restrictive
   - Check if DAG has `max_active_tasks` parameter set

---

### Problem: State Mismatch Errors

**Symptoms**: "Executor reported finished with state failed, but task instance's state is queued"

**Diagnosis**:
```bash
# Check database connections
docker-compose logs postgres | grep -i error

# Check Celery result backend
docker-compose logs redis | grep -i error
```

**Solutions**:

1. **Increase database connection pool**:
   ```yaml
   AIRFLOW__DATABASE__SQL_ALCHEMY_POOL_SIZE: 10
   AIRFLOW__DATABASE__SQL_ALCHEMY_MAX_OVERFLOW: 20
   ```

2. **Add retry logic**:
   ```yaml
   AIRFLOW__DATABASE__SQL_ALCHEMY_POOL_RECYCLE: 3600
   AIRFLOW__DATABASE__SQL_ALCHEMY_POOL_PRE_PING: 'true'
   ```

3. **Clear task state manually**:
   ```bash
   docker-compose exec airflow-scheduler airflow tasks clear <dag_id> -t <task_id>
   ```

---

## Monitoring

### Enable Flower (Celery Monitoring UI)

Add to your docker-compose.yml (already present in your file):

```bash
docker-compose --profile flower up -d
```

Access at: http://localhost:5555

**What to monitor**:
- Active workers count
- Task queue length
- Worker resource usage
- Task success/failure rates

---

### CLI Monitoring Commands

```bash
# Check worker status
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect stats

# Check active tasks
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect active

# Check registered workers
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect registered

# Monitor resource usage
docker stats

# Check pool usage (via Airflow)
docker-compose exec airflow-scheduler airflow pools list
```

---

### Container Resource Monitoring

```bash
# Real-time stats for all containers
docker stats

# Monitor specific service
docker stats airflow-worker-1

# Check container logs
docker-compose logs -f airflow-worker
docker-compose logs -f airflow-scheduler
```

---

## Quick Reference Table

| Docker Resources | Worker Concurrency | Parallelism | Max Tasks/DAG |
|-----------------|-------------------|-------------|---------------|
| 4 CPU, 8GB      | 4-8               | 8-16        | 4-8           |
| 8 CPU, 16GB     | 8-16              | 16-32       | 8-16          |
| 16 CPU, 32GB    | 16-32             | 32-64       | 16-32         |
| Multiple Workers| 8-16 each         | Concurrency × Workers × 1.25 | Based on total |

---

## Step-by-Step Implementation

### 1. Check Your Resources
```bash
docker info | grep -E "CPUs|Total Memory"
docker stats
```

### 2. Calculate Your Values
Use the formulas from the "Calculation Strategy" section.

### 3. Update docker-compose.yml
Add the environment variables to your `airflow-common-env` section.

### 4. Apply Changes
```bash
docker-compose down
docker-compose up -d
```

### 5. Verify Configuration
```bash
# Check worker picked up new settings
docker-compose logs airflow-worker | grep -i concurrency

# Verify capacity
docker-compose exec airflow-worker celery -A airflow.providers.celery.executors.celery_executor.app inspect stats
```

### 6. Monitor Performance
```bash
# Enable Flower
docker-compose --profile flower up -d

# Watch container resources
docker stats

# Check task execution
# Access Airflow UI: http://localhost:8080
```

### 7. Tune as Needed
- Start conservative (lower values)
- Monitor for 24-48 hours
- Increase gradually if you have capacity
- Decrease if seeing memory issues

---

## Best Practices

### ✅ DO
- Start with conservative values
- Monitor resource usage before scaling up
- Use Flower for visibility
- Set resource limits on containers
- Scale horizontally (more workers) rather than vertically (higher concurrency)
- Test configuration changes in staging first

### ❌ DON'T
- Set parallelism > your actual available resources
- Ignore memory constraints
- Set worker_concurrency higher than CPU cores × 4
- Forget to update parallelism when scaling workers
- Use the same settings for dev and production

---

## Additional Resources

### Airflow Documentation
- [CeleryExecutor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html)
- [Configuration Reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html)

### Docker Resources
- [Docker Resource Constraints](https://docs.docker.com/config/containers/resource_constraints/)
- [Docker Compose Deploy Specification](https://docs.docker.com/compose/compose-file/deploy/)

### Celery Documentation
- [Celery Workers](https://docs.celeryq.dev/en/stable/userguide/workers.html)
- [Celery Concurrency](https://docs.celeryq.dev/en/stable/userguide/concurrency/index.html)

---

## Support and Feedback

If you encounter issues not covered in this guide:

1. Check Airflow logs: `docker-compose logs airflow-worker`
2. Check the Airflow troubleshooting guide: https://airflow.apache.org/docs/apache-airflow/stable/troubleshooting.html
3. Review Celery worker logs for connection issues
4. Use Flower UI for real-time monitoring
5. Join the Apache Airflow Slack community

---

## Version Information

This guide is written for:
- **Apache Airflow**: 3.x
- **Executor**: CeleryExecutor
- **Deployment**: Docker Compose

Last Updated: November 2025