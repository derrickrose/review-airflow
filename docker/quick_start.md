1 Find your Docker resources:

docker info | grep -E "CPUs|Total Memory"

```

2. **Use this formula:**
```

3 Start conservative:





Worker Concurrency = (Available CPUs ÷ Number of Workers) × 2
Parallelism = Worker Concurrency × 1.5 to 2

AIRFLOW__CELERY__WORKER_CONCURRENCY: 4
AIRFLOW__CORE__PARALLELISM: 8
# Monitor resource usage
docker stats

# If you have capacity, increase settings
# and restart
docker-compose down && docker-compose up -d

