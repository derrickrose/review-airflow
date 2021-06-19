# airflow plugin

https://airflow.apache.org/docs/apache-airflow/1.10.1/plugins.html

# notes

* after how much time a new DAGs should be picked up from the filesystem

> min_file_process_interval = 0
> dag_dir_list_interval = 60

* Note to install and configure awscli (à verifier)

* copy dags from dev to airflow dags

> cp -r /d/review-airflow-wsl/dev/dags/ /airflow_home/

* copy plugins from dev to airflow plugins (should restart both scheduler and webserver)

> cp -r /d/review-airflow-wsl/dev/plugins/ /airflow_home/

* S3 operators

https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html#create-and-delete-amazon-s3-buckets

* dependencies aws providers (for using the s3 operators before)

> pip install 'apache-airflow[amazon]'